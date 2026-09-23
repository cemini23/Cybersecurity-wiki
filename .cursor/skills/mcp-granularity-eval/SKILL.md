---
name: mcp-granularity-eval
description: >-
  K376 MCP tool interface granularity eval helper. Count tools in a frozen local
  catalog JSON and label UNDER/SWEET/ELEVATED/HIGH bands before harness ablations.
  Use when the operator says MCP granularity / tool count eval / MCP-GRANITE axis.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# MCP granularity eval (K376)

Canon: `@wiki/concepts/mcp-tool-interface-granularity-eval.md` (arXiv **2609.24161**). Helper: `scripts/mcp_granularity_eval.py`.

## Procedure

```bash
python3 scripts/mcp_granularity_eval.py checklist
python3 scripts/mcp_granularity_eval.py json --json config/mcp_granularity_eval.example.json
python3 scripts/mcp_granularity_eval.py selftest
```

| Verdict | Meaning | Exit |
|---------|---------|------|
| `OK` | Band SWEET or ELEVATED without dupes | 0 |
| `REVIEW` | UNDER, HIGH band, or duplicate tool names | 2 |

## NEVER

- Do not treat SWEET band as universal — MCP-GRANITE benchmark steal only.
- No live MCP catalog fetch. No auto-evolve skills tree.
