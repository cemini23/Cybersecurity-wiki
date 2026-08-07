---
title: Gradient Immunity — null-space resistance to malicious fine-tuning
type: concept
tags: [concept, llm-safety, fine-tuning]
keywords: [USG, PPOW, null space, malicious fine-tuning, 2608.05045]
related:
  - sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - entities/tools/datashield.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
  - concepts/post-training-adaptation-taxonomy.md
  - sources/arxiv-2608-06246-post-training-adaptation-taxonomy.md
maturity: draft
created: 2026-08-06
updated: 2026-08-07
---

## Relations

- @sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md
- @concepts/datashield-risky-finetune-data-filtering.md
- @entities/tools/datashield.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/ai-for-cybersecurity.md
- @concepts/post-training-adaptation-taxonomy.md
- @sources/arxiv-2608-06246-post-training-adaptation-taxonomy.md

## Raw Concept

Preserve a calibrated null-space safety gate in open-weight releases so harmful fine-tune gradients cannot easily undo alignment.

## Narrative

Complementary to DataShield (filter risky FT data). Relevant when publishing or adopting open-weight models that others will fine-tune. Abliterated local stacks intentionally weaken refusal — this paper is the **provider defense** side. Code not shippable yet. [CONFIRMED abstract]
