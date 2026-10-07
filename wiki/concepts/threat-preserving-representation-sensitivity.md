---
title: "Threat-preserving representation sensitivity (TPRS) (K396)"
type: concept
tags: [concept, agent-security, k396]
keywords: [2610.03585, K396]
related:
  - @ccc-wiki/concepts/threat-preserving-representation-sensitivity.md
  - sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md
  - concepts/adversarial-region-estimation-vs-single-example.md
  - sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-10-06
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K396)"
---

## Relations

- @@ccc-wiki/concepts/threat-preserving-representation-sensitivity.md — CCC harness-side counterpart (K423)
- @sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md — K403-K407 ingest source page
- @concepts/adversarial-region-estimation-vs-single-example.md — K403 estimate the failure region, not one example
- @sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md — K398-K402 ingest source page
- @concepts/compliance-boundary-adjacent-pair-search.md — K398 replace one judged score with a controlled pair
- @sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/benchmark-shortcut-attack-pyramid-audit.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

Question: **Threat-preserving representation sensitivity (TPRS)** — operator steal from arXiv 2610.03585?

## Narrative

Before quoting an ASR, ask what it is a property *of*. **TPRS** changes only the agent-visible representation of a threat — tool names, descriptions — while the task, harmful action, policy, ground truth, environment, and criteria stay fixed, and measures how far the score moves. It moved **11.67–13.21 pp** on ASB and **11.00 pp** on MCPTox across 28,904 runs; on ASB the movement is **upward**, because the original threat-flavoured names were acting as a defence the benchmark did not intend. Practical rules: **report sensitivity, not a single number**; say explicitly when an attack counts as success (native vs committed ASR differ in both value and sensitivity); and measure **utility** under the same transformations, since representation can move that too. Pairs the K388 breaking-level rule — both ask whether a score certifies the capability it claims.

## Snippets

> See arXiv 2610.03585 abstract. [Source: arXiv 2610.03585 (retrieved 2026-10-06)]
