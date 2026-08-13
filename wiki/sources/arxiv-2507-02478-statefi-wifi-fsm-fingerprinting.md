---
title: StateFi — Wi-Fi device identification via state transitions (arXiv 2507.02478)
type: source
tags: [source, arxiv, wifi, privacy, mac-randomization]
keywords: [2507.02478, StateFi, FSM, Cunche, Mishra, management frames]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/wireless-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — paper; no public tool adopt"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md
- @concepts/wireless-pentest.md — FSM de-randomization vs IE/SEQ lineage

## Raw Concept

| Field | Value |
|-------|-------|
| Title | StateFi: Effectively Identifying Wi-Fi Devices through State Transitions |
| Authors | Abhishek K. Mishra, Mathieu Cunche (Inria / INSA-Lyon) |
| arXiv | 2507.02478 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2507.02478-statefi-wifi-device-state-transitions.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

2025 result: randomization hides identifiers, not **management-plane behavior** (scan/assoc/retry timing as FSMs). Campus + public datasets: in-network full-management FSM accuracy 94–97%; probe-only under randomization up to 97%; discrimination accuracy up to 98% (+17 pp vs strongest prior IE+SEQ+RSSI signature). Authors call for behavioral obfuscation in future 802.11, not just address rotation. [CONFIRMED abstract]

OPSEC steal: 2016 “IE fingerprint” findings were not a historical footnote — 2025 behavior models still de-randomize at high accuracy.

## Snippets

> "randomized identifiers provide incomplete protection against behavioral re-identification."
[Source: arxiv-2507.02478 §1]
