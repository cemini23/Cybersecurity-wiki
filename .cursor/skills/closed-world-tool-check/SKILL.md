---
name: closed-world-tool-check
description: >-
  K369 closed-world tool membership check before execution. Validate tool name
  and optional arg keys against a local registry (skills + scripts + example
  schema). Use when the operator says closed-world check / validate tool name /
  is this tool registered. Pairs scout-tool-search and step-gate.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Closed-world tool check (K369)

Canon: `@wiki/concepts/closed-world-tool-hallucination-resolution.md` (arXiv **2609.19425**). Helper: `scripts/closed_world_tool_check.py`. **Membership only** — not BM25 search.

## Procedure

```bash
python3 scripts/closed_world_tool_check.py check <tool> [arg_key...]
python3 scripts/closed_world_tool_check.py list   # operator-only registry dump
python3 scripts/closed_world_tool_check.py selftest
```

| Verdict | Meaning | Exit |
|---------|---------|------|
| `ALLOW` | Tool in registry; arg keys match schema when present | 0 |
| `HOLD` | Unknown tool or hallucinated arg keys | 2 |
| `ESCALATE` | Ambiguous prefix or args without schema | 3 |

**Order:** `scout-tool-search` (retrieve) → this check (membership) → `step-gate` (blast).

## NEVER

- Do not treat this as live MCP catalog validation or broker install.
- Do not dump the full registry in chat unless the operator runs `list`.
- No network calls. No secrets. No auto-evolve `.cursor/skills`.
