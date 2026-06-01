#!/usr/bin/env python3
"""Wiki source index for URL/arXiv duplicate checks (preingest + daily digest fetch)."""

from __future__ import annotations

import os
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})(v\d+)?\b")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[A-Za-z0-9._;()<>/-]+)\b")
URL_RE = re.compile(r"https?://[^\s`<>\)]+")
TITLE_FRONTMATTER_RE = re.compile(r'^title:\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)
RC_FIELD_RE_TEMPLATE = r"^\s*-\s+\*\*{key}\*\*:\s*(.+?)\s*$"

STOPWORDS = {
    "a", "an", "the", "of", "and", "or", "for", "to", "in", "on", "with",
    "by", "from", "is", "are", "as", "at", "via", "vs", "into", "over",
    "under", "between", "across", "using", "based", "toward", "towards",
}


def arxiv_id_from_url(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url, re.I)
    return m.group(1) if m else None


def normalize_title(t: str) -> str:
    if not t:
        return ""
    nfkd = unicodedata.normalize("NFKD", t)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    ascii_only = re.sub(r"[^a-z0-9]+", " ", ascii_only.lower()).strip()
    return re.sub(r"\s+", " ", ascii_only)


def title_token_set(t: str) -> set[str]:
    norm = normalize_title(t)
    if not norm:
        return set()
    return {w for w in norm.split() if w not in STOPWORDS and len(w) > 1}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def normalize_url(u: str) -> str:
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
    rx = re.compile(RC_FIELD_RE_TEMPLATE.format(key=re.escape(key)), re.MULTILINE)
    m = rx.search(text)
    return m.group(1).strip() if m else ""


def _extract_own_metadata_section(text: str) -> str:
    parts = text.split("---", 2)
    fm = parts[1] if len(parts) >= 2 else ""
    rc = ""
    m = re.search(r"^## Raw Concept\s*\n(.*?)(?=^##\s)", text, re.MULTILINE | re.DOTALL)
    if m:
        rc = m.group(1)
    return fm + "\n" + rc


def build_wiki_index(sources_dir: Path) -> dict:
    idx = {
        "arxiv": defaultdict(list),
        "doi": defaultdict(list),
        "url": defaultdict(list),
        "location_basename": defaultdict(list),
        "title_norm": defaultdict(list),
        "all_titles": [],
    }
    wiki = sources_dir.parent
    for md in sources_dir.rglob("*.md"):
        text = md.read_text(errors="replace")
        rel = str(md.relative_to(wiki))
        tm = TITLE_FRONTMATTER_RE.search(text)
        title_raw = tm.group(1).strip() if tm else ""
        location = extract_field(text, "Location")
        own = _extract_own_metadata_section(text)
        for m in ARXIV_RE.finditer(own):
            idx["arxiv"][m.group(1)].append(rel)
        for m in DOI_RE.finditer(own):
            idx["doi"][m.group(1)].append(rel)
        for m in URL_RE.finditer(own):
            idx["url"][normalize_url(m.group(0))].append(rel)
        if location:
            bn = os.path.basename(location.strip("`'\"").split()[-1] if location else "")
            if bn:
                idx["location_basename"][bn.lower()].append(rel)
        if title_raw:
            idx["title_norm"][normalize_title(title_raw)].append(rel)
            idx["all_titles"].append(
                (normalize_title(title_raw), title_token_set(title_raw), rel, title_raw)
            )
    return idx


def inbox_arxiv_ids(inbox: Path) -> set[str]:
    ids: set[str] = set()
    if not inbox.is_dir():
        return ids
    for p in inbox.iterdir():
        if not p.is_file() or p.name.startswith("."):
            continue
        for m in ARXIV_RE.finditer(p.name):
            ids.add(m.group(1))
    return ids


def verdict_for_remote_hit(
    url: str,
    title: str,
    idx: dict,
    inbox_ids: set[str],
    *,
    fuzzy_threshold: float = 0.5,
) -> tuple[str, list[str]]:
    """Return (NEW|LIKELY|DUPLICATE, notes) for an Exa hit before download."""
    notes: list[str] = []
    verdict = "NEW"

    aid = arxiv_id_from_url(url)
    if aid:
        if aid in inbox_ids:
            return "DUPLICATE", [f"arXiv {aid} already in inbox"]
        if aid in idx["arxiv"]:
            paths = sorted(set(idx["arxiv"][aid]))
            return "DUPLICATE", [f"arXiv {aid} in wiki → {', '.join(paths[:3])}"]

    nu = normalize_url(url)
    if nu in idx["url"]:
        soft = re.search(
            r"github\.com/.+/.+|gist\.github\.com/.+|arxiv\.org/(abs|pdf)/.+|ssrn\.com/.+abstract_id=",
            nu,
        )
        severity = "DUPLICATE" if soft else "LIKELY"
        verdict = severity
        for p in sorted(set(idx["url"][nu]))[:3]:
            notes.append(f"URL {severity} → {p}")

    title_norm = normalize_title(title)
    if title_norm and title_norm in idx["title_norm"]:
        verdict = "DUPLICATE"
        for p in sorted(set(idx["title_norm"][title_norm]))[:3]:
            notes.append(f"Title exact → {p}")

    if verdict == "NEW" and title:
        cts = title_token_set(title)
        if cts:
            for _norm, toks, p, raw in idx["all_titles"]:
                if jaccard(cts, toks) >= fuzzy_threshold:
                    verdict = "LIKELY"
                    notes.append(f"Title fuzzy → {p} ('{raw[:60]}')")
                    break

    return verdict, notes
