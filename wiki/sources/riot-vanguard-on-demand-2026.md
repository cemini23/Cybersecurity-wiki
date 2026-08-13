---
title: Vanguard On-Demand (Riot Games, 2026)
type: source
tags: [source, anti-cheat, riot, vanguard, vendor-doc]
keywords: [Vanguard On-Demand, Pre-Check, TPM EK, fTPM, Runtime Driver Attestation, 25H2]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - entities/tools/riot-vanguard.md
  - sources/microsoft-getruntimeattestationreport.md
  - concepts/game-hacking.md
  - sources/microsoft-kernel-dma-protection.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Riot architecture/policy; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — load-order exception when attestation exists; TPM EK as HWID
- @entities/tools/riot-vanguard.md
- @sources/microsoft-getruntimeattestationreport.md
- @concepts/game-hacking.md
- @sources/microsoft-kernel-dma-protection.md — IOMMU fencing is one of the Pre-Check requirements
- @concepts/secure-boot-vs-device-ownership.md — Pre-Check is the AC face of the boot trust stack; custom-device owners fail it

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Vanguard On-Demand - Anti-Cheat Update |
| Publisher | Riot Games |
| URL | https://www.riotgames.com/en/news/vanguard-on-demand |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party announcement: on machines that pass **Vanguard Pre-Check**, `vgk` need not load at boot. Driver starts with the Riot title and can stop after. Pre-Check: Windows 11 **25H2+**, Secure Boot, TPM 2.0, VBS, HVCI, IOMMU. Mechanism: Microsoft **Runtime Driver Attestation Report** measures on-demand drivers into the TPM so Vanguard can see loads that happened while it was dormant. [CONFIRMED Riot]

Hardware-identity steal: Riot states a TPM **Endorsement Key** is factory-burned and “non-fungible”; a ban on that key would require physically replacing the TPM (or the CPU, for fTPM). Pre-Check accepts dTPM or fTPM; **restricted** accounts must use **fTPM** because discrete TPMs are often socketed and cheap to swap. [CONFIRMED Riot]

This does **not** make registry HWID changers viable. It moves the observation window from boot-start to attested driver history + TPM identity.

## Snippets

> "A TPM’s Endorsement Key is physically burned into its non-volatile memory at the factory, so if we were to decide to ban this key on sight, any cheater hoping to bypass that ban would need to physically remove and replace their banned chip, or even more amusingly, replace the entire CPU"
[Source: https://www.riotgames.com/en/news/vanguard-on-demand (retrieved 2026-08-12)]

> "we can only allow fTPMs to satisfy this requirement, because discrete TPMs are often not even soldered to the motherboard anymore, and we think a hardware ban bypass should cost more than $5 and the 10 minutes it takes to pop in a new one."
[Source: same]
