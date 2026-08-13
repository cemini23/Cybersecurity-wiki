---
title: Commercial Spyware and Stalkerware Defense
type: concept
tags: [spyware, stalkerware, mobile-security, lockdown-mode, mvt, defense]
keywords: [Pegasus, Predator, mercenary spyware, NSO, zero-click, Lockdown Mode, MVT, mobile verification toolkit, stalkerware, endpoint compromise]
related:
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/system-hardening.md
  - concepts/operator-lab-playbook.md
  - concepts/owned-target-whitehat-lab.md
  - sources/apple-lockdown-mode.md
  - sources/amnesty-mobile-verification-toolkit.md
  - sources/amnesty-pegasus-forensic-methodology.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
---

## Relations

- @concepts/metadata-traffic-analysis-anonymity.md — spyware defeats network anonymity; different defense layer
- @concepts/system-hardening.md — Lockdown Mode is a mobile hardening control, sibling to the desktop trust stack
- @concepts/operator-lab-playbook.md — operator-owned devices in a hostile-network threat model
- @concepts/owned-target-whitehat-lab.md — authorized lab: spyware class is studied as defense, never installed
- @sources/apple-lockdown-mode.md — first-party extreme-protection mode
- @sources/amnesty-mobile-verification-toolkit.md — open-source forensic triage tool (IOCs; consensual use only)
- @sources/amnesty-pegasus-forensic-methodology.md — what Pegasus-class infection actually leaves behind

## Raw Concept

**In scope:** how threats work at the *class* level; first-party privacy/security controls; what an operator inventories; how to design a product so it does not become the deanonymizer or the spyware implant.

**Out of scope:** installing Pegasus/stalkerware; hidden-volume step-by-steps for hiding evidence; GFW/Tor-bridge recipes as a runbook; SIM-swap *how to steal a number*; exploits/PoCs; HWID spoofers; keygens; Magisk/Play Integrity Fix.

Freedom-of-information / anonymity framing: journalists, dissidents, operators, product users in hostile networks. **Not** "evade a lawful US warrant." Compelled-disclosure is a *threat model to document*, not a crime guide.

Distinguishes the two commercial-espionage product families by threat model and documents the **defense** class: Lockdown Mode, MVT triage, and the reinstall/hardware-replacement decision. No spyware installers, no implant code.

## Narrative

### 1. Two different product families, one shared endpoint assumption

| Family | Typical operator | Delivery | Defensive posture |
|--------|------------------|----------|-------------------|
| **Mercenary spyware (NSO Pegasus, Predator class)** | Surveillance vendors selling to governments | Exploit chains: SMS links, iMessage zero-click (2019/2021), network injection via rogue cell towers, app abuse (Apple Music 2020) | Assume endpoint fully compromised; extreme hardening + forensic triage |
| **Consumer stalkerware** | Individuals with physical/coerced access to a device | Physical install, sideloaded APK, paid spouse-monitoring services, MDM enrollment trick | Screen lock, profile/MDM check, app review, factory reset; often simpler to detect |

[CONFIRMED Amnesty methodology for mercenary class, retrieved 2026-08-12]

The unifying fact: **both are endpoint compromise**, not a Tor failure and not an account-password problem. The attacker does not observe your network path — they run code on the device. Network anonymity (@concepts/metadata-traffic-analysis-anonymity.md) is the wrong defense layer.

### 2. What mercenary spyware leaves behind (Amnesty forensic methodology)

Amnesty's Security Lab published a forensic methodology with the Pegasus Project; the traces it documented are the *class* of evidence a defender checks:

- **Process execution records** — `DataUsage.sqlite` / `netusage.sqlite` showing a `bh` process seconds after visits to Pegasus installation domains; post-exploitation processes spoofing legitimate daemon names (`roleaccountd`, `launchrexd`, `stagingd`, …).
- **Anti-forensics** — `com.apple.CrashReporter.plist` written to disable crash reporting; later versions deleting process names from `ZPROCESS` while leaving `ZLIVEUSAGE`, a detectable inconsistency.
- **Staging** — payload binaries in `/private/var/db/com.apple.xpc.roleaccountd.staging/`.
- **Network traces** — Safari redirects to 4th-level-subdomain installation servers on non-standard high ports; entries in `Favicon.db`, WebKit IndexedDB, Session Resource logs.

Notably: "there are significantly more forensic traces accessible to investigators on Apple iOS devices than on stock Android devices," so the methodology is iOS-centric. [CONFIRMED Amnesty, retrieved 2026-08-12]

### 3. The defense class

1. **Extreme hardening for high-risk users: Lockdown Mode.** Apple's optional mode is aimed at "the very few individuals who… might be personally targeted by some of the most sophisticated digital threats" and reduces "the attack surface that could potentially be exploited by highly targeted mercenary spyware." It blocks most message attachments, disables JIT web technologies, blocks unknown incoming FaceTime, forbids configuration-profile/MDM enrollment, won't join non-secure Wi-Fi, and turns off 2G/3G cellular. [CONFIRMED Apple, retrieved 2026-08-12] The trade-off is deliberate: "your device won't function like it typically does."
2. **Forensic triage: Amnesty Mobile Verification Toolkit (MVT).** `mvt-ios` / `mvt-android` parse iOS backups/filesystem dumps and Android data against published STIX-format indicators of compromise. MVT is explicit that public IOCs are insufficient to declare a device "clean" and that it "is not intended for end-user self-assessment." License note: MVT uses a **custom license** that allows consensual forensic analysis but not surveillance of non-consenting people — a deliberate design choice, and a reason this wiki treats it as **REFERENCE** (`wont_wire`), not a clone-and-run lab tool. [CONFIRMED MVT README, retrieved 2026-08-12]
3. **Assume-burn for high-confidence infection.** If triage or behavioral evidence indicates a live mercenary implant: assume disk, mic, camera, and any stored certificates/keys are compromised. Recovery class: restore from a trusted known-good backup (or migrate data selectively), reinstall OS from a known-good source, rotate every credential and key the device touched, and for high-confidence, fully-remote compromise **replace the hardware** — a persistent implant can survive a reinstall if it lives in firmware, the baseband, or the bootchain.
4. **Behavioral / organizational hygiene.** Keep the device's iOS/macOS updated; treat unknown config profiles and unrequested MDM enrollment as a red flag; for high-value targets, a dedicated device for the most sensitive work; never assume a "clean" scan is a clean device — the absence of public-IOC hits is not proof of absence.

### 4. Operator + product steals

- **Operator:** if you work on sensitive client work, separate your attack box and your personal device; a personal device compromised by stalkerware becomes a corporate-engagement leak. Lockdown Mode is the high-threat default; MVT is the check you run *before* trusting a device again.
- **Product:** do not ship your app as a telemetry implant. Minimize always-on mic/location/camera collection; make sensor access user-gated and disclosed; no silent profile installation; no hidden MDM enrollment. A product whose business model is surveillance-by-default is the same class as the stalkerware this page defends against — and the entity page for such a tool would be a liability, not an adoption.

## Snippets

> "To reduce the attack surface that could potentially be exploited by highly targeted mercenary spyware, certain apps, websites, and features are strictly limited for security and some experiences might not be available at all."
[Source: https://support.apple.com/en-us/105120 (retrieved 2026-08-12)]

> "Reliable and comprehensive digital forensic support and triage requires access to non-public indicators, research and threat intelligence."
[Source: https://github.com/mvt-project/mvt (retrieved 2026-08-12)]

> "a successful 'zero-click' attack has been observed exploiting multiple zero-days to attack a fully patched iPhone 12 running iOS 14.6 in July 2021."
[Source: https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/ (retrieved 2026-08-12)]
