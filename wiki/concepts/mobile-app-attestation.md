---
title: Mobile app attestation
type: concept
tags: [concept, mobile, attestation, android, ios, play-integrity, app-attest, product-pentest]
keywords: [Play Integrity, App Attest, DeviceCheck, SafetyNet, attestation, integrity verdict, MEETS_STRONG_INTEGRITY, app attestation, server verification, anti-tamper]
related:
  - concepts/mobile-pentest.md
  - concepts/pre-release-product-pentest.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - sources/google-play-integrity-api.md
  - sources/apple-app-attest.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — first-party attestation APIs for owned mobile products; no Magisk/PIF kits"
---

## Relations

- @concepts/mobile-pentest.md — attestation is the control your mobile pentest must test around (server-side verification)
- @concepts/pre-release-product-pentest.md — attestation checks are part of the mobile product ship bar
- @concepts/hardware-bound-identity-anticheat-licensing.md — hardware-bound identity's mobile cousin: TPM EK ↔ Secure Enclave / Play verdicts
- @sources/google-play-integrity-api.md — Play Integrity verdicts + server verification
- @sources/apple-app-attest.md — App Attest key/attestation flow + DeviceCheck bits
- @concepts/secure-boot-vs-device-ownership.md — STRONG-tier attestation is the mobile face of the boot trust stack; custom-ROM users fail it

## Raw Concept

Operator asked (2026-08-12): how do Android/iOS first parties attest that the client app is genuine on a genuine device — and how does **our** mobile product use it? Lane 5 of the license-bind / anti-tamper ingest.

**In scope:** architecture, what is collected/verified, class names of attacks (patch / keygen / loader / emulator / unpack) as *catalog*, official repair/re-bind paths, how to design **your** license.

**Out of scope:** working keygens, serial algorithms, Denuvo/Steam/EAC bypass, VMProtect/Themida unpack scripts, license emulators, warez, "unban this title." Cite *Epic v. Araujo* (`@sources/epic-games-v-araujo-hwid-spoofer-judgment.md`) as legal ceiling.

## Narrative

### 1. What attestation is

Attestation = the platform (Google Play / Apple) vouches for the app+device to **your server**, in a signed token the client cannot forge. The invariant: **the server verifies the token; the client merely relays it.** A client-side `bool deviceOk` is worth nothing. [CONFIRMED both first-party docs]

Attestation is the mobile instance of the online-heartbeat / server-authority class in @concepts/anti-tamper-protection-classes.md §2 — and the mobile cousin of the hardware-bound identity map in @concepts/hardware-bound-identity-anticheat-licensing.md.

### 2. Android — Play Integrity API

Play Integrity replaces the deprecated **SafetyNet** attestation. Verdicts (returned as a signed token from Google Play services):

| Verdict family | What it asserts |
|----------------|-----------------|
| `appRecognitionVerdict` = `PLAY_RECOGNIZED` | The calling binary is the unmodified app Google Play recognizes |
| `appLicensingVerdict` = `LICENSED` | The user installed/paid via Google Play |
| `deviceIntegrity` | Runs on a genuine, certified Android device (or Google Play Games for PC) |
| Trust tiers | `MEETS_BASIC_INTEGRITY` (weakest) → `MEETS_DEVICE_INTEGRITY` (certified genuine device) → `MEETS_STRONG_INTEGRITY` (hardware-backed signals; Android 13+) |

Request modes: **classic** (infrequent, high-value actions; server-side nonce against replay) vs **standard** (warm-up + low latency; frequent checks; Google-managed replay protection). Google explicitly warns against caching verdicts — cached verdicts enable *proxying* (reusing a good device's verdict elsewhere). [CONFIRMED developer.android.com — @sources/google-play-integrity-api.md]

### 3. iOS — App Attest + DeviceCheck

App Attest binds the **app identity** (Team ID + Bundle ID) to a key generated and stored in the **Secure Enclave** — one attestation key per install. Flow: server issues one-time challenge → app hashes it and `attestKey`s → **attestation object** (JWS: app ID, challenge hash, public key, cert chain to Apple's App Attest CA) → server verifies the chain + challenge and stores the key. Subsequent requests are signed **assertions** with a monotonic counter (replay detection). DeviceCheck adds 2 bits of server-settable per-key storage (bit 1 = verified, bit 2 = revoked/compromised). [CONFIRMED developer.apple.com — @sources/apple-app-attest.md]

**Important asymmetry:** App Attest attests the *app*, not the *device*. It does **not** detect jailbreak, OS tampering, or bots — unlike Play Integrity's `deviceIntegrity`. [CONFIRMED Apple doc]

### 4. Android vs iOS

| | Play Integrity (Android) | App Attest + DeviceCheck (iOS) |
|--|--------------------------|-------------------------------|
| What is attested | App binary + licensing + device integrity | App identity (Team/Bundle ID) via Secure Enclave key |
| Hardware anchor | Hardware-backed signals for STRONG tier | Secure Enclave keypair |
| Jailbreak/tamper signal | Yes (`deviceIntegrity` tiers) | **No** (app-level only) |
| Server verification | Mandatory — signed verdict token + `requestHash`/`nonce` | Mandatory — cert chain + challenge + assertion counter |
| Replay protection | nonce (classic) / Play-managed (standard) | One-time challenge + monotonic counter |

### 5. Design rules (product steal)

1. **Server verifies, never the client.** Treat attestation tokens like JWTs — validate signature, nonce, and expected app ID on the backend. [CONFIRMED both first-party docs]
2. **Don't cache verdicts** — proxying attack. Fresh verdict per high-value action. [CONFIRMED Google]
3. **Tiered enforcement** (allow / allow-with-limits / CAPTCHA / deny) beats binary allow-deny — harder to fingerprint the threshold. [CONFIRMED Google guidance]
4. **Attestation ≠ anti-abuse.** Use alongside server-side analytics/rate limits ("works best when used alongside other signals… not as your sole anti-abuse mechanism"). [CONFIRMED Google]
5. **Know the asymmetry:** on iOS you get app authenticity, not device health — pair with your own runtime checks if jailbreak matters to your threat model.

### 6. Pentest lens

For the pre-release mobile pentest (@concepts/mobile-pentest.md + @concepts/pre-release-product-pentest.md): the attestation call is a **client surface** — instrument it (Frida-class tooling) to prove your backend *actually* verifies rather than accepting a client bool. Attestation raises the bar for client tampering; it does not replace server-side authorization. [TENTATIVE synthesis]

## Snippets

> "Caching integrity verdicts increases the risk of proxying, which is an attack where a bad actor reuses a verdict from a good device for abusive purposes in another environment."
[Source: https://developer.android.com/google/play/integrity/overview (retrieved 2026-08-12)]

> "The Play Integrity API works best when used alongside other signals as part of your overall anti-abuse strategy and not as your sole anti-abuse mechanism."
[Source: same]

> "App Attest helps you ensure that the app your server is communicating with is the app you think it is, and that it hasn't been tampered with." … "The system stores the private key in the Secure Enclave."
[Source: https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity (retrieved 2026-08-12)]

## Dead Ends

- **Magisk / Play Integrity Fix-class write-ups** — existence-only NO-GO (catalogued as the counter to `deviceIntegrity`; no kit paths, no module steps).
- **Client-side-only attestation designs** — rejected pattern (bool in the app); the whole point is server verification.
- **SafetyNet as a live API** — deprecated; superseded by Play Integrity. [CONFIRMED Google ecosystem]
