---
title: Anonymity Networks (Tor / I2P)
type: concept
tags: [anonymity, privacy, tor]
keywords: [tor, onion routing, anonymity, dark web, i2p]
related:
  - concepts/osint-for-cybersecurity.md
  - sources/the-onion-router-overview-pt-1.md
  - entities/people/joas-a-santos.md
  - sources/python-ethical-hacking-masterclass.md
  - entities/tools/torbot.md
  - concepts/hardware-id-masking-opsec.md
  - sources/tails-mac-address-anonymization.md
  - sources/vanhoef-asiaccs2016-mac-randomization-not-enough.md
  - sources/kohno-2005-remote-physical-device-fingerprinting.md
  - sources/arxiv-1905-01051-browser-fingerprinting-survey.md
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/censorship-circumvention-pluggable-transports.md
  - sources/tor-support-entry-guards.md
  - sources/murdoch-danezis-low-cost-traffic-analysis.md
  - sources/tor-snowflake.md
  - sources/tor-pluggable-transports.md
  - sources/signal-sealed-sender.md
  - concepts/endpoint-encryption-deniable-storage.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
created: 2026-05-12
updated: 2026-08-12
---

## Relations


- @entities/tools/torbot.md — K220 Tor crawler — GPL-3 Reference-only
- @concepts/osint-for-cybersecurity.md
- @sources/the-onion-router-overview-pt-1.md
- @entities/people/joas-a-santos.md
- @sources/python-ethical-hacking-masterclass.md — video course; section 14 covers anonymity tactics
- @concepts/hardware-id-masking-opsec.md — Tor hides path, not hardware IDs / MAC / clock skew
- @sources/tails-mac-address-anonymization.md — Tails default MAC anonymization (local LAN only)
- @sources/vanhoef-asiaccs2016-mac-randomization-not-enough.md — random MAC ≠ unlinkability
- @sources/kohno-2005-remote-physical-device-fingerprinting.md — clock skew survives IP/Tor path change
- @sources/arxiv-1905-01051-browser-fingerprinting-survey.md — browser fingerprint lane vs host HWID
- @concepts/metadata-traffic-analysis-anonymity.md — traffic-confirmation layer: AS/global observer still links via timing/volume
- @concepts/censorship-circumvention-pluggable-transports.md — DPI/IP blocking is a different threat than traffic confirmation
- @sources/tor-support-entry-guards.md — guard pinning vs a relay-controlling adversary
- @sources/murdoch-danezis-low-cost-traffic-analysis.md — single-AS traffic confirmation (IEEE S&P 2005)
- @sources/tor-snowflake.md — WebRTC volunteer-proxy pluggable transport
- @sources/tor-pluggable-transports.md — PT class taxonomy (obfs4 / meek / FTE / ScrambleSuit)
- @sources/signal-sealed-sender.md — sender hidden from service; destination + timing remain
- @concepts/endpoint-encryption-deniable-storage.md — at-rest confidentiality is a separate plane from network-path anonymity
- @concepts/secure-boot-vs-device-ownership.md — USB-boot anonymity (Tails) collides with Secure Boot policy

## Raw Concept

Anchored by The Onion Router - Overview PT 1.pdf.

## Narrative

Tor (The Onion Router) is the most widely used anonymity network. Each request is wrapped in three layers of encryption + routed through three relay nodes (entry / middle / exit), each peeling one layer — neither any single relay nor any single observer sees both source + destination. **Tor is not magic anonymity**: traffic correlation attacks (NetFlow + timing) work against under-resourced attackers; misuse (logging in to identity-tied accounts over Tor) defeats the design; many onion services have been deanonymized through OPSEC mistakes by their operators (FBI v. Silk Road etc.). Hardware identifiers (MAC, SMBIOS, TPM-backed Windows IDs, clock skew, GPU fingerprints) are a **separate plane** — see @concepts/hardware-id-masking-opsec.md. For cybersecurity investigators: Tor browser in a VM for dark-web OSINT, never copy-paste anything identifying.
