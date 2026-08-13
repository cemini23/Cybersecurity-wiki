---
title: FACEIT Enhanced Verification (first-party support)
type: source
tags: [source, anti-cheat, faceit, vendor-doc]
keywords: [FACEIT, hardware identifiers, multi-account, ban evasion, biometric]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party policy; FACEIT AC not cloned"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — hardware identifiers used in multi-account / evasion checks
- @concepts/game-hacking.md
- @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md — FACEIT AC classified rootkit-like under ARES metrics

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Enhanced Verification: Verified by FACEIT Staff |
| Publisher | FACEIT Support |
| URL | https://support.faceit.com/hc/en-us/articles/23653660734492-Enhanced-Verification-Verified-by-FACEIT-Staff |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

FACEIT’s high-profile verification protocol. Stage 1 **Multi-Account Checks** explicitly review **hardware identifiers**, network data, and historical matching telemetry for smurfing or ban evasion. Later stages: live webcam interview of hardware/driver/software setup; exceptional in-person play on FACEIT hardware. Failures → platform ban. [CONFIRMED FACEIT support]

Confirms hardware IDs are a **backend** signal, not the whole identity (they also use face recapture and live setup inspection).

## Snippets

> "Multi-Account Checks: A review of hardware identifiers, network data, and historical matching telemetry to cross-reference for smurfing or ban evasion."
[Source: https://support.faceit.com/hc/en-us/articles/23653660734492-Enhanced-Verification-Verified-by-FACEIT-Staff (retrieved 2026-08-12)]
