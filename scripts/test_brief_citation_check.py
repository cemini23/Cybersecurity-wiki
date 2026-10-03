#!/usr/bin/env python3
"""Tests for brief_citation_check. Offline; reads the real CLAUDE.md alias table.

The point of these is to catch a regression of the 2026-10-03 alias bug: the
`osint-wiki` row read `../../OSINT WORKSPACE/wiki/`, which is not where OSINT
lives, so the alias resolved to a missing directory and every `@osint-wiki/...`
link in the wiki linted as dangling. One wrong relative path silently hid 126
working cross-wiki links.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("bcc", ROOT / "scripts/brief_citation_check.py")
bcc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bcc)


def test_alias_table_parses() -> None:
    assert bcc.WIKI_ALIASES, "no aliases parsed from CLAUDE.md"
    # The Related Wikis table must not be polluted by other backticked tables
    # (the MCP-tools table has the same row shape).
    for alias in bcc.WIKI_ALIASES:
        assert not alias.startswith("mcp__"), f"alias table picked up MCP tool row: {alias}"


def test_every_sibling_alias_points_at_a_real_wiki() -> None:
    """A sibling wiki that exists on disk must resolve to its wiki/ directory."""
    bad = []
    for alias, base in bcc.WIKI_ALIASES.items():
        if alias == "cybersecurity-wiki":
            continue
        sibling_root = base.parent
        if not sibling_root.is_dir():
            continue  # genuinely absent checkout (CI) — not a path bug
        if not base.is_dir():
            bad.append(f"{alias} -> {base}")
    assert not bad, "alias resolves to a missing dir: " + "; ".join(bad)


def test_osint_alias_resolves_to_the_real_workspace() -> None:
    """The specific path that was wrong."""
    base = bcc.WIKI_ALIASES.get("osint-wiki")
    assert base is not None, "osint-wiki alias missing"
    assert base.name == "wiki", f"osint-wiki should point at a wiki/ dir, got {base}"
    assert base.parent.name == "OSINT WORKSPACE", f"osint-wiki points at {base}"


def test_owners_of_finds_osint_for_a_known_page() -> None:
    base = bcc.WIKI_ALIASES.get("osint-wiki")
    if base is None or not base.is_dir():
        return  # sibling absent — nothing to assert
    rel = "concepts/k276-ood-stub-wave.md"
    if not (base / rel).is_file():
        return  # page retired upstream; not this test's business
    assert "osint-wiki" in bcc.owners_of(rel)


def test_citation_regex() -> None:
    text = "## Sources\n\n- [Source: wiki/concepts/foo.md]\n- [Source: @osint-wiki/concepts/bar.md]\n"
    got = bcc.CITE_RE.findall(text)
    assert got == ["wiki/concepts/foo.md"], got


if __name__ == "__main__":
    test_alias_table_parses()
    test_every_sibling_alias_points_at_a_real_wiki()
    test_osint_alias_resolves_to_the_real_workspace()
    test_owners_of_finds_osint_for_a_known_page()
    test_citation_regex()
    print("OK test_brief_citation_check")
