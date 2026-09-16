#!/usr/bin/env python3
"""Free arXiv Atom API search — Exa fallback for daily research digest.

Keyword search stays on export.arxiv.org Atom API. Official OAI-PMH
(https://oaipmh.arxiv.org/oai) is a full-corpus metadata harvest, not a
search fallback — candidate for a later nightly mirror, not used here.
"""

from __future__ import annotations

import fcntl
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

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
_ARXIV_LOCK_REL = Path(".cemini") / "arxiv-api.lock"
_MAX_ATTEMPTS = 3


def natural_query_to_arxiv_search(query: str, *, max_terms: int = 4) -> str:
    """Map a natural-language digest query to arXiv API search_query syntax.

    Exa-style AND of 6+ tokens almost never hits within a short window. Prefer:
    - explicit Atomic queries already containing ``all:`` / ``ti:`` / ``abs:``
    - otherwise: (core1 AND core2) OR specialty_terms  (sparse OR, not dense AND)
    """
    q = (query or "").strip()
    if not q:
        return ""

    # Already Atom/API syntax — pass through (strip leading "arxiv " noise only)
    low = q.lower()
    if re.search(r"\b(all|ti|abs|au|cat):", low) or "site:arxiv.org" in low:
        q2 = re.sub(r"(?i)\bsite:arxiv\.org\b", " ", q)
        q2 = re.sub(r"(?i)\barxiv\b", " ", q2)
        q2 = re.sub(r"\s+", " ", q2).strip()
        return q2

    q = low
    q = re.sub(r"\bresearch\s+paper\b", " ", q)
    q = re.sub(r"\barxiv\b", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    if not q:
        return ""

    branches = re.split(r"\s+or\s+", q, flags=re.I)
    branch_queries: list[str] = []
    max_terms = max(2, min(int(max_terms), 6))

    for branch in branches[:3]:
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
        if not terms:
            continue
        # Dense AND of every token is too tight — use core AND + OR of the rest.
        if len(terms) == 1:
            branch_queries.append(terms[0])
        elif len(terms) == 2:
            branch_queries.append(" AND ".join(terms))
        else:
            core = " AND ".join(terms[:2])
            extras = " OR ".join(terms[2:])
            branch_queries.append(f"({core}) OR ({extras})")

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


def _retry_sleep_seconds(exc: BaseException, attempt: int) -> float:
    """Retry-After seconds if parseable, else 5 * 2^attempt (5, 10, 20)."""
    if isinstance(exc, urllib.error.HTTPError):
        headers = getattr(exc, "headers", None)
        raw = headers.get("Retry-After") if headers is not None else None
        if raw:
            try:
                return max(0.0, float(str(raw).strip()))
            except ValueError:
                pass
    return float(5 * (2 ** attempt))


def arxiv_search(
    natural_query: str,
    from_date: str,
    *,
    max_results: int = 5,
    request_interval_seconds: float = 3.0,
    max_terms: int = 4,
    arxiv_query: str | None = None,
) -> list[dict]:
    """Run one arXiv API query; returns Exa-shaped hits (url, title, publishedDate).

    Prefer ``arxiv_query`` (raw Atom syntax) when provided — NL mapping is best-effort.
    """
    search_query = (arxiv_query or "").strip() or natural_query_to_arxiv_search(
        natural_query, max_terms=max_terms
    )
    if not search_query:
        return []

    params = urllib.parse.urlencode(
        {
            "search_query": search_query,
            "start": 0,
            # Over-fetch then date-filter: short windows otherwise starve after AND/OR map.
            "max_results": max(1, min(max(max_results * 5, 25), 50)),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    lock_path = Path.home() / _ARXIV_LOCK_REL
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_f = open(lock_path, "a+")
    xml_text = ""
    try:
        fcntl.flock(lock_f.fileno(), fcntl.LOCK_EX)
        _throttle(request_interval_seconds)
        last_err: BaseException | None = None
        for attempt in range(_MAX_ATTEMPTS):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    xml_text = resp.read().decode("utf-8", errors="replace")
                break
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code in (429, 503) and attempt < _MAX_ATTEMPTS - 1:
                    time.sleep(_retry_sleep_seconds(e, attempt))
                    continue
                print(f"WARNING: arXiv API {e}", file=sys.stderr)
                return []
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last_err = e
                msg = str(e).lower()
                retryable = "timed out" in msg or "429" in msg
                if retryable and attempt < _MAX_ATTEMPTS - 1:
                    time.sleep(_retry_sleep_seconds(e, attempt))
                    continue
                print(f"WARNING: arXiv API {e}", file=sys.stderr)
                return []
        else:
            if last_err is not None:
                print(f"WARNING: arXiv API {last_err}", file=sys.stderr)
            return []
    finally:
        try:
            fcntl.flock(lock_f.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        lock_f.close()

    parsed = parse_arxiv_atom(xml_text, from_date=from_date)
    return parsed[:max_results]
