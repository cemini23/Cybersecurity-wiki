---
title: ARMOR++ — agentic attacks on deepfake detectors
type: concept
tags: [concept, deepfake, adversarial-ml, agentic, black-box]
keywords: [armor++, aadd-2025, transferable asr, deepfake detector reliability]
related:
  - sources/arxiv-2610-11112-false-claims-credible-images.md
  - sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md
  - concepts/verification-generation-gap.md
  - concepts/lipsync-forgery-detection-attribution.md
  - concepts/llm-adversarial-fuzzing.md
  - sources/arxiv-2610-06339-babelfake-multilingual-av-deepfake.md
  - sources/arxiv-armor-plusplus-deepfake-agentic-2607.15246.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agentic-hard-example-synthesis-content-safety.md
maturity: draft
created: 2026-07-18
updated: 2026-10-09
---

## Relations

- @sources/arxiv-2610-11112-false-claims-credible-images.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md — K408-K417 ingest / 2026-10-09
- @concepts/verification-generation-gap.md — K408-K417 ingest / 2026-10-09
- @concepts/lipsync-forgery-detection-attribution.md — K408-K417 ingest / 2026-10-09
- @concepts/llm-adversarial-fuzzing.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-06339-babelfake-multilingual-av-deepfake.md — K-b: BabelFake multilingual AV deepfake detection benchmark
- @sources/arxiv-armor-plusplus-deepfake-agentic-2607.15246.md — paper
- @concepts/agentic-hard-example-synthesis-content-safety.md — complementary agentic safety-data synthesis (defense side)

## Raw Concept

How fragile are deepfake detectors under agent-orchestrated, no-query black-box transfer?

## Narrative

ARMOR++ shows detectors that look strong against classical transfer (TI-FGSM ~0.15 ASR) still fall to **~0.44 ASR** (LQ ViT) under agentic multi-primitive orchestration. Defense implication: report agentic-transfer ASR in detector claims; assume residual gap until proven otherwise.

### Ops note

Authorized lab / research only. Dual-use attack methodology — wiki documents for detector hardening eval, not for producing undetectable deepfakes in the wild.
