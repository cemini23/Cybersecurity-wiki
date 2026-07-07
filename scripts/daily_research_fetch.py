#!/usr/bin/env python3
"""Download non-duplicate arXiv PDFs from daily digest paper hits into the inbox."""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from wiki_source_index import (  # noqa: E402
    arxiv_id_from_url,
    build_wiki_index,
    inbox_arxiv_ids,
    verdict_for_remote_hit,
)


@dataclass
class FetchOutcome:
    cluster: str
    title: str
    url: str
    arxiv_id: str | None
    status: str  # fetched | skipped-dup | skipped-likely | skipped-no-arxiv | skipped-cap | failed
    path: str | None = None
    detail: str = ""


def safe_slug(title: str, max_len: int = 48) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return (slug[:max_len] or "paper").strip("-")


def inbox_dest(inbox: Path, arxiv_id: str, title: str) -> Path:
    return inbox / f"arxiv-{arxiv_id}-{safe_slug(title)}.pdf"


def download_arxiv_pdf(arxiv_id: str, dest: Path) -> None:
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "cemini-daily-digest/1.0 (OSINT workspace)"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    if len(data) < 1024 or not data[:5].startswith(b"%PDF"):
        raise ValueError("response is not a PDF")
    dest.write_bytes(data)


def fetch_papers(
    repo: Path,
    paper_sections: list[tuple[str, str, str | None, list[dict]]],
    *,
    max_downloads: int,
    fetch_likely: bool = False,
) -> list[FetchOutcome]:
    inbox = repo / "research to be indexed"
    inbox.mkdir(parents=True, exist_ok=True)
    sources = repo / "wiki" / "sources"
    idx = build_wiki_index(sources)
    pending_inbox = inbox_arxiv_ids(inbox)

    outcomes: list[FetchOutcome] = []
    downloaded = 0
    seen_arxiv: set[str] = set()

    for cluster, _query, _category, results in paper_sections:
        for r in results:
            url = (r.get("url") or "").strip()
            title = (r.get("title") or "").strip() or "(no title)"
            aid = arxiv_id_from_url(url)

            if not aid:
                outcomes.append(
                    FetchOutcome(cluster, title, url, None, "skipped-no-arxiv", detail="not arxiv.org")
                )
                continue

            if aid in seen_arxiv:
                outcomes.append(
                    FetchOutcome(cluster, title, url, aid, "skipped-dup", detail="duplicate in this run")
                )
                continue
            seen_arxiv.add(aid)

            verdict, notes = verdict_for_remote_hit(url, title, idx, pending_inbox)
            if verdict == "DUPLICATE":
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, aid, "skipped-dup", detail="; ".join(notes) or verdict
                    )
                )
                continue
            if verdict == "LIKELY" and not fetch_likely:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, aid, "skipped-likely", detail="; ".join(notes) or verdict
                    )
                )
                continue

            if downloaded >= max_downloads:
                outcomes.append(
                    FetchOutcome(cluster, title, url, aid, "skipped-cap", detail=f"cap {max_downloads}")
                )
                continue

            dest = inbox_dest(inbox, aid, title)
            if dest.is_file():
                outcomes.append(
                    FetchOutcome(cluster, title, url, aid, "skipped-dup", str(dest.name), "file exists")
                )
                pending_inbox.add(aid)
                continue

            try:
                download_arxiv_pdf(aid, dest)
                downloaded += 1
                pending_inbox.add(aid)
                outcomes.append(FetchOutcome(cluster, title, url, aid, "fetched", dest.name))
            except (urllib.error.URLError, OSError, ValueError) as e:
                outcomes.append(
                    FetchOutcome(cluster, title, url, aid, "failed", detail=str(e)[:200])
                )

    return outcomes
