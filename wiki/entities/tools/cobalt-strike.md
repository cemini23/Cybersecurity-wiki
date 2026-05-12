---
title: Cobalt Strike
type: entity
tags: [c2, post-exploitation, commercial, red-team-standard]
keywords: [cobalt strike, beacon, fortra, c2 framework, red team commercial tooling]
related:
  - concepts/red-team-operations.md
  - concepts/adversary-emulation.md
  - concepts/av-edr-bypass.md
  - sources/adversary-emulation-com-cobalt-strike.md
  - entities/people/joas-a-santos.md
  - entities/certifications/crto.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/red-team-operations.md
- @concepts/adversary-emulation.md
- @concepts/av-edr-bypass.md
- @sources/adversary-emulation-com-cobalt-strike.md
- @entities/people/joas-a-santos.md
- @entities/certifications/crto.md

## Raw Concept

Single most-cited commercial C2 in the corpus (Adversary Emulation com Cobalt Strike.pdf). Stub anchored to the corpus PDF; expand on next ingest pass.

## Narrative

Commercial command-and-control (C2) framework from Fortra (formerly Strategic Cyber LLC), originally written by Raphael Mudge. The de-facto standard for professional red team operations. [CONFIRMED]

**Architecture:** Team server (Java) + client GUI + Beacon implants. Beacon is the workhorse — supports HTTP/HTTPS/DNS/SMB-pipe communication, sleep + jitter for stealth, malleable C2 profiles for traffic shaping, and Aggressor Script for automation.

**Dual-use reality:** Cobalt Strike is licensed legitimately for red team consultancies but is **also one of the most-abused tools in criminal intrusions** — cracked Beacon builds are common in ransomware operator toolchains. As a result, vendor detections (CrowdStrike, Defender for Endpoint, etc.) signature heavily on default Beacon profiles. Operational red teams use malleable C2 profiles, [CobaltBus](https://github.com/Mr-Un1k0d3r/CobaltBus)-style transport switching, and process injection / sleep-mask techniques to stay ahead of signatures. See @concepts/av-edr-bypass.md for the broader evasion playbook.
