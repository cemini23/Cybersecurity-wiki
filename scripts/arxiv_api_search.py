#!/usr/bin/env python3
"""Free arXiv Atom API search — Exa fallback for daily research digest."""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_API = "https://export.arxiv.org/api/query"
USER_AGENT = "cemini-daily-digest/1.0 (OSINT workspace; mailto:local)"

ARXIV_STOPWORDS = {
    "a", "an", "the", "of", "and", "or", "for", "to", "in", "on", "with",
    "by", "from", "is", "are", "as", "at", "via", "vs", "into", "over",
    "under", "between", "across", "using", "based", "toward", "towards",
    "research", "paper", "papers", "study", "arxiv", "new", "recent",
}

_LAST_REQUEST_AT = 0.0


def natural_query_to_arxiv_search(query: str, *, max_terms: int = 6) -> str:
    """Map a natural-language digest query to arXiv API search_query syntax."""
    q = (query or "").strip().lower()
    q = re.sub(r"\bresearch\s+paper\b", " ", q)
    q = re.sub(r"\barxiv\b", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    if not q:
        return ""

    branches = re.split(r"\s+or\s+", q, flags=re.I)
    branch_queries: list[str] = []
    for branch in branches[:2]:
        phrases = re.findall(r'"([^"]+)"', branch)
        branch = re.sub(r'"[^"]+"', " ", branch)
        tokens = [
            w
            for w in re.findall(r"[a-z0-9]{3,}", branch)
            if w not in ARXIV_STOPWORDS
        ]
        terms: list[str] = []
        seen: set[str] = set()
        for phrase in phrases:
            phrase = phrase.strip()
            if phrase and phrase not in seen:
                seen.add(phrase)
                terms.append(f'all:"{phrase}"')
        for token in tokens:
            if token in seen:
                continue
            seen.add(token)
            terms.append(f"all:{token}")
            if len(terms) >= max_terms:
                break
        if terms:
            branch_queries.append(" AND ".join(terms[:max_terms]))

    if not branch_queries:
        return ""
    if len(branch_queries) == 1:
        return branch_queries[0]
    return "(" + ") OR (".join(branch_queries) + ")"


def arxiv_id_from_entry_id(entry_id: str) -> str | None:
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", entry_id or "", re.I)
    return m.group(1) if m else None


def parse_arxiv_atom(xml_text: str, *, from_date: str) -> list[dict]:
    """Parse Atom feed into Exa-compatible result dicts (arxiv abs URLs only)."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    cutoff: date | None = None
    try:
        cutoff = date.fromisoformat(from_date[:10])
    except ValueError:
        cutoff = None

    results: list[dict] = []
    for entry in root.findall(f"{ATOM}entry"):
        entry_id = (entry.findtext(f"{ATOM}id") or "").strip()
        aid = arxiv_id_from_entry_id(entry_id)
        if not aid:
            continue

        published = ""
        for tag in ("published", "updated"):
            el = entry.find(f"{ATOM}{tag}")
            if el is not None and el.text:
                published = el.text.strip()
                break
        if cutoff and published:
            try:
                if date.fromisoformat(published[:10]) < cutoff:
                    continue
            except ValueError:
                pass

        title = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}title") or "").strip())
        url = f"https://arxiv.org/abs/{aid}"
        results.append(
            {
                "url": url,
                "title": title[:200] if title else "(no title)",
                "publishedDate": published[:10] if published else "",
                "source": "arxiv-api",
            }
        )
    return results


def _throttle(interval_seconds: float) -> None:
    global _LAST_REQUEST_AT
    if interval_seconds <= 0:
        return
    now = time.monotonic()
    wait = interval_seconds - (now - _LAST_REQUEST_AT)
    if wait > 0:
        time.sleep(wait)
    _LAST_REQUEST_AT = time.monotonic()


def arxiv_search(
    natural_query: str,
    from_date: str,
    *,
    max_results: int = 5,
    request_interval_seconds: float = 3.0,
    max_terms: int = 6,
) -> list[dict]:
    """Run one arXiv API query; returns Exa-shaped hits (url, title, publishedDate)."""
    search_query = natural_query_to_arxiv_search(natural_query, max_terms=max_terms)
    if not search_query:
        return []

    params = urllib.parse.urlencode(
        {
            "search_query": search_query,
            "start": 0,
            "max_results": max(1, min(max_results, 30)),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API}?{params}"
    _throttle(request_interval_seconds)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            xml_text = resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError) as e:
        print(f"WARNING: arXiv API {e}", file=sys.stderr)
        return []

    parsed = parse_arxiv_atom(xml_text, from_date=from_date)
    # API may return older papers before cutoff — keep client-side filter, cap count.
    return parsed[:max_results]
