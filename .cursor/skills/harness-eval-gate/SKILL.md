---
name: harness-eval-gate
description: >-
  K334 harness-as-eval-artifact gate before persisting a harness version.
  Use when evaluating Creation/Evolution harness changes, HarnessDev-style
  iterations, or when the user says harness eval gate / held-out harness /
  executor swap. Does not rewrite pass criteria or auto-evolve skills.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Harness eval gate (K334)

Canon: `@wiki/concepts/harness-as-eval-artifact.md` (arXiv **2609.01437**). Helper: `scripts/harness_eval_checklist.py`. Evaluate **runnable harness infrastructure**, not only terminal task output.

## Procedure

```bash
python3 scripts/harness_eval_checklist.py checklist
python3 scripts/harness_eval_checklist.py selftest
```

JSON keys: `hidden_held_out`, `executor_swap`, `state_fires`, `external_eval`, `no_skill_autowrite` — all must be true for SHIP.

Pair with: K281/K292 external eval contract, K332 vague-goal self-evolution (judge vs base model), `env-harness-wrap` (keep the verifier).

## NEVER

- Do not rewrite `## Verify` or lint rules to match a failing agent (K162).
- Do not auto-evolve `.cursor/skills` from harness-dev feedback.
- Visible feedback alone ≠ held-out transfer.
