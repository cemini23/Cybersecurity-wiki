---
title: Activate clients running Windows — volume activation (Microsoft Learn)
type: source
tags: [source, windows, licensing, activation, vendor-doc]
keywords: [KMS, ADBA, MAK, GVLK, volume activation, activation threshold, 180-day, _VLMCS._TCP, license binding]
related:
  - concepts/software-license-binding.md
  - sources/microsoft-oa3-hardware-hash.md
  - sources/microsoft-autopilot-motherboard-replacement.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party activation docs; Learn ms.date 2025-05-14"
wire_status: wont_wire
---

## Relations

- @concepts/software-license-binding.md — the online-lease half of the binding menu
- @sources/microsoft-oa3-hardware-hash.md — OEM hardware-bound cousin of the lease models
- @sources/microsoft-autopilot-motherboard-replacement.md — hardware-change path for the *device-bound* model

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Activate clients running Windows |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/deployment/volume-activation/activate-windows-clients-vamt |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party volume-activation overview: **KMS** (client-server lease: 180-day validity, renew every 7 days, retry every 2h; activation thresholds 25 Windows clients / 5 servers; DNS SRV `_VLMCS._TCP` discovery; anonymous RPC over 1688/TCP), **ADBA** (activation object stored in AD DS; domain-joined clients activate automatically via GVLK), **MAK** (one-time counted activations against Microsoft, independent or VAMT-proxy). A GVLK-configured client "just works" when org infrastructure is reachable.

For the license-binding lens: this is the **online lease** class — validity is a renewable server relationship, not a device fingerprint. Pair with @sources/microsoft-oa3-hardware-hash.md (device-bound) and the digital-license account path for the full first-party menu.

## Snippets

> "KMS activations are valid for 180 days (the activation validity interval). To remain activated, KMS client computers must renew their activation by connecting to the KMS host at least once every 180 days."

> "KMS client computers can locate KMS host computers by using DNS or a static configuration. KMS clients contact the KMS host by using RPCs carried over TCP/IP."

[Source: https://learn.microsoft.com/en-us/windows/deployment/volume-activation/activate-windows-clients-vamt (retrieved 2026-08-12)]
