---
title: A Study of MAC Address Randomization in Mobile Devices and When it Fails (PETS 2017)
type: source
tags: [source, arxiv, wifi, privacy, mac-randomization]
keywords: [1703.02874, PETS 2017, Martin, USNA, UUID-E, control frame]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/wireless-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — paper; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md
- @concepts/wireless-pentest.md — extends Vanhoef-style probe fingerprinting in the wild

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Study of MAC Address Randomization in Mobile Devices and When it Fails |
| Authors | Martin, Mayberry, Donahue, Foppe, Brown, Riggins, Rye, Brown (USNA / MITRE) |
| arXiv | 1703.02874 |
| Venue | PoPETs 2017(4) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-1703.02874-mac-address-randomization-when-it-fails.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

First wide-scale wild measurement of MAC randomization by OS/vendor/model. Failures: devices send the **global** MAC when they should randomize; extended Vanhoef-style passive identification to ~96% of Android phones in their corpus; previously unknown wireless-chipset control-frame handling flaw allowed tracking **100%** of tested randomizing devices (Android still susceptible in some cases with Wi-Fi off / airplane mode). [CONFIRMED abstract]

OPSEC steal: implementation quality varies by vendor; “randomization enabled” in settings is not a measurement. Control-frame / chipset bugs are below the OS toggle.

## Snippets

> "we show a method that can be used to track 100% of devices using randomization, regardless of manufacturer, by exploiting a previously unknown flaw in the way existing wireless chipsets handle low-level control frames."
[Source: arxiv-1703.02874 abstract]
