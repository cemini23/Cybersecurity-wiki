#!/usr/bin/env python3
"""Lint pass over the wiki/.

Reports:
  1. Orphans              — pages with zero inbound `related:` references
  2. Bidirectional gaps   — A lists B as related but B doesn't list A
  3. Dangling links       — `related:` paths that don't resolve to a real file
  4. Missing pages        — `@path` mentions in body where the file doesn't exist
  5. Cited unread stubs   — source pages with read_status=unread-stub but ≥1 inbound related: edge
  6. Frontmatter quality  — missing `type` / `maturity` / mismatched `updated:`
  7. Stale verification   — `[NEEDS VERIFICATION YYYY-MM-DD]` tags older than --verify-age-days
                            (default 7) — Exa-resolution candidates per CLAUDE.md "External research"
  8. Cross-wiki gaps     — `@wiki-alias/path` references to other wikis that don't resolve
"""

import argparse
import os
import re
import sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_resolver import (  # noqa: E402
    WikiResolver,
    load_federation_table,
    normalize_path,
)
from pathlib import Path
from collections import defaultdict

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--verify-age-days", type=int, default=7,
                    help="Flag [NEEDS VERIFICATION YYYY-MM-DD] tags older than this many days (default: 7)")
parser.add_argument("--fix-bidirectional", action="store_true",
                    help="Propose (dry-run) missing-backlink fixes for bidirectional gaps (Phase 4 of "
                         "obsidian-llm-wiki-local port). Use --apply to actually write.")
parser.add_argument("--apply", action="store_true",
                    help="With --fix-bidirectional: write the proposed backlinks. Without --apply, dry-run only.")
parser.add_argument("--hub-threshold", type=int, default=4,
                    help="With --fix-bidirectional: skip target pages with > N missing backlinks "
                         "(those are likely intentional hub-index pages). Default: 4")
parser.add_argument("--fail-on-graph", action="store_true",
                    help="Exit 1 on graph integrity errors (used by pre-commit). "
                         "Gates dangling related: links, dangling body @path mentions, and "
                         "dangling cross-wiki links. When wiki/ paths are staged in git, only "
                         "staged pages are gated. Full-wiki gate when nothing under wiki/ is staged.")
parser.add_argument("--domain", default=None,
                    help="Restrict the run to one domain directory under wiki/ (e.g. osint). "
                         "A filter, not a root change: WIKI stays at <repo>/wiki so alias "
                         "loading and the pre-commit staged slice keep working.")
args = parser.parse_args()
TODAY = date.today()

# Resolve WIKI relative to this script (scripts/wiki_lint.py → repo root → wiki/),
# with WIKI_DIR env-var override for non-standard layouts (e.g. CI checkout paths).
WIKI = Path(os.environ.get("WIKI_DIR", Path(__file__).resolve().parent.parent / "wiki")).resolve()

# -- cross-wiki resolution -------------------------------------------
# The resolver lives in wiki_resolver.py so the migration harness can call the same
# logic. Two implementations could disagree about whether a link resolves, which is
# exactly what a verification gate exists to prevent.

WIKI_ALIASES = load_federation_table(WIKI.parent / "CLAUDE.md")
RESOLVER = WikiResolver(WIKI, WIKI_ALIASES)

# -- frontmatter parsing (no PyYAML dep) ----------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RELATED_LIST_RE = re.compile(r"^related:\s*\n((?:\s+-\s+.+\n?)*)", re.MULTILINE)
RELATED_INLINE_RE = re.compile(r"^related:\s*\[([^\]]*)\]", re.MULTILINE)
SCALAR_RE = lambda key: re.compile(rf"^{key}:\s*(.+?)\s*$", re.MULTILINE)

def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm_text = m.group(1)
    out = {}
    # related: list block
    rl = RELATED_LIST_RE.search(fm_text)
    if rl:
        items = []
        for line in rl.group(1).splitlines():
            s = line.strip()
            if s.startswith("- "):
                v = s[2:].strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
                    v = v[1:-1].strip()
                items.append(v)
        out["related"] = items
    else:
        # try inline form: related: [a, b, c]
        ri = RELATED_INLINE_RE.search(fm_text)
        if ri:
            raw_items = [s.strip() for s in ri.group(1).split(",") if s.strip()]
            cleaned = []
            for v in raw_items:
                if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
                    v = v[1:-1].strip()
                cleaned.append(v)
            out["related"] = cleaned
        else:
            out["related"] = []
    # scalars
    for key in ("type", "maturity", "title", "created", "updated", "read_status", "hub"):
        m2 = SCALAR_RE(key).search(fm_text)
        if m2:
            out[key] = m2.group(1).strip()
    return out

# Resolution is delegated to wiki_resolver.py (see the import at the top).

# -- walk ----------------------------------------------------------------

pages = {}                  # rel_path -> frontmatter dict
all_paths = set()

for p in WIKI.rglob("*.md"):
    rel = str(p.relative_to(WIKI))
    # Navigational files, matched by BASENAME. An exact-path test stops working the
    # moment a page sits at wiki/osint/index.md, which would then be scanned as an
    # ordinary page and reported as an orphan with no frontmatter.
    if os.path.basename(rel) in ("index.md", "log.md", "dashboard.md"):
        continue
    text = p.read_text(errors="replace")
    fm = parse_frontmatter(text)
    if fm is None:
        # log later
        pages[rel] = {"_no_frontmatter": True, "related": [], "_body": text}
        all_paths.add(rel)
        continue
    fm["_body"] = text
    pages[rel] = fm
    all_paths.add(rel)

# -- 1+2+3: build inbound edge map ---------------------------------------

inbound = defaultdict(set)  # target -> {source, ...}
outbound = defaultdict(set) # source -> {target, ...}
dangling = []               # (source, raw_target) where target file doesn't exist

ambiguous_refs = []   # (source, raw, [candidate keys]) — never silently resolved

for src, fm in pages.items():
    for tgt_raw in fm.get("related", []):
        kind, value = RESOLVER.resolve(src, tgt_raw, all_paths)
        if kind == "local":
            inbound[value].add(src)
            outbound[src].add(value)
        elif kind == "out":
            pass  # exists outside the wiki tree; not a graph edge
        elif kind == "ambiguous":
            ambiguous_refs.append((src, tgt_raw, value))
        else:
            dangling.append((src, tgt_raw))

# orphans: pages with zero inbound edges (excluding index/log already excluded).
# sweeps/ holds periodic Tier-2 sweep reports — append-only, like log.md; they
# are legitimately orphan, so exempt them from the orphan check.
# Matched by basename, not by full relative path: once a page sits at
# wiki/osint/dashboard.md an exact-path match fails and it becomes an orphan with
# no frontmatter.
_NAV_EXEMPT = frozenset({
    "index.md", "log.md", "dashboard.md", "_CLAUDE.md",
    "log-archive.md", "_daily-template.md",
})


def _is_nav_exempt(rel_path):
    return os.path.basename(rel_path) in _NAV_EXEMPT


orphans = sorted(
    p for p in all_paths
    if p not in inbound
    and not p.startswith("sweeps/")
    and "/sweeps/" not in p
    and not _is_nav_exempt(p)
)

# bidirectional gaps: src→tgt without tgt→src
# Hub pages (frontmatter `hub: true`) are exempt: many spokes legitimately
# tag the hub without the hub having to enumerate every spoke (would explode
# to 100+ entry related: lists).
def _is_hub(page_path):
    fm = pages.get(page_path) or {}
    return str(fm.get("hub", "")).lower() == "true"

gaps = []
for src, tgts in outbound.items():
    for tgt in tgts:
        if _is_hub(tgt):
            continue
        if src not in outbound.get(tgt, set()):
            gaps.append((src, tgt))
gaps.sort()

# -- 4: @path body mentions that don't resolve ---------------------------

# `@path/to/page.md` style references in markdown body
# Capture the @ so cross-wiki paths retain the alias prefix for resolution.
AT_PATH_RE = re.compile(r"(@[a-z0-9_./-]+\.md)")


def is_inside_backticks(body, match_start, match_end):
    """True if [match_start, match_end) sits inside a `...` span on the same line."""
    line_start = body.rfind("\n", 0, match_start) + 1
    line_end = body.find("\n", match_end)
    if line_end == -1:
        line_end = len(body)
    line = body[line_start:line_end]
    rel_start = match_start - line_start
    # Count unescaped backticks before the match on this line; odd → inside a span
    return line.count("`", 0, rel_start) % 2 == 1


# Paths that are intentionally outside wiki/ (briefs/, ephemera/, etc.) — skip.
BODY_MENTION_SKIP_PREFIXES = ("briefs/", "hot.md", "research to be indexed/")

missing_mentions = defaultdict(set)  # mentioned_path -> {source, ...}
for src, fm in pages.items():
    body = fm.get("_body", "")
    if not body:
        continue
    for m in AT_PATH_RE.finditer(body):
        if is_inside_backticks(body, m.start(), m.end()):
            continue
        raw = m.group(1)
        mentioned = normalize_path(raw).lstrip("@")
        if mentioned.startswith(BODY_MENTION_SKIP_PREFIXES):
            continue
        if _is_nav_exempt(mentioned):
            continue
        kind, _value = RESOLVER.resolve(src, raw, all_paths)
        if kind == "missing":
            missing_mentions[mentioned].add(src)

# -- 8: cross-wiki @wiki-alias/path links ---------------------------
# Check @wiki-alias/path/to/page.md references to other wikis.

# Exclude quote and bracket chars from the path: cross-wiki `related:` entries
# are YAML-quoted (a plain scalar can't start with the reserved `@` indicator)
# and inline refs often sit inside a `[Source: ...]` citation tag — a naive
# class would swallow the closing quote / `]` / `)` into the path.
CROSS_WIKI_RE = re.compile(r"""@([a-z0-9_-]+)/([^\s`)\]"']+)""")

cross_wiki_dangling = []  # (src, alias, rel_path, target_path)
cross_wiki_ok = 0

if WIKI_ALIASES:
    for src, fm in pages.items():
        body = fm.get("_body", "")
        if not body:
            continue
        for m in CROSS_WIKI_RE.finditer(body):
            alias = m.group(1)
            # Only treat as cross-wiki link if alias is in WIKI_ALIASES
            if alias not in WIKI_ALIASES:
                continue  # skip local wiki links like @concepts/..., @entities/...
            # A directory named in backticks is documentation, not a link. AT_PATH_RE
            # already skips these; this check did not, so `@game-dev-wiki/briefs/`
            # was resolved against disk.
            if is_inside_backticks(body, m.start(), m.end()):
                continue
            rel_path = m.group(2).lstrip("/")
            kind, value = RESOLVER.resolve(src, "@" + alias + "/" + rel_path, all_paths)
            if kind in ("local", "out"):
                cross_wiki_ok += 1
            else:
                cross_wiki_dangling.append((src, alias, rel_path, value))

# -- 5: cited unread stubs -----------------------------------------------

cited_unread = []
for p, fm in pages.items():
    if not p.startswith("sources/"):
        continue
    rs = (fm.get("read_status") or "").lower()
    # Only an explicit unread status counts here. A *missing* read_status is a
    # metadata gap, not evidence the source is unread — it is reported under
    # check 6 instead, so a forgotten field can't masquerade as an unread source.
    if rs in ("unread-stub", "unread"):
        if p in inbound and len(inbound[p]) >= 1:
            cited_unread.append((p, len(inbound[p])))
cited_unread.sort(key=lambda x: -x[1])

# -- 6: frontmatter quality ----------------------------------------------

# sweeps/ files are append-only Tier-2 reports (log-like) — no frontmatter
# expected, same rationale as the orphan exemption above.
no_frontmatter = sorted(p for p, fm in pages.items()
                        if fm.get("_no_frontmatter") and not p.startswith("sweeps/"))
no_type = sorted(p for p, fm in pages.items()
                 if not fm.get("_no_frontmatter") and not fm.get("type"))
no_maturity = sorted(p for p, fm in pages.items()
                     if not fm.get("_no_frontmatter") and not fm.get("maturity")
                     and fm.get("type") in ("source", "entity", "concept"))
# Source pages should declare read_status in frontmatter (deep-read / read /
# read-skim / skimmed / unread-stub / …). A missing field is a metadata gap.
source_no_read_status = sorted(
    p for p, fm in pages.items()
    if not fm.get("_no_frontmatter") and fm.get("type") == "source"
    and not fm.get("read_status"))

# -- 7: stale [NEEDS VERIFICATION YYYY-MM-DD] tags -----------------------

# Match [NEEDS VERIFICATION YYYY-MM-DD] with optional date. Date is required for staleness check;
# tags without a date are flagged separately as "undated" (can't compute age).
NEEDS_VERIFY_DATED_RE = re.compile(r"\[NEEDS VERIFICATION\s+(\d{4}-\d{2}-\d{2})\]")
NEEDS_VERIFY_BARE_RE = re.compile(r"(?<!`)\[NEEDS VERIFICATION\](?!`)(?!\s+\d{4})")

stale_verifications = []  # (page, date_str, age_days, line_num, line_text)
undated_verifications = []  # (page, line_num, line_text)

for src, fm in pages.items():
    body = fm.get("_body", "")
    if not body:
        continue
    for line_num, line in enumerate(body.splitlines(), start=1):
        for m in NEEDS_VERIFY_DATED_RE.finditer(line):
            try:
                tag_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
            age = (TODAY - tag_date).days
            if age >= args.verify_age_days:
                stale_verifications.append((src, m.group(1), age, line_num, line.strip()))
        if NEEDS_VERIFY_BARE_RE.search(line):
            undated_verifications.append((src, line_num, line.strip()))

stale_verifications.sort(key=lambda x: -x[2])  # oldest first

# -- print report --------------------------------------------------------

def header(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)

print(f"Wiki lint scan — {len(all_paths)} pages indexed (excluding index.md / log.md / dashboard.md)")
print(f"Outbound edges: {sum(len(v) for v in outbound.values())}; "
      f"Inbound edge coverage: {len(inbound)} pages")

# -- optional domain filter -------------------------------------------------
# A reporting scope, not a resolution scope: WIKI stays at the repo's wiki/ so alias
# loading, cross-domain resolution and the pre-commit staged slice all keep working.
if args.domain:
    _dom = args.domain.strip("/")

    def _src_in_dom(p):
        return p == _dom or p.startswith(_dom + "/")

    orphans = [p for p in orphans if _src_in_dom(p)]
    dangling = [(a, b) for a, b in dangling if _src_in_dom(a)]
    gaps = [(a, b) for a, b in gaps if _src_in_dom(a)]
    missing_mentions = defaultdict(set, {
        p: {s for s in srcs if _src_in_dom(s)}
        for p, srcs in missing_mentions.items()
    })
    missing_mentions = defaultdict(set, {p: v for p, v in missing_mentions.items() if v})
    cross_wiki_dangling = [t for t in cross_wiki_dangling if _src_in_dom(t[0])]
    ambiguous_refs = [t for t in ambiguous_refs if _src_in_dom(t[0])]

header(f"1. Orphans — {len(orphans)} pages with zero inbound references (informational — not gated)")
for p in orphans:
    fm = pages[p]
    t = fm.get("type", "?")
    m = fm.get("maturity", "?")
    print(f"  [{t}/{m}] {p}")

header(f"2. Bidirectional gaps — {len(gaps)} asymmetric edges")
# group by target so the "target page is missing N backlinks" view is readable
gaps_by_target = defaultdict(list)
for src, tgt in gaps:
    gaps_by_target[tgt].append(src)
for tgt in sorted(gaps_by_target.keys(), key=lambda x: -len(gaps_by_target[x])):
    srcs = gaps_by_target[tgt]
    print(f"  → {tgt}  (missing backlinks from {len(srcs)} source page(s))")
    for s in srcs[:5]:
        print(f"      - {s}")
    if len(srcs) > 5:
        print(f"      ... and {len(srcs)-5} more")

header(f"3. Dangling related: links — {len(dangling)} edges to missing files")
for src, tgt in dangling:
    print(f"  {src}  →  {tgt}  (file not found)")

header(f"3b. Ambiguous @path references — {len(ambiguous_refs)} matched more than one domain")
for src, raw, keys in ambiguous_refs[:30]:
    print(f"  {src}  →  {raw}")
    for k in keys[:4]:
        print(f"      candidate: {k}")
if len(ambiguous_refs) > 30:
    print(f"  ... and {len(ambiguous_refs)-30} more")

header(f"4. @path body mentions to missing files — {len(missing_mentions)} unique paths")
for path in sorted(missing_mentions.keys()):
    srcs = missing_mentions[path]
    print(f"  {path}  (mentioned in {len(srcs)} page(s))")
    for s in sorted(srcs)[:5]:
        print(f"      - {s}")
    if len(srcs) > 5:
        print(f"      ... and {len(srcs)-5} more")

header(f"5. Cited but unread source stubs — {len(cited_unread)} pages")
for p, n in cited_unread[:30]:
    print(f"  {p}  ({n} inbound)")
if len(cited_unread) > 30:
    print(f"  ... and {len(cited_unread)-30} more (showing top 30 by citation count)")

header("6. Frontmatter quality")
print(f"  no frontmatter at all: {len(no_frontmatter)}")
for p in no_frontmatter:
    print(f"    - {p}")
print(f"  missing 'type' field: {len(no_type)}")
for p in no_type[:20]:
    print(f"    - {p}")
print(f"  missing 'maturity' field (source/entity/concept only): {len(no_maturity)}")
for p in no_maturity[:20]:
    print(f"    - {p}")
print(f"  source pages missing 'read_status' field: {len(source_no_read_status)}")
for p in source_no_read_status[:20]:
    print(f"    - {p}")
if len(source_no_read_status) > 20:
    print(f"    ... and {len(source_no_read_status)-20} more")

header(f"7. Stale [NEEDS VERIFICATION] tags — {len(stale_verifications)} dated tag(s) "
       f"≥{args.verify_age_days} days old (Exa-resolution candidates)")
if not stale_verifications:
    print(f"  (none — all dated NEEDS VERIFICATION tags are within the {args.verify_age_days}-day window)")
for page, date_str, age, line_num, line_text in stale_verifications[:30]:
    print(f"  [{age:>4}d old, tagged {date_str}] {page}:{line_num}")
    snippet = line_text if len(line_text) <= 140 else line_text[:137] + "..."
    print(f"      {snippet}")
if len(stale_verifications) > 30:
    print(f"  ... and {len(stale_verifications)-30} more (showing top 30 by age)")

if undated_verifications:
    print(f"\n  Also: {len(undated_verifications)} undated [NEEDS VERIFICATION] tag(s) "
          f"— add a date so age can be tracked:")
    for page, line_num, line_text in undated_verifications[:20]:
        snippet = line_text if len(line_text) <= 140 else line_text[:137] + "..."
        print(f"    - {page}:{line_num}  {snippet}")
    if len(undated_verifications) > 20:
        print(f"    ... and {len(undated_verifications)-20} more")

header(f"8. Cross-wiki @wiki-alias/path links — {len(cross_wiki_dangling)} dangling, {cross_wiki_ok} ok")
if not WIKI_ALIASES:
    print("  (no Related Wikis defined in CLAUDE.md)")
elif not cross_wiki_dangling:
    print(f"  (all {cross_wiki_ok} cross-wiki references resolve correctly)")
else:
    for src, alias, rel_path, target in sorted(cross_wiki_dangling):
        if target is None:
            print(f"  {src}  →  @{alias}/{rel_path}  (wiki alias not found in CLAUDE.md)")
        else:
            print(f"  {src}  →  @{alias}/{rel_path}  (file not found: {target})")

# -- fix-bidirectional ---------------------------------------------------
# Phase 4 of obsidian-llm-wiki-local port (`@entities/tools/obsidian-llm-wiki-local.md`).
# Append missing backlinks to target-page `related:` blocks. Hub pages (intentional
# many-to-one indexes) skipped via --hub-threshold. Dry-run by default; --apply writes.

RELATED_BLOCK_RE = re.compile(
    r"(?P<head>^related:\s*\n)(?P<items>(?:\s+-\s+.+\n)*)",
    re.MULTILINE,
)
UPDATED_LINE_RE = re.compile(r"^updated:\s*\d{4}-\d{2}-\d{2}\s*$", re.MULTILINE)


def _rewrite_target_page(target_path: Path, new_backlinks: list[str]) -> tuple[bool, str]:
    """Append *new_backlinks* to target page's `related:` block + bump `updated:` to today.

    Returns (changed, reason). Idempotent on re-run: skips entries already present.
    """
    text = target_path.read_text(errors="replace")
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        return False, "no frontmatter"
    fm_text = fm_match.group(1)
    fm_start, fm_end = fm_match.start(1), fm_match.end(1)

    block_match = RELATED_BLOCK_RE.search(fm_text)
    if not block_match:
        # No `related:` field at all — insert one before closing of frontmatter.
        new_block = "related:\n" + "".join(f"  - {bl}\n" for bl in new_backlinks)
        new_fm = fm_text.rstrip("\n") + "\n" + new_block.rstrip("\n")
    else:
        existing_items = set()
        for line in block_match.group("items").splitlines():
            s = line.strip()
            if s.startswith("- "):
                existing_items.add(s[2:].strip())
        to_add = [bl for bl in new_backlinks if bl not in existing_items]
        if not to_add:
            return False, "already present"
        insertion = "".join(f"  - {bl}\n" for bl in to_add)
        block_end = block_match.end("items")
        new_fm = fm_text[:block_end] + insertion + fm_text[block_end:]

    # Bump updated: today
    today_str = TODAY.isoformat()
    if UPDATED_LINE_RE.search(new_fm):
        new_fm = UPDATED_LINE_RE.sub(f"updated: {today_str}", new_fm, count=1)
    else:
        # Insert at end of frontmatter
        new_fm = new_fm.rstrip("\n") + f"\nupdated: {today_str}"

    new_text = text[:fm_start] + new_fm + text[fm_end:]
    target_path.write_text(new_text)
    return True, f"+{len(new_backlinks if not block_match else to_add)}"


if args.fix_bidirectional:
    header(f"FIX-BIDIRECTIONAL — proposed backlink writes (hub-threshold={args.hub_threshold})")
    proposed = []  # (target, [backlinks])
    skipped_hubs = []  # (target, count)
    for tgt in sorted(gaps_by_target.keys()):
        srcs = gaps_by_target[tgt]
        if len(srcs) > args.hub_threshold:
            skipped_hubs.append((tgt, len(srcs)))
            continue
        proposed.append((tgt, sorted(srcs)))

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"  Mode: {mode}")
    print(f"  Proposing {sum(len(b) for _,b in proposed)} backlinks across {len(proposed)} target pages")
    print(f"  Skipping {len(skipped_hubs)} hub target(s) "
          f"(more than {args.hub_threshold} missing backlinks — manual review)")
    if skipped_hubs:
        print()
        print("  Hubs skipped:")
        for tgt, n in skipped_hubs:
            print(f"    {n:3d}  {tgt}")
    print()
    applied = 0
    skipped_nochange = 0
    failed = 0
    for tgt, backlinks in proposed:
        tgt_path = WIKI / tgt
        if not tgt_path.exists():
            print(f"  [SKIP] {tgt}  (target file missing)")
            failed += 1
            continue
        if args.apply:
            changed, reason = _rewrite_target_page(tgt_path, backlinks)
            tag = "WROTE" if changed else "SKIP"
            if changed:
                applied += 1
            else:
                skipped_nochange += 1
            print(f"  [{tag}] {tgt}  ({reason})")
        else:
            print(f"  [PREVIEW] {tgt}  (+{len(backlinks)} backlinks)")
            for bl in backlinks:
                print(f"      - {bl}")
    print()
    if args.apply:
        print(f"  Summary: {applied} pages written, {skipped_nochange} already-present, "
              f"{failed} target-missing, {len(skipped_hubs)} hubs skipped")
    else:
        print(f"  Dry-run complete. Re-run with --apply to write {sum(len(b) for _,b in proposed)} "
              f"backlinks. Adjust --hub-threshold to include/exclude hub targets.")

# -- exit code summary ---------------------------------------------------
# Hard errors fail the build; informational findings (orphans, stale tags,
# cited-unread stubs, missing optional frontmatter) report but pass.
# Folded in from the Image gen fork during the 2026-10-14 linter reconciliation —
# it was the only one of the eight forks carrying a summary, and the other seven
# had no equivalent.

hard_errors = {
    "bidirectional gaps":        len(gaps),
    "dangling related: links":   len(dangling),
    "ambiguous references":      len(ambiguous_refs),
    "missing @path mentions":    len(missing_mentions),
    "cross-wiki dangling":       len(cross_wiki_dangling),
    "pages without frontmatter": len(no_frontmatter),
}
total_hard = sum(hard_errors.values())

header(f"Summary — {total_hard} hard error(s)")
for label, n in hard_errors.items():
    marker = "FAIL" if n else "ok  "
    print(f"  [{marker}] {label}: {n}")
if total_hard:
    print()
    print("Hard errors found. Fix the issues above, or bypass locally with "
          "`git commit --no-verify`.")

# Every dangling class, as (source, target) pairs. Check 4 (body @path mentions)
# and Check 8 (cross-wiki links) were reported but never gated: --fail-on-graph
# looked only at related: bidirectionality and related: targets.
mention_pairs = [(s, p) for p, srcs in missing_mentions.items() for s in srcs]
xw_pairs = [(s, f"{a}/{r}") for s, a, r, _t in cross_wiki_dangling]

if args.fail_on_graph and (gaps or dangling or mention_pairs or xw_pairs):
    staged = None
    try:
        import subprocess
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "wiki/"],
            cwd=str(WIKI.parent),
            text=True,
            stderr=subprocess.DEVNULL,
        )
        staged = {
            line.strip()[len("wiki/"):]
            for line in out.splitlines()
            if line.strip().startswith("wiki/") and line.strip().endswith(".md")
        }
    except Exception:
        staged = None

    if staged:
        gaps_f = [(a, b) for a, b in gaps if a in staged and b in staged]
        dangling_f = [(a, b) for a, b in dangling if a in staged]
        mention_f = [(s, p) for s, p in mention_pairs if s in staged]
        xw_f = [(s, t) for s, t in xw_pairs if s in staged]
        if gaps_f or dangling_f or mention_f or xw_f:
            print(
                "\nFAIL: staged wiki graph errors "
                f"(gaps={len(gaps_f)}, dangling={len(dangling_f)}, "
                f"missing mentions={len(mention_f)}, cross-wiki={len(xw_f)}).",
                file=sys.stderr,
            )
            for a, b in gaps_f[:20]:
                print(f"  gap: {a} → {b}", file=sys.stderr)
            for a, b in dangling_f[:20]:
                print(f"  dangling: {a} → {b}", file=sys.stderr)
            for a, b in mention_f[:20]:
                print(f"  missing mention: {a} → {b}", file=sys.stderr)
            for a, b in xw_f[:20]:
                print(f"  cross-wiki: {a} → {b}", file=sys.stderr)
            sys.exit(1)
        print(
            f"\nOK: staged wiki graph clean "
            f"({len(staged)} staged page(s); full-wiki debt not gated).",
            file=sys.stderr,
        )
    else:
        print(
            "\nFAIL: graph integrity errors "
            f"(gaps={len(gaps)}, dangling={len(dangling)}, "
            f"missing mentions={len(mention_pairs)}, cross-wiki={len(xw_pairs)}).",
            file=sys.stderr,
        )
        sys.exit(1)
