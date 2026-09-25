---
title: "Learning to Link — BLE re-identification under MAC randomization"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.26079, k365]
related:
  - concepts/ble-mac-randomization-reidentification-lab.md
  - concepts/bluetooth-nft-soft-pairing.md
maturity: validated
read_status: deep-read
created: 2026-09-24
updated: 2026-09-24
phase_0_verdict: "REFERENCE 2026-09-24 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K365)"
---

## Relations

- @concepts/ble-mac-randomization-reidentification-lab.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Learning to Link — BLE re-identification under MAC randomization |
| arXiv | 2609.26079 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.26079-learning-to-link-automatic-re-identification-of.pdf |
| Retrieved | 2026-09-24 |
| Read status | deep-read (2026-09-25) |

## Narrative

**K365** — ML **linking** of BLE **RPA** epochs from **Extended Advertising** plaintext fields (KAUST/Politecnico). **14** target devices in pools of hundreds; with **two** observed RPA epochs, a **decision tree** reaches **~98.6% recall**, **<2%** packet-level FPR, **0.38%** false device IDs after MAC aggregation. Field note: only **~1/3** of observed devices in their traces actually use RPA **15 years** after introduction.

Defensive steal: **pairing ≠ authorization**; MAC randomization ≠ unlinkability. **Runtime:** `k365_ble_reid_lab_precheck.py`. **Owned devices only.**
## Snippets

> "Even when trained on only two observed RPA epochs, a simple decision tree can recover almost all advertisements from the target (98.6% recall), with a packet-level FPR below 2%." [Source: arXiv 2609.26079 abstract]

> "Only 1/3 of observed devices do not even support [RPA]." [Source: arXiv 2609.26079]