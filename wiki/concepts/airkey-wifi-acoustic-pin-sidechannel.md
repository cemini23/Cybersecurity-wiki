---
title: AirKey — Wi-Fi CSI + acoustic PIN side channel
type: concept
tags: [concept, wireless, side-channel, privacy]
keywords: [AirKey, CSI, ACK harvesting, PIN inference, 2608.03151]
related:
  - sources/arxiv-2608-03151-airkey-wifi-acoustic-pin-inference.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
  - concepts/inaudible-low-frequency-audio-attacks.md
maturity: draft
created: 2026-08-05
updated: 2026-08-11
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2608-03151-airkey-wifi-acoustic-pin-inference.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md
- @concepts/social-engineering.md
- @concepts/ai-for-cybersecurity.md
- @concepts/inaudible-low-frequency-audio-attacks.md — cross-modal sensing sibling: inaudible LF audio exfiltration/red-team on LALM targets

## Raw Concept

Unauthenticated ACK-CSI plus cheap audio can recover PINs without joining the victim WLAN.

## Narrative

Extends wireless-pentest beyond handshake/WPS into **cross-modal sensing**. Operator/friend labs: treat nearby PIN entry + Wi-Fi + mic as in-scope physical risk on owned devices only. Dual-use — document defenses; do not ship attack code. [CONFIRMED abstract]
