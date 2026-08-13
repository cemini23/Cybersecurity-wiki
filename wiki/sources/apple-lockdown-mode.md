---
title: Apple — About Lockdown Mode
type: source
tags: [source, apple, lockdown-mode, spyware, mobile-security, vendor-doc]
keywords: [Lockdown Mode, mercenary spyware, Pegasus, JIT, MDM, profile, 2G 3G, high-risk users]
related:
  - concepts/commercial-spyware-stalkerware-defense.md
  - concepts/system-hardening.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Apple support article"
wire_status: wont_wire
---

## Relations

- @concepts/commercial-spyware-stalkerware-defense.md — Lockdown Mode as the extreme-hardening defense
- @concepts/system-hardening.md — mobile high-assurance hardening control

## Raw Concept

| Field | Value |
|-------|-------|
| Title | About Lockdown Mode (Apple Support) |
| Publisher | Apple Inc. |
| URL | https://support.apple.com/en-us/105120 |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Apple's first-party description of Lockdown Mode: "an optional, extreme protection that's designed for the very few individuals who, because of who they are or what they do, might be personally targeted by some of the most sophisticated digital threats." The stated goal is to reduce "the attack surface that could potentially be exploited by highly targeted mercenary spyware," with the explicit trade-off that "your device won't function like it typically does." Available in iOS 16+, iPadOS 16+, watchOS 10+, macOS Ventura+. [CONFIRMED, retrieved 2026-08-12]

Protections it enables (iOS 17/macOS Sonoma-era list): **Messages** — most attachment types blocked (only certain images/video/audio), links and link previews unavailable; **Web browsing** — complex web technologies blocked (JIT disabled), web fonts and some images suppressed; **FaceTime** — incoming calls blocked unless previously called within 30 days; **Photos** — location stripped on share, shared albums removed; **Device connections** — accessory/computer connection requires the device to be unlocked; **Wireless** — no auto-join of non-secure Wi-Fi, disconnects from non-secure Wi-Fi, 2G/3G cellular turned off; **Configuration profiles** — cannot be installed, no MDM enrollment or supervision. Phone calls and plain-text messages continue to work; SOS is unaffected. [CONFIRMED, retrieved 2026-08-12]

Enabled per-device (Settings → Privacy & Security → Lockdown Mode on iOS; System Settings → Privacy & Security → Lockdown Mode on macOS), with a passcode/password step to turn on and restart. Websites and individual apps can be excluded from WebKit restrictions, with Apple's caution to exclude "only trusted apps or websites and only if necessary."

## Snippets

> "Lockdown Mode is an optional, extreme protection that's designed for the very few individuals who, because of who they are or what they do, might be personally targeted by some of the most sophisticated digital threats."

> "To reduce the attack surface that could potentially be exploited by highly targeted mercenary spyware, certain apps, websites, and features are strictly limited for security and some experiences might not be available at all."
[Source: https://support.apple.com/en-us/105120 (retrieved 2026-08-12)]
