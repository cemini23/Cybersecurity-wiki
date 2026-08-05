---
title: Adaptive fuzzy test-time sampling budgets
type: concept
tags: [concept, llm, test-time-compute]
keywords: [fuzzy controller, adaptive sampling, best-of-N, 2608.03961]
related:
  - sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md
  - concepts/gradcuit-test-time-latent-reasoning.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/toktier-exact-stateful-tokenization.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md
- @concepts/gradcuit-test-time-latent-reasoning.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/toktier-exact-stateful-tokenization.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

Map prompt hardness + confidence to an inspectable per-query sample budget instead of fixed best-of-N.

## Narrative

Local abliterated stacks and prod agents both burn VRAM/time on uniform TTS. Adaptive budgets save easy turns and spend on hard recon/exploit reasoning. Federation ACEM cost vocabulary (K243) is the budget language; this paper is a concrete controller shape. [CONFIRMED abstract]
