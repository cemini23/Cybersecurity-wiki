---
title: "SIDE — sensor impersonation detection at the edge (arXiv 2609.06271)"
type: source
tags: [source, arxiv, iot, edge, wireless, lab-only, k338]
keywords: [2609.06271, SIDE, sensor impersonation, IoT, LSTM, sequence prediction]
related:
  - concepts/side-sensor-impersonation-edge-detection.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — edge sensor impersonation PoC; owned-device lab only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K338)"
---

## Relations

- @concepts/side-sensor-impersonation-edge-detection.md — K338 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SIDE: Sensor Impersonation Detection at the Edge via Sequence Prediction |
| arXiv | 2609.06271 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.06271-side-sensor-impersonation-detection-at-the-edge.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

Low-cost IoT deployments without device-level authentication are vulnerable to **sensor impersonation**. **K338 (SIDE)** detects injected readings via **sequence prediction** on univariate sensor streams (LSTM PoC). **Authorized lab / owned devices only** — not a substitute for cryptographic source authentication; pairs open-set RF/device identity research (K326).

## Snippets

> Sequence-prediction anomaly detection for sensor impersonation on unauthenticated IoT streams. [Source: arXiv 2609.06271 abstract]
