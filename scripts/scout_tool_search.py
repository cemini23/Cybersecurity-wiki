#!/usr/bin/env python3
"""SCOUT tool-search (CCC K311 leftover, shipped 2026-08-28; BM25 2026-08-31).

Operator-invoked federation helper: index LOCAL .cursor/skills/*/SKILL.md
frontmatter (name + description, plus one line from the body's first heading)
and return BM25-lite top-k (k~=5). 'execute' means READ that SKILL.md --
never a live MCP invoke, never a catalog dump.

Scoring is BM25-lite (k1=1.5, b=0.75) with IDF computed over the local skill
corpus; a small substring bonus handles e.g. "git" inside "GitHub". No pip
dependency, no HF, no vector DB.

Usage:
  python3 scripts/scout_tool_search.py query <terms...> [-k 5]
  python3 scripts/scout_tool_search.py read <skill-name>   # prints the SKILL.md path
  python3 scripts/scout_tool_search.py selftest
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".cursor" / "skills"

STOP = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with",
    "use", "using", "when", "how", "what", "that", "this", "is", "are", "it",
}

K1 = 1.5
B = 0.75
SUBSTRING_BONUS = 0.05  # small per-query-token bonus for substring hits


def _tokens(text: str) -> Counter:
    return Counter(
        w for w in re.findall(r"[a-z0-9][a-z0-9\-_]{1,}", text.lower()) if w not in STOP
    )


def _parse_frontmatter(text: str) -> dict:
    fm: dict[str, str] = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return fm
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line.lstrip().startswith("-"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val in (">", ">-", "|", "|-"):
                # YAML block scalar: fold following indented lines
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or lines[i].strip() == ""):
                    block.append(lines[i].strip())
                    i += 1
                fm[key] = " ".join(x for x in block if x)
                continue
            fm[key] = val.strip('"').strip("'")
        i += 1
    return fm


def _first_heading_line(text: str) -> str:
    m = re.search(r"^#+\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def index_skills(skills_dir: Path | None = None) -> list[dict]:
    base = skills_dir or SKILLS_DIR
    out = []
    if not base.is_dir():
        return out
    for sk in sorted(base.iterdir()):
        f = sk / "SKILL.md"
        if not f.is_file():
            continue
        raw = f.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(raw)
        name = fm.get("name") or sk.name
        desc = fm.get("description") or ""
        # description may be a YAML block scalar (>-) -- keep first line if long
        desc_one = " ".join(desc.split())[:300]
        out.append(
            {
                "name": name,
                "path": str(f.relative_to(REPO_ROOT)),
                "desc": desc_one,
                "heading": _first_heading_line(raw)[:120],
                "text": f"{name} {desc_one} {_first_heading_line(raw)}",
            }
        )
    return out


def _corpus_stats(skills: list[dict]) -> tuple[dict, dict, float]:
    """Return (doc_freq, doc_lengths, avgdl) over the skill corpus.

    doc_freq: term -> number of skills containing it.
    doc_lengths: name -> token count.
    """
    doc_freq: Counter = Counter()
    doc_lengths: dict[str, int] = {}
    total_len = 0
    for sk in skills:
        toks = _tokens(sk["text"])
        doc_lengths[sk["name"]] = sum(toks.values())
        total_len += sum(toks.values())
        for w in toks:
            doc_freq[w] += 1
    n = len(skills)
    avgdl = total_len / n if n else 0.0
    return dict(doc_freq), doc_lengths, avgdl


def _idf(n: int, df: int) -> float:
    return math.log(1.0 + (n - df + 0.5) / (df + 0.5))


def score_bm25(sk: dict, query: Counter, doc_freq: dict, doc_lengths: dict, avgdl: float) -> tuple[float, str]:
    text_l = sk["text"].lower()
    sk_tok = _tokens(sk["text"])
    dl = doc_lengths.get(sk["name"], 1)
    n = max(len(doc_lengths), 1)
    denom_norm = 1 - B + B * (dl / avgdl) if avgdl else 1.0

    total = 0.0
    matched = 0
    for w, qf in query.items():
        f = sk_tok.get(w, 0)
        if f > 0:
            idf = _idf(n, doc_freq.get(w, 0))
            total += idf * (f * (K1 + 1)) / (f + K1 * denom_norm)
            matched += 1
        elif w in text_l:
            # substring fallback: query token contained in a description word
            # (e.g. "git" in "GitHub") -- small bonus, keeps IDF-free
            total += SUBSTRING_BONUS * qf
            matched += 1

    if matched == 0:
        return 0.0, "no shared terms"
    why = "BM25 match" if any(sk_tok.get(w, 0) > 0 for w in query) else "substring match in description"
    return total, why


def search(terms: list[str], k: int = 5) -> list[dict]:
    query = _tokens(" ".join(terms))
    if not query:
        return []
    skills = index_skills()
    doc_freq, doc_lengths, avgdl = _corpus_stats(skills)
    ranked = []
    for sk in skills:
        s, why = score_bm25(sk, query, doc_freq, doc_lengths, avgdl)
        if s > 0:
            ranked.append({"name": sk["name"], "path": sk["path"], "score": round(s, 3), "why": why, "desc": sk["desc"]})
    ranked.sort(key=lambda r: (-r["score"], r["name"]))
    return ranked[:k]


def cmd_search(args: argparse.Namespace) -> int:
    if not args.terms:
        print("query terms required", file=sys.stderr)
        return 2
    for r in search(args.terms, args.k):
        print(f"{r['score']:.3f}  {r['name']:<28} {r['path']}")
        print(f"        why: {r['why']} | {r['desc'][:110]}")
    return 0


def cmd_read(args: argparse.Namespace) -> int:
    for sk in index_skills():
        if sk["name"].lower() == args.name.lower():
            print(sk["path"])
            return 0
    print(f"no skill named '{args.name}'", file=sys.stderr)
    return 1


def selftest() -> int:
    skills = index_skills()
    fed = 0
    for s in skills:
        raw = (REPO_ROOT / s["path"]).read_text(encoding="utf-8", errors="replace")
        if re.search(r"^federation:\s*true", raw, re.M):
            fed += 1
    if fed < 3:
        raise SystemExit(f"selftest FAIL: expected >=3 federation skills, found {fed}")
    res = search(["route"])
    if not any(r["name"].lower() == "route" for r in res):
        names = [r["name"] for r in res]
        raise SystemExit(f"selftest FAIL: query 'route' did not return the route skill ({names})")
    # query must prefer a match over nothing
    empty = search(["zzzzzzzz"])
    if empty:
        raise SystemExit(f"selftest FAIL: non-empty result for nonsense query ({empty})")
    # BM25 path: query 'step' must rank the step-gate skill in top-k
    st = search(["step"])
    if not any(r["name"].lower() == "step-gate" for r in st):
        names = [r["name"] for r in st]
        raise SystemExit(f"selftest FAIL: query 'step' did not rank step-gate in top-k ({names})")
    print(f"selftest PASS: {len(skills)} skills indexed; {fed} federation; "
          f"'route' and 'step'->step-gate in top-k (BM25)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("query", help="top-k skill search (BM25-lite)")
    q.add_argument("terms", nargs="+")
    q.add_argument("-k", type=int, default=5)
    q.set_defaults(fn=cmd_search)
    r = sub.add_parser("read", help="print path of a SKILL.md to read")
    r.add_argument("name")
    r.set_defaults(fn=cmd_read)
    s = sub.add_parser("selftest", help="run selftest")
    s.set_defaults(fn=lambda _a: selftest())
    args = ap.parse_args()
    try:
        return int(args.fn(args))
    except SystemExit as e:
        code = e.code
        if isinstance(code, int):
            return code
        print(code, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
