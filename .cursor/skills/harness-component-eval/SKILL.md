---
name: harness-component-eval
description: >-
  K370 harness component eval checklist — decompose coding harness into planning,
  action space, and context management under a fixed loop. Use before
  harness-eval-gate when evaluating harness changes or ablation studies.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Harness component eval (K370)

Canon: `@wiki/concepts/coding-agent-harness-component-design.md` (arXiv **2609.20804**). Helper: `scripts/harness_component_eval.py`.

## Procedure

```bash
python3 scripts/harness_component_eval.py checklist
python3 scripts/harness_component_eval.py json --json answers.json
python3 scripts/harness_component_eval.py selftest
```

Keys (all true → `SHIP`): `fixed_execution_loop`, `planning_evidence`, `action_space_evidence`, `context_management_evidence`, `not_monolithic`, `no_skill_autowrite`.

**Order:** run this **before** `harness-eval-gate` / `scripts/harness_eval_checklist.py` (K334).

Pairs: K281 external eval contract, K350 harness supply-chain preflight, `eval-first-rubric`, `env-harness-wrap`.

## NEVER

- Do not accept a monolithic end-to-end score only.
- Do not rewrite `## Verify` or auto-evolve `.cursor/skills`.
- No harness clone until SPDX + Phase-0.
