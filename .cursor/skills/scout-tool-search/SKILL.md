---
name: scout-tool-search
description: >-
  Search local Cursor skills by keyword before choosing one (SCOUT-style tool
  search, K311, BM25). Use when the operator says scout / tool-search / which
  skill / find a skill. Returns top-k skill names and paths. 'execute' = READ
  the SKILL.md — never a live MCP invoke, never a catalog dump.
license: MIT
metadata.author: cemini23
metadata.version: "1.1.1"
disable-model-invocation: true
federation: true
---

# Scout tool search — local SKILL.md top-k, BM25 (K311)

Canon: CCC `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md` (arXiv **2608.23992**, K311). Helper: CCC `scripts/scout_tool_search.py`. **HITL:** operator-invoked; do not auto-invoke; do not auto-evolve this skill.

Never load every skill's full body to pick one. Index **local** `.cursor/skills/*/SKILL.md` frontmatter (name + description, plus one line from the body's first heading) and return **BM25-lite** top-k (k≈5) — k1=1.5, b=0.75, IDF from the local corpus, small substring bonus. No pip, no HF, no vector DB.

## Procedure

1. Run `python3 scripts/scout_tool_search.py query <terms...> [-k 5]`.
2. Read the top hit(s): `python3 scripts/scout_tool_search.py read <skill-name>` prints the SKILL.md path — then read it.
3. Choose one skill. Do not invoke an MCP tool; do not dump the catalog.

## Selftest

`python3 scripts/scout_tool_search.py selftest` — requires ≥3 federation skills, query `route` returns the route skill, and query `step` ranks `step-gate` in top-k.

## NEVER

- Do not use this to enumerate every skill (that is a catalog dump).
- Do not execute a skill's actions — only read its SKILL.md.
- No pipe-to-shell install patterns. No network calls. No secrets.
- Do not rewrite `## Verify`. Do not rewrite `route-task.ps1`. Do not edit the tracked Claude Code user settings file.
