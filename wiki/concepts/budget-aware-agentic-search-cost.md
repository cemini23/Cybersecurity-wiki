---
title: "Budget-aware agentic search cost (K397)"
type: concept
tags: [concept, agent-security, k397]
keywords: [2610.03675, K397]
related:
  - concepts/reliable-inference-procurement-routing.md
  - sources/arxiv-2610-03675-frugalevo-cost-aware-program-evolution.md
  - concepts/fragtoken-inference-cost-amplification-lab.md
maturity: draft
created: 2026-10-06
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K397)"
---

## Relations

- @concepts/reliable-inference-procurement-routing.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-03675-frugalevo-cost-aware-program-evolution.md
- @concepts/fragtoken-inference-cost-amplification-lab.md

## Raw Concept

Question: **Budget-aware agentic search cost** — operator steal from arXiv 2610.03675?

## Narrative

Score an agentic search loop by **gain per unit cost**, not gain per iteration. **BA-AUC** is the area under the best-so-far score curve against cumulative model spend, so a method that is slower but cheaper can win. Two design moves travel: **split the roles** — an expensive model proposes strategies, a cheap one implements them — and **shape the harness for cache reuse**, maximising shared prefixes across steps. Reported at **$0.55–$1.68** against ~**$50** for multi-agent baselines. Applies to budgeted red-team or evolve loops: cap the spend, then compare. Pairs the inference-cost threads at K376 / K366.

## Snippets

> See arXiv 2610.03675 abstract. [Source: arXiv 2610.03675 (retrieved 2026-10-06)]
