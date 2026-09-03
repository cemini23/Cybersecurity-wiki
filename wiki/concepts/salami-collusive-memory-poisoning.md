---
title: Salami / collusive memory poisoning against agents
type: concept
tags: [concept, agent-security, memory, poisoning]
keywords: [Salami Attack, MemCollusion, collusive memory, OpenClaw, 2608.01637]
related:
  - sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md
  - concepts/agent-data-injection-attacks.md
  - concepts/codepoisonrag-racg-knowledge-poisoning.md
  - concepts/experiential-abstraction-memory.md
  - concepts/stair-hierarchical-repair-plans.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md
- @concepts/agent-data-injection-attacks.md
- @concepts/experiential-abstraction-memory.md
- @concepts/stair-hierarchical-repair-plans.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Individually innocuous memory records can collude to poison long-term agent behavior.

## Narrative

Defenses that score single memories miss coalition attacks. Operational rule: before promoting observed content into durable agent memory, rewrite/validate as a set against the current task; reject unexplained multi-fragment "consensus/authority" stacks from untrusted external surfaces. Pairs ADI (trusted vs untrusted tool data) and reconstruct-before-inject. [CONFIRMED abstract; attack code closed]
