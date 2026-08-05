---
title: AirKey Wi-Fi CSI + acoustic PIN inference (arXiv 2608.03151)
type: source
tags: [source, arxiv, wireless, side-channel, wifi, privacy]
keywords: [2608.03151, AirKey, CSI, PIN inference, keystroke, ACK harvesting]
related:
  - concepts/airkey-wifi-acoustic-pin-sidechannel.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-05
updated: 2026-08-05
phase_0_verdict: "REFERENCE 2026-08-05 — no public code; dual-use side-channel; lab/authorized only"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

**Briefs:** `briefs/2026-08-05_k242-airkey-pin-sidechannel-prod.md`

## Relations

- @concepts/airkey-wifi-acoustic-pin-sidechannel.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md
- @concepts/social-engineering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AirKey: Multimodal Acoustic-Assisted WiFi Sensing for Zero-Training Robust PIN Inference |
| Authors | Wu, Liu, Zhang, Liu, Zhang, Liu, Yan, Li |
| arXiv | 2608.03151 |
| DOI | 10.1145/3767308.3836211 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.03151-airkey-multimodal-acoustic-assisted-wifi-sensing.pdf` |
| Retrieved | 2026-08-05 |

## Narrative

Contactless PIN/keystroke inference via **Wi-Fi CSI** + lightweight **acoustic temporal anchors**. Bypasses need for network association: elicits 802.11 **ACK**s from unmodified targets and harvests CSI on a cheap MCU. Pure-WiFi fails on rapid muscle-memory typing ("waveform fusion"); audio provides timing. Zero-training, stealthy eavesdrop class. [CONFIRMED abstract]

### Steal (defender + authorized lab)

1. Physical/wireless scope: CSI-from-ACK + mic is a realistic PIN side channel — not just classic aircrack
2. Mitigations: distance/RF hygiene, disable unused radios, acoustic masking, PIN entry shielding
3. **No LIVE / unauthorized** use — lab or written physical-pentest scope only

## Snippets

> "AirKey secures a continuous spatial sensing stream entirely without network association."
[Source: arXiv 2608.03151 abstract]
