---
title: App Attest — establishing your app's integrity (Apple, DeviceCheck framework)
type: source
tags: [source, ios, attestation, app-attest, vendor-doc]
keywords: [App Attest, DeviceCheck, Secure Enclave, attestation key, attestation object, assertion counter, DCAppAttestService]
related:
  - concepts/mobile-app-attestation.md
  - concepts/mobile-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Apple attestation docs"
wire_status: wont_wire
---

## Relations

- @concepts/mobile-app-attestation.md — the iOS half of the attestation map
- @concepts/mobile-pentest.md — attestation is an app-integrity control, not a jailbreak detector

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Establishing your app's integrity (App Attest) |
| Publisher | Apple Developer Documentation (DeviceCheck framework) |
| URL | https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

App Attest (iOS 14+ / macOS 11+) lets your server verify the client is a **genuine, unmodified build of your app** (Team ID + Bundle ID) on a device with a **Secure Enclave**. Per-install **attestation key**: private half generated and held in the Secure Enclave, never leaves it. Flow: server issues one-time challenge → app hashes (SHA-256) and `attestKey`s → **attestation object** (JWS: app ID, challenge hash, public key, cert chain rooted at Apple's App Attest CA) → server verifies chain + challenge (also via Apple's endpoint `data.appattest.apple.com/v1/attestationData`) and stores key ID/public key. Ongoing requests carry signed **assertions** with a monotonic counter (replay detection). **DeviceCheck** adds two server-settable bits per key (bit 1 verified, bit 2 no-longer-trusted).

Boundary honesty (important for threat modeling): App Attest attests the **app**, not the **device** — it does not detect jailbreaks, OS tampering, or bots (contrast with Play Integrity `deviceIntegrity`).

## Snippets

> "App Attest helps you ensure that the app your server is communicating with is the app you think it is, and that it hasn't been tampered with."

> "The system stores the private key in the Secure Enclave."

> "App Attest also provides two bits of storage that you can use to track the state of the key."

[Source: https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity (retrieved 2026-08-12)]
