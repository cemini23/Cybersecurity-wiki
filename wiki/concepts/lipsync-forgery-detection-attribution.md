---
title: "Lipsync forgery detection and attribution (K-av2)"
type: concept
tags: [concept, deepfake-detection, k-av2]
keywords: [arXiv 2610.08417, K-av2]
related:
  - sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K-av2)"
---

## Relations

- @sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md — K408-K417 ingest / 2026-10-09
- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md — K408-K417 ingest / 2026-10-09

## Raw Concept

Question: **Lipsync forgery detection and attribution** — operator steal from the inbound brief (arXiv 2610.08417)?

## Narrative

Lipsync generators break a coupling real faces keep: **the mouth moves in a way the head pose predicts.** Aligning a lip encoder against a **6-DoF head-pose encoder** turns that broken coupling into a detector — **AUC 99.42 / 99.82 / 97.50** across three benchmarks, roughly 8 points over the prior method — and per-generator fingerprints push **attribution to 97.5% / 93.9 F1**.

Read those numbers honestly. **Attribution measures generator leakage, not field detectability** — the fingerprints are distinctive because the generators are stylistically distinct. And the generator set is fixed, so on a generator it has never seen, accuracy falls to **84-95%**; that is the bound to quote, not 97.5%. Pairs the K413 image-generator red-team benchmark and the deepfake-detector-attack line.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-09)]
