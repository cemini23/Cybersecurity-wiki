---
title: Rubric capability-tree diagnosis (CRAFT pattern)
type: concept
tags: [llm-eval, fine-tuning, rubrics, harness]
keywords: [CRAFT, EvalTree, capability tree, rubric criteria, targeted SFT]
related:
  - sources/arxiv-2607-16122-craft-rubric-capability-diagnosis.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-15081-datashield-risky-finetune-data.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/arxiv-2607-16122-craft-rubric-capability-diagnosis.md — Scale AI CRAFT paper
- @concepts/datashield-risky-finetune-data-filtering.md — filter risky FT samples after targeting gaps
- @concepts/ai-for-cybersecurity.md
- @sources/arxiv-2607-15081-datashield-risky-finetune-data.md

## Raw Concept

Benchmark scores answer "how good today?" Post-training needs "what to fix next?" CRAFT-style pipelines convert **rubric criteria** into a hierarchical **capability tree**, score the model at each node, and generate SFT data only for the weakest clear failures — sharper than prompt-level clustering (EvalTree) or random data.

## Narrative

### Pipeline

1. Score model answers against rubric criteria
2. Extract a capability description per criterion
3. Cluster into a hierarchical tree
4. Select low nodes at the granularity where the failure is clearest
5. Generate targeted SFT for those capabilities
6. Re-eval on **held-out** benchmarks disjoint from diagnostic rubrics

### When to use in Cemini / cyber

- Security-domain model FT: diagnose which *answer requirements* fail (not just "weak on CTI")
- Agent harness eval: cluster decide()/tool-use rubric fails before rewriting skills
- Always pair with risk filters (@entities/tools/datashield.md) before FT

### Limits

- No public CRAFT code at ingest — reimplement pattern or wait for release
- Needs high-quality rubrics; garbage criteria → garbage trees
