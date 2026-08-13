---
title: Amnesty International — Mobile Verification Toolkit (MVT)
type: source
tags: [source, amnesty, mvt, spyware, forensics, open-source]
keywords: [MVT, mvt-ios, mvt-android, indicators of compromise, Pegasus, forensics, consensual]
related:
  - concepts/commercial-spyware-stalkerware-defense.md
  - sources/amnesty-pegasus-forensic-methodology.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — README reviewed; NO-GO clone (custom license, forensic scope)"
wire_status: wont_wire
---

## Relations

- @concepts/commercial-spyware-stalkerware-defense.md — MVT is the forensic-triage step of spyware defense
- @sources/amnesty-pegasus-forensic-methodology.md — MVT shipped with this report; the trace classes it checks for

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Mobile Verification Toolkit (MVT) — README |
| Publisher | Amnesty International Security Lab / mvt-project |
| URL | https://github.com/mvt-project/mvt |
| Retrieved | 2026-08-12 |
| Location | README HTML (raw.githubusercontent.com); no clone (custom license + forensic scope) |

## Narrative

MVT is "a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices." Released by Amnesty International's Security Lab in July 2021 alongside the Pegasus Project and the forensic methodology report, and still maintained. It exposes two commands, `mvt-ios` and `mvt-android`, and scans against public indicators of compromise (IOCs) published by Amnesty and other research groups. [CONFIRMED README, retrieved 2026-08-12]

Critical caveats from the README: public IOCs are "insufficient to determine that a device is 'clean'"; reliable triage "requires access to non-public indicators, research and threat intelligence"; and MVT "is a forensic research tool intended for technologists and investigators… not intended for end-user self-assessment." [CONFIRMED README, retrieved 2026-08-12]

License (Phase-0 relevant): MVT is released under **its own custom license**, designed so the tool facilitates "consensual forensic analysis" of people who might be targets of sophisticated spyware and explicitly to avoid enabling "privacy violations of non-consenting individuals." This wiki therefore records it as **REFERENCE** with `wont_wire` — no local clone; the license is bespoke and the tool class is forensic, not a lab pentest harness.

## Snippets

> "Mobile Verification Toolkit (MVT) is a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices."

> "Reliable and comprehensive digital forensic support and triage requires access to non-public indicators, research and threat intelligence."

> "MVT is a forensic research tool intended for technologists and investigators. It requires understanding digital forensics and using command-line tools. This is not intended for end-user self-assessment."
[Source: https://github.com/mvt-project/mvt (retrieved 2026-08-12)]
