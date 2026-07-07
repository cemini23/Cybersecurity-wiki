"""Strict schema helpers for the standalone Agent-Reach wrapper."""

from __future__ import annotations

import hashlib
import re
from datetime import datetime
from typing import Any
from urllib.parse import urlparse


class SchemaError(ValueError):
    """Raised when an item does not match the social ingest schema."""


REQUIRED_CAPTURE_FIELDS: dict[str, type] = {
    "source": str,
    "source_url": str,
    "author_or_channel": str,
    "captured_at": str,
    "raw_text": str,
    "license_or_terms_note": str,
}

REQUIRED_SOCIAL_ITEM_FIELDS: dict[str, type] = {
    **REQUIRED_CAPTURE_FIELDS,
    "content_hash": str,
    "operator_review": bool,
}

OPTIONAL_SOCIAL_ITEM_FIELDS: dict[str, type] = {
    "sanitized_text": str,
    "injection_flags": list,
}

_SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
_SECRET_FIELD_RE = re.compile(
    r"(cookie|session|auth[_-]?token|bearer|password|secret|csrf|xsrf)",
    re.IGNORECASE,
)


def normalize_text(value: str) -> str:
    return " ".join(value.split())


def compute_content_hash(raw_text: str) -> str:
    normalized = normalize_text(raw_text)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def validate_capture_schema(capture: dict[str, Any]) -> None:
    validate_no_secret_fields(capture)
    _validate_mapping(capture, REQUIRED_CAPTURE_FIELDS, {})
    if not normalize_text(capture["raw_text"]):
        raise SchemaError("raw_text must not be empty")
    _validate_url_shape(capture["source_url"])
    _validate_captured_at(capture["captured_at"])


def validate_social_item_schema(item: dict[str, Any]) -> None:
    validate_no_secret_fields(item)
    _validate_mapping(item, REQUIRED_SOCIAL_ITEM_FIELDS, OPTIONAL_SOCIAL_ITEM_FIELDS)
    if not _SHA256_RE.match(item["content_hash"]):
        raise SchemaError("content_hash must be a sha256:<64 hex> digest")
    if not normalize_text(item["raw_text"]):
        raise SchemaError("raw_text must not be empty")
    if not normalize_text(item.get("sanitized_text", "")):
        raise SchemaError("sanitized_text must not be empty when present")
    if "injection_flags" in item and not all(isinstance(flag, str) for flag in item["injection_flags"]):
        raise SchemaError("injection_flags must contain strings only")
    _validate_url_shape(item["source_url"])
    _validate_captured_at(item["captured_at"])


def validate_no_secret_fields(value: Any, prefix: str = "item") -> None:
    for key in _flatten_keys(value, prefix):
        if _SECRET_FIELD_RE.search(key):
            raise SchemaError(f"forbidden secret/session field: {key}")


def _flatten_keys(value: Any, prefix: str) -> list[str]:
    if isinstance(value, dict):
        keys: list[str] = []
        for key, nested in value.items():
            child = f"{prefix}.{key}"
            keys.append(child)
            keys.extend(_flatten_keys(nested, child))
        return keys
    if isinstance(value, list):
        keys = []
        for index, nested in enumerate(value):
            keys.extend(_flatten_keys(nested, f"{prefix}[{index}]"))
        return keys
    return []


def _validate_mapping(
    data: dict[str, Any],
    required: dict[str, type],
    optional: dict[str, type],
) -> None:
    if not isinstance(data, dict):
        raise SchemaError("item must be a JSON object")

    allowed_fields = set(required) | set(optional)
    missing = sorted(set(required) - set(data))
    extra = sorted(set(data) - allowed_fields)
    if missing:
        raise SchemaError(f"missing required fields: {', '.join(missing)}")
    if extra:
        raise SchemaError(f"unknown fields: {', '.join(extra)}")

    for field, expected_type in {**required, **optional}.items():
        if field in data and not isinstance(data[field], expected_type):
            raise SchemaError(f"{field} must be {expected_type.__name__}")


def _validate_url_shape(value: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise SchemaError("source_url must be an absolute https URL")
    if parsed.username or parsed.password:
        raise SchemaError("source_url must not include userinfo")


def _validate_captured_at(value: str) -> None:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SchemaError("captured_at must be ISO-8601") from exc
