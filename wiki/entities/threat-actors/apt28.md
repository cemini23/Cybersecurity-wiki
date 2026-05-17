---
title: APT28 (Fancy Bear / Sofacy)
type: entity
tags: [threat-actor, apt, nation-state, russia-attributed]
keywords: [apt28, fancy bear, sofacy, strontium, pawn storm, gru, russia]
related:
  - concepts/adversary-emulation.md
  - concepts/cyberwarfare.md
  - entities/frameworks/mitre-attack.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/apt29.md
  - sources/apt28-understanding-a-group-specialized-in-attacks-against-intelligence-sectors.md
  - concepts/threat-intelligence.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
---

## Relations

- @concepts/adversary-emulation.md
- @concepts/cyberwarfare.md
- @entities/frameworks/mitre-attack.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/apt29.md
- @sources/apt28-understanding-a-group-specialized-in-attacks-against-intelligence-sectors.md
- @concepts/threat-intelligence.md


## Raw Concept

Sole named APT group in the corpus (APT28 — Understanding a group specialized in attacks against intelligence sectors.pdf). Stub upgraded with public threat-intel context; deeper expansion will come from the corpus PDF on next deep-read pass.

## Narrative

APT28 — aliases Fancy Bear, Sofacy, Strontium, Pawn Storm, Sednit — is a Russian state-sponsored advanced persistent threat group widely attributed to the GRU (Russian military intelligence, Unit 26165) by Western government agencies and threat-intel vendors (CrowdStrike, Mandiant, Microsoft Threat Intelligence, US-CERT). [NEEDS VERIFICATION 2026-05-12]

**Notable operations** (public attribution):
- DNC + DCCC intrusions, 2016 US election interference
- TV5Monde attack, 2015
- German Bundestag intrusion, 2015
- WADA / IAAF (anti-doping) intrusions, 2016
- Long-running campaigns against NATO members, defense contractors, foreign ministries

**TTPs (high-level, MITRE-keyed):** spear-phishing with credential-harvesting + zero-day exploits; custom malware families (X-Agent, X-Tunnel, Komplex, Zebrocy, Cannon, LoJax UEFI implant); use of 0day exploits when justified; aggressive operational tempo. MITRE ATT&CK [group page G0007](https://attack.mitre.org/groups/G0007/) is the canonical mapping. [Sources: attack.mitre.org/groups/G0007/, APT28 - Understanding a group specialized in attacks against intelligence sectors.pdf]

**Adversary emulation:** the MITRE Engenuity Center for Threat-Informed Defense and various red-team teams (SCYTHE, AttackIQ) publish APT28 emulation plans. These are good starting points for Purple Team exercises (see @concepts/purple-team-operations.md).
