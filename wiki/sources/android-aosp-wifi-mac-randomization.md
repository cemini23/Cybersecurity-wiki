---
title: Android AOSP — Wi-Fi MAC randomization (Android 10+)
type: source
tags: [source, android, privacy, mac-randomization, vendor-doc]
keywords: [AOSP, Android 10, persistent randomized MAC, LOCAL_MAC_ADDRESS, per-SSID]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/mobile-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — AOSP docs"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md — OS-supported MAC control
- @concepts/mobile-pentest.md — Android identifier / privacy surface

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Implement MAC randomization / MAC randomization behavior / Immutable device IDs |
| Publisher | Android Open Source Project |
| URLs | https://source.android.com/docs/core/connect/wifi-mac-randomization · https://source.android.com/docs/core/connect/wifi-mac-randomization-behavior · https://source.android.com/docs/core/permissions/immutable-device-ids |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Android 8: randomized MAC while **probing** unassociated. Android 10: randomization **default on** for client, SoftAp, Wi-Fi Direct; per-SSID toggle in Settings. Default type is **persistent** randomization: same randomized MAC for a network profile (SSID + security type / Passpoint FQDN) until factory reset — forgetting and re-adding the network does **not** re-roll, because the MAC is derived from profile parameters. Non-persistent (re-roll each connection) exists from Android 12+ for some networks / developer option. Factory MAC hidden from unprivileged APIs; `LOCAL_MAC_ADDRESS` for privileged apps. [CONFIRMED AOSP, retrieved 2026-08-12]

OPSEC steal: Android’s default is **stable per network**, not a new MAC every probe burst after association. That is good against venue tracking across cafes **until** you return to the same SSID. It is not a session-ephemeral identity. Pair with the 2016–2026 de-randomization papers: even rotating MACs leak IEs/behavior.

## Snippets

> "Android generates a persistent randomized MAC address based on the network profile's parameters, including SSID, security type, or FQDN (for Passpoint networks). This MAC address remains the same until a factory reset."
[Source: https://source.android.com/docs/core/connect/wifi-mac-randomization-behavior (retrieved 2026-08-12)]
