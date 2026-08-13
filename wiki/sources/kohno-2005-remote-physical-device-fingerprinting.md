---
title: Remote Physical Device Fingerprinting (Kohno / Broido / claffy 2005)
type: source
tags: [source, fingerprinting, privacy, clock-skew, opsec]
keywords: [Kohno, clock skew, TCP timestamps, ICMP timestamp, physical device fingerprint]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/anonymity-networks.md
  - concepts/agent-vm-sandboxing.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — classic paper; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md — physical fingerprints survive software ID changes
- @concepts/anonymity-networks.md — IP/Tor path change does not reset clock skew
- @concepts/agent-vm-sandboxing.md — paper notes some VM clocks look unlike real hardware

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Remote Physical Device Fingerprinting |
| Authors | Tadayoshi Kohno, Andre Broido, kc claffy |
| Venue | IEEE S&P / TDSC 2005 |
| PDF | https://www.caida.org/catalog/papers/2005_fingerprinting/KohnoBroidoClaffy05-devicefingerprinting.pdf |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/kohno-2005-remote-physical-device-fingerprinting.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

Introduces **remote physical** (not OS-class) fingerprinting via microscopic clock skew, mainly from TCP timestamps (works with NTP) and optionally ICMP timestamp replies. Measurements stay consistent across thousands of miles, NATs, and access technologies. Applications they list include tracking a laptop across access points, counting hosts behind NAT, detecting virtual honeynets, and helping de-anonymize traces. [CONFIRMED paper]

OPSEC steal: changing IP, MAC, or cookies does not change the oscillator. High-threat anonymity needs a different physical clock domain (different machine / carefully configured VM), not an identifier patch.

## Snippets

> "We introduce the area of remote physical device fingerprinting, or fingerprinting a physical device, as opposed to an operating system or class of devices, remotely, and without the fingerprinted device's known cooperation."
[Source: Kohno 2005 abstract]
