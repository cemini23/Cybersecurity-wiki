---
title: Check Point Evasions — firmware tables (SMBIOS / FIRM)
type: source
tags: [source, windows, firmware, hardware-id, sandbox]
keywords: [NtQuerySystemInformation, SystemFirmwareTableInformation, RSMB, FIRM, SMBIOS]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/windows-pentest.md
  - sources/s4dbrd-kernel-anti-cheats.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — defensive encyclopedia of the firmware-table API; no hook recipes filed"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — how kernel/usermode readers dump SMBIOS
- @concepts/windows-pentest.md
- @sources/s4dbrd-kernel-anti-cheats.md — same identifier path, AC-side

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evasions: Firmware tables |
| Publisher | Check Point (InviZzzible / evasions encyclopedia) |
| URL | https://evasions.checkpoint.com/src/Evasions/techniques/firmware-tables.html |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Sandbox/malware-evasion encyclopedia documenting how Windows exposes firmware: `NtQuerySystemInformation` info-class **76** (`SystemFirmwareTableInformation`) with `SYSTEM_FIRMWARE_TABLE_INFORMATION`. Provider signatures `'FIRM'` (legacy physical ranges) and `'RSMB'` (raw SMBIOS). Same dump path anti-cheats use for board UUID/serial. [CONFIRMED Check Point page]

This wiki steals the **API identity** (class 76, FIRM/RSMB). It does not file their “hook NtQuerySystemInformation” countermeasure as a runbook.

## Snippets

> "Firmware tables are retrieved via SYSTEM_FIRMWARE_TABLE_INFORMATION ... NtQuerySystemInformation(SystemFirmwareTableInformation, // 76"
[Source: https://evasions.checkpoint.com/src/Evasions/techniques/firmware-tables.html (retrieved 2026-08-12)]
