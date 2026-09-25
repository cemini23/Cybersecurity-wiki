---
title: "Controller-only false confirmation in passive RF UAV link detection"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.25294, k364]
related:
  - concepts/passive-rf-uav-controller-only-false-confirmation.md
  - concepts/through-wall-detection-sdr-pca.md
maturity: validated
read_status: deep-read
created: 2026-09-24
updated: 2026-09-24
phase_0_verdict: "REFERENCE 2026-09-24 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K364)"
---

## Relations

- @concepts/passive-rf-uav-controller-only-false-confirmation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Controller-only false confirmation in passive RF UAV link detection |
| arXiv | 2609.25294 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.25294-controller-only-false-confirmation-in-passive-rf.pdf |
| Retrieved | 2026-09-24 |
| Read status | deep-read (2026-09-25) |

## Narrative

**K364** — dual-band **USRP B210** passive RF study (GMU) on **DJI Phantom 3 4K, Hubsan H501S, DJI Mavic Mini** with explicit **ambient**, **controller-only**, and **linked** states (20 rounds; 2.4 + 5.8 GHz window grid). Detector trained on **linked + ambient only** hits **0.992** balanced linked-vs-ambient accuracy but **false-confirms 30/60** controller-only scans (**FCR_ctrl = 0.500**). Adding controller-only negatives with **confirm / reject / defer** under an **FCR constraint** cuts pooled **FCR_ctrl** from **0.350 → 0.050** but drops confirm-linked TPR **0.900 → 0.400** with **42.1% deferred**; platform mix matters (Hubsan/Mavic vs Phantom). **HIL** scan time **82.9 s → 28.9 s** for compact ranked scan.

Steal: always report **controller-only false confirmation** separately from linked-vs-background accuracy. **Authorized RF lab / owned spectrum only.**
## Snippets

> "An energy-feature detector trained only on linked and ambient scans reaches 0.992 balanced accuracy … but false-confirms 30 of 60 controller-only scans." [Source: arXiv 2609.25294 abstract]

> "For the pooled all-platform analysis, the constraint reduces observed FCR_ctrl from 0.350 to 0.050, while confirm-linked TPR decreases from 0.900 to 0.400 and 42.1% of scans are deferred." [Source: arXiv 2609.25294]