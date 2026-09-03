---
name: safeevolve-harness-audit
description: >-
  K324 advisory checklist for SafeEvolve harness-policy co-evolution lab runs.
  Use when operator says SafeEvolve / K324 / harness-policy co-evolution audit.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# SafeEvolve — K324 advisory checklist

Canon: `@wiki/concepts/safeevolve-harness-policy-co-evolution.md` (arXiv **2609.02786**). Helper: `scripts/k324_safeevolve_precheck.py`. **Defensive lab pattern** — HITL before prod harness/skill writes.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k324_safeevolve_precheck.py checklist
python3 scripts/k324_safeevolve_precheck.py selftest
```

Require **bounded reversible harness edits**, **external eval contract**, **no unattended `.cursor/skills` evolve**. Pair `@wiki/concepts/skill-misevolution.md`.

## NEVER

- Do not auto-evolve prod Cursor/Claude harnesses from trajectories.
- Cybersec K324 SafeEvolve ≠ CCC K324 RedEvoAgent validation ratchet.
