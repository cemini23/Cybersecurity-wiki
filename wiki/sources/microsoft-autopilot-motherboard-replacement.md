---
title: Windows Autopilot motherboard replacement (Microsoft Learn)
type: source
tags: [source, windows, autopilot, hardware-id, vendor-doc]
keywords: [Autopilot, 4K HH, hardware hash, motherboard replacement]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - sources/microsoft-oa3-hardware-hash.md
  - sources/microsoft-systemidentification-getsystemidforpublisher.md
  - sources/oofhours-autopilot-hardware-hash.md
  - concepts/windows-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party repair path; the official hardware-change procedure"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — Microsoft’s documented hardware-change path
- @sources/microsoft-oa3-hardware-hash.md — 4K HH is the OA3 blob
- @sources/microsoft-systemidentification-getsystemidforpublisher.md — publisher-scoped ID; not the Autopilot hash
- @sources/oofhours-autopilot-hardware-hash.md — decode of the 4K HH fields
- @concepts/windows-pentest.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Repair Windows Autopilot devices that have motherboard replacement |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/autopilot/autopilot-motherboard-replacement |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Autopilot requires uniqueness at the **hardware hash** (also called hardware ID / 4K HH). After motherboard replacement Microsoft’s prescribed path is: deregister → replace board → capture a **new** 4K HH (`Get-WindowsAutopilotInfo`) → reregister → reset. OEM uniqueness rules (boards, MACs) and Autopilot hash uniqueness can conflict. [CONFIRMED Learn]

This is the first-party answer to “the license/enrollment is bound to hardware”: you change the hardware and **re-enroll**, you do not spoof the old hash.

Community decode of 4K HH (Oofhours / OA3Tool) lists critical fields including DiskSerialNumber, TpmVersion, EkPubHash, MacAddress, SMBIOS UUID/serial/manufacturer/product. [TENTATIVE third-party decode 2022; fields match OA3 tooling]

## Snippets

> "If a motherboard is replaced on a Windows Autopilot registered device, then the following process is recommended: 1. Deregister ... 2. Replace the motherboard. 3. Capture a new Windows Autopilot device ID (4K HH) ..."
[Source: https://learn.microsoft.com/en-us/autopilot/autopilot-motherboard-replacement (retrieved 2026-08-12)]
