---
name: guardrail-construct-validity-audit
description: >-
  K321 advisory checklist before licensing guardrail welfare/safety claims in agent
  simulations. Use when operator says guardrail construct validity / K321 precheck /
  protocol isolation / incentive validity. Pairs K277 measurement integrity.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Guardrail construct validity — K321 advisory checklist

Canon: `@wiki/concepts/guardrail-construct-validity-agent-eval.md` (arXiv **2609.01519**). Helper: `scripts/k321_guardrail_construct_validity_precheck.py`. **Audit pattern only** — not a runtime guard.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k321_guardrail_construct_validity_precheck.py checklist
python3 scripts/k321_guardrail_construct_validity_precheck.py selftest
```

Four core checks: **incentive validity**, **protocol isolation**, **stochastic stability**, **welfare accounting**. Plus **Invalid/Inconclusive gate** and **no causal claim without pass**. Pair `@wiki/concepts/measurement-integrity-mcp-security-eval.md`.

## NEVER

- Do not publish causal guardrail efficacy claims without all checks passing.
- Schema-valid simulation output ≠ construct-valid measurement.
