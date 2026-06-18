---
title: Cyberwarfare
type: concept
tags: [nation-state, geopolitics, strategy]
keywords: [cyberwarfare, nation state, apt, cyber operations]
related:
  - concepts/adversary-emulation.md
  - concepts/red-team-operations.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/apt28.md
  - entities/threat-actors/apt29.md
  - entities/threat-actors/lazarus.md
  - sources/cyberwarfare-books-1.md
  - sources/arxiv-2606-19106-exceptional-access-compromise-risk-quantification.md
  - concepts/exceptional-access-risk-quantification.md
maturity: draft
created: 2026-05-12
updated: 2026-06-18
---

## Relations

- @concepts/adversary-emulation.md
- @concepts/red-team-operations.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/apt28.md
- @entities/threat-actors/apt29.md
- @entities/threat-actors/lazarus.md
- @sources/cyberwarfare-books-1.md


## Raw Concept

Anchored by cyberwarfare books #1.pdf.

## Narrative

Cyberwarfare = nation-state use of cyber operations as a strategic instrument. Covers espionage (intelligence collection — APTs), sabotage (Stuxnet, NotPetya, Industroyer), influence operations (information warfare overlapping with cybersecurity but distinct), and the doctrinal / legal questions (Tallinn Manual, application of LOAC to cyber, attribution challenges). Adjacent reading anchors live in the threat-actor profiles.

### Lawful-intercept and platform key infrastructure as campaign objectives

Recent campaigns demonstrate that **cryptographic control points** — not just end-user endpoints — are primary nation-state targets:

- **Salt Typhoon (2024):** compromise of CALEA-mandated lawful-intercept infrastructure at US carriers — transmission-layer EA (T-EA) surface.
- **Storm-0558 (2023):** theft of Microsoft consumer signing key enabling token forgery at platform scale — OTT-EA analogue.
- **Crypto AG / Operation Rubicon:** covert operation of cryptographic infrastructure as an intelligence channel.

arXiv:2606.19106 formalises why these incidents matter structurally: EA mandates and platform master-key custody create **irreversible** compromise outcomes (retrospective decryption) that standard expected-value policy framing may underweight. See @concepts/exceptional-access-risk-quantification.md.
