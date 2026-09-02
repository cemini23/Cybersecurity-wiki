---
title: "Guardrail construct validity — Invalid before policy claims (K321)"
type: concept
tags: [concept, agent-security, audit, measurement, guardrails, k321]
keywords: [construct validity, protocol isolation, incentive validity, stochastic stability, welfare accounting, agent market eval, guardrail measurement]
related:
  - sources/arxiv-2609-01519-guardrail-construct-validity.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K321)"
---

## Relations

- @sources/arxiv-2609-01519-guardrail-construct-validity.md — construct validity contract (2609.01519)
- @concepts/measurement-integrity-mcp-security-eval.md — K277 labels ≠ endpoints; integrity chain

## Raw Concept

Question: **when does a guardrail eval actually measure guardrail effect, not protocol drift?**

## Narrative

Agent guardrail studies can show large welfare or safety lifts that **reverse** when the transaction **protocol** (schemas, choosers, incentives) is held fixed. **K321 (2609.01519)** proposes a **construct-validity contract** with four checks:

1. **Incentive validity** — manipulations move incentives in the expected direction.
2. **Protocol isolation** — guarded vs unguarded agents share the same offer/choice interface.
3. **Stochastic stability** — enough generations; report uncertainty (bootstrap CIs).
4. **Welfare accounting** — scripted positive controls bound interpretability.

Return **Invalid** or **Inconclusive** before licensing causal guardrail claims. Pairs K277 measurement integrity and K271 faithful ASR reporting.

## Snippets

> The case study does not establish that guardrails are ineffective; it establishes that their apparent value is unidentified until the simulated agents and protocol pass these checks. [Source: arXiv 2609.01519 abstract, paraphrase]
