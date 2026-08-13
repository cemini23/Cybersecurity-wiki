---
title: Early Launch Anti-Malware (ELAM) overview (Microsoft Learn)
type: source
tags: [source, windows, hardening, boot-security, vendor-doc]
keywords: [ELAM, boot-start driver, early launch anti-malware, PPL, measured boot, kernel driver signing]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/system-hardening.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/microsoft-wdac-appcontrol-overview.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party boot-security doc; Learn ms.date 2024-08-19"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — boot-start AC vs ELAM-classified drivers share the boot order
- @concepts/system-hardening.md — pre-OS trusted boot control
- @sources/microsoft-hvci-memory-integrity.md — sibling trust-stack layer (post-boot code integrity)
- @sources/microsoft-wdac-appcontrol-overview.md — sibling trust-stack layer (policy allow-list)
- @concepts/secure-boot-vs-device-ownership.md — the boot-trust stack's owner-exclusion trade-off

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Overview of Early Launch AntiMalware |
| Publisher | Microsoft Learn (Windows drivers) |
| URL | https://learn.microsoft.com/en-us/windows-hardware/drivers/install/early-launch-antimalware |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

ELAM is Microsoft's supported mechanism for an anti-malware driver to **start before other third-party boot drivers** and control their initialization — including not initializing unknown drivers. Boot-start AM driver gets initialized first; once boot drivers are initialized and persistent storage is available, regular AM continues blocking. The ELAM service runs as a Protected Process Light (PPL); debugging requires a kernel debugger.

Trust-stack position: ELAM is the *boot-order* gate (who may load), HVCI the *code-integrity* gate (may loaded code execute), WDAC the *policy* gate (what is allowed at all). Together they are the pre-OS → OS boundary that modern AC (Vanguard On-Demand) and high-assurance clients inherit.

## Snippets

> "The ELAM feature provides a Microsoft-supported mechanism for antimalware (AM) software to start before other third-party components. AM drivers are initialized first and allowed to control the initialization of subsequent boot drivers, potentially not initializing unknown boot drivers."

> "Because an ELAM service runs as a PPL (Protected Process Light), you need to debug using a kernel debugger."

[Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/install/early-launch-antimalware (retrieved 2026-08-12)]
