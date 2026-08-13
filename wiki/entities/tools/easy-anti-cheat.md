---
title: Easy Anti-Cheat (Epic)
type: entity
tags: [tool, anti-cheat, kernel, windows]
keywords: [Easy Anti-Cheat, EAC, Epic, HWID, cross-game ban]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
  - sources/s4dbrd-kernel-anti-cheats.md
  - entities/tools/battleye.md
  - entities/tools/riot-vanguard.md
  - sources/epic-games-v-araujo-hwid-spoofer-judgment.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE — Epic AC; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md
- @concepts/game-hacking.md
- @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md — minor rootkit-like traits
- @sources/s4dbrd-kernel-anti-cheats.md — demand-start, three-component like BattlEye
- @entities/tools/battleye.md
- @entities/tools/riot-vanguard.md
- @sources/epic-games-v-araujo-hwid-spoofer-judgment.md — Epic pled HWID bans + spoofers as DMCA circumvention (Fortnite; adjacent to EAC titles)

## Raw Concept

Epic-owned kernel anti-cheat (Fortnite, Apex, Rust, many others — list rots). Demand-start driver with the title.

## Narrative

Same architectural class as BattlEye (session-bound kernel + service + game DLL). Public commentary claims **cross-title** hardware-ban sharing inside the EAC network — treat as [TENTATIVE] until a first-party Epic policy page is ingested. Steam-hosted EAC EULA (https://store.steampowered.com/eula/292000_eula_0) states permanent bans and delayed bans — [TENTATIVE] re-read before citing retention windows. ARES 2024: not classified rootkit-like under their metrics. Lab: no spoof kits; if you ship a game on EAC, assume the HWID tuple is Epic’s, not yours. US docket *Epic v. Araujo* shows Epic will plead HWID spoof as circumvention.
