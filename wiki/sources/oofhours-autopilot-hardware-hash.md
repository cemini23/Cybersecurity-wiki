---
title: Breaking down the Windows Autopilot hardware hash (Oofhours, 2022)
type: source
tags: [source, windows, licensing, hardware-id, blog]
keywords: [OA3, 4K HH, OA3Tool, DiskSerialNumber, EkPubHash, SmbiosUuid]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/hardware-id-masking-opsec.md
  - sources/microsoft-oa3-hardware-hash.md
  - sources/microsoft-autopilot-motherboard-replacement.md
  - concepts/software-license-binding.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — third-party decode of first-party OA3Tool fields"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — field inventory for hardware-bound licensing
- @concepts/hardware-id-masking-opsec.md — Autopilot hash is a composite identifier, not anonymity
- @sources/microsoft-oa3-hardware-hash.md — first-party OA3 association
- @sources/microsoft-autopilot-motherboard-replacement.md — official board-swap path when too many fields change at once
- @concepts/software-license-binding.md — per-field matching is the reason one-field checks fail

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Breaking down the Windows Autopilot hardware hash |
| Author | Michael Niehaus (Oofhours) |
| URL | https://oofhours.com/2022/06/03/breaking-down-the-windows-autopilot-hardware-hash/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

The 4K “hardware hash” is an **encoded inventory**, not a cryptographic digest. OA3Tool `/ValidateHwHash` names critical fields: DiskSerialNumber, TpmVersion, EkPubHash, MacAddress, ProductKeyId, SmbiosSystemFamily/Manufacturer/ProductName/SerialNumber/Uuid. Matching is **per-field**, not literal blob equality; capture timestamp/OS build are in the blob so recapture changes the encoding. TPM 1.2 fails some Autopilot scenarios. Motherboard replacement changes too many attributes at once — Microsoft documents deregister/recapture instead of spoof. [CONFIRMED Oofhours 2022 + Microsoft Autopilot repair doc]

## Snippets

> "the hardware hash (which isn’t really a hash at all, but instead is just an encoded conglomeration of a list of attributes of the device) ... the hash is not compared literally, it’s broken apart and compared using those “critical” fields."
[Source: https://oofhours.com/2022/06/03/breaking-down-the-windows-autopilot-hardware-hash/ (retrieved 2026-08-12)]
