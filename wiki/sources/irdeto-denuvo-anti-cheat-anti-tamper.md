---
title: Denuvo Anti-Cheat kernel + Anti-Piracy (Irdeto)
type: source
tags: [source, anti-tamper, anti-cheat, denuvo, vendor-doc]
keywords: [Denuvo, Irdeto, kernel anti-cheat, anti-piracy, anti-tamper, binary protection, server-side enforcement]
related:
  - concepts/anti-tamper-protection-classes.md
  - entities/tools/denuvo.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — vendor marketing/architecture pages only; no scene RE ingested"
wire_status: wont_wire
---

## Relations

- @concepts/anti-tamper-protection-classes.md — vendor exemplar of the anti-tamper + kernel-AC classes
- @entities/tools/denuvo.md — entity stub (REFERENCE, wont_wire)
- @concepts/hardware-bound-identity-anticheat-licensing.md — kernel AC as a sibling of the mapped ACs

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Denuvo Kernel Anti-Cheat; Denuvo Anti-Piracy (two product pages) |
| Publisher | Irdeto |
| URL | https://irdeto.com/video-games/denuvo-anti-cheat/kernel-anti-cheat ; https://irdeto.com/video-games/denuvo-anti-piracy/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Two sibling Denuvo-by-Irdeto products, ingested as **vendor architecture/marketing claims** (first-party only; scene RE explicitly not ingested).

**Kernel Anti-Cheat:** kernel-mode AC for online/esports titles — monitors low-level activity (memory, drivers, system manipulation) "beyond the reach of user-mode cheats"; feeds a server-side layer with real-time response and "confident sanctioning with auditable technical evidence"; the driver runs only while the protected game is active (demand-start class, like BattlEye/EAC); post-build binary rewriting; Windows 10/11 + Linux via Proton. Claimed stats: 4.8M+ cheat-detection events, 87K+ sanctioned, 17M+ users, 758K+ binaries protected.

**Anti-Piracy (anti-tamper):** protects executables against cracking/tampering at launch, secures DLC/content, "reinforcing platform DRM systems"; three-part model — protection (binary anti-tamper, no technical internals disclosed), intelligence (P2P/piracy-site monitoring), enforcement (takedowns, payment disruption). No quantitative claims on this page.

Class mapping for the wiki: kernel AC = kernel/OS trust-stack class + server-authority class; anti-piracy = integrity-check + online-heartbeat class. Both sit in @concepts/anti-tamper-protection-classes.md §2.

## Snippets

> "Monitor low-level system activity beyond the reach of user-mode cheats"

> "The kernel driver runs only while the protected game is active."

[Source: https://irdeto.com/video-games/denuvo-anti-cheat/kernel-anti-cheat (retrieved 2026-08-12)]

> "Prevent piracy at launch by securing executables with robust anti-piracy technology." … "reinforcing platform DRM systems to ensure only legitimate users can play"

[Source: https://irdeto.com/video-games/denuvo-anti-piracy/ (retrieved 2026-08-12)]
