---
title: Interpretable adaptive sampling for LLM test-time scaling (arXiv 2608.03961)
type: source
tags: [source, arxiv, llm, test-time-compute, sampling]
keywords: [2608.03961, adaptive sampling, fuzzy controller, test-time scaling, best-of-N]
related:
  - concepts/adaptive-fuzzy-test-time-sampling.md
  - concepts/gradcuit-test-time-latent-reasoning.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/toktier-exact-stateful-tokenization.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
read_status: read
created: 2026-08-05
updated: 2026-08-05
phase_0_verdict: "REFERENCE 2026-08-05 — no public code; pattern steal for TTS budgets"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
---

**Briefs:** `briefs/2026-08-05_k243-adaptive-tts-sampling-prod.md`

## Relations

- @concepts/adaptive-fuzzy-test-time-sampling.md
- @concepts/gradcuit-test-time-latent-reasoning.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/toktier-exact-stateful-tokenization.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Interpretable Adaptive Sampling for LLM Test-Time Scaling |
| Authors | Mobina Kashaniyan, Ali Jannesari |
| arXiv | 2608.03961 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.03961-interpretable-adaptive-sampling-for-llm-test-tim.pdf` |
| Retrieved | 2026-08-05 |

## Narrative

Fixed best-of-N wastes compute on easy prompts. Lightweight **fuzzy controller** maps estimated complexity + model confidence → per-query sample budget (inspectable). Fair-alignment eval vs best-of-N / compute-aware / self-certainty baselines on QA + math. [CONFIRMED abstract]

### Steal

1. Do not hardcode the same TTS sample count for every pentest/agent query
2. Prefer inspectable budget rules (complexity × confidence) over opaque fixed N
3. Pair with TokTier/TTFT and GradCuit: test-time spend is a security+cost surface

## Snippets

> "The controller assigns fewer samples to easier or more confident prompts and more samples to harder or less certain prompts, making inference-time compute inspectable rather than fixed or opaque."
[Source: arXiv 2608.03961 abstract]
