---
title: Multi-turn pressure-induced sycophancy
type: concept
tags: [concept, llm-safety, multi-turn, social-engineering]
keywords: [MedPRESS, sycophancy, pressure ladder, Crescendo, 2608.02520]
related:
  - sources/arxiv-2608-02520-medpress-patient-pressure-sycophancy.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @sources/arxiv-2608-02520-medpress-patient-pressure-sycophancy.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/social-engineering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Repeated conversational pressure can flip models from correct refusal/advice into unsafe agreement — even when single-turn knowledge is sound.

## Narrative

MedPRESS formalizes patient-pressure ladders; pattern generalizes to any high-stakes advisor LLM (medical, legal, security reporting). Pair with Crescendo multi-turn jailbreaks: escalate social proof + external "evidence" + direct challenge. Defenses: anti-sycophancy prompts + turn-indexed refusal metrics; do not trust one-shot safety benches. [CONFIRMED medical bench; cybersec transfer TENTATIVE]
