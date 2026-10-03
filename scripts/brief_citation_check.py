#!/usr/bin/env python3
"""brief_citation_check — do the source paths cited in briefs/ actually resolve?

Why this exists
---------------
The daily "cyber lab" wave is authored in the **OSINT** wiki. Its brief is written
once and then copied **verbatim** into sibling `briefs/` directories, including
this one. The citations inside are bare `wiki/...` paths, which resolve correctly
in the authoring wiki and dangle everywhere else.

Between 2026-09-23 and 2026-10-03 that produced a silent backlog. Nothing
detected it because `briefs/` is gitignored — CI never sees these files.

On 2026-10-03 every dangling citation resolved in a sibling wiki. Not one needed
a page created here. So the fix is to qualify the path (`@osint-wiki/...`), not
to duplicate the page.

Two citation forms appear, and both are checked:
  - `[Source: wiki/concepts/x.md]`   — the newer form
  - `@wiki/concepts/x.md`            — an older form; `wiki` is not a real alias

Usage
-----
  python3 scripts/brief_citation_check.py            # report
  python3 scripts/brief_citation_check.py --fix      # qualify unambiguous refs
  python3 scripts/brief_citation_check.py --quiet

Exit 0 when every citation resolves; 1 otherwise.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS = ROOT / "briefs"
WIKI = ROOT / "wiki"

# `[Source: wiki/path.md]` or `[Source: @alias/path.md]`
SOURCE_RE = re.compile(r"\[Source:\s*@?([A-Za-z0-9_-]+)/([^\s\]]+\.md)\s*\]")
# `@alias/path.md` used as a relation line
AT_RE = re.compile(r"@([A-Za-z0-9_-]+)/([^\s)\]]+\.md)")

# Tokens that mean "this wiki" but are not aliases in the CLAUDE.md table.
PSEUDO_LOCAL = {"wiki", "cybersec-wiki"}


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


_INDEX: dict[str, list[str]] | None = None


def _index() -> dict[str, list[str]]:
    """Lazy map of relative-path -> sibling aliases holding it.

    Built once so suffix lookups below do not re-walk eight wikis per ref.
    """
    global _INDEX
    if _INDEX is None:
        _INDEX = {}
        for alias, base in WIKI_ALIASES.items():
            if not base.is_dir():
                continue
            for p in base.rglob("*.md"):
                _INDEX.setdefault(p.relative_to(base).as_posix(), []).append(alias)
    return _INDEX


def _trailing(rel: str) -> list[str]:
    """Index paths whose trailing components equal `rel`'s (exact match excluded).

    Briefs written before ~2026-09-15 cite sibling pages by a partial path —
    `tools/cyberchef.md` for `entities/tools/cyberchef.md`, or a bare
    `eval-foo-2026-05-13.md` for `sources/eval-foo-2026-05-13.md`. Comparing
    trailing components catches both; a plain `endswith("/" + rel)` would miss
    the bare-filename case, which has no slash to anchor on.
    """
    idx = _index()
    if rel in idx:
        return []
    want = rel.split("/")
    n = len(want)
    return sorted(p for p in idx if p.split("/")[-n:] == want)


def owners_of(rel: str) -> list[str]:
    """Aliases of sibling wikis that hold this page (exact path, or by suffix)."""
    idx = _index()
    if rel in idx:
        return sorted(set(idx[rel]))
    return sorted({a for path in _trailing(rel) for a in idx[path]})


def suffix_hits(rel: str) -> list[str]:
    """Full relative paths in siblings matching `rel` by trailing components."""
    return _trailing(rel)


class Ref:
    __slots__ = ("file", "token", "rel", "raw")

    def __init__(self, file: Path, token: str, rel: str, raw: str) -> None:
        self.file, self.token, self.rel, self.raw = file, token, rel, raw

    @property
    def local_rel(self) -> str:
        """The path that identifies the page, relative to whichever wiki holds it.

        - A real alias (`@osint-wiki/concepts/x.md`): `rel` is relative to that
          sibling's wiki/, so it stands alone.
        - A pseudo token (`@wiki/concepts/x.md`): means this wiki with a redundant
          token, so the token is dropped.
        - Anything else (`@sources/x.md`): `@path` is relative to wiki/, so the
          token is part of the path.
        """
        if self.token in WIKI_ALIASES or self.token in PSEUDO_LOCAL:
            return self.rel
        return f"{self.token}/{self.rel}"

    @property
    def local_ok(self) -> bool:
        lr = self.local_rel
        # `briefs/` sits beside wiki/, not inside it.
        if lr.startswith("briefs/"):
            return (ROOT / lr).exists()
        return (WIKI / lr).exists()


def collect() -> list[Ref]:
    refs: list[Ref] = []
    if not BRIEFS.is_dir():
        return refs
    for md in sorted(BRIEFS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        seen = set()
        for rx in (SOURCE_RE, AT_RE):
            for token, rel in rx.findall(text):
                key = (token, rel)
                if key in seen:
                    continue
                seen.add(key)
                refs.append(Ref(md, token, rel, f"@{token}/{rel}"))
    return refs


def classify(ref: Ref) -> str:
    """'ok' | 'sibling' | 'pseudo' | 'unknown-alias' | 'dangling'."""
    if ref.token in WIKI_ALIASES:
        base = WIKI_ALIASES[ref.token]
        if not base.is_dir():
            return "ok"  # sibling not checked out here — not this wiki's problem
        if (base / ref.rel).is_file():
            return "ok"
        # briefs/ in a sibling lives beside its wiki/, not inside it.
        if ref.rel.startswith("briefs/") and (base.parent / ref.rel).is_file():
            return "ok"
        # Self-reference with a redundant `wiki/` segment, e.g.
        # @cybersecurity-wiki/wiki/log.md -> log.md.
        if ref.token == "cybersecurity-wiki" and ref.rel.startswith("wiki/"):
            if (base / ref.rel[len("wiki/"):]).is_file():
                return "self-strip"
        return "sibling" if sibling_target(ref) else "dangling"
    if ref.token in PSEUDO_LOCAL:
        # A bogus alias that means "this wiki": resolve the path as local.
        if ref.local_ok:
            return "pseudo"
        return "sibling" if owners_of(ref.local_rel) else "dangling"
    if ref.local_ok:
        return "ok"
    if (WIKI / ref.token).is_dir() or ref.token == "briefs":
        # `@sources/...` and friends: the token is a real local dir, so a miss
        # here is a genuinely missing page, not an alias problem.
        return "sibling" if owners_of(ref.local_rel) else "dangling"
    return "unknown-alias"


def sibling_target(ref: Ref) -> tuple[str, str] | None:
    """(alias, full relative path) when exactly one sibling owns the page."""
    owners = owners_of(ref.local_rel)
    if len(owners) != 1:
        return None
    hits = suffix_hits(ref.local_rel)
    if hits:
        if len(hits) != 1:
            return None  # ambiguous suffix — never guess
        return owners[0], hits[0]
    return owners[0], ref.local_rel


def report(ref: Ref, kind: str) -> None:
    loc = f"{ref.file.name}: {ref.raw}"
    if kind == "pseudo":
        print(f"{loc}\n    -> resolves locally, but `@wiki/` is not an alias — drop the token")
    elif kind == "sibling":
        target = sibling_target(ref)
        if target:
            alias, rel = target
            note = "" if rel == ref.local_rel else f" (path completed from `{ref.local_rel}`)"
            print(f"{loc}\n    -> in @{alias}/ — cite it as @{alias}/{rel}{note}")
        else:
            owners = owners_of(ref.local_rel)
            if len(owners) > 1:
                print(f"{loc}\n    -> resolves in several wikis ({', '.join(owners)}) — qualify it")
            else:
                hits = suffix_hits(ref.local_rel)
                print(f"{loc}\n    -> ambiguous in @{owners[0] if owners else '?'}/: "
                      f"{len(hits)} candidate paths — fix by hand")
    elif kind == "unknown-alias":
        print(f"{loc}\n    -> `@{ref.token}` is not an alias in CLAUDE.md and not a local path")
    else:
        print(f"{loc}\n    -> dangling — the page does not exist here or in any sibling")


def apply_fix(refs: list[Ref]) -> int:
    """Rewrite the unambiguous cases: drop a redundant pseudo token, and qualify
    a sibling-owned path. Never guesses when the target is ambiguous."""
    fixed = 0
    by_file: dict[Path, list[Ref]] = {}
    for r in refs:
        kind = classify(r)
        if kind == "sibling" and sibling_target(r):
            by_file.setdefault(r.file, []).append(r)
        elif kind in ("pseudo", "self-strip"):
            by_file.setdefault(r.file, []).append(r)

    for md, items in by_file.items():
        text = md.read_text(encoding="utf-8")
        changed = False
        for r in items:
            kind = classify(r)
            if kind == "pseudo":
                # Drop the redundant token: @wiki/concepts/x -> @concepts/x
                old_forms = (
                    (f"[Source: {r.token}/{r.rel}]", f"[Source: {r.rel}]"),
                    (f"@{r.token}/{r.rel}", f"@{r.rel}"),
                )
            elif kind == "self-strip":
                # @cybersecurity-wiki/wiki/log.md -> @log.md
                trimmed = r.rel[len("wiki/"):]
                old_forms = (
                    (f"[Source: {r.token}/{r.rel}]", f"[Source: {trimmed}]"),
                    (f"@{r.token}/{r.rel}", f"@{trimmed}"),
                )
            else:
                target = sibling_target(r)
                if not target:
                    continue
                alias, rel = target
                if alias == "cybersecurity-wiki":
                    continue
                old_forms = (
                    (f"[Source: {r.raw}]", f"[Source: @{alias}/{rel}]"),
                    (f"[Source: {r.token}/{r.rel}]", f"[Source: @{alias}/{rel}]"),
                    (f"@{r.token}/{r.rel}", f"@{alias}/{rel}"),
                )
            for old, new in old_forms:
                if old in text and old != new:
                    text = text.replace(old, new)
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

    refs = collect()
    if not refs:
        print("brief_citation_check: no briefs/ here (gitignored; normal in CI)")
        return 0

    bad = [r for r in refs if classify(r) != "ok"]
    if not args.quiet:
        for r in bad:
            report(r, classify(r))

    fixed = apply_fix(bad) if args.fix and bad else 0
    if args.fix and fixed:
        print(f"\nqualified {fixed} citation(s)")

    remaining = [r for r in bad if classify(r) != "ok"] if not args.fix else []
    print(f"\nbrief_citation_check: {len({r.file for r in refs})} brief(s), "
          f"{len(refs)} ref(s), {len(bad)} unresolvable, {fixed} fixed")
    if args.fix:
        # Re-scan: the rewrite may have cleared everything.
        after = [r for r in collect() if classify(r) != "ok"]
        print(f"after fix: {len(after)} unresolvable")
        return 1 if after else 0
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
