#!/usr/bin/env python3
"""Bidirectional converter between wiki @path annotations and Obsidian [[wikilinks]].

Usage:
    python3 scripts/obsidian-link-convert.py --to-wikilinks        # @path → [[wikilink]]
    python3 scripts/obsidian-link-convert.py --to-atpath           # [[wikilink]] → @path
    python3 scripts/obsidian-link-convert.py --report              # preview changes (dry-run)

Safety:
    - Default mode is --report (no files modified).
    - --to-wikilinks and --to-atpath write changes in-place (use git to revert).
    - Always backs up each file as <path>.bak before modifying.
    - The lint script's body-mention check (#4) must be updated if you convert.
      See obsidian-navigation.md § "Optional: convert to wikilinks for full Obsidian fidelity".

Convention mapping:
    @concepts/google-business-profile.md  → [[google-business-profile|concepts/google-business-profile]]
    @entities/tools/yoast-seo.md          → [[yoast-seo|entities/tools/yoast-seo]]
    [[google-business-profile]]           → @concepts/google-business-profile.md
    [[yoast-seo|entities/tools/yoast-seo]] → @entities/tools/yoast-seo.md

Scope:
    Only converts links inside wiki/ (skips index.md, log.md, dashboard.md).
    Handles both `## Relations` section links and inline body mentions.
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

# ── Resolve WIKI root ──────────────────────────────────────────────────────

WIKI = Path(os.environ.get("WIKI_DIR", Path(__file__).resolve().parent.parent / "wiki"))
SKIP_PAGES = {"index.md", "log.md", "dashboard.md"}

# ── Backup ──────────────────────────────────────────────────────────────────

backup_dir = WIKI.parent / ".obsidian-convert-backups" / datetime.now().strftime("%Y%m%d-%H%M%S")

def backup(path: Path) -> Path:
    rel = path.relative_to(WIKI.parent)
    dest = backup_dir / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, dest)
    return dest

# ── Patterns ────────────────────────────────────────────────────────────────

# Matches @path/to/page.md in body text or Relations sections
AT_PATH_RE = re.compile(r"@([a-z0-9_./-]+\.md)")

# Matches Obsidian wikilinks: [[slug]] or [[slug|display text]]
# We are conservative: only match links that look like wiki page references
# (contain a slash or match a known page slug from the index).
WIKILINK_RE = re.compile(r"\[\[([a-z0-9_./|-]+?)\]\]")

# Known page slugs (built from the full relative paths in wiki/)
# We build this at scan time so we only convert links that resolve to real pages.
known_paths: set[str] = set()


def scan_known_paths():
    """Populate known_paths with all wiki page relative paths."""
    for p in WIKI.rglob("*.md"):
        rel = str(p.relative_to(WIKI))
        if rel not in SKIP_PAGES:
            known_paths.add(rel.replace(".md", ""))


def resolve_atpath_to_slug(raw: str) -> Optional[str]:
    """Given '@concepts/foo.md', return the Obsidian slug 'concepts/foo'."""
    path = raw.lstrip("@").rstrip(".md")
    if path in known_paths:
        return path
    # Try stripping 'wiki/' prefix if someone wrote @wiki/concepts/foo.md
    if path.startswith("wiki/"):
        stripped = path[len("wiki/"):]
        if stripped in known_paths:
            return stripped
    return None


def wikilink_to_atpath(display: str) -> Optional[str]:
    """Given 'concepts/foo' or 'concepts/foo|Display Text', return '@concepts/foo.md' or None."""
    # Strip optional display text
    pipe = display.find("|")
    if pipe != -1:
        path_part = display[:pipe]
    else:
        path_part = display

    path_part = path_part.strip()

    # Must contain a slash (our convention: category/slug)
    if "/" not in path_part:
        return None

    candidate = path_part + ".md"
    if candidate in known_paths or ("wiki/" + candidate) in known_paths:
        return f"@{candidate}"

    # Also try with wiki/ prefix stripped
    clean = candidate
    if clean.startswith("wiki/"):
        clean = clean[len("wiki/"):]
    if clean in known_paths:
        return f"@{clean}"

    return None


# ── Convert functions ───────────────────────────────────────────────────────

def convert_atpath_to_wikilink(text: str) -> tuple[str, int]:
    """Replace @path.md → [[path|path.md]] and return (new_text, count)."""
    count = 0
    result = []
    last_end = 0

    for m in AT_PATH_RE.finditer(text):
        raw = m.group(1)
        slug = resolve_atpath_to_slug(raw)
        if slug is None:
            continue  # not a known wiki page — leave it alone

        # Build wikilink: [[slug|category/slug]]
        display = slug
        wikilink = f"[[{slug}|{display}]]"

        result.append(text[last_end:m.start()])
        result.append(wikilink)
        last_end = m.end()
        count += 1

    result.append(text[last_end:])
    return "".join(result), count


def convert_wikilink_to_atpath(text: str) -> tuple[str, int]:
    """Replace [[path|display]] or [[path]] → @path.md and return (new_text, count)."""
    count = 0
    result = []
    last_end = 0

    for m in WIKILINK_RE.finditer(text):
        inner = m.group(1)
        atpath = wikilink_to_atpath(inner)
        if atpath is None:
            continue  # not a resolvable wiki link — leave it alone

        result.append(text[last_end:m.start()])
        result.append(atpath)
        last_end = m.end()
        count += 1

    result.append(text[last_end:])
    return "".join(result), count


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Convert between wiki @path annotations and Obsidian [[wikilinks]]."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--to-wikilinks", action="store_true",
                        help="Convert @path.md → [[path|path]]")
    group.add_argument("--to-atpath", action="store_true",
                        help="Convert [[path|display]] → @path.md")
    group.add_argument("--report", action="store_true",
                        help="Dry-run: show what would change without modifying files")
    parser.add_argument("--backup", action="store_true", default=True,
                        help="Create .bak files before modifying (default: true)")
    parser.add_argument("--no-backup", action="store_false", dest="backup",
                        help="Skip backup files")
    parser.add_argument("--wiki-dir", type=Path, default=None,
                        help="Override wiki directory (default: repo wiki/)")
    args = parser.parse_args()

    global WIKI
    if args.wiki_dir:
        WIKI = args.wiki_dir

    scan_known_paths()
    print(f"Indexed {len(known_paths)} wiki pages from {WIKI}")

    converter = convert_atpath_to_wikilink if args.to_wikilinks else convert_wikilink_to_atpath
    direction = "→ wikilinks" if args.to_wikilinks else "→ @path"
    dry_run = args.report

    total_files_changed = 0
    total_links_changed = 0
    modified_files: list[str] = []

    for p in sorted(WIKI.rglob("*.md")):
        rel = str(p.relative_to(WIKI))
        if rel in SKIP_PAGES:
            continue

        text = p.read_text(errors="replace")
        new_text, count = converter(text)

        if count > 0:
            total_files_changed += 1
            total_links_changed += count
            modified_files.append(f"  {rel} ({count} link{'s' if count != 1 else ''})")

            if not dry_run:
                if args.backup:
                    bk = backup(p)
                    print(f"  backup → {bk}")
                p.write_text(new_text, encoding="utf-8")
                print(f"  updated {rel}", file=sys.stderr)

    if dry_run:
        print(f"\n--- DRY RUN REPORT ({direction}) ---")
        if modified_files:
            print(f"Would modify {total_files_changed} file(s), {total_links_changed} link(s):\n")
            for f in modified_files:
                print(f)
        else:
            print("No changes needed — all links are already in the target format.")
    else:
        print(f"\nDone: {total_files_changed} file(s) updated, {total_links_changed} link(s) converted.")
        if args.backup:
            print(f"Backups saved to: {backup_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())