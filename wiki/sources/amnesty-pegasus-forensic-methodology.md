---
title: Amnesty International — Forensic Methodology: How to Catch NSO Group's Pegasus
type: source
tags: [source, amnesty, pegasus, nso, spyware, forensics, public-report]
keywords: [Pegasus, NSO, zero-click, iMessage, DataUsage.sqlite, Mobile Verification Toolkit, Pegasus Project, forensic methodology]
related:
  - concepts/commercial-spyware-stalkerware-defense.md
  - sources/amnesty-mobile-verification-toolkit.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — Amnesty public research report (implant architecture, not a kit)"
wire_status: wont_wire
---

## Relations

- @concepts/commercial-spyware-stalkerware-defense.md — the trace/infection-class evidence the defense checks for
- @sources/amnesty-mobile-verification-toolkit.md — MVT shipped with this report to operationalize the checks

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Forensic methodology report: How to catch NSO Group's Pegasus |
| Publisher | Amnesty International Security Lab (with the Pegasus Project / Forbidden Stories) |
| URL | https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/ |
| Retrieved | 2026-08-12 |
| Location | HTML (no PDF archive) |

## Narrative

Amnesty's public methodology report, published with the Pegasus Project ("a collaborative investigation that involves more than 80 journalists from 17 media organizations in 10 countries coordinated by Forbidden Stories with technical support of Amnesty International's Security Lab"). It documents forensic traces of NSO Pegasus on iOS devices and rebuts NSO's claims that Pegasus "leaves no traces whatsoever." [CONFIRMED, retrieved 2026-08-12]

Trace classes documented (architecture-level, for defenders):
- **Network injection / Safari redirects** — e.g. a Yahoo.fr visit redirecting to a Pegasus installation domain with a 4th-level subdomain, non-standard high port, random URI; traces in Safari history, `Favicon.db`, WebKit IndexedDB, Session Resource logs. Staging/trampoline domains used before redirect to exploit servers.
- **Process execution records** — `DataUsage.sqlite` / `netusage.sqlite` showing a process named `bh` seconds after visits to installation domains (linked to the 2016 Mansoor Pegasus sample).
- **Post-exploitation processes** — `roleaboutd`, `msgacntd`, `pcsd`, `fmld`, `stagingd`, `roleaccountd`, `launchrexd`, etc., several spoofing legitimate iOS daemon names; binaries staged in `/private/var/db/com.apple.xpc.roleaccountd.staging/`.
- **Anti-forensics** — `com.apple.CrashReporter.plist` written to disable crash reporting; later Pegasus versions deleting `ZPROCESS` names while leaving `ZLIVEUSAGE`, a detectable inconsistency.

Attack vectors documented: SMS links (2016–2018), network injection via rogue cell towers/operator equipment (Morocco), iMessage zero-click exploits (2019 and 2021, "Megalodon"), possible Apple Photos/Photostream abuse, and Apple Music abuse (2020). The report observed "a successful 'zero-click' attack … exploiting multiple zero-days to attack a fully patched iPhone 12 running iOS 14.6 in July 2021." [CONFIRMED, retrieved 2026-08-12]

Android caveat: "there are significantly more forensic traces accessible to investigators on Apple iOS devices than on stock Android devices," so the methodology is iOS-centric. Infrastructure: 1,748 unique subdomain resolutions across just 23 domains in passive DNS — "Pegasus may have been used in thousands of attacks over the past three years"; hosting concentrated in European datacentres of US providers (Germany 212 servers, UK 79; Digital Ocean, Linode, AWS), with recent attacks using Amazon CloudFront.

## Snippets

> "Widespread, persistent and ongoing unlawful surveillance" — the Pegasus Project's finding across victim devices.
[Source: https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/ (retrieved 2026-08-12)]

> "A successful 'zero-click' attack has been observed exploiting multiple zero-days to attack a fully patched iPhone 12 running iOS 14.6 in July 2021."
[Source: https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/ (retrieved 2026-08-12)]
