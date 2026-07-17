---
title: Agentic hard-example synthesis for content-safety robustness
type: concept
tags: [concept, multimodal, content-safety, red-teaming, data-curation]
keywords: [hard examples, agentic curation, fnr, boundary cases]
related:
  - sources/arxiv-2607-14256-agentic-hard-example-synthesis.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- @sources/arxiv-2607-14256-agentic-hard-example-synthesis.md — Google/UCLA paper

## Raw Concept

Passive datasets miss multimodal policy boundary cases. Agentic synthesis proposes hypotheses, mutates failures, and verifies with a multi-level rater committee.

## Narrative

Steal the loop: Architect → generate (incl. images) → multi-level verify → bank hard demos → retrieve at test time. Track **FNR** on safety classifiers (paper: 41.2% → 24.5%). Complements jailbreak ASR metrics (AMT-X dual ASR). [CONFIRMED — abstract]

No public harness — pattern-only until Google releases artifacts.
