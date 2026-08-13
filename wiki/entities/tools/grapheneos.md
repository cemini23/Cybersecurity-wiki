---
title: GrapheneOS
type: entity
tags: [tool, os, android, hardening, privacy, grapheneos]
keywords: [GrapheneOS, Pixel, hardened_malloc, MTE, sandboxed Google Play, Vanadium, verified boot]
related:
  - concepts/hardened-alternative-operating-systems.md
  - sources/grapheneos-features.md
  - sources/grapheneos-faq.md
  - concepts/secure-boot-vs-device-ownership.md
  - concepts/mobile-app-attestation.md
  - concepts/commercial-spyware-stalkerware-defense.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party OS; do not clone the tree (~huge); Pixel hardware is operator-purchased"
wire_status: wont_wire
---

## Relations

- @concepts/hardened-alternative-operating-systems.md — landscape
- @sources/grapheneos-features.md
- @sources/grapheneos-faq.md — Pixel-only; relock required
- @concepts/secure-boot-vs-device-ownership.md — relock verified boot; still not Google-certified STRONG
- @concepts/mobile-app-attestation.md — if your app must run here, do not binary-deny on STRONG
- @concepts/commercial-spyware-stalkerware-defense.md — exploit bar is higher, not implant-proof

## Raw Concept

Privacy/security-focused Android OS (AOSP + Graphene hardening). Operator asked for “Graphine.” Official site: https://grapheneos.org/

## Narrative

Official production devices are **Google Pixels** (FAQ list; prefer current-gen for update years). After install, **relock** the bootloader — Setup Wizard warns if it is unlocked. Optional **sandboxed Google Play**: official Play APKs as normal apps, no privileged OS backend. [CONFIRMED features + FAQ]

Notable controls vs stock AOSP: hardened_malloc, MTE (Pixel 8+ class hardware), Network permission, extra user profiles, locked-device auto-reboot, duress wipe, Vanadium. [CONFIRMED features]

This wiki does not ship a flash guide. Operator install is a **human** hardware purchase + first-party installer. `wont_wire` clone.
