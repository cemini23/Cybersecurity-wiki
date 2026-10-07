---
title: "Post-quantum out-of-band pairing for implants (K404)"
type: concept
tags: [concept, agent-security, k404]
keywords: [2610.07870, K404]
related:
  - sources/arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant.md
  - concepts/wireless-pentest.md
  - concepts/ble-mac-randomization-reidentification-lab.md
  - concepts/ble-backscatter-polarization-shift-identification-lab.md
  - concepts/mobile-app-attestation.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K404)"
---

## Relations

- @sources/arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant.md
- @concepts/wireless-pentest.md
- @concepts/ble-mac-randomization-reidentification-lab.md
- @concepts/ble-backscatter-polarization-shift-identification-lab.md
- @concepts/mobile-app-attestation.md

## Raw Concept

Question: **Post-quantum out-of-band pairing for implants** — operator steal from arXiv 2610.07870?

## Narrative

Devices without a screen cannot use MITM-resistant BLE association, so pairing leans on an **out-of-band** channel — usually NFC. Two things follow. First, **harvest-now-decrypt-later reaches pairing**: if the OOB channel merely *authenticates* a classical key exchange, the session is recorded today and broken later. Run the **post-quantum KEM on the OOB channel itself** so no shared secret crosses it. Second, **proximity is a threat-model control** — a very short-range channel shrinks the set of attackers who can inject — but it does not replace authentication, because the channel is still eavesdroppable. Cost is small: under 0.57% overhead, no BLE stack change. Authorized device lab only.

## Snippets

> See arXiv 2610.07870 abstract. [Source: arXiv 2610.07870 (retrieved 2026-10-07)]
