---
title: "Secure polarization-shift backscatter identification for battery-free BLE"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.29213, k370]
related:
  - concepts/ble-backscatter-polarization-shift-identification-lab.md
  - concepts/ble-mac-randomization-reidentification-lab.md
maturity: draft
read_status: read
created: 2026-09-25
updated: 2026-09-25
phase_0_verdict: "REFERENCE 2026-09-25 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K370)"
---


## Relations

- @concepts/ble-backscatter-polarization-shift-identification-lab.md
- @concepts/ble-mac-randomization-reidentification-lab.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Secure polarization-shift backscatter identification for battery-free BLE |
| arXiv | 2609.29213 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609-29213-secure-polarization-shift-backscatter-identifica.pdf |
| Retrieved | 2026-09-25 |
| Read status | read (abstract + triage) |

## Narrative

**K370** — **SWIPT** battery-free BLE nodes can transmit **AES-128 encrypted device ID** via **polarization-shift backscatter** on the power wave before data traffic, using an external RF switch + orthogonal antennas (no rectifier modification). Defensive **device authentication** steal for IoT lab eval — **owned devices / authorized RF only**; pairs K305/K365 service-auth vs radio anonymity.

## Snippets

> See arXiv 2609.29213 abstract. [Source: arXiv 2609.29213 (retrieved 2026-09-25)]
