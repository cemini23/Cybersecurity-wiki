---
name: enterprise-scale-gate
description: >-
  K373 EnterpriseVal scale gate — check frozen socio-technical config and metric
  thresholds before SCALE. Outputs REJECT | CONDITIONAL | SCALE with confidence
  bounds. Use when reviewing enterprise GenAI rollout or before expanding a
  use case. Pairs evaluation-first rubric and evidence-tree eval.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Enterprise scale gate (K373)

Canon: `@wiki/concepts/enterprise-use-case-genai-evaluation.md` (arXiv **2609.21841**). Helper: `scripts/enterprise_scale_gate.py`. Example: `config/enterprise_scale_gate.example.json`.

## Procedure

JSON input keys: `use_case`, `consequence_tier` (`low` | `medium` | `high`), `frozen_config` (model, prompts, retrieval, tools, guardrails, oversight), `metrics` (name, value, threshold_min/max, optional confidence bounds), `human_review_confirmed` (bool).

```bash
python3 scripts/enterprise_scale_gate.py checklist
python3 scripts/enterprise_scale_gate.py json --json eval.json
python3 scripts/enterprise_scale_gate.py selftest
```

| Verdict | When |
|---------|------|
| `REJECT` | Incomplete frozen config, missing metrics, or value fails thresholds |
| `CONDITIONAL` | Metrics pass but `human_review_confirmed` false on medium/high tier |
| `SCALE` | Frozen config + metrics pass; cleared to expand |

Never promote `CONDITIONAL` → `SCALE` without operator-confirmed human review on medium/high consequence tiers.

Pairs: `harness-eval-gate`, K331 rubric-before-run, K289 evidence-tree eval, K277 measurement integrity.

## NEVER

- Do not write `watches.json`, Discord, wiki, or git from this helper.
- Do not treat model refusal as authorization.
- No LIVE Discord without LIVE OK.
