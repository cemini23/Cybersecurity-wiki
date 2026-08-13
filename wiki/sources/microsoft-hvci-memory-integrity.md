---
title: Enable memory integrity / HVCI (Microsoft Learn)
type: source
tags: [source, windows, hardening, code-integrity, vendor-doc]
keywords: [HVCI, memory integrity, VBS, hypervisor-protected code integrity, Device Guard, Win32_DeviceGuard, kernel-mode code signing]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/system-hardening.md
  - concepts/windows-pentest.md
  - sources/microsoft-getruntimeattestationreport.md
  - sources/microsoft-wdac-appcontrol-overview.md
  - sources/microsoft-elam.md
  - sources/microsoft-kernel-dma-protection.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party enable/verify doc; Learn ms.date 2025-08-15"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — HVCI is the precondition for Vanguard On-Demand's attestation trust
- @concepts/system-hardening.md — high-assurance client control
- @concepts/windows-pentest.md — kernel tradecraft now runs against this enforcement
- @sources/microsoft-getruntimeattestationreport.md — report generation requires HVCI
- @sources/microsoft-wdac-appcontrol-overview.md — App Control policy can enable HVCI
- @sources/microsoft-elam.md — sibling trust-stack layer (boot-order gate)
- @sources/microsoft-kernel-dma-protection.md — sibling trust-stack layer (IOMMU physical-access gate)
- @concepts/secure-boot-vs-device-ownership.md — the trust stack's ownership/attestation tension (product policy)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Enable memory integrity |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Memory integrity (a.k.a. HVCI / hypervisor-enforced code integrity; originally Device Guard) runs kernel-mode code integrity inside the **VBS isolated environment**: the hypervisor becomes the root of trust *assuming the kernel can be compromised*. Kernel memory pages become executable only after passing CI, and executable pages are never writable; it also protects the kernel CFG bitmap. Best on Intel Kaby Lake+ (MBEC) / AMD Zen 2+ (GMET); older CPUs emulate via Restricted User Mode. Enable via Windows Security, Intune/CSP, GPO (UEFI-lock optional), registry (`DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity`), or App Control policy. Verify via `Win32_DeviceGuard` WMI / `msinfo32`. Default-on for clean installs of Windows 11 on compatible hardware + Windows 10 S mode. Incompatible drivers can malfunction or blue-screen.

For the wiki: HVCI is the **load-and-execute trust boundary** that both enterprise hardening (WDAC/ELAM stack) and consumer AC (GetRuntimeAttestationReport, Riot On-Demand) build on.

## Snippets

> "VBS uses the Windows hypervisor to create an isolated virtual environment that becomes the root of trust of the OS that assumes the kernel can be compromised. Memory integrity is a critical component that protects and hardens Windows by running kernel mode code integrity within the isolated virtual environment of VBS."

> "Memory integrity also restricts kernel memory allocations that could be used to compromise the system."

[Source: https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity (retrieved 2026-08-12)]
