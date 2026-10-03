#!/usr/bin/env python3
"""brief_citation_check — do the source paths cited in briefs/ actually resolve?

Why this exists
---------------
The daily "cyber lab" wave is authored in the **OSINT** wiki. Its brief is written
once and then copied **verbatim** into sibling `briefs/` directories, including
this one. The citations inside are bare `wiki/...` paths, which resolve correctly
in the authoring wiki and dangle everywhere else.

Between 2026-09-23 and 2026-10-03 that produced a silent backlog: nine briefs
citing pages that looked local but were only ever created in OSINT. Nothing
detected it because `briefs/` is gitignored — CI never sees these files.

On 2026-10-03 all 12 dangling citations resolved in OSINT. Not one needed a page
created here. So the fix is to qualify the path (`@osint-wiki/...`), not to
duplicate the page.

Usage
-----
  python3 scripts/brief_citation_check.py            # report
  python3 scripts/brief_citation_check.py --fix      # rewrite qualified paths
  python3 scripts/brief_citation_check.py --quiet

Exit 0 when every citation resolves; 1 when any does not (or is reported).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS = ROOT / "briefs"
WIKI = ROOT / "wiki"


def load_wiki_aliases() -> dict[str, Path]:
    """Parse the CLAUDE.md 'Related Wikis' table into alias -> wiki dir.

    Scoped to that section on purpose: other tables in the file (the MCP-tools
    table) use the same two-cell row shape and would otherwise be parsed as
    aliases. Duplicated from wiki_lint.py rather than imported, because that file
    is a script and importing it runs a full lint scan.
    """
    claude_md = ROOT / "CLAUDE.md"
    aliases: dict[str, Path] = {}
    if not claude_md.exists():
        return aliases
    text = claude_md.read_text(errors="replace")
    section = re.search(r"^##\s+Related Wikis\s*$(.*?)(?=^##\s|\Z)", text, re.MULTILINE | re.DOTALL)
    if not section:
        return aliases
    table_re = re.compile(r"^\|\s*`([a-z0-9_-]+)`\s*\|\s*`?([^`\n\|]+)`?\s*\|", re.MULTILINE)
    for m in table_re.finditer(section.group(1)):
        alias = m.group(1).strip()
        wiki_path = Path(m.group(2).strip().rstrip("/"))
        if not wiki_path.is_absolute():
            wiki_path = (claude_md.parent / wiki_path).resolve()
        if wiki_path.is_dir():
            aliases[alias] = wiki_path
        elif (wiki_path / "wiki").is_dir():
            aliases[alias] = wiki_path / "wiki"
        else:
            aliases[alias] = wiki_path / "wiki" if wiki_path.name != "wiki" else wiki_path
    return aliases


WIKI_ALIASES = load_wiki_aliases()

# `[Source: wiki/path/to/page.md]` — the citation form these briefs use.
CITE_RE = re.compile(r"\[Source:\s*(wiki/[^\s\]]+\.md)\s*\]")


def owners_of(rel: str) -> list[str]:
    """Aliases of sibling wikis that hold wiki/<rel>."""
    return sorted(a for a, base in WIKI_ALIASES.items() if (base / rel).is_file())


def audit() -> tuple[list[tuple[Path, str, str, list[str]]], int]:
    """Return (problems, files_scanned). Each problem: (file, cited, rel, owners)."""
    problems: list[tuple[Path, str, str, list[str]]] = []
    scanned = 0
    if not BRIEFS.is_dir():
        return problems, 0
    for md in sorted(BRIEFS.glob("*.md")):
        scanned += 1
        text = md.read_text(encoding="utf-8")
        for cited in sorted(set(CITE_RE.findall(text))):
            rel = cited[len("wiki/"):]
            if (WIKI / rel).exists():
                continue
            problems.append((md, cited, rel, owners_of(rel)))
    return problems, scanned


def apply_fix(problems: list[tuple[Path, str, str, list[str]]]) -> int:
    """Rewrite citations that have exactly one sibling owner. Return count fixed."""
    fixed = 0
    by_file: dict[Path, list[tuple[str, str, list[str]]]] = {}
    for md, cited, rel, owners in problems:
        by_file.setdefault(md, []).append((cited, rel, owners))
    for md, items in by_file.items():
        text = md.read_text(encoding="utf-8")
        changed = False
        for cited, rel, owners in items:
            if len(owners) != 1:
                continue  # ambiguous or dangling everywhere — never guess
            alias = owners[0]
            if alias == "cybersecurity-wiki":
                continue  # already local to us; a missing page is a real gap
            new = f"[Source: @{alias}/{rel}]"
            text = text.replace(f"[Source: {cited}]", new)
            changed = True
            fixed += 1
        if changed:
            md.write_text(text, encoding="utf-8")
    return fixed


def main() -> int:
    ap = argparse.ArgumentParser(description="Check that brief citations resolve")
    ap.add_argument("--fix", action="store_true",
                    help="qualify citations that resolve in exactly one sibling wiki")
    ap.add_argument("--quiet", action="store_true", help="only print the summary")
    args = ap.parse_args()

    problems, scanned = audit()
    if not args.quiet:
        for md, cited, rel, owners in problems:
            if len(owners) == 1:
                print(f"{md.name}: {cited}")
                print(f"    -> resolves in @{owners[0]}/ — cite it as @{owners[0]}/{rel}")
            elif owners:
                print(f"{md.name}: {cited}")
                print(f"    -> resolves in several wikis ({', '.join(owners)}) — qualify it")
            else:
                print(f"{md.name}: {cited}")
                print("    -> dangling everywhere — the page was never created")

    fixed = apply_fix(problems) if args.fix and problems else 0
    if args.fix and fixed:
        print(f"\nqualified {fixed} citation(s)")

    if not scanned:
        print("brief_citation_check: no briefs/ here (gitignored; normal in CI)")
        return 0

    remaining = len(problems) - fixed
    print(f"\nbrief_citation_check: {scanned} brief(s), {len(problems)} unresolvable, {fixed} fixed")
    return 1 if remaining > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
