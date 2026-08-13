---
title: "System Hardening"
type: concept
tags: [hardening, defensive-security, compliance, system-administration]
keywords: [system hardening, CIS benchmarks, STIG, security baseline, attack surface reduction, defense]
related:
  - concepts/linux-security.md
  - concepts/network-security.md
  - concepts/defense-in-depth.md
  - sources/red-hat-linux-security-and-optimization.md
  - sources/ssh-hardening-and-offensive-mastery.md
  - concepts/npm-supply-chain-defense.md
  - entities/tools/betterleaks.md
  - entities/tools/openvpn-install.md
  - entities/tools/vpn-self-hosted.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/operator-lab-playbook.md
  - concepts/hardware-id-masking-opsec.md
  - sources/microsoft-systemidentification-getsystemidforpublisher.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/microsoft-elam.md
  - sources/microsoft-kernel-dma-protection.md
  - sources/microsoft-wdac-appcontrol-overview.md
  - concepts/commercial-spyware-stalkerware-defense.md
  - sources/apple-lockdown-mode.md
  - concepts/endpoint-encryption-deniable-storage.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
created: 2026-05-15
updated: 2026-08-12
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

Process of reducing a system's attack surface by removing unnecessary services, applying secure configurations, and enforcing least-privilege access. Frameworks: CIS Benchmarks (consensus-derived configuration guides), DISA STIGs (US DoD hardened baselines). Key domains: OS hardening (Windows/Linux), network device hardening, database hardening, web server hardening. Core defensive practice — hardening reduces the number of exploitable vulnerabilities before they can be discovered.

**High-assurance Windows clients (2026-08-12):** for clients that gate on hardware trust (attested anti-cheat/DRM, TPM-backed identity, high-value endpoints), enable the Windows CI stack: **HVCI / memory integrity** (hypervisor-enforced kernel code integrity; default-on for clean Win11 installs on capable hardware), **ELAM** (boot-start AM classification), **WDAC / App Control for Business** (policy allow-list under MSRC servicing criteria), and **Kernel DMA Protection** (IOMMU fencing of hot-plug PCIe). This is a hardening control, not a crack guide — it is the same stack AC vendors require before relaxing their own drivers (Riot Vanguard Pre-Check: Secure Boot, TPM 2.0, VBS, HVCI, IOMMU).

## Relations

- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/owned-target-whitehat-lab.md — harden attack box / operator host; keep deliberately weak lab targets separate
- @concepts/linux-security.md
- @concepts/network-security.md
- @concepts/defense-in-depth.md
- @sources/red-hat-linux-security-and-optimization.md
- @sources/ssh-hardening-and-offensive-mastery.md
- @concepts/npm-supply-chain-defense.md — dependency-pinning + release-age cooldown as build-toolchain hardening
- @entities/tools/betterleaks.md — CEL+BPE secrets scanner — pre-IP-sale codebase audit / credential-exposure hardening
- @entities/tools/openvpn-install.md — hardened OpenVPN deployment automation; secure-defaults server config reference
- @entities/tools/vpn-self-hosted.md — VPN tool hub; hardened VPN configs as system-hardening reference pattern
- @concepts/hardware-id-masking-opsec.md — enable OS MAC randomization; TPM-backed Windows IDs survive reimage
- @sources/microsoft-systemidentification-getsystemidforpublisher.md — check SystemIdentification Source (TPM/UEFI vs registry)
- @sources/microsoft-hvci-memory-integrity.md — hypervisor-enforced kernel CI (VBS); default-on for clean Win11 installs on capable hardware
- @sources/microsoft-elam.md — boot-start AM driver classification (PPL)
- @sources/microsoft-kernel-dma-protection.md — IOMMU fencing of hot-plug PCIe (Thunderbolt/USB4)
- @sources/microsoft-wdac-appcontrol-overview.md — App Control for Business allow-list (MSRC servicing criteria)
- @concepts/commercial-spyware-stalkerware-defense.md — Lockdown Mode is the mobile high-assurance hardening control
- @sources/apple-lockdown-mode.md — extreme-protection mode for mercenary-spyware threat models
- @concepts/endpoint-encryption-deniable-storage.md — at-rest confidentiality layer; FDE ≠ running-OS confidentiality
- @concepts/secure-boot-vs-device-ownership.md — pre-OS boot-trust gate; the same trust stack HVCI/ELAM/WDAC live in