"""Versioned source allowlist checks for manual social snapshots."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


class AllowlistError(ValueError):
    """Raised when allowlist config is invalid or an item is not allowed."""


@dataclass(frozen=True)
class SourceAllowlist:
    allowed_sources: frozenset[str]
    allowed_domains: frozenset[str]
    allowed_author_or_channel: frozenset[str]

    @classmethod
    def from_file(cls, path: Path) -> "SourceAllowlist":
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return cls.from_mapping(data)

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "SourceAllowlist":
        if not isinstance(data, dict):
            raise AllowlistError("allowlist config must be a JSON object")

        allowed_sources = _string_set(data, "allowed_sources")
        allowed_domains = frozenset(domain.lower() for domain in _string_set(data, "allowed_domains"))
        allowed_author_or_channel = _string_set(data, "allowed_author_or_channel")

        if not allowed_sources or not allowed_domains or not allowed_author_or_channel:
            raise AllowlistError("allowlist entries must not be empty")

        return cls(
            allowed_sources=allowed_sources,
            allowed_domains=allowed_domains,
            allowed_author_or_channel=allowed_author_or_channel,
        )

    def require_allowed(self, item: dict[str, Any]) -> None:
        source = item.get("source")
        author = item.get("author_or_channel")
        url = item.get("source_url")

        if source not in self.allowed_sources:
            raise AllowlistError(f"source is not allowlisted: {source!r}")
        if "*" not in self.allowed_author_or_channel and author not in self.allowed_author_or_channel:
            raise AllowlistError(f"author_or_channel is not allowlisted: {author!r}")

        domain = urlparse(url).hostname
        if not domain:
            raise AllowlistError("source_url is missing a hostname")

        normalized_domain = domain.lower().rstrip(".")
        if normalized_domain.startswith("www."):
            normalized_domain = normalized_domain[4:]
        if normalized_domain not in self.allowed_domains:
            raise AllowlistError(f"domain is not allowlisted: {normalized_domain}")


def _string_set(data: dict[str, Any], key: str) -> frozenset[str]:
    values = data.get(key)
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise AllowlistError(f"{key} must be a list of strings")
    return frozenset(value for value in values if value)
