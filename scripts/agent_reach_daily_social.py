"""Optional Agent Reach/OpenCLI social pass for the daily research digest."""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml

try:
    from .agent_reach_wrapper import SourceAllowlist
    from .agent_reach_wrapper.manual_snapshot import (
        ProcessResult,
        process_captures,
        write_audit_log,
        write_output,
    )
except ImportError:  # Direct script import from daily_research_digest_run.py
    from agent_reach_wrapper import SourceAllowlist
    from agent_reach_wrapper.manual_snapshot import (
        ProcessResult,
        process_captures,
        write_audit_log,
        write_output,
    )


@dataclass
class SocialPassResult:
    enabled: bool
    ok: bool
    lines: list[str]
    snapshot_path: Path | None = None
    output_path: Path | None = None
    audit_path: Path | None = None


def run_agent_reach_social_pass(repo: Path, cfg: dict[str, Any], today: date) -> SocialPassResult:
    social_cfg = cfg.get("agent_reach_social") or {}
    if not social_cfg.get("enabled", False):
        return SocialPassResult(enabled=False, ok=True, lines=[])

    queries = social_cfg.get("queries") or []
    if not queries:
        return SocialPassResult(
            enabled=True,
            ok=False,
            lines=["Agent Reach social pass enabled but no queries configured."],
        )

    if not shutil.which("opencli"):
        return SocialPassResult(
            enabled=True,
            ok=False,
            lines=["`opencli` not found on PATH; run Agent Reach install pack first."],
        )

    out_dir = repo / ".local" / "agent-reach-daily" / today.isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    snapshot_path = out_dir / "social-snapshot.json"
    output_path = out_dir / "normalized-social-items.json"
    audit_path = out_dir / "audit.jsonl"
    allowlist_path = repo / social_cfg.get("allowlist", "config/agent_reach_daily_sources.example.json")
    timeout = int(social_cfg.get("timeout_seconds", 45))
    max_items = int(social_cfg.get("max_items_per_query", 5))

    captures: list[dict[str, str]] = []
    rows: list[dict[str, Any]] = []
    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    for item in queries:
        cluster = str(item.get("cluster", "social"))
        platform = str(item.get("platform", "unknown"))
        command = item.get("command")
        if not isinstance(command, list) or not all(isinstance(part, str) for part in command):
            rows.append({"cluster": cluster, "platform": platform, "status": "bad-config", "count": 0})
            continue

        try:
            proc = subprocess.run(
                command,
                cwd=str(repo),
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            rows.append({"cluster": cluster, "platform": platform, "status": "timeout", "count": 0})
            continue
        except OSError as exc:
            rows.append({"cluster": cluster, "platform": platform, "status": f"error: {exc}", "count": 0})
            continue

        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout or "").strip().splitlines()
            rows.append(
                {
                    "cluster": cluster,
                    "platform": platform,
                    "status": f"exit-{proc.returncode}: {(detail[0] if detail else 'no output')[:80]}",
                    "count": 0,
                }
            )
            continue

        parsed = _parse_opencli_yaml(proc.stdout)
        records = parsed if isinstance(parsed, list) else ([parsed] if isinstance(parsed, dict) else [])
        count = 0
        for record in records[:max_items]:
            capture = _record_to_capture(record, platform, captured_at)
            if capture:
                captures.append(capture)
                count += 1
        rows.append({"cluster": cluster, "platform": platform, "status": "ok", "count": count})

    snapshot = {"connector": "manual_snapshot", "captures": captures}
    snapshot_path.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines: list[str] = []
    if captures:
        allowlist = SourceAllowlist.from_file(allowlist_path)
        result = process_captures(captures, allowlist)
        write_audit_log(audit_path, connector="manual_snapshot", snapshot_path=snapshot_path, result=result)
        if result.items:
            write_output(output_path, result.items)
        _render_social_lines(lines, rows, result, snapshot_path, output_path if result.items else None, audit_path)
        return SocialPassResult(
            enabled=True,
            ok=bool(result.items),
            lines=lines,
            snapshot_path=snapshot_path,
            output_path=output_path if result.items else None,
            audit_path=audit_path,
        )

    result = ProcessResult(ok=False)
    write_audit_log(audit_path, connector="manual_snapshot", snapshot_path=snapshot_path, result=result)
    _render_social_lines(lines, rows, result, snapshot_path, None, audit_path)
    return SocialPassResult(enabled=True, ok=False, lines=lines, snapshot_path=snapshot_path, audit_path=audit_path)


def _parse_opencli_yaml(text: str) -> Any:
    cleaned_lines = []
    for line in text.splitlines():
        if line.startswith("  Update available") or line.startswith("  Extension update available"):
            break
        cleaned_lines.append(line)
    cleaned = "\n".join(cleaned_lines).strip()
    if not cleaned:
        return []
    return yaml.safe_load(cleaned)


def _record_to_capture(record: dict[str, Any], platform: str, captured_at: str) -> dict[str, str] | None:
    url = str(record.get("url") or "").strip()
    if not url:
        return None

    author = str(record.get("author") or record.get("username") or record.get("subreddit") or record.get("name") or platform)
    text_parts = [
        str(record.get("title") or "").strip(),
        str(record.get("text") or "").strip(),
        str(record.get("selftext") or "").strip(),
        str(record.get("bio") or "").strip(),
    ]
    raw_text = "\n\n".join(part for part in text_parts if part)
    if not raw_text:
        return None

    return {
        "source": "manual_snapshot",
        "source_url": url,
        "author_or_channel": author[:120],
        "captured_at": captured_at,
        "raw_text": raw_text[:5000],
        "license_or_terms_note": f"Agent Reach/OpenCLI {platform} result; human review required before wiki or prod use.",
    }


def _render_social_lines(
    lines: list[str],
    rows: list[dict[str, Any]],
    result: ProcessResult,
    snapshot_path: Path,
    output_path: Path | None,
    audit_path: Path,
) -> None:
    lines.extend(
        [
            "---",
            "",
            "## Agent Reach social pass (DRY_RUN)",
            "",
            "OpenCLI/Agent Reach ran as an optional social discovery lane. Outputs are local-only and require human review before wiki ingest, briefs, or prod handoff.",
            "",
            "| Cluster | Platform | Status | Captures |",
            "|---------|----------|--------|----------|",
        ]
    )
    for row in rows:
        lines.append(f"| {row['cluster']} | {row['platform']} | {row['status']} | {row['count']} |")
    lines.extend(
        [
            "",
            f"- Snapshot: `{_display_path(snapshot_path)}`",
            f"- Audit: `{_display_path(audit_path)}`",
            f"- Normalized: `{_display_path(output_path) if output_path else 'not written; validation failed'}`",
            f"- Accepted: **{len(result.items)}** · Rejected: **{len(result.rejections)}**",
            "",
        ]
    )
    if result.rejections:
        lines.append("### Rejections")
        lines.append("")
        for rejection in result.rejections[:10]:
            lines.append(f"- `{rejection.reason}` index={rejection.index}: {rejection.detail[:160]}")
        lines.append("")


def _display_path(path: Path) -> str:
    parts = path.parts
    if ".local" in parts:
        idx = parts.index(".local")
        return str(Path(*parts[idx:]))
    return str(path)
