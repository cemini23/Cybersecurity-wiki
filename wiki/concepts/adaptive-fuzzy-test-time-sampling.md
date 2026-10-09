---
title: Adaptive fuzzy test-time sampling budgets
type: concept
tags: [concept, llm, test-time-compute]
keywords: [fuzzy controller, adaptive sampling, best-of-N, 2608.03961]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md
  - concepts/gradcuit-test-time-latent-reasoning.md
  - concepts/toktier-exact-stateful-tokenization.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-08-05
updated: 2026-10-09
wire_status: policy_wired
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md
- @concepts/gradcuit-test-time-latent-reasoning.md
- @concepts/toktier-exact-stateful-tokenization.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

Map prompt hardness + confidence to an inspectable per-query sample budget instead of fixed best-of-N.

## Narrative

Local abliterated stacks and prod agents both burn VRAM/time on uniform TTS. Adaptive budgets save easy turns and spend on hard recon/exploit reasoning. Federation ACEM cost vocabulary (K243) is the budget language; this paper is a concrete controller shape. [CONFIRMED abstract]
