---
title: ARMOR++ — agentic attacks on deepfake detectors
type: concept
tags: [concept, deepfake, adversarial-ml, agentic, black-box]
keywords: [armor++, aadd-2025, transferable asr, deepfake detector reliability]
related:
  - sources/arxiv-armor-plusplus-deepfake-agentic-2607.15246.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agentic-hard-example-synthesis-content-safety.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-armor-plusplus-deepfake-agentic-2607.15246.md — paper
- @concepts/llm-adversarial-fuzzing.md — adversarial eval umbrella
- @concepts/agentic-hard-example-synthesis-content-safety.md — complementary agentic safety-data synthesis (defense side)

## Raw Concept

How fragile are deepfake detectors under agent-orchestrated, no-query black-box transfer?

## Narrative

ARMOR++ shows detectors that look strong against classical transfer (TI-FGSM ~0.15 ASR) still fall to **~0.44 ASR** (LQ ViT) under agentic multi-primitive orchestration. Defense implication: report agentic-transfer ASR in detector claims; assume residual gap until proven otherwise.

### Ops note

Authorized lab / research only. Dual-use attack methodology — wiki documents for detector hardening eval, not for producing undetectable deepfakes in the wild.
