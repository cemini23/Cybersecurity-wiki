---
title: How kernel anti-cheats work (s4dbrd, 2026)
type: source
tags: [source, anti-cheat, kernel, windows, blog]
keywords: [s4dbrd, BEDaisy, vgk.sys, ObRegisterCallbacks, HWID fingerprint]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - concepts/av-edr-bypass.md
  - entities/tools/battleye.md
  - entities/tools/easy-anti-cheat.md
  - entities/tools/riot-vanguard.md
  - sources/checkpoint-evasions-firmware-tables.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — independent RE blog; single-source; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md
- @concepts/game-hacking.md
- @concepts/av-edr-bypass.md — same kernel callback APIs as EDR
- @entities/tools/battleye.md
- @entities/tools/easy-anti-cheat.md
- @entities/tools/riot-vanguard.md
- @sources/checkpoint-evasions-firmware-tables.md — firmware-table API the identifier list rides on

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Kernel Anti-Cheats Work: A Deep Dive into Modern Game Protection |
| Author | Adrian (s4dbrd.github.io) |
| URL | https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Long-form Windows-internals survey of kernel AC. Usermode AC is bypassable from ring 0. Three-component model. BattlEye/EAC demand-start vs Vanguard boot-start allowlist. Callbacks (`ObRegisterCallbacks`, process/thread/image). Arms race: BYOVD → hypervisor → PCIe DMA. §12 lists HWID collection (SMBIOS via firmware table, disk serial via storage IOCTL, GPU LUID, MAC, MachineGuid vs UEFI UUID) and **detection of cheap spoofs** (all-F UUID, serial/model mismatch, firmware≠registry). [TENTATIVE single blog; not a vendor spec]

This wiki steals the identifier map and load-order lesson. It does not copy spoof-driver recipes.

## Snippets

> "BattlEye and EAC load their kernel drivers when the game is launched. ... Vanguard loads vgk.sys at system boot. ... This is an allowlist model rather than a blocklist model, which is architecturally much stronger."
[Source: https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/ (retrieved 2026-08-12)]
