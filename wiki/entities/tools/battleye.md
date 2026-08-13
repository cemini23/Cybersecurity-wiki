---
title: BattlEye
type: entity
tags: [tool, anti-cheat, kernel, windows]
keywords: [BattlEye, BEDaisy, BEService, BEClient, HWID]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - sources/secret-club-battleye-architecture-2019.md
  - sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
  - sources/s4dbrd-kernel-anti-cheats.md
  - entities/tools/easy-anti-cheat.md
  - entities/tools/riot-vanguard.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE — third-party AC; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md
- @concepts/game-hacking.md
- @sources/secret-club-battleye-architecture-2019.md
- @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md — minor rootkit-like traits under ARES metrics
- @sources/s4dbrd-kernel-anti-cheats.md — demand-start `BEDaisy.sys`
- @entities/tools/easy-anti-cheat.md
- @entities/tools/riot-vanguard.md

## Raw Concept

Third-party kernel anti-cheat (Bastian Suter). Used across many titles (PUBG, R6, DayZ, Arma, … — title list rots). Four-part public model: BEDaisy / BEService / BEClient / BEServer.

## Narrative

Demand-start kernel driver with the game process. ARES 2024 did **not** classify BattlEye as rootkit-like under their metrics (unlike Vanguard/FACEIT). HWID bans are a backend policy on the identifier bundle, not a single registry value. Lab: architecture RE only; no ban-evasion kits.
