---
title: Play Integrity API (Google, developer.android.com)
type: source
tags: [source, android, attestation, play-integrity, vendor-doc]
keywords: [Play Integrity, integrity verdict, MEETS_STRONG_INTEGRITY, appRecognitionVerdict, appLicensingVerdict, SafetyNet, standard request, classic request, proxying]
related:
  - concepts/mobile-app-attestation.md
  - concepts/mobile-pentest.md
  - concepts/pre-release-product-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Android attestation API docs"
wire_status: wont_wire
---

## Relations

- @concepts/mobile-app-attestation.md — the Android half of the attestation map
- @concepts/mobile-pentest.md — client surface a mobile pentest must test server-side
- @concepts/pre-release-product-pentest.md — attestation checks in the mobile product ship bar

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Play Integrity API overview |
| Publisher | Google (Android Developers) |
| URL | https://developer.android.com/google/play/integrity/overview |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Play Integrity (successor to the deprecated SafetyNet Attestation) answers: is the caller **your** unmodified app, installed via Play, on a genuine certified Android device — via a **signed verdict token the server must verify**. Verdict families: `appRecognitionVerdict` (`PLAY_RECOGNIZED`), `appLicensingVerdict` (`LICENSED`), `deviceIntegrity` tiers (`MEETS_BASIC_INTEGRITY` / `MEETS_DEVICE_INTEGRITY` / `MEETS_STRONG_INTEGRITY` — strong is hardware-backed, Android 13+). Opt-in extras: `appAccessRiskVerdict`, `playProtectVerdict`, `recentDeviceActivity`, `deviceRecall`.

**Classic vs standard:** classic = infrequent high-value checks, server-side `nonce` for replay protection; standard = warm-up, few-hundred-ms latency, Google-managed replay protection, suited to frequent checks. Google: do **not** cache classic verdicts (proxying risk); prefer tiered enforcement over binary allow/deny; gather telemetry before enforcing.

## Snippets

> "The Play Integrity API helps you check that user actions and server requests are coming from your genuine app, installed by Google Play, running on a genuine and certified Android device."

> "Caching integrity verdicts increases the risk of proxying, which is an attack where a bad actor reuses a verdict from a good device for abusive purposes in another environment."

> "The Play Integrity API works best when used alongside other signals as part of your overall anti-abuse strategy and not as your sole anti-abuse mechanism."

[Source: https://developer.android.com/google/play/integrity/overview (retrieved 2026-08-12)]
