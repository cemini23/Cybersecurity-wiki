---
title: Denuvo (Irdeto)
type: entity
tags: [tool, anti-tamper, anti-cheat, vendor, drm]
keywords: [Denuvo, Irdeto, anti-tamper, anti-piracy, kernel anti-cheat, DRM]
related:
  - concepts/anti-tamper-protection-classes.md
  - sources/irdeto-denuvo-anti-cheat-anti-tamper.md
  - concepts/game-hacking.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE — commercial protection vendor; no clone, no scene RE"
wire_status: wont_wire
---

## Relations

- @concepts/anti-tamper-protection-classes.md — exemplar of the integrity-check / online-heartbeat / kernel classes
- @sources/irdeto-denuvo-anti-cheat-anti-tamper.md — first-party product pages (kernel AC + anti-piracy)
- @concepts/game-hacking.md — anti-cheat vendor adjacent to the mapped ACs
- @concepts/hardware-bound-identity-anticheat-licensing.md — same consumer space as BattlEye/EAC/Vanguard entities

## Raw Concept

Vendor entity for Irdeto's Denuvo product family, prompted by the 2026-08-12 anti-tamper ingest. REFERENCE-only: closed-source commercial protection; nothing to clone, nothing to wire.

## Narrative

**Denuvo Kernel Anti-Cheat** — demand-start kernel AC for online/esports titles; kernel-level monitoring + server-side enforcement with auditable evidence; Windows 10/11 + Linux via Proton.

**Denuvo Anti-Piracy** — executable anti-tamper ("securing executables with robust anti-piracy technology"), DLC/content protection, plus piracy intelligence + enforcement services.

Vendor claims only — no technical internals disclosed on the ingested pages, and no scene RE is ingested in this wiki. Attackers' view of Denuvo is a class problem, not a product problem: see @concepts/anti-tamper-protection-classes.md.
