#!/usr/bin/env python3
"""Tier 1 gap detection for the wiki.

Surfaces three classes of gap that a human (or the LLM) can decide to fix in
this session, with concrete proposed Exa queries / actions for each:

  Type A — Cited-unread stubs ready for deep-read
    Source pages with read_status=unread-stub AND ≥N inbound `related:` edges.
    These are pages we cite but haven't deep-read. Proposed action: deep-read.

  Type D — Stale [NEEDS VERIFICATION YYYY-MM-DD] tags
    Tags whose age is ≥7 days. Proposed action: Exa-resolution per CLAUDE.md
    "External research" workflow.

  Type E — Thin concept pages
    Concept pages whose `## Narrative` section has fewer than W words.
    Proposed action: deep-read N source pages that cite this concept, write narrative.

Tier 1 is descriptive only — it does NOT fetch anything via Exa, does NOT modify
any wiki page. It produces a candidate list. The user picks which items to act
on; the LLM (next session) executes the chosen items via the existing Exa MCP.

This is the "gap-detection lint" half of the wiki proactive-search design
(2026-04-29). Tier 2 (proactive Exa with user-gated commit) is roadmapped but
not yet built — see ROADMAP.md "Soon" / "Eventually" sections.
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

# --- argv -------------------------------------------------------------------

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--wiki",
    default=None,
    help="Wiki directory to scan (default: 'wiki/' relative to this script)",
)
parser.add_argument(
    "--type-a-min-inbound",
    type=int,
    default=2,
    help="Type A: minimum inbound edges to flag a cited-unread stub (default: 2)",
)
parser.add_argument(
    "--type-a-max-shown",
    type=int,
    default=15,
    help="Type A: max items in the report (default: 15)",
)
parser.add_argument(
    "--type-d-min-age-days",
    type=int,
    default=7,
    help="Type D: minimum age in days for a stale [NEEDS VERIFICATION] tag (default: 7)",
)
parser.add_argument(
    "--type-e-min-words",
    type=int,
    default=100,
    help="Type E: a concept narrative under this word count is flagged thin (default: 100)",
)
args = parser.parse_args()

REPO = Path(__file__).resolve().parent.parent
WIKI = Path(args.wiki) if args.wiki else REPO / "wiki"
TODAY = date.today()

# --- regexes / parsing helpers ----------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RELATED_LIST_RE = re.compile(r"^related:\s*\n((?:\s+-\s+.+\n?)*)", re.MULTILINE)
SCALAR_RE = lambda key: re.compile(rf"^{key}:\s*(.+?)\s*$", re.MULTILINE)
NARRATIVE_RE = re.compile(r"^##\s+Narrative\b\s*\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
RAW_CONCEPT_RE = re.compile(r"^##\s+Raw Concept\b\s*\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
NEEDS_VERIFY_DATED_RE = re.compile(
    r"(?<!`)\[NEEDS VERIFICATION\s+(\d{4}-\d{2}-\d{2})\](?!`)"
)
URL_RE = re.compile(r"https?://[^\s`<>\)]+")


def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm_text = m.group(1)
    out = {}
    rl = RELATED_LIST_RE.search(fm_text)
    if rl:
        items = []
        for line in rl.group(1).splitlines():
            s = line.strip()
            if s.startswith("- "):
                items.append(s[2:].strip())
        out["related"] = items
    else:
        out["related"] = []
    for key in ("type", "title", "read_status", "maturity", "created", "updated"):
        m2 = SCALAR_RE(key).search(fm_text)
        if m2:
            out[key] = m2.group(1).strip()
    return out


def normalize_path(p: str) -> str:
    p = p.strip().lstrip("/")
    if p.startswith("wiki/"):
        p = p[len("wiki/") :]
    return p


def word_count(s: str) -> int:
    if not s:
        return 0
    # rough: tokens of length ≥2 made of letters/digits
    return len(re.findall(r"\b\w{2,}\b", s))


# --- walk the wiki -----------------------------------------------------------

pages = {}
all_paths = set()

for p in WIKI.rglob("*.md"):
    rel = str(p.relative_to(WIKI))
    if rel in ("index.md", "log.md", "dashboard.md"):
        continue
    text = p.read_text(errors="replace")
    fm = parse_frontmatter(text)
    if fm is None:
        continue
    fm["_body"] = text
    pages[rel] = fm
    all_paths.add(rel)

# Build inbound-edge map (mirror of wiki_lint.py logic)
inbound = defaultdict(set)
for src, fm in pages.items():
    for raw in fm.get("related", []):
        tgt = normalize_path(raw)
        if tgt in all_paths:
            inbound[tgt].add(src)


# --- helpers for "propose Exa query" ----------------------------------------

def propose_exa_query_from_stub(rel: str, fm: dict) -> str:
    """Pick the most query-shaped string from the page's title + Raw Concept block."""
    title = fm.get("title", "").strip().strip('"')
    rc_match = RAW_CONCEPT_RE.search(fm.get("_body", ""))
    rc_block = rc_match.group(1) if rc_match else ""
    # If a URL is in the Raw Concept block, propose crawling_exa on that URL
    urls = URL_RE.findall(rc_block)
    if urls:
        return f"crawling_exa(url='{urls[0]}')"
    # Otherwise propose web_search_exa with the title
    if title:
        return f"web_search_exa(query='{title}', numResults=3)"
    return f"web_search_exa(query='{rel}', numResults=3)"


def extract_claim_sentence(body: str, line_num: int) -> str:
    """Given the body and the 1-based line number of a NEEDS VERIFICATION tag,
    return the surrounding sentence (or up to ~200 chars of context)."""
    lines = body.splitlines()
    if not (1 <= line_num <= len(lines)):
        return ""
    line = lines[line_num - 1].strip()
    # Strip leading list markers / formatting
    line = re.sub(r"^[-*]\s*", "", line)
    line = re.sub(r"^\d+\.\s*", "", line)
    # If the line is short, grab the next few too
    out = line
    j = line_num
    while len(out) < 200 and j < len(lines):
        nxt = lines[j].strip()
        if not nxt or nxt.startswith("##"):
            break
        out += " " + nxt
        j += 1
    return out[:300]


# --- Type A — cited-unread stubs ready for deep-read -----------------------

type_a = []
for rel, fm in pages.items():
    if not rel.startswith("sources/"):
        continue
    rs = (fm.get("read_status") or "").lower()
    if rs not in ("unread-stub", "unread", ""):
        continue
    n_in = len(inbound.get(rel, set()))
    if n_in >= args.type_a_min_inbound:
        type_a.append((n_in, rel, fm))
type_a.sort(key=lambda x: -x[0])


# --- Type D — stale dated [NEEDS VERIFICATION] tags ------------------------

type_d = []
for rel, fm in pages.items():
    body = fm.get("_body", "")
    for line_num, line in enumerate(body.splitlines(), start=1):
        for m in NEEDS_VERIFY_DATED_RE.finditer(line):
            try:
                tag_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
            age = (TODAY - tag_date).days
            if age >= args.type_d_min_age_days:
                claim = extract_claim_sentence(body, line_num)
                type_d.append((age, rel, line_num, claim))
type_d.sort(key=lambda x: -x[0])


# --- Type E — thin concept pages -------------------------------------------

type_e = []
for rel, fm in pages.items():
    if not rel.startswith("concepts/"):
        continue
    body = fm.get("_body", "")
    nm = NARRATIVE_RE.search(body)
    narrative_words = word_count(nm.group(1)) if nm else 0
    if narrative_words < args.type_e_min_words:
        type_e.append((narrative_words, rel, fm, nm is not None))
type_e.sort(key=lambda x: x[0])


# --- print -----------------------------------------------------------------

def header(s: str):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


print(f"Tier 1 gap-detection report — {len(all_paths)} pages scanned")
print(
    f"thresholds: A inbound≥{args.type_a_min_inbound}, "
    f"D age≥{args.type_d_min_age_days}d, E narrative<{args.type_e_min_words} words"
)

header(
    f"Type A — Cited-unread stubs ready for deep-read ({len(type_a)} found, top {args.type_a_max_shown} shown)"
)
if not type_a:
    print("  (none — no cited stubs above the inbound threshold)")
for n_in, rel, fm in type_a[: args.type_a_max_shown]:
    title = fm.get("title", "").strip().strip('"')
    if not title:
        title = "(no title in frontmatter)"
    proposal = propose_exa_query_from_stub(rel, fm)
    citing = sorted(inbound.get(rel, []))
    print()
    print(f"  📄 {rel}  ({n_in} inbound)")
    print(f"     title: {title[:100]}")
    print(f"     proposal: {proposal}")
    print(f"     cited from: {', '.join(citing[:3])}{'  …' if len(citing) > 3 else ''}")

header(
    f"Type D — Stale [NEEDS VERIFICATION] tags (≥{args.type_d_min_age_days} days) ({len(type_d)} found)"
)
if not type_d:
    print(f"  (none — all dated tags are within the {args.type_d_min_age_days}-day window)")
for age, rel, line_num, claim in type_d:
    print()
    print(f"  ⏰ {rel}:{line_num}  ({age}d old)")
    print(f"     claim: {claim[:200]}")
    print(f"     proposal: web_search_exa(query=<extract from claim>, numResults=3); if URL")
    print(f"               cited, prefer crawling_exa for primary-source verification")

header(
    f"Type E — Thin concept pages (narrative <{args.type_e_min_words} words) ({len(type_e)} found)"
)
if not type_e:
    print(f"  (none — all concept pages have ≥{args.type_e_min_words} narrative words)")
for n_words, rel, fm, has_section in type_e:
    title = fm.get("title", "").strip().strip('"') or "(no title)"
    citing = sorted(inbound.get(rel, []))
    print()
    print(
        f"  📝 {rel}  ({n_words} narrative words"
        f"{'; no ## Narrative section' if not has_section else ''})"
    )
    print(f"     title: {title[:100]}")
    print(f"     {len(citing)} inbound page(s) reference this concept; "
          f"likely deep-read targets:")
    for c in citing[:5]:
        print(f"       - {c}")
    if len(citing) > 5:
        print(f"       ... and {len(citing)-5} more")

print()
print("---")
print(
    f"Summary: {len(type_a)} type-A, {len(type_d)} type-D, {len(type_e)} type-E gaps"
)
print("Tier 1 is descriptive only. Decide which items to act on, then ask the LLM")
print("to run the proposed Exa query / deep-read source / write the narrative.")
