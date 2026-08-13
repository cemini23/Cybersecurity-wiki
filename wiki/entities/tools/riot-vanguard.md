---
title: Riot Vanguard
type: entity
tags: [tool, anti-cheat, kernel, windows, boot-start]
keywords: [Vanguard, vgk.sys, vgauth, Valorant, TPM, Secure Boot, allowlist]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
  - sources/s4dbrd-kernel-anti-cheats.md
  - sources/riot-vanguard-on-demand-2026.md
  - sources/microsoft-getruntimeattestationreport.md
  - entities/tools/battleye.md
  - entities/tools/easy-anti-cheat.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE — Riot AC; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — boot-start allowlist is the load-order lesson
- @concepts/game-hacking.md
- @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md — classified rootkit-like
- @sources/s4dbrd-kernel-anti-cheats.md — `vgk.sys` SERVICE_BOOT_START (classic)
- @sources/riot-vanguard-on-demand-2026.md — 2026 On-Demand + TPM EK as HWID
- @sources/microsoft-getruntimeattestationreport.md — the Windows primitive that made On-Demand possible
- @entities/tools/battleye.md
- @entities/tools/easy-anti-cheat.md

## Raw Concept

Riot kernel anti-cheat (Valorant / LoL). Classic model: `vgk.sys` boot-start; `vgauth.exe` service. **On-Demand (2026):** on Win11 25H2+ with TPM 2.0 + Secure Boot + VBS + HVCI + IOMMU, the driver need not load at boot — Microsoft runtime driver attestation covers the gap. Riot first-party: TPM Endorsement Key as hardware identity; restricted accounts require **fTPM** (dTPM swap is treated as too cheap).

## Narrative

Architectural difference that still matters: without Pre-Check, the driver is present **before** most other drivers, so “load a spoof driver at game launch” is the wrong threat model. With On-Demand, the threat model is **attested driver history + TPM EK**, not “Vanguard wasn’t watching.” ARES 2024 classified Vanguard as rootkit-like. This wiki does not document Vanguard ban evasion.
