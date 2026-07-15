#!/usr/bin/env python3
"""Daily research digest — Exa discovery, wiki-deduped arXiv fetch → inbox, sweep report.

Does NOT ingest wiki pages or commit. Fetched PDFs wait in `research to be indexed/`
for a morning Cursor session ("full ingest").
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

from agent_reach_daily_social import run_agent_reach_social_pass  # noqa: E402
from arxiv_api_search import arxiv_search  # noqa: E402
from daily_research_fetch import FetchOutcome, fetch_papers  # noqa: E402


def load_exa_key() -> str:
    key = load_exa_key_optional()
    if not key:
        print("ERROR: set EXA_API_KEY or write ~/.cemini/exa-api-key", file=sys.stderr)
        sys.exit(1)
    return key


def load_exa_key_optional() -> str | None:
    if os.environ.get("EXA_API_KEY"):
        return os.environ["EXA_API_KEY"].strip()
    path = Path.home() / ".cemini" / "exa-api-key"
    if path.is_file():
        return path.read_text().strip()
    return None


def normalize_url(url: str) -> str:
    u = (url or "").strip().lower().rstrip("/")
    u = re.sub(r"^https?://www\.", "https://", u)
    return u


def exa_search(
    api_key: str,
    query: str,
    from_date: str,
    category: str | None,
    num: int,
    *,
    include_domains: list[str] | None = None,
    search_type: str = "auto",
) -> dict:
    """Exa /search — billed per request (~$7/1k). Keep type=auto; never deep-* for digest."""
    payload: dict = {
        "query": query,
        "startPublishedDate": from_date,
        "numResults": num,
        "type": search_type or "auto",
    }
    if category:
        payload["category"] = category
    if include_domains:
        payload["includeDomains"] = list(include_domains)
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://api.exa.ai/search",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def normalize_exa_cfg(cfg: dict) -> dict:
    """Cost-control defaults after free Exa credits.

    Modes (paper_mode):
      arxiv-only  — free Atom API only (default; zero Exa for papers)
      arxiv-first — arXiv first; Exa only when empty (includeDomains apply)
      exa-first   — legacy Exa then arXiv fallback
      exa-only    — Exa only (no arXiv)
    """
    exa = dict(cfg.get("exa") or {})
    exa.setdefault("news_enabled", False)
    exa.setdefault("paper_mode", "arxiv-only")
    exa.setdefault("search_type", "auto")
    domains = exa.get("include_domains")
    if domains is None:
        exa["include_domains"] = ["arxiv.org"]
    return exa


def title_from_result(r: dict) -> str:
    title = (r.get("title") or "").strip()
    if title:
        return title[:200]
    for line in (r.get("text") or "").splitlines():
        line = line.strip()
        if 30 <= len(line) <= 200 and not line.startswith(("[", "#")):
            return line
    return "(no title)"


def inbox_files(repo: Path) -> list[Path]:
    inbox = repo / "research to be indexed"
    if not inbox.is_dir():
        return []
    return sorted(
        p for p in inbox.iterdir()
        if p.is_file() and not p.name.startswith(".")
    )


def run_preingest(repo: Path) -> str:
    script = repo / "scripts" / "preingest_check.py"
    if not script.is_file():
        return "(preingest_check.py not found)"
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(repo),
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        return (proc.stdout or proc.stderr or "").strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return "(preingest_check timed out after 120s)"
    except OSError as e:
        return f"(preingest_check failed: {e})"


def gap_detect_status(repo: Path) -> tuple[bool, str]:
    meta = repo / "wiki" / "meta" / "wiki-gap-detect-cadence.md"
    if not meta.is_file():
        return False, "no cadence file"
    text = meta.read_text(encoding="utf-8")
    last_m = re.search(r"\|\s*\*\*Last run\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})", text)
    if not last_m:
        return True, "last run unknown — consider running gap detect"
    last = date.fromisoformat(last_m.group(1))
    age = (date.today() - last).days
    due = age >= 7
    msg = f"{age}d since last run ({last.isoformat()})"
    return due, msg


def load_config(repo: Path) -> dict:
    path = repo / "scripts" / "daily_research_config.yaml"
    if not path.is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def run_queries(
    api_key: str | None,
    query_defs: list[dict],
    from_date: str,
    default_per_query: int,
    seen_urls: set[str],
    *,
    include_domains: list[str] | None = None,
    search_type: str = "auto",
) -> tuple[list[tuple[str, str, str | None, list[dict]]], bool]:
    sections: list[tuple[str, str, str | None, list[dict]]] = []
    partial = False
    if not api_key:
        for q in query_defs:
            query = q.get("query", "")
            if query:
                sections.append((q.get("cluster", "unknown"), query, q.get("category"), []))
        return sections, True

    for q in query_defs:
        cluster = q.get("cluster", "unknown")
        query = q.get("query", "")
        category = q.get("category")
        per_query = int(q.get("num_results", default_per_query))
        if not query:
            continue
        try:
            data = exa_search(
                api_key,
                query,
                from_date,
                category,
                per_query,
                include_domains=include_domains,
                search_type=search_type,
            )
            raw = data.get("results") or []
        except urllib.error.HTTPError as e:
            partial = True
            raw = []
            print(f"WARNING: {cluster} HTTP {e.code}", file=sys.stderr)
        except Exception as e:
            partial = True
            raw = []
            print(f"WARNING: {cluster} {e}", file=sys.stderr)

        deduped: list[dict] = []
        for r in raw:
            url = r.get("url") or ""
            key = normalize_url(url)
            if not key or key in seen_urls:
                continue
            seen_urls.add(key)
            deduped.append(r)
        sections.append((cluster, query, category, deduped))
    return sections, partial


def _dedupe_results(
    raw: list[dict], seen_urls: set[str]
) -> list[dict]:
    deduped: list[dict] = []
    for r in raw:
        url = r.get("url") or ""
        key = normalize_url(url)
        if not key or key in seen_urls:
            continue
        seen_urls.add(key)
        deduped.append(r)
    return deduped


def run_paper_queries(
    api_key: str | None,
    query_defs: list[dict],
    from_date: str,
    default_per_query: int,
    seen_urls: set[str],
    arxiv_cfg: dict,
    exa_cfg: dict,
) -> tuple[list[tuple[str, str, str | None, list[dict], str]], bool, int]:
    """Paper lane — mode-driven (default arxiv-only to avoid Exa burn)."""
    sections: list[tuple[str, str, str | None, list[dict], str]] = []
    partial = False
    arxiv_used_count = 0
    fallback_enabled = bool(arxiv_cfg.get("enabled", True))
    interval = float(arxiv_cfg.get("request_interval_seconds", 3))
    max_terms = int(arxiv_cfg.get("max_terms_per_query", 6))
    paper_mode = str(exa_cfg.get("paper_mode") or "arxiv-only").strip().lower()
    include_domains = exa_cfg.get("include_domains") or None
    search_type = str(exa_cfg.get("search_type") or "auto")

    for q in query_defs:
        cluster = q.get("cluster", "unknown")
        query = q.get("query", "")
        category = q.get("category")
        per_query = int(q.get("num_results", default_per_query))
        if not query:
            continue

        # Per-query overrides (rare paid enrichment clusters)
        q_mode = str(q.get("paper_mode") or paper_mode).strip().lower()
        q_domains = q.get("include_domains")
        if q_domains is None:
            q_domains = include_domains

        raw: list[dict] = []
        source = "none"
        exa_failed = False

        def _call_arxiv() -> list[dict]:
            nonlocal arxiv_used_count
            if not fallback_enabled and q_mode not in ("arxiv-only", "arxiv-first"):
                return []
            aq = (q.get("arxiv_query") or "").strip() or None
            hits = arxiv_search(
                query,
                from_date,
                max_results=per_query,
                request_interval_seconds=interval,
                max_terms=max_terms,
                arxiv_query=aq,
            )
            if hits:
                arxiv_used_count += 1
                via = "arxiv_query" if aq else "nl-map"
                print(
                    f"INFO: {cluster} arXiv API ({len(hits)} hits) [{q_mode}/{via}]",
                    file=sys.stderr,
                )
            return hits

        def _call_exa() -> list[dict]:
            nonlocal exa_failed, partial
            if not api_key:
                exa_failed = True
                partial = True
                return []
            try:
                data = exa_search(
                    api_key,
                    query,
                    from_date,
                    category,
                    per_query,
                    include_domains=q_domains,
                    search_type=search_type,
                )
                return data.get("results") or []
            except urllib.error.HTTPError as e:
                exa_failed = True
                partial = True
                print(f"WARNING: {cluster} HTTP {e.code}", file=sys.stderr)
                return []
            except Exception as e:
                exa_failed = True
                partial = True
                print(f"WARNING: {cluster} {e}", file=sys.stderr)
                return []

        if q_mode == "arxiv-only":
            raw = _call_arxiv()
            source = "arxiv-api" if raw else "none"
        elif q_mode == "arxiv-first":
            raw = _call_arxiv()
            if raw:
                source = "arxiv-api"
            else:
                raw = _call_exa()
                source = "exa" if raw else ("exa-empty" if not exa_failed else "exa-failed")
                if not raw and not exa_failed:
                    source = "none"
        elif q_mode == "exa-only":
            raw = _call_exa()
            source = "exa" if raw else ("exa-failed" if exa_failed else "none")
        else:  # exa-first (legacy)
            raw = _call_exa()
            if raw:
                source = "exa"
            elif fallback_enabled and (exa_failed or not api_key or not raw):
                raw = _call_arxiv()
                source = "arxiv-api" if raw else ("exa-failed" if exa_failed else "none")
            else:
                source = "exa-failed" if exa_failed else "none"

        deduped = _dedupe_results(raw, seen_urls)
        sections.append((cluster, query, category, deduped, source))

    return sections, partial, arxiv_used_count


def render_fetch_table(outcomes: list[FetchOutcome]) -> list[str]:
    lines = [
        "| Status | arXiv | Title | File / reason |",
        "|--------|-------|-------|---------------|",
    ]
    for o in outcomes:
        title = o.title.replace("|", "\\|")[:80]
        file_col = o.path or o.detail[:80]
        aid = o.arxiv_id or "—"
        lines.append(f"| {o.status} | `{aid}` | {title} | {file_col} |")
    return lines


def repo_root() -> Path:
    """Wiki repo root — env set by ~/bin LaunchAgent wrappers (not Desktop script path)."""
    for key in ("CEMINI_WIKI_ROOT", "WIKI_ROOT"):
        val = os.environ.get(key)
        if val:
            return Path(val)
    return Path(__file__).resolve().parent.parent


def main() -> int:
    repo = repo_root()
    cfg = load_config(repo)
    loop = cfg.get("loop") or {}
    fetch_cfg = cfg.get("fetch") or {}
    exa_cfg = normalize_exa_cfg(cfg)
    window = int(loop.get("recency_window_days", 7))
    per_query = int(loop.get("max_results_per_query", 3))
    per_paper = int(fetch_cfg.get("max_results_per_paper_query", 5))
    today = date.today()
    from_date = (today - timedelta(days=window)).isoformat()

    out_tpl = (cfg.get("output") or {}).get("path_template", "wiki/sweeps/{date}-daily.md")
    report = repo / out_tpl.format(date=today.isoformat())
    report.parent.mkdir(parents=True, exist_ok=True)

    paper_mode = str(exa_cfg.get("paper_mode") or "arxiv-only").lower()
    news_enabled = bool(exa_cfg.get("news_enabled"))
    needs_exa = news_enabled or paper_mode in ("exa-first", "arxiv-first", "exa-only")

    api_key = load_exa_key_optional()
    if needs_exa and not api_key:
        print(
            "WARNING: no Exa API key — paper lane uses arXiv where allowed; news lane skipped",
            file=sys.stderr,
        )
    paper_defs = cfg.get("paper_queries") or []
    news_defs = (cfg.get("queries") or []) if news_enabled else []
    news_defs_configured = len(cfg.get("queries") or [])
    arxiv_cfg = cfg.get("arxiv_fallback") or {}
    active_topics = cfg.get("active_topics") or []
    brief_note = (cfg.get("brief_routing_note") or "").strip()
    social = cfg.get("social") or {}
    agent_reach_social = run_agent_reach_social_pass(repo, cfg, today)

    seen_urls: set[str] = set()
    paper_sections, paper_partial, arxiv_fallback_clusters = run_paper_queries(
        api_key,
        paper_defs,
        from_date,
        per_paper,
        seen_urls,
        arxiv_cfg,
        exa_cfg,
    )
    if news_enabled:
        news_sections, news_partial = run_queries(
            api_key,
            news_defs,
            from_date,
            per_query,
            seen_urls,
            search_type=str(exa_cfg.get("search_type") or "auto"),
        )
    else:
        news_sections, news_partial = [], False
    partial = paper_partial or news_partial

    # fetch_papers expects 4-tuple sections (no source field)
    paper_sections_for_fetch = [
        (cluster, query, category, results)
        for cluster, query, category, results, _source in paper_sections
    ]

    fetch_outcomes: list[FetchOutcome] = []
    if fetch_cfg.get("enabled", True) and paper_sections_for_fetch:
        fetch_outcomes = fetch_papers(
            repo,
            paper_sections_for_fetch,
            max_downloads=int(fetch_cfg.get("max_downloads", 8)),
            fetch_likely=bool(fetch_cfg.get("fetch_likely", False)),
        )

    inbox = inbox_files(repo)
    gap_due, gap_msg = gap_detect_status(repo)
    preingest_out = run_preingest(repo) if inbox else ""

    n_fetched = sum(1 for o in fetch_outcomes if o.status == "fetched")
    n_skipped_dup = sum(1 for o in fetch_outcomes if o.status == "skipped-dup")
    fetched_names = {o.path for o in fetch_outcomes if o.status == "fetched" and o.path}

    paper_lane_note = {
        "arxiv-only": (
            f"Paper lane: {len(paper_defs)} queries via **free arXiv API** "
            f"(exa.paper_mode=arxiv-only; zero Exa paper calls)."
        ),
        "arxiv-first": (
            f"Paper lane: {len(paper_defs)} queries (arXiv first; Exa only when empty, "
            f"domains={exa_cfg.get('include_domains')})."
        ),
        "exa-first": (
            f"Paper lane: {len(paper_defs)} queries (Exa first; arXiv fallback when Exa fails)."
        ),
        "exa-only": f"Paper lane: {len(paper_defs)} Exa-only queries (wiki-deduped).",
    }.get(
        paper_mode,
        f"Paper lane: {len(paper_defs)} queries (mode={paper_mode}).",
    )
    if news_enabled:
        news_lane_note = f"News lane: {len(news_defs)} Exa queries (digest only)."
    else:
        news_lane_note = (
            f"News lane: **disabled** (`exa.news_enabled=false`; "
            f"{news_defs_configured} queries retained in config)."
        )
    lines = [
        f"# Daily Research Digest — {today.isoformat()}",
        "",
        f"Window: `{from_date}` → `{today.isoformat()}` ({window} days). "
        f"{paper_lane_note} "
        f"{news_lane_note}",
        "",
    ]
    if arxiv_fallback_clusters:
        lines.append(
            f"_Paper discovery: **{arxiv_fallback_clusters}** cluster(s) used free arXiv API._"
        )
        lines.append("")
    lines.extend(
        [
        "Reference: `@scripts/daily_research_config.yaml`. "
        "**Does NOT ingest wiki** — fetched arXiv PDFs go to `research to be indexed/`.",
        "",
        "---",
        "",
        "## Active topics (sync from ROADMAP)",
        "",
        ]
    )
    for t in active_topics:
        lines.append(f"- {t}")
    if brief_note:
        lines.extend(
            [
                "",
                "### Brief routing",
                "",
                brief_note.strip(),
                "",
                "Canonical: `scripts/active_project_brief_targets.yaml` · @concepts/active-project-research-routing.md",
            ]
        )
    lines.extend(["", "---", ""])

    lines.extend(["## Inbox (`research to be indexed/`)", ""])
    if inbox:
        lines.append(
            f"**{len(inbox)} file(s) ready** — say **full ingest** in Cursor to start the ingest ritual:"
        )
        lines.append("")
        for p in inbox:
            tag = " _(new tonight)_" if p.name in fetched_names else ""
            lines.append(f"- `{p.name}`{tag}")
        lines.extend(["", "### preingest_check", "", "```", preingest_out[:6000], "```", ""])
    else:
        lines.append("_Empty — no PDFs fetched overnight (all hits were dupes or non-arXiv)._")
        lines.append("")

    if fetch_outcomes:
        lines.extend(
            [
                "---",
                "",
                "## Auto-fetched papers (overnight)",
                "",
                f"Downloaded **{n_fetched}** new PDF(s); skipped **{n_skipped_dup}** wiki/inbox duplicates.",
                "",
            ]
        )
        lines.extend(render_fetch_table(fetch_outcomes))
        lines.append("")

    lines.extend(["---", "", "## Paper candidates", ""])
    paper_total = 0
    for i, (cluster, query, category, results, source) in enumerate(paper_sections, 1):
        cat_label = category or "research paper"
        if source == "arxiv-api":
            src_label = "arXiv API"
        elif source in ("exa", "exa-empty", "exa-failed"):
            src_label = "Exa"
        else:
            src_label = source or "none"
        lines.append(f"### P{i}: {cluster} ({len(results)} hits · {src_label})")
        lines.append("")
        lines.append(f"Query: `{query}` · category: `{cat_label}`")
        lines.append("")
        lines.append("| Date | Title | URL |")
        lines.append("|------|-------|-----|")
        for r in results:
            url = r.get("url", "")
            d = (r.get("publishedDate") or "")[:10]
            title = title_from_result(r).replace("|", "\\|")[:100]
            lines.append(f"| {d} | [{title}]({url}) | {url[:70]}… |" if len(url) > 70 else f"| {d} | [{title}]({url}) | {url} |")
        lines.append("")
        paper_total += len(results)

    lines.extend(["---", "", "## News & links (not auto-downloaded)", ""])
    if not news_enabled:
        lines.append(
            "_Skipped — `exa.news_enabled: false` (set true to spend Exa credits on digest-only news)._ "
            f"Config still lists **{news_defs_configured}** news queries."
        )
        lines.append("")
    news_total = 0
    row_id = 0
    for i, (cluster, query, category, results) in enumerate(news_sections, 1):
        cat_label = category or "auto"
        lines.append(f"### Q{i}: {cluster} ({len(results)} hits)")
        lines.append("")
        lines.append(f"Query: `{query}` · category: `{cat_label}`")
        lines.append("")
        lines.append("| Pick | Date | Title | Cluster | URL |")
        lines.append("|------|------|-------|---------|-----|")
        for r in results:
            row_id += 1
            url = r.get("url", "")
            d = (r.get("publishedDate") or "")[:10]
            title = title_from_result(r)
            safe_title = title.replace("|", "\\|")[:100]
            lines.append(
                f"| [ ] R{row_id} | {d} | [{safe_title}]({url}) | {cluster} | {url[:60]}… |"
                if len(url) > 60
                else f"| [ ] R{row_id} | {d} | [{safe_title}]({url}) | {cluster} | {url} |"
            )
        lines.append("")
        news_total += len(results)

    lines.extend(["---", "", "## Wiki gap detect", ""])
    if gap_due:
        lines.append(f"**DUE** — {gap_msg}. Run: `bash scripts/run_wiki_gap_detect.sh`")
    else:
        lines.append(f"OK — {gap_msg}.")
    lines.append("")

    manual = social.get("manual_pass") or []
    if agent_reach_social.enabled:
        lines.extend(agent_reach_social.lines)

    if manual:
        lines.extend(["---", "", "## Social pass (Cursor session — not automated)", ""])
        for item in manual:
            tool = item.get("tool", "reader")
            prompt = item.get("prompt", "")
            lines.append(f"- **{tool}**: {prompt}")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Morning ingest (copy into Cursor)",
            "",
            "```",
            "Full ingest — process everything in research to be indexed/ and any checked rows above.",
            "- preingest_check → discuss takeaways → 3–15 wiki pages → lint → ingest_session_gate → commit",
            "- Briefs: co-primary per scripts/active_project_brief_targets.yaml (poker · ceminidfs · xsp-killer · family-tree); secondary: wc-ticket-monitor · pm-kalshi · castle-sim (legacy)",
            "- Do NOT auto-scp generic quant-finance / MAPPO / Riskfolio briefs to cemini-prod",
            "```",
            "",
            "---",
            "",
            "## Summary",
            "",
            "| Metric | Count |",
            "|--------|-------|",
            f"| Paper hits (deduped) | {paper_total} |",
            f"| arXiv API fallback clusters | {arxiv_fallback_clusters} |",
            f"| PDFs fetched to inbox | {n_fetched} |",
            f"| Dupes skipped | {n_skipped_dup} |",
            f"| News hits (digest only) | {news_total} |",
            f"| Inbox files (total) | {len(inbox)} |",
            f"| Gap detect due | {'yes' if gap_due else 'no'} |",
            "",
            "### Next steps",
            "",
            "1. Say **full ingest** if inbox has PDFs.",
            "2. Optional: check news rows `R1`… for URLs worth manual fetch.",
            "3. Optional: social pass tools above.",
            "",
            "### Discard",
            "",
            f"`rm wiki/sweeps/{today.isoformat()}-daily.md` if nothing worth acting on.",
            "",
        ]
    )

    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report}")
    if n_fetched:
        print(f"Inbox: {n_fetched} new PDF(s) in research to be indexed/")

    meta = repo / "wiki" / "meta" / "daily-research-digest-cadence.md"
    if meta.is_file():
        text = meta.read_text(encoding="utf-8")
        text = re.sub(
            r"(\|\s*\*\*Last run\*\*\s*\|\s*)[^\|]+",
            rf"\g<1>{today.isoformat()} ",
            text,
            count=1,
        )
        meta.write_text(text, encoding="utf-8")

    return 3 if partial else 0


if __name__ == "__main__":
    raise SystemExit(main())
