---
title: GetRuntimeAttestationReport (Microsoft Learn)
type: source
tags: [source, windows, attestation, anti-cheat, vendor-doc]
keywords: [GetRuntimeAttestationReport, HVCI, VBS, TPM, Secure Boot, IOMMU, runtime report]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - entities/tools/riot-vanguard.md
  - sources/riot-vanguard-on-demand-2026.md
  - concepts/windows-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Win32 API; Learn ms.date 2026-01-21"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — why boot-start AC can become on-demand
- @entities/tools/riot-vanguard.md — Vanguard On-Demand consumes this report
- @sources/riot-vanguard-on-demand-2026.md
- @concepts/windows-pentest.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | GetRuntimeAttestationReport function (sysinfoapi.h) |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getruntimeattestationreport |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

VTL0 usermode API to fetch a **Secure-Kernel-signed** runtime attestation report: loaded-driver list + code-integrity info. Learn text names anti-cheat as an intended consumer. Report generation requires **HVCI**. Security requirements: TPM 2.0, Secure Boot, VBS, HVCI, IOMMU; test-signing and debug flags off. Nonce (32 bytes) against replay. [CONFIRMED Learn, ms.date 2026-01-21]

This is the Windows primitive that lets an AC **not** sit at `SERVICE_BOOT_START` and still learn which drivers loaded while it was dormant.

## Snippets

> "This report provides a list of loaded drivers and code integrity information, which is essential for validating system integrity and enforcing anti-cheat policies in gaming and security-sensitive applications."
[Source: https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getruntimeattestationreport (retrieved 2026-08-12)]

> "TPM 2.0, Secure Boot, VBS, HVCI, and IOMMU must be enabled. Test-signing and debug flags must be off."
[Source: same]
