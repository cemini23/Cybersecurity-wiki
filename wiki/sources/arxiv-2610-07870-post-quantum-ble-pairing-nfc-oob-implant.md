---
title: "Plug-and-play quantum-resistant BLE pairing for medical implants via NFC out-of-band"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.07870, k404]
related:
  - concepts/post-quantum-oob-pairing-medical-implants.md
  - concepts/wireless-pentest.md
  - concepts/ble-mac-randomization-reidentification-lab.md
  - concepts/ble-backscatter-polarization-shift-identification-lab.md
  - concepts/mobile-app-attestation.md
maturity: draft
read_status: read
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K404)"
---

## Relations

## Relations

- @concepts/post-quantum-oob-pairing-medical-implants.md
- @concepts/wireless-pentest.md
- @concepts/ble-mac-randomization-reidentification-lab.md
- @concepts/ble-backscatter-polarization-shift-identification-lab.md
- @concepts/mobile-app-attestation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Plug-and-play quantum-resistant BLE pairing for medical implants via NFC out-of-band |
| arXiv | 2610.07870 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.07870-plug-and-play-quantum-resistant-ble-pairing-for.pdf |
| Retrieved | 2026-10-07 |
| Read status | read (deep-read) |

## Narrative

**K404** — BLE pairing is the cryptographic foundation for implant communication, but the MITM-resistant association models (**Numeric Comparison**, **Passkey Entry**) need a UI that an implantable medical device does not have. **NFC out-of-band** pairing is the usual workaround; the problem is that existing NFC-OOB schemes only *authenticate* a **classical** BLE key exchange (quantum-vulnerable), and the NFC channel itself is eavesdroppable and open to active injection under a stronger threat model. The proposal runs a **post-quantum KEM (Kyber / FireSABER) entirely over the NFC channel**, so **no shared secret is transmitted over NFC** at all, long-range RF exposure during pairing drops, the **BLE stack is unchanged**, and it inherently resists **RF battery-depletion** attacks. On an IMD-class testbed the overhead is **under 0.57% for Kyber-1024 and 0.56% for FireSABER**. Operator steal: **harvest-now-decrypt-later applies to pairing**, not just transport — an OOB channel that authenticates a classical exchange is a temporary fix; and a very short-range channel is a **threat-model** control, not just a convenience. Authorized device lab only. **No pairing bypass or key-recovery recipes in wiki.**

## Snippets

> See arXiv 2610.07870 abstract. [Source: arXiv 2610.07870 (retrieved 2026-10-07)]
