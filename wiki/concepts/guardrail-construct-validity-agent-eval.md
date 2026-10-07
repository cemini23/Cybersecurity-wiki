---
title: "Guardrail construct validity — Invalid before policy claims (K321)"
type: concept
tags: [concept, agent-security, audit, measurement, guardrails, k321]
keywords: [construct validity, protocol isolation, incentive validity, stochastic stability, welfare accounting, agent market eval, guardrail measurement]
related:
  - sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md
  - concepts/adversarial-region-estimation-vs-single-example.md
  - sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md
  - concepts/certified-selective-prediction-guardrails.md
  - sources/arxiv-2609-22048-available-guardrails-selective-prediction.md
  - sources/arxiv-2609-01519-guardrail-construct-validity.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/culturally-responsive-llm-benchmark-audit.md
maturity: draft
created: 2026-09-02
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K321)"
---

## Relations

- @sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md — K403-K407 ingest source page
- @concepts/adversarial-region-estimation-vs-single-example.md — K403 active-learning level-set estimation for robustness audit
- @sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md — K398-K402 ingest source page
- @concepts/compliance-boundary-adjacent-pair-search.md — K398 adjacent-pair compliance boundary testing
- @sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md — K395-K397 ingest source page
- @concepts/threat-preserving-representation-sensitivity.md — K396 TPRS — representation moves the score while the security problem is fixed
- @concepts/benchmark-shortcut-attack-pyramid-audit.md — K387-K391 cross-link
- @sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md — K387-K391 ingest source page
- @sources/arxiv-2609-01519-guardrail-construct-validity.md — construct validity contract (2609.01519)
- @sources/arxiv-2609-22048-available-guardrails-selective-prediction.md — K354 certified availability (2609.22048)
- @concepts/certified-selective-prediction-guardrails.md — K354 pairs construct validity with deployment availability
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
