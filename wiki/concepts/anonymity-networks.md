---
title: Anonymity Networks (Tor / I2P)
type: concept
tags: [anonymity, privacy, tor]
keywords: [tor, onion routing, anonymity, dark web, i2p]
related:
  - concepts/osint-for-cybersecurity.md
  - sources/the-onion-router-overview-pt-1.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/osint-for-cybersecurity.md
- @sources/the-onion-router-overview-pt-1.md
- @entities/people/joas-a-santos.md

## Raw Concept

Anchored by The Onion Router - Overview PT 1.pdf.

## Narrative

Tor (The Onion Router) is the most widely used anonymity network. Each request is wrapped in three layers of encryption + routed through three relay nodes (entry / middle / exit), each peeling one layer — neither any single relay nor any single observer sees both source + destination. **Tor is not magic anonymity**: traffic correlation attacks (NetFlow + timing) work against under-resourced attackers; misuse (logging in to identity-tied accounts over Tor) defeats the design; many onion services have been deanonymized through OPSEC mistakes by their operators (FBI v. Silk Road etc.). For cybersecurity investigators: Tor browser in a VM for dark-web OSINT, never copy-paste anything identifying.
