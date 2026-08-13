---
title: Coding-agent context pruning (SWE-Pruner Pro pattern)
type: concept
tags: [coding-agent, context-management, efficiency]
keywords: [tool-output pruning, internal representations, SWE-Bench tokens]
related:
  - sources/arxiv-2607-18213-swe-pruner-pro.md
  - entities/tools/swe-pruner-pro.md
  - concepts/ai-for-cybersecurity.md
  - concepts/evidence-aware-long-context-grounding.md
  - sources/arxiv-2607-19345-gear-evidence-aware-rl.md
  - concepts/experiential-abstraction-memory.md
  - entities/tools/notes-to-self.md
  - sources/arxiv-2607-20372-notes-to-self-experiential.md
  - concepts/stair-hierarchical-repair-plans.md
  - sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md
  - concepts/blast-radius-reversible-context-eviction.md
  - sources/arxiv-2608-07440-blast-radius.md
  - entities/tools/blast-radius-necrophoresis.md
  - sources/arxiv-2608-12311-rsm-role-specialization.md
  - concepts/role-specialization-multi-tool-coordination.md
maturity: draft
created: 2026-07-21
updated: 2026-08-13
---

## Relations

- @sources/arxiv-2607-20372-notes-to-self-experiential.md
- @entities/tools/notes-to-self.md
- @concepts/experiential-abstraction-memory.md
- @sources/arxiv-2607-19345-gear-evidence-aware-rl.md
- @concepts/evidence-aware-long-context-grounding.md
- @sources/arxiv-2607-18213-swe-pruner-pro.md
- @entities/tools/swe-pruner-pro.md
- @concepts/ai-for-cybersecurity.md
- @concepts/stair-hierarchical-repair-plans.md
- @sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md
- @concepts/blast-radius-reversible-context-eviction.md
- @sources/arxiv-2608-07440-blast-radius.md
- @entities/tools/blast-radius-necrophoresis.md

- @sources/arxiv-2608-12311-rsm-role-specialization.md
- @concepts/role-specialization-multi-tool-coordination.md
## Raw Concept

Multi-turn coding agents drown in tool stdout. Pruning from the **agent's own hidden states** can cut tokens (~39%) without a separate classifier — and sometimes improve resolve rates.

## Narrative

Use when trajectories are tool-output heavy. Measure resolve/quality + latency overhead of the prune head. Lab-only until LICENSE file lands alongside pyproject Apache-2.0 claim.
