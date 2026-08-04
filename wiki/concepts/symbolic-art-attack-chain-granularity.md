---
title: Symbolic ART attack-chain predicate granularity
type: concept
tags: [concept, adversary-emulation, planning, atomic-red-team]
keywords: [PDDL, AALM, Atomic Red Team, attack chain, 2608.00143]
related:
  - sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md
  - concepts/adversary-emulation.md
  - concepts/red-team-operations.md
  - entities/tools/caldera.md
  - entities/frameworks/mitre-attack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md
- @concepts/adversary-emulation.md
- @concepts/red-team-operations.md
- @entities/tools/caldera.md
- @entities/frameworks/mitre-attack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

When auto-building ATT&CK/ART attack chains via PDDL, predicate category count may matter less for plan validity than for plan explainability.

## Narrative

Purple-team automation often overfits complex linking ontologies. Empirical ART→PDDL study: 5- vs 9-category schemes yield mostly identical valid plans; extra categories buy structural resolution. Operational takeaway: start from ART execution evidence; escalate ontology complexity only when justification/fidelity gaps appear. [CONFIRMED abstract]
