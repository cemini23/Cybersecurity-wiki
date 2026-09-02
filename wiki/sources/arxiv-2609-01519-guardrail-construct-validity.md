---
title: "When Guardrails Look Effective — construct validity in agent commerce eval (arXiv 2609.01519)"
type: source
tags: [source, arxiv, agent-security, audit, measurement, guardrails, k321]
keywords: [2609.01519, construct validity, protocol isolation, agent market evaluation, welfare accounting, guardrail effectiveness]
related:
  - concepts/guardrail-construct-validity-agent-eval.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
phase_0_verdict: "REFERENCE 2026-09-02 — measurement/audit pattern steal; no commerce exploit payloads. Pairs K277 measurement integrity."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K321)"
---

## Relations

- @concepts/guardrail-construct-validity-agent-eval.md — primary steal (Invalid/Inconclusive before policy claims)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation |
| Authors | Peiying Zhu, Sidi Chang |
| arXiv | 2609.01519 |
| Location | inbox `research to be indexed/arxiv-2609.01519-when-guardrails-look-effective-construct-validit.pdf` (archive pending) |
| Retrieved | 2026-09-02 |
| Read status | read (abstract + contract) |
| Public code | none at hunt |

## Narrative

Interactive **LLM agent market** simulations can output prices, surplus, and welfare that **look economic** without instantiating the behavior named in the claim. The paper audits a multi-turn buyer–seller hotel testbed: initial guardrail welfare gains (+87.4, +35.0, +28.8) **collapse** when offer schemas and buyer choice procedures are held fixed (+7.2, −13.9, +23.8). Single-generation effects are unstable (generation residuals ~50% of variance).

**Construct-validity contract:** separate **incentive validity**, **protocol isolation**, **stochastic stability**, and **welfare accounting** — return **Invalid** or **Inconclusive** before substantive policy claims. Original estimate **Invalid** under protocol isolation.

**Why filed (K321):** guardrail/agent-safety evals need the same endpoint-integrity discipline as MCP security eval (K277). Does **not** prove guardrails ineffective — proves apparent value is **unidentified** until validity checks pass.

## Snippets

> We contribute a construct-validity contract … returning Invalid or Inconclusive before allowing a substantive policy claim. [Source: arXiv 2609.01519 abstract, paraphrase]
