---
title: GrapheneOS FAQ (first-party)
type: source
tags: [source, grapheneos, android, vendor-doc]
keywords: [Pixel, device support, bootloader lock, hardware attestation, Auditor]
related:
  - concepts/hardened-alternative-operating-systems.md
  - entities/tools/grapheneos.md
  - sources/grapheneos-features.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — grapheneos.org/faq"
wire_status: wont_wire
---

## Relations

- @concepts/hardened-alternative-operating-systems.md
- @entities/tools/grapheneos.md
- @sources/grapheneos-features.md
- @concepts/secure-boot-vs-device-ownership.md — relock is the Graphene security model; unlocked = incomplete install

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Frequently Asked Questions |
| Publisher | GrapheneOS |
| URL | https://grapheneos.org/faq |
| Retrieved | 2026-08-12 |
| Location | vendor HTML |

## Narrative

Official **production** device list is Pixel-only (6 through current 10-series, Fold, Tablet as of retrieve date). Broad device support is explicitly **counter** to the project’s aims. 8th-gen+ Pixels: 7-year support floor + hardware MTE. Setup Wizard warns if the bootloader is still unlocked; GrapheneOS does not support running with an unlocked bootloader (incomplete install; lock wipes user data). Hardware key attestation (TEE + StrongBox) is first-party; Auditor app. [CONFIRMED FAQ]

## Snippets

> "GrapheneOS doesn't provide any support to users running GrapheneOS with an unlocked bootloader, as this is considered to be an incomplete installation."
[Source: https://grapheneos.org/faq (retrieved 2026-08-12)]

> "Devices are carefully chosen based on their merits rather than the project aiming to have broad device support. Broad device support is counter to the aims of the project"
[Source: https://grapheneos.org/faq (retrieved 2026-08-12)]
