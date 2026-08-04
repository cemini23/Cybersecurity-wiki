---
title: MITRE Caldera
type: entity
tags: [adversary-emulation, automation, foss, mitre]
keywords: [caldera, mitre, adversary emulation, automated, atomic red team]
related:
  - concepts/adversary-emulation.md
  - concepts/purple-team-operations.md
  - entities/frameworks/mitre-attack.md
  - sources/adversary-simulation-with-caldera-and-mitre.md
  - entities/people/joas-a-santos.md
  - concepts/symbolic-art-attack-chain-granularity.md
  - sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md
maturity: draft
created: 2026-05-12
updated: 2026-08-04
---

## Relations

- @concepts/adversary-emulation.md
- @concepts/purple-team-operations.md
- @entities/frameworks/mitre-attack.md
- @sources/adversary-simulation-with-caldera-and-mitre.md
- @entities/people/joas-a-santos.md
- @concepts/symbolic-art-attack-chain-granularity.md
- @sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md

## Raw Concept

Anchored by Adversary Simulation with Caldera and Mitre.pdf.

## Narrative

MITRE's open-source adversary-emulation platform — automates the execution of ATT&CK-mapped TTPs against test environments. [CONFIRMED]

**Architecture:** server (Python) + agents (sandcat — Go, manx — TCP/HTTP, ragdoll — Python). Operators define **adversary profiles** (ordered lists of abilities, each ability tied to one or more MITRE techniques), then run **operations** that execute those abilities against agents.

**Distinguishing features vs Atomic Red Team:** Caldera is fully automated (it picks the next ability based on planner logic — atomic / batch / look-ahead); Atomic Red Team is a library of atomic tests you run manually. Caldera is better for unattended purple-team exercises; Atomic is better for focused detection-engineering work. See @concepts/purple-team-operations.md.
