---
title: Kernel anti-cheat vs rootkit taxonomy (ARES 2024 / arXiv 2408.00500)
type: source
tags: [source, arxiv, anti-cheat, kernel, privacy]
keywords: [2408.00500, ARES 2024, Dorner, Klausner, FACEIT, Vanguard, BattlEye, EAC]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - entities/tools/battleye.md
  - entities/tools/easy-anti-cheat.md
  - entities/tools/riot-vanguard.md
  - sources/faceit-enhanced-verification.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — paper; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md
- @concepts/game-hacking.md
- @entities/tools/battleye.md
- @entities/tools/easy-anti-cheat.md
- @entities/tools/riot-vanguard.md
- @sources/faceit-enhanced-verification.md — FACEIT first-party hardware-identifier policy

## Raw Concept

| Field | Value |
|-------|-------|
| Title | If It Looks Like a Rootkit and Deceives Like a Rootkit: A Critical Examination of Kernel-Level Anti-Cheat Systems |
| Authors | Christoph Dorner, Lukas Daniel Klausner (FH St. Pölten) |
| Venue | ARES 2024 |
| arXiv | 2408.00500 |
| DOI | 10.1145/3664476.3670433 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2408.00500-kernel-anticheat-rootkit-taxonomy.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

Taxonomy paper: define rootkit-like metrics, then score BattlEye, EAC, FACEIT AC, Vanguard. BattlEye and EAC = minor similarities, not classified as rootkits under their metrics. FACEIT AC and Vanguard = rootkit-like (intrusiveness / stealth / boot behavior). Authors separate **capability** from **intent** and flag privacy cost of kernel AC. [CONFIRMED abstract]

Steal: when building or pentesting an AC, budget privacy + boot-start vs demand-start as first-class design axes, not afterthoughts.

## Snippets

> "The anti-cheat systems BattlEye and Easy Anti-Cheat showed minor similarities to rootkits, which were insufficient to classify them as such according to our metrics. FACEIT Anti-Cheat and Vanguard, however, were identified as rootkit-like applications"
[Source: arxiv-2408.00500 abstract]
