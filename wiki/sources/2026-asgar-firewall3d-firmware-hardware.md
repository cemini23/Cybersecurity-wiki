---
title: Firewall3D: Hardware Firewall for Defending 3D Printers Against Firmware Attacks
type: source
tags: []
keywords: []
related: []
maturity: draft
created: 2026-07-15
updated: 2026-07-31
cross-wiki-source: @3d-printing-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md
wire_status: wont_wire
wire_target: "Phase-0 NO-GO"
---

# Firewall3D: Hardware Firewall for Defending 3D Printers Against Firmware Attacks

## Relations

- @3d-printing-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@3d-printing-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

**Firewall3D** (Asgar & Reddy, Texas A&M, arXiv:2607.10484) is a bump-in-the-wire hardware monitor between an FDM motherboard and sensors/actuators. Independently measures stepper currents, endstops, temperatures, and fan PWM; alarms/halts when physical behavior diverges from intended G-code under compromised firmware.

**Cybersec angle:** OT / embedded physical attestation under untrusted device firmware / supply-chain motherboard compromise. Assumes the monitoring appliance itself is trusted. No public BOM/firmware — **REFERENCE** (Phase-0 NO-GO install).

Primary ingest: `@3d-printing-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md`. Complements QuietPrint SHM + Bambu AMNC on that wiki.
