#!/usr/bin/env python3
"""Pre-ingest duplicate detector.

Scans every file in `research to be indexed/` and reports whether each looks
like a duplicate of something already indexed in `wiki/sources/`. Run this BEFORE
creating any new source page (Step 0 of the ingest workflow per CLAUDE.md).

Match signals, in confidence order:
  1. SHA-256 of the file (would catch "I dropped the same PDF twice"). NOTE:
     v1 does NOT match against existing source pages because we haven't been
     recording PDF SHAs in frontmatter. The SHA of the candidate file is
     printed so future runs can spot a re-drop manually.
  2. arXiv ID exact match  (highest reliability)
  3. DOI exact match
  4. URL match (normalized: lowercase scheme/host, strip trailing slash, strip .git)
  5. Filename match in any source page's `Location:` field
  6. Title exact match (case/punct-normalized)
  7. Title fuzzy match (Jaccard on word shingles, ≥0.5 → flagged)

Each candidate file gets a verdict:
  - NEW       — no matches above any threshold
  - LIKELY    — fuzzy title match, or filename in a Location field
  - DUPLICATE — exact arXiv ID / DOI / URL / title match

Exit codes:
  0 — ran cleanly (any number of duplicates is fine; this is informational)
  1 — could not open the input directory or the wiki directory
"""

import argparse
import hashlib
import os
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

# --- argv -------------------------------------------------------------------

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--inbox",
    default=None,
    help="Directory of new sources to check (default: 'research to be indexed/')",
)
parser.add_argument(
    "--wiki",
    default=None,
    help="Wiki directory whose sources/ is the canonical index (default: 'wiki/')",
)
parser.add_argument(
    "--fuzzy-threshold",
    type=float,
    default=0.5,
    help="Title-Jaccard threshold above which a match is flagged LIKELY (default: 0.5)",
)
parser.add_argument(
    "--max-content-bytes",
    type=int,
    default=15_000,
    help="Bytes of file content to scan for arXiv/DOI/URL extraction (default: 15000)",
)
args = parser.parse_args()

REPO = Path(__file__).resolve().parent.parent
INBOX = Path(args.inbox) if args.inbox else REPO / "research to be indexed"
WIKI = Path(args.wiki) if args.wiki else REPO / "wiki"
SOURCES = WIKI / "sources"

if not INBOX.is_dir():
    print(f"ERROR: inbox directory not found: {INBOX}", file=sys.stderr)
    sys.exit(1)
if not SOURCES.is_dir():
    print(f"ERROR: wiki/sources directory not found: {SOURCES}", file=sys.stderr)
    sys.exit(1)

# --- regexes ---------------------------------------------------------------

# arXiv: 4-digit YR/MM + 4-5 digit ID, optional vN (e.g. 2604.25850, 2604.25850v1)
ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})(v\d+)?\b")
# DOI: 10.XXXX/something — common forms only
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[A-Za-z0-9._;()<>/-]+)\b")
# URL: http(s)://, terminated by whitespace or backtick or angle-bracket
URL_RE = re.compile(r"https?://[^\s`<>\)]+")
# Frontmatter title field
TITLE_FRONTMATTER_RE = re.compile(r'^title:\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)
# Raw-Concept fields: `- **Original title**: foo` / `- **arXiv ID**: foo`
RC_FIELD_RE_TEMPLATE = r"^\s*-\s+\*\*{key}\*\*:\s*(.+?)\s*$"

STOPWORDS = {
    "a", "an", "the", "of", "and", "or", "for", "to", "in", "on", "with",
    "by", "from", "is", "are", "as", "at", "via", "vs", "into", "over",
    "under", "between", "across", "using", "based", "toward", "towards",
}


def normalize_title(t: str) -> str:
    """Strip diacritics, lowercase, collapse whitespace + punctuation."""
    if not t:
        return ""
    nfkd = unicodedata.normalize("NFKD", t)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    ascii_only = ascii_only.lower()
    # collapse non-alnum to single space
    ascii_only = re.sub(r"[^a-z0-9]+", " ", ascii_only).strip()
    return re.sub(r"\s+", " ", ascii_only)


def title_token_set(t: str) -> set:
    """Tokenize a normalized title into a content-word set (stopwords stripped)."""
    norm = normalize_title(t)
    if not norm:
        return set()
    return {w for w in norm.split() if w not in STOPWORDS and len(w) > 1}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def normalize_url(u: str) -> str:
    """Light URL canonicalization for dup-matching.

    - lowercase scheme + host
    - strip trailing slash on path (but keep root /)
    - strip trailing punctuation (commas, periods, parens) from naked URLs in prose
    - strip a single trailing .git from a path component
    """
    u = u.rstrip(",.;:)\"'`")
    m = re.match(r"^(https?)://([^/]+)(/.*)?$", u, re.IGNORECASE)
    if not m:
        return u
    scheme, host, path = m.group(1).lower(), m.group(2).lower(), m.group(3) or ""
    if path.endswith(".git"):
        path = path[:-4]
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def extract_field(text: str, key: str) -> str:
    """Pull `- **<key>**: value` from a Raw Concept block. Returns first match or ''."""
    rx = re.compile(RC_FIELD_RE_TEMPLATE.format(key=re.escape(key)), re.MULTILINE)
    m = rx.search(text)
    return m.group(1).strip() if m else ""


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for blk in iter(lambda: f.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


# --- index existing wiki sources ----------------------------------------------


def _extract_own_metadata_section(text: str) -> str:
    """Return the page's own metadata: frontmatter + Raw Concept section only.

    Cross-references in Narrative/Relations/Snippets sections mention other
    papers' arXiv IDs, DOIs, and URLs. Scanning those sections would falsely
    index foreign identifiers as belonging to this page. We scope extraction
    to the two sections that describe *this* page's own identity.
    """
    # Frontmatter is between the first --- and the next ---
    parts = text.split("---", 2)
    fm = parts[1] if len(parts) >= 2 else ""
    # Raw Concept section: from "## Raw Concept" to the next "## " heading
    rc = ""
    m = re.search(r"^## Raw Concept\s*\n(.*?)(?=^##\s)", text, re.MULTILINE | re.DOTALL)
    if m:
        rc = m.group(1)
    return fm + "\n" + rc


def build_wiki_index():
    """Walk wiki/sources/ and collect dup-match keys into one structure."""
    idx = {
        "arxiv": defaultdict(list),       # arxiv_id_no_version -> [path, ...]
        "doi": defaultdict(list),
        "url": defaultdict(list),
        "location_basename": defaultdict(list),
        "title_norm": defaultdict(list),
        "all_titles": [],                 # list of (norm_title, token_set, path, raw_title)
    }
    for md in SOURCES.rglob("*.md"):
        text = md.read_text(errors="replace")
        rel = str(md.relative_to(WIKI))
        # frontmatter title (from full text — only in frontmatter)
        tm = TITLE_FRONTMATTER_RE.search(text)
        title_raw = tm.group(1).strip() if tm else ""
        # Raw-Concept fields
        location = extract_field(text, "Location")
        # Own-metadata section: frontmatter + Raw Concept only (NOT cross-refs in body)
        own = _extract_own_metadata_section(text)
        for m in ARXIV_RE.finditer(own):
            idx["arxiv"][m.group(1)].append(rel)
        for m in DOI_RE.finditer(own):
            idx["doi"][m.group(1)].append(rel)
        for m in URL_RE.finditer(own):
            n = normalize_url(m.group(0))
            idx["url"][n].append(rel)
        if location:
            # parse the basename out of the location string
            # supports forms like "raw-sources/foo.pdf", "/abs/path/foo.pdf",
            # "remote-host:/path/to/foo.pdf", or just "foo.pdf"
            bn = os.path.basename(location.strip("`'\"").split()[-1] if location else "")
            if bn:
                idx["location_basename"][bn.lower()].append(rel)
        if title_raw:
            idx["title_norm"][normalize_title(title_raw)].append(rel)
            idx["all_titles"].append(
                (normalize_title(title_raw), title_token_set(title_raw), rel, title_raw)
            )
    return idx


# --- candidate-file extraction --------------------------------------------


def extract_pdf_text_first_page(path: Path) -> tuple[str, dict]:
    """Return (first_page_text, metadata_dict). Empty/empty if pypdf unavailable or fails."""
    try:
        import pypdf
    except ImportError:
        return "", {}
    try:
        reader = pypdf.PdfReader(str(path))
        md = {k.lstrip("/"): str(v) for k, v in (reader.metadata or {}).items()}
        text = ""
        if len(reader.pages) > 0:
            text = reader.pages[0].extract_text() or ""
        return text, md
    except Exception as e:
        return f"<pdf parse error: {e}>", {}


def extract_docx_text_first(path: Path) -> tuple[str, dict]:
    """Return (first_paragraphs_text, core_properties_dict)."""
    try:
        import docx
    except ImportError:
        return "", {}
    try:
        d = docx.Document(str(path))
        paras = []
        for p in d.paragraphs[:30]:  # first ~30 paragraphs is plenty for title + abstract
            t = (p.text or "").strip()
            if t:
                paras.append(t)
            if sum(len(x) for x in paras) > 4000:
                break
        cp = d.core_properties
        meta = {}
        for k in ("title", "author", "subject", "created", "modified"):
            v = getattr(cp, k, None)
            if v:
                meta[k] = str(v)
        return "\n".join(paras), meta
    except Exception as e:
        return f"<docx parse error: {e}>", {}


def candidate_extract(path: Path):
    """Pull title, arxiv, doi, urls, content_blob from a single inbox file."""
    suffix = path.suffix.lower()
    title = ""
    blob = ""
    metadata = {}
    if suffix == ".pdf":
        blob, metadata = extract_pdf_text_first_page(path)
        title = (metadata.get("Title") or "").strip()
    elif suffix == ".docx":
        blob, metadata = extract_docx_text_first(path)
        title = (metadata.get("title") or "").strip()
        if not title and blob:
            title = blob.split("\n", 1)[0][:200]
    elif suffix in (".md", ".markdown", ".txt"):
        blob = path.read_text(errors="replace")[: args.max_content_bytes]
        # md: first frontmatter or first heading
        tm = TITLE_FRONTMATTER_RE.search(blob)
        if tm:
            title = tm.group(1).strip()
        else:
            for line in blob.splitlines():
                line = line.strip()
                if line.startswith("#"):
                    title = line.lstrip("#").strip()
                    break
                elif line:
                    title = line[:200]
                    break
    else:
        return None  # skip unknown types
    blob = blob[: args.max_content_bytes]
    arxiv_ids = sorted({m.group(1) for m in ARXIV_RE.finditer(blob)})
    dois = sorted({m.group(1) for m in DOI_RE.finditer(blob)})
    urls = sorted({normalize_url(m.group(0)) for m in URL_RE.finditer(blob)})
    return {
        "title": title,
        "arxiv": arxiv_ids,
        "doi": dois,
        "urls": urls,
        "metadata": metadata,
    }


# --- match candidate against wiki index --------------------------------------


def diagnose(cand: dict, basename: str, idx) -> tuple[str, list[str]]:
    """Return (verdict, list_of_human-readable_match_lines).

    verdict ∈ {"DUPLICATE", "LIKELY", "NEW"}
    """
    notes = []
    verdict = "NEW"

    for aid in cand["arxiv"]:
        if aid in idx["arxiv"]:
            verdict = "DUPLICATE"
            for p in sorted(set(idx["arxiv"][aid])):
                notes.append(f"  arXiv ID {aid} EXACT MATCH → {p}")
    for d in cand["doi"]:
        if d in idx["doi"]:
            verdict = "DUPLICATE"
            for p in sorted(set(idx["doi"][d])):
                notes.append(f"  DOI {d} EXACT MATCH → {p}")
    for u in cand["urls"]:
        if u in idx["url"]:
            # Soften: a URL hit might be incidental (e.g. an arxiv homepage).
            # Treat as DUPLICATE only if it looks repo-shaped or arxiv/abs-shaped.
            soft = re.search(r"github\.com/.+/.+|gist\.github\.com/.+|arxiv\.org/(abs|pdf)/.+|ssrn\.com/.+abstract_id=", u)
            severity = "DUPLICATE" if soft else "LIKELY"
            if verdict == "NEW" or (verdict == "LIKELY" and severity == "DUPLICATE"):
                verdict = severity
            for p in sorted(set(idx["url"][u])):
                notes.append(f"  URL {severity} match {u} → {p}")
    bn_lower = basename.lower()
    if bn_lower in idx["location_basename"]:
        if verdict == "NEW":
            verdict = "LIKELY"
        for p in sorted(set(idx["location_basename"][bn_lower])):
            notes.append(f"  Filename in another page's Location field → {p}")
    title_norm = normalize_title(cand["title"])
    if title_norm and title_norm in idx["title_norm"]:
        verdict = "DUPLICATE"
        for p in sorted(set(idx["title_norm"][title_norm])):
            notes.append(f"  Title EXACT match → {p}")

    if verdict == "NEW" and cand["title"]:
        cts = title_token_set(cand["title"])
        if cts:
            scored = []
            for norm, toks, p, raw in idx["all_titles"]:
                j = jaccard(cts, toks)
                if j >= args.fuzzy_threshold:
                    scored.append((j, raw, p))
            scored.sort(reverse=True)
            for j, raw, p in scored[:5]:
                if verdict == "NEW":
                    verdict = "LIKELY"
                notes.append(f"  Title Jaccard {j:.2f} → {p}  ('{raw[:80]}')")
    return verdict, notes


# --- run --------------------------------------------------------------------


def main():
    print(f"Pre-ingest duplicate check")
    print(f"  inbox:  {INBOX}")
    print(f"  wiki:   {WIKI}")
    print()

    inbox_files = sorted(p for p in INBOX.iterdir() if p.is_file() and not p.name.startswith("."))
    if not inbox_files:
        print("(inbox is empty — nothing to check)")
        return 0
    print(f"Indexing existing wiki sources... ", end="", flush=True)
    idx = build_wiki_index()
    print(
        f"{sum(len(v) for v in idx['arxiv'].values())} arXiv refs, "
        f"{sum(len(v) for v in idx['doi'].values())} DOIs, "
        f"{len(idx['all_titles'])} titles cataloged from {len(list(SOURCES.rglob('*.md')))} pages"
    )
    print()

    n_dup = 0
    n_likely = 0
    n_new = 0
    for f in inbox_files:
        cand = candidate_extract(f)
        sha = sha256_file(f)
        print(f"📄 {f.name}")
        print(f"   sha256: {sha[:16]}...")
        print(f"   size:   {f.stat().st_size:,} bytes")
        if cand is None:
            print(f"   verdict: SKIP (unsupported type {f.suffix})")
            print()
            continue
        if cand["title"]:
            print(f"   title:  {cand['title'][:100]}")
        if cand["arxiv"]:
            print(f"   arXiv:  {', '.join(cand['arxiv'])}")
        if cand["doi"]:
            print(f"   DOI:    {', '.join(cand['doi'])}")
        repo_or_paper_urls = [u for u in cand["urls"] if re.search(r"github\.com/.+/.+|arxiv\.org/.+|ssrn\.com/.+|gist\.github\.com/.+", u)]
        if repo_or_paper_urls:
            print(f"   URLs (paper/repo-like): {', '.join(repo_or_paper_urls[:5])}")
        verdict, notes = diagnose(cand, f.name, idx)
        marker = {"DUPLICATE": "⛔", "LIKELY": "⚠️", "NEW": "✅"}[verdict]
        print(f"   verdict: {marker} {verdict}")
        for n in notes:
            print(n)
        if verdict == "DUPLICATE":
            n_dup += 1
        elif verdict == "LIKELY":
            n_likely += 1
        else:
            n_new += 1
        print()

    print("---")
    print(
        f"Summary: {n_new} NEW, {n_likely} LIKELY duplicates, {n_dup} DUPLICATES across "
        f"{len(inbox_files)} inbox files"
    )
    if n_dup:
        print("⛔ DUPLICATE verdicts: do NOT ingest without first deciding (re-download? supersede existing? fold into existing?).")
    if n_likely:
        print("⚠️  LIKELY verdicts: human review recommended (could be a different version / different paper with similar title).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
