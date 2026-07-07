"""Manual snapshot connector for a safe Agent-Reach wrapper.

This connector only reads operator-provided local JSON snapshots. It never
uses browser cookies, logged-in scraping, network calls, or production ingest.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .allowlist import AllowlistError, SourceAllowlist
from .filters import InjectionDetected, require_no_prompt_injection
from .schema import (
    SchemaError,
    compute_content_hash,
    validate_capture_schema,
    validate_no_secret_fields,
    validate_social_item_schema,
)


class SnapshotError(ValueError):
    """Raised when a manual snapshot cannot be safely processed."""


@dataclass
class Rejection:
    reason: str
    detail: str
    index: int | None = None
    content_hash: str | None = None


@dataclass
class ProcessResult:
    ok: bool
    items: list[dict[str, Any]] = field(default_factory=list)
    rejections: list[Rejection] = field(default_factory=list)


def load_snapshot(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise SnapshotError("snapshot must be a JSON object")
    validate_no_secret_fields(data, "snapshot")
    extra_fields = sorted(set(data) - {"connector", "captures"})
    if extra_fields:
        raise SnapshotError(f"unknown snapshot fields: {', '.join(extra_fields)}")
    if data.get("connector") != "manual_snapshot":
        raise SnapshotError("snapshot connector must be manual_snapshot")

    captures = data.get("captures")
    if not isinstance(captures, list):
        raise SnapshotError("snapshot captures must be a list")
    if not all(isinstance(capture, dict) for capture in captures):
        raise SnapshotError("each capture must be a JSON object")
    return captures


def process_captures(
    captures: list[dict[str, Any]],
    allowlist: SourceAllowlist,
    *,
    seen_hashes: set[str] | None = None,
) -> ProcessResult:
    if not captures:
        return ProcessResult(
            ok=False,
            rejections=[Rejection(reason="EMPTY_CAPTURE", detail="snapshot contained no captures")],
        )

    seen = set(seen_hashes or set())
    accepted: list[dict[str, Any]] = []
    rejections: list[Rejection] = []

    for index, capture in enumerate(captures):
        content_hash = None
        try:
            validate_capture_schema(capture)
            allowlist.require_allowed(capture)

            content_hash = compute_content_hash(capture["raw_text"])
            if content_hash in seen:
                raise SnapshotError("duplicate content_hash detected")

            sanitized_text, injection_flags = require_no_prompt_injection(capture["raw_text"])
            item = {
                **capture,
                "content_hash": content_hash,
                "operator_review": True,
                "sanitized_text": sanitized_text,
                "injection_flags": injection_flags,
            }
            validate_social_item_schema(item)

            seen.add(content_hash)
            accepted.append(item)
        except SchemaError as exc:
            rejections.append(Rejection("SCHEMA_REJECTED", str(exc), index, content_hash))
        except AllowlistError as exc:
            rejections.append(Rejection("ALLOWLIST_REJECTED", str(exc), index, content_hash))
        except InjectionDetected as exc:
            rejections.append(Rejection("PROMPT_INJECTION_REJECTED", str(exc), index, content_hash))
        except SnapshotError as exc:
            rejections.append(Rejection("SNAPSHOT_REJECTED", str(exc), index, content_hash))

    return ProcessResult(ok=bool(accepted), items=accepted, rejections=rejections)


def write_output(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "mode": "DRY_RUN",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": items,
    }
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def write_audit_log(
    path: Path,
    *,
    connector: str,
    snapshot_path: Path,
    result: ProcessResult,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "connector": connector,
        "snapshot": str(snapshot_path),
        "mode": "DRY_RUN",
        "ok": result.ok,
        "accepted_count": len(result.items),
        "accepted_hashes": [item["content_hash"] for item in result.items],
        "rejections": [
            {
                "reason": rejection.reason,
                "detail": rejection.detail,
                "index": rejection.index,
                "content_hash": rejection.content_hash,
            }
            for rejection in result.rejections
        ],
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True))
        handle.write("\n")
