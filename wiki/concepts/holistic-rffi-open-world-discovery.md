---
title: "Keep the open-set score; it is the discovery signal (K419)"
type: concept
tags: [concept, agent-security, k419]
keywords: [2610.05979, K419]
related:
  - sources/arxiv-2610-05979-holistic-rffi-vector-quantization.md
  - concepts/horffi-high-openness-rffi.md
  - concepts/wifi-rf-fingerprinting-open-set.md
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/rf-fingerprint-temperature-drift.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K419)"
---

## Relations

- @sources/arxiv-2610-05979-holistic-rffi-vector-quantization.md
- @concepts/horffi-high-openness-rffi.md
- @concepts/wifi-rf-fingerprinting-open-set.md
- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/rf-fingerprint-temperature-drift.md

## Raw Concept

Question: **Keep the open-set score; it is the discovery signal** — operator steal from arXiv 2610.05979?

## Narrative

Device identification from RF fingerprints is usually three pipelines bolted together: classify a registered device, reject an unknown one, then cluster the rejects. K419 shows the three are one problem and that **the coupling is the point** — the **uncertainty the open-set stage produces is the signal that makes discovery work**, so collapsing it to a binary reject/fail decision before clustering throws away exactly what is needed.

One **learned codebook** carries all three: codewords name registered devices, codebook **geometry** gives the open-set score, and expansion of the codebook registers a newly discovered transmitter. Measured on LoRa and Wi-Fi: **97.9%** closed-set at ten devices, **81.8%** new-device accuracy with five unseen devices, **90.3%** with seven rogue transmitters. Operator rule for a rogue-device or unauthorized-transmitter detector: **preserve the continuous novelty score and design for expansion** — an unknown device should become a named one without a retrain. Pairs K326 (open-set Wi-Fi CSI) and K245 (high-openness RFFI). Authorized RF lab only.

## Snippets

> See arXiv 2610.05979 abstract. [Source: arXiv 2610.05979 (retrieved 2026-10-12)]
