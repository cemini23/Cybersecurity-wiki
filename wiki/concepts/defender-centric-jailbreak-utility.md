---
title: Defender-centric jailbreak utility (A-MESS / AttackSHAP)
type: concept
tags: [llm-security, jailbreak, safety-training, evaluation]
keywords: [AttackSHAP, A-MESS, ASR vs utility, red-team data selection]
related:
  - sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/pair-prompt-pattern.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/pair-prompt-pattern.md
- @concepts/datashield-risky-finetune-data-filtering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Jailbreak research usually optimizes **ASR**. Defenders need attacks ranked by how much they improve safety when used as training/red-team data. A-MESS / AttackSHAP operationalizes that gap.

## Narrative

### Pipeline

1. Define black-box safety utility of an attack *subset* (post-train / eval)
2. Estimate AttackSHAP attributions with limited utility queries
3. Select compact subsets under budget (greedy / surrogate)
4. Prefer selected subsets over top-ASR lists

### Ops rule

Do not promote a jailbreak corpus into FT solely because ASR is high — measure defender utility, then risk-filter (@concepts/datashield-risky-finetune-data-filtering.md).
