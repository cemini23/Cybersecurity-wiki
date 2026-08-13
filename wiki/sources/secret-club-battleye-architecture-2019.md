---
title: BattlEye architecture (secret.club, 2019)
type: source
tags: [source, anti-cheat, battleye, reverse-engineering]
keywords: [secret.club, BEDaisy, BEService, BEClient, BEServer]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - entities/tools/battleye.md
maturity: draft
read_status: skimmed
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — architecture only; bypass body not ingested as runbook"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — four-entity model
- @concepts/game-hacking.md
- @entities/tools/battleye.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BattlEye anti-cheat: analysis and mitigation |
| Author | secret.club |
| URL | https://secret.club/2019/02/10/battleye-anticheat.html |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Public RE of BattlEye’s four entities: **BEService** (SYSTEM service ↔ BEServer), **BEDaisy** (kernel callbacks/minifilters), **BEClient** (DLL mapped into the game — most detection vectors in this article), **BEServer** (ban/kick decisions). Dated 2019; detections rot. The rest of the post is cheat-oriented (shellcode dump, pattern checks). This wiki keeps the **architecture** and does not file the bypass body as a runbook. [CONFIRMED architecture list; rest unused]

## Snippets

> "BattlEye consists of multiple organs ... BEService ... BEDaisy ... BEClient ... BEServer"
[Source: https://secret.club/2019/02/10/battleye-anticheat.html (retrieved 2026-08-12)]
