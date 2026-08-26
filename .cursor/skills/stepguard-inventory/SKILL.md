---
name: stepguard-inventory
description: >-
  StepGuard LICENSE re-hunt + REFERENCE clone inventory (K307). Use when the
  user says StepGuard adopt / step guard inventory. No HF weights; wont_wire MCP.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# StepGuard inventory — LICENSE gate, no weights

Canon: `@wiki/concepts/step-level-agent-guardrails.md` (arXiv **2608.24777**, Cybersec **K307**). Repo: `zheng977/StepGuard`. **HITL:** operator-invoked.

Runtime stays **`wont_wire`**. Do not download `ninty-seven/StepGuard` weights unless the operator explicitly scopes a lab eval.

## Procedure

```bash
# Re-hunt SPDX (no clone if still missing)
bash scripts/stepguard_inventory.sh check

# Shallow clone to .local/adopts/StepGuard only when LICENSE appears
bash scripts/stepguard_inventory.sh adopt
```

## NEVER

- No `huggingface-cli download` / HF weight pulls in wiki automation.
- No Cursor MCP wire without operator OK + separate Phase-1 proposal.
- Dual-ID: Cybersec K307 ≠ CCC MediSkill-Evo K307.
