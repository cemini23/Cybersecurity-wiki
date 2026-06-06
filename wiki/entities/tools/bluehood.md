---
title: "bluehood — Bluetooth telemetry monitoring for physical-environment threat detection"
type: entity
tags: [tool, bluetooth, physical-security, telemetry, ble, python, flask, docker, mit, steal-from]
keywords: [bluehood, dannymcc, bluetooth, ble, mac correlation, physical security, telemetry monitoring, threat detection, device discovery]
related:
  - concepts/wireless-pentest.md
  - concepts/network-security.md
  - concepts/threat-intelligence.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md"
---

# bluehood — Bluetooth telemetry monitoring

## Relations

- @concepts/wireless-pentest.md — BLE device discovery + MAC correlation
- @concepts/network-security.md — physical-environment threat detection
- @concepts/threat-intelligence.md — threat-actor profiling via device fingerprinting

## Raw Concept

Routed from K55 OSINT-wiki tool eval (2026-05-20). Bluetooth telemetry monitoring via Python + Flask + Docker + BlueZ. Steal-from tier, MIT, 977 stars.

## Narrative

`dannymcc/bluehood` (MIT, 977 stars, 62 open issues) provides continuous Bluetooth telemetry monitoring via Python + Flask + Docker + BlueZ. Scans the physical environment for BLE devices and correlates MAC addresses over time.

Cybersec-wiki extraction value: the BLE device discovery patterns and MAC correlation mapping logic are reusable for physical-security threat-actor profiling. Rather than adopting the full Flask+Docker stack, extract the core correlation algorithm for integration into existing wireless-pentest tooling.

Steal-from because of 62 open issues and maintenance uncertainty — the methodology is sound but the implementation may need independent redevelopment.
