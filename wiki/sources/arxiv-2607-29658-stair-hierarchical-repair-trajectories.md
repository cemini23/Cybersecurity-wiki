---
title: STAIR hierarchical repair trajectories (arXiv 2607.29658)
type: source
tags: [source, arxiv, coding-agents, repair, trajectory, memory]
keywords: [2607.29658, STAIR, SWE-bench, hierarchical abstraction, repair plans]
related:
  - concepts/stair-hierarchical-repair-plans.md
  - concepts/experiential-abstraction-memory.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
read_status: read
created: 2026-08-03
updated: 2026-08-03
phase_0_verdict: "REFERENCE 2026-08-03 — no public STAIR repo located"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (hierarchical reconstruct-before-inject)"
---

**Briefs:** `briefs/2026-08-03_k234-stair-prod.md`

## Relations

- @concepts/stair-hierarchical-repair-plans.md
- @concepts/experiential-abstraction-memory.md
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents |
| Authors | Yisen Xu, Jiayuan Zhou, Ruiqi Pan, Tse-Hsun Chen |
| arXiv | 2607.29658 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.29658-reusing-past-repairs-through-hierarchical-trajec.pdf` |
| Retrieved | 2026-08-03 |

## Narrative

Repair agents usually discard procedural knowledge after each issue. **STAIR** turns past repair trajectories into multi-level trees (fine diagnostic actions → high-level strategies), retrieves nodes across levels, and injects tailored plans into the agent prompt. SWE-bench Verified: **81.2%** Pass@1 (Lingxi + MiniMax M2.5); **79.2%** with GPT-5. Plans transfer across scaffolds: mini-SWE-agent v2 **75.8% → 81.0%** with no code change. Ablations: mixed abstraction levels beat any single level; raw unabstracted trajectories transfer substantially worse. [CONFIRMED abstract]

### Steal

1. Abstract past repairs into **hierarchical plans** before re-inject (extends MemHarness reconstruct-before-inject)
2. Mix fine + coarse levels — do not pick one granularity
3. Never dump raw trajectories as "memory"

## Snippets

> "mixing multiple abstraction levels surpasses any single level and that raw, unabstracted trajectories transfer substantially worse."
[Source: arXiv 2607.29658 abstract]
