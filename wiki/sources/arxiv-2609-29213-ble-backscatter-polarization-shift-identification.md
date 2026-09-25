---
title: "Secure polarization-shift backscatter identification for battery-free BLE"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.29213, k370]
related:
  - concepts/ble-backscatter-polarization-shift-identification-lab.md
  - concepts/ble-mac-randomization-reidentification-lab.md
maturity: validated
read_status: deep-read
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
| Read status | deep-read (2026-09-25) |

## Narrative

**K370** adds a **protocol-independent** identification layer for **battery-free BLE** nodes in **SWIPT**: before each BLE advertising burst, the node backscatters an **AES-128** identification frame on the wireless power wave using **orthogonal polarization** (incident P-wave vs backscattered ID on H vs V monopoles) and a **fail-safe SPDT RF switch** (default routes harvest path; toggled for controlled backscatter). **PvK** frame: 16-bit preamble `0xAAAA` + 16-byte key, **Manchester-coded** up to **50 kHz**, key material from on-chip ADC entropy. Platform: **NXP QN9080** BLE SoC, **e-peas AEM30940** PMU, 868 MHz rectifier; CN uses RF source + **Tektronix RSA306B** on orthogonal receive antenna.

Goal: authenticate the BFSN **before** sensor data advertisements (replay/flooding resistance). Defensive lab steal — test **service authorization** after link establishment, not RF anonymity alone (pairs K365/K305). **Authorized owned devices / RF lab only.**
## Snippets

> "The backscattered identification signal is transmitted using a polarization orthogonal to that of the incident P-wave." [Source: arXiv 2609.29213]

> "The PvK frame includes a 16-bit preamble (0xAAAA) followed by a 16-byte key, Manchester-coded at up to 50 kHz. The key is generated using AES-128." [Source: arXiv 2609.29213]