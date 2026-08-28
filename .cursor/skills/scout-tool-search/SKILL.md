---
name: scout-tool-search
description: >-
  Search local Cursor skills by keyword before choosing one (SCOUT-style tool
  search, K311). Use when the operator says scout / tool-search / which skill
  / find a skill. Returns top-k skill names and paths. 'execute' = READ the
  SKILL.md — never a live MCP invoke, never a catalog dump.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Scout tool search — local SKILL.md top-k (K311)

Canon: CCC `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md` (arXiv **2608.23992**, K311). Helper: CCC `scripts/scout_tool_search.py`. **HITL:** operator-invoked; do not auto-invoke; do not auto-evolve this skill.

Never load every skill's full body to pick one. Index **local** `.cursor/skills/*/SKILL.md` frontmatter (name + description, plus one line from the body's first heading) and return keyword / term-overlap **top-k (k≈5)**.

## Procedure

1. Run `python3 scripts/scout_tool_search.py query <terms...> [-k 5]`.
2. Read the top hit(s): `python3 scripts/scout_tool_search.py read <skill-name>` prints the SKILL.md path — then read it.
3. Choose one skill. Do not invoke an MCP tool; do not dump the catalog.

## Selftest

`python3 scripts/scout_tool_search.py selftest` — requires ≥3 federation skills and that query `route` returns the route skill.

## NEVER

- Do not use this to enumerate every skill (that is a catalog dump).
- Do not execute a skill's actions — only read its SKILL.md.
- No pipe-to-shell install patterns (`curl` piped to `bash`). No network calls. No secrets.
- Do not rewrite `## Verify`. Do not rewrite `route-task.ps1`. Do not edit `~/.claude/settings.json`.
