---
title: Kernel DMA Protection (Microsoft Learn)
type: source
tags: [source, windows, hardening, dma, iommu, vendor-doc]
keywords: [Kernel DMA Protection, IOMMU, DMA remapping, Thunderbolt, drive-by DMA, VT-d, BitLocker countermeasures, DmaGuard]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/system-hardening.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/riot-vanguard-on-demand-2026.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party IOMMU/DMA doc; Learn ms.date 2025-08-15"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — IOMMU is one of the Vanguard Pre-Check requirements (attested AC trust stack)
- @concepts/system-hardening.md — high-assurance client control against drive-by DMA
- @sources/microsoft-hvci-memory-integrity.md — sibling VBS-adjacent layer (Secure Boot with DMA option)
- @sources/riot-vanguard-on-demand-2026.md — Riot Pre-Check lists IOMMU as an On-Demand precondition

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Kernel DMA Protection |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Kernel DMA Protection blocks **drive-by DMA attacks** from external hot-plug PCIe devices (Thunderbolt, USB4, CFexpress): Windows uses the **IOMMU** so DMA-capable peripherals start and DMA only if their drivers support memory isolation (DMA-remapping). Remapping-incompatible peripherals are blocked until an authorized user signs in (DmaGuard policy / MDM adjustable). Requires UEFI firmware support + IOMMU (Intel VT-d / AMD-Vi) enabled in firmware; **VBS is not required** for the feature itself. Supersedes the older BitLocker DMA countermeasures (recommended to disable those when supported); does not protect during boot (firmware's job) nor against 1394/FireWire/PCMCIA/CardBus/ExpressCard. Windows 11 WDDM 3.0 adds DMA-remapping support for graphics devices.

Trust-stack position: IOMMU is the *physical-access* gate of the stack — the layer that keeps a hostile peripheral (hardware cheat / DMA implant) out of memory regardless of what the kernel believes.

## Snippets

> "Windows uses the system Input/Output Memory Management Unit (IOMMU) to block external peripherals from starting and performing DMA, unless the drivers for these peripherals support memory isolation (such as DMA-remapping)."

> "Kernel DMA Protection requires UEFI firmware support, and Virtualization-based Security (VBS) isn't required."

[Source: https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt (retrieved 2026-08-12)]
