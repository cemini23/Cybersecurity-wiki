---
title: "BLE backscatter polarization-shift identification (lab) (K370)"
type: concept
tags: [concept, agent-security, k370]
keywords: [2609.29213, K370]
related:
  - sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md
  - concepts/ble-mac-randomization-reidentification-lab.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K370)"
---

## Relations

- @sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md
- @concepts/ble-mac-randomization-reidentification-lab.md

## Raw Concept

Question: **BLE backscatter polarization-shift identification (lab)** — operator steal from arXiv 2609.29213?

## Narrative

Lab eval: verify **orthogonal-polarization backscatter ID** completes before BLE advertisements on owned **BFSN** hardware; then test whether application-layer **authorization** still holds. This is **device authentication at the RF harvest layer**, not a substitute for BLE pairing/service access control.
## Snippets

> Polarization-shift backscatter ID under SWIPT before data traffic. [Source: arXiv 2609.29213; K370]