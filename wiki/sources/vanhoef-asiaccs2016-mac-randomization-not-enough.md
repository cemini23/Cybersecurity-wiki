---
title: Why MAC Address Randomization is not Enough (AsiaCCS 2016)
type: source
tags: [source, wifi, privacy, mac-randomization, opsec]
keywords: [Vanhoef, AsiaCCS 2016, probe request, IE fingerprint, scrambler seed, Hotspot 2.0, ANQP]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/wireless-pentest.md
  - concepts/anonymity-networks.md
  - concepts/association-inference-attack-wireless.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-13
phase_0_verdict: "REFERENCE 2026-08-12 — paper; no clone"
wire_status: wont_wire
wire_target: "REFERENCE — MAC randomization insufficiency evidence"
---

## Relations

- @concepts/hardware-id-masking-opsec.md — primary synthesis
- @concepts/wireless-pentest.md — probe-request / fake-AP surfaces
- @concepts/anonymity-networks.md — Tails MAC design is discussed in §2.1.4 of this paper

- @concepts/association-inference-attack-wireless.md
## Raw Concept

| Field | Value |
|-------|-------|
| Title | Why MAC Address Randomization is not Enough: An Analysis of Wi-Fi Network Discovery Mechanisms |
| Authors | Vanhoef, Matte, Cunche, Cardoso, Piessens |
| Venue | AsiaCCS 2016 |
| DOI | 10.1145/2897845.2897883 |
| PDF | https://papers.mathyvanhoef.com/asiaccs2016.pdf |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/vanhoef-asiaccs2016-why-mac-address-randomization-is-not-enough.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

Shows that random MACs alone do not guarantee privacy for unassociated Wi-Fi clients. IE content/order fingerprints devices; sequence numbers often continue across identifier changes; 802.11 scrambler seeds are hardware-predictable (harder to patch in software). Active: fake popular SSIDs (17.4% global MAC with 5 SSIDs) and Hotspot 2.0 ANQP (Linux/Windows used real MAC; 5.2%). Tracking algorithm linked ~50% of devices for ≥20 minutes in their datasets. [CONFIRMED paper]

OPSEC steal: enable OS randomization **and** assume probe metadata + PHY still link; do not treat MAC change as unlinkability.

## Snippets

> "using random MAC addresses, on its own, does not guarantee privacy."
[Source: vanhoef-asiaccs2016 abstract]

> "The scrambler seed is managed by the hardware. Hence it is more difficult, if not impossible, to fix this unwanted predictability through software updates."
[Source: vanhoef-asiaccs2016 §1]
