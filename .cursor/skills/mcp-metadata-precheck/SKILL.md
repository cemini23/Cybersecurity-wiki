---
name: mcp-metadata-precheck
description: >-
  K382 MCP tool metadata supply-chain precheck. Static scan of local tool
  name/description JSON for authority/hidden-instruction heuristics before catalog
  adoption. Use when the operator says MCP metadata precheck / A2M awareness scan.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# MCP metadata precheck (K382)

Canon: `@wiki/concepts/mcp-tool-metadata-supply-chain-risk.md` (arXiv **2609.26761**). Helper: `scripts/mcp_metadata_precheck.py`.

## Procedure

```bash
python3 scripts/mcp_metadata_precheck.py checklist
python3 scripts/mcp_metadata_precheck.py json --json config/mcp_metadata_precheck.example.json
python3 scripts/mcp_metadata_precheck.py selftest
```

| Verdict | Meaning | Exit |
|---------|---------|------|
| `PASS` | No heuristic hits | 0 |
| `REVIEW` | Flagged descriptions — human review | 2 |
| `REJECT` | Invalid JSON shape | 1 |

Pair `cursor-security-preflight` before third-party MCP packs.

## NEVER

- No PoCs or attack templates. REVIEW is not auto-deny.
- No network calls. No auto-evolve skills tree.
