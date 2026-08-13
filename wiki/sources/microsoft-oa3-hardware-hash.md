---
title: OEM Activation 3.0 hardware hash (Microsoft Learn)
type: source
tags: [source, windows, licensing, hardware-id, vendor-doc]
keywords: [OA3, hardware hash, hardware association, product key, Computer Build Report]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/hardware-id-masking-opsec.md
  - sources/microsoft-autopilot-motherboard-replacement.md
  - sources/microsoft-systemidentification-getsystemidforpublisher.md
  - sources/oofhours-autopilot-hardware-hash.md
  - concepts/software-license-binding.md
  - sources/microsoft-volume-activation-clients.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party OEM licensing docs"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — licensed cousin of AC HWID bundles
- @concepts/hardware-id-masking-opsec.md
- @sources/microsoft-autopilot-motherboard-replacement.md — same 4K HH used for Autopilot
- @sources/microsoft-systemidentification-getsystemidforpublisher.md — publisher-scoped ID; distinct from OA3 hash
- @sources/oofhours-autopilot-hardware-hash.md — OA3Tool critical-field list
- @concepts/software-license-binding.md — the device-hash binding class this page anchors
- @sources/microsoft-volume-activation-clients.md — the online-lease cousin (KMS/ADBA)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | OEM Activation 3.0 system |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-activation-3 |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

OA 3.0 joins **one Microsoft-issued product key to one computer** via a **hardware hash** of component information, reported in the Computer Build Report (hash + product key ID). That association is what Windows AVS later validates at OOBE. [CONFIRMED Learn]

This is hardware-bound **licensing**, not a game ban list. Forging it is fraud. For a product you own: same design — bind license to a multi-field hash, not a single registry GUID.

## Snippets

> "Hardware Association — A unique association that joins a single Microsoft-issued Windows product key to a single computer. The OA 3.0 Tool generates this value by using the hardware hash and the product key value."
[Source: https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-activation-3 (retrieved 2026-08-12)]
