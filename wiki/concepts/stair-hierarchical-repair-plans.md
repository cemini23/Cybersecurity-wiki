---
title: STAIR — hierarchical repair plans from agent trajectories
type: concept
tags: [concept, coding-agents, repair, trajectory, memory]
keywords: [STAIR, hierarchical abstraction, repair plans, SWE-bench, 2607.29658]
related:
  - sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md
  - concepts/experiential-abstraction-memory.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
  - concepts/salami-collusive-memory-poisoning.md
  - sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md
maturity: draft
created: 2026-08-03
updated: 2026-08-04
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md
- @concepts/experiential-abstraction-memory.md — sibling experiential abstraction (Notes-to-self)
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md
- @concepts/salami-collusive-memory-poisoning.md
- @sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md

## Raw Concept

Reuse coding-agent repairs as hierarchical plans, not raw transcripts.

## Narrative

Past tool traces contain reusable diagnosis → patch → verify structure. Dumping them whole causes negative transfer. **STAIR** builds multi-level trees and re-injects selected nodes. Operational rule for Cemini harness: when reusing prior repair/engagement trajectories, **rewrite into hierarchical plans** (fine actions + coarse strategy) before the next turn — same spirit as MemHarness reconstruct-before-inject, with explicit multi-granularity. [CONFIRMED abstract; code closed]
