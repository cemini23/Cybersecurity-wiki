---
title: Salami Attack collusive memory poisoning (arXiv 2608.01637)
type: source
tags: [source, arxiv, agent-security, memory, poisoning, openclaw]
keywords: [2608.01637, Salami Attack, MemCollusion, memory poisoning, OpenClaw]
related:
  - concepts/salami-collusive-memory-poisoning.md
  - concepts/agent-data-injection-attacks.md
  - concepts/experiential-abstraction-memory.md
  - concepts/stair-hierarchical-repair-plans.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-04
updated: 2026-08-04
phase_0_verdict: "REFERENCE 2026-08-04 — MemCollusion code not public; OpenClaw is victim surface"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (collusive memory)"
---

**Briefs:** `briefs/2026-08-04_k238-salami-memory-poisoning-prod.md`

## Relations

- @concepts/salami-collusive-memory-poisoning.md
- @concepts/agent-data-injection-attacks.md
- @concepts/experiential-abstraction-memory.md
- @concepts/stair-hierarchical-repair-plans.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw |
| Authors | Lin, Huang, Niu, Ye, Gao (Xidian) |
| arXiv | 2608.01637 |
| Code | MemCollusion not published; cites OpenClaw as target |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.01637-salami-attack-stealthy-collusive-memory-poisonin.pdf` |
| Retrieved | 2026-08-04 |

## Narrative

**Compositional** memory poisoning: many individually benign-looking memory fragments jointly induce unsafe behavior ("salami" slicing). **MemCollusion** automates coalitions via four design constraints + five theory-informed strategies + LoRA generator. Cross-session: adversary posts crafted external content → agent summarizes into persistent MEMORY → later benign request steered by coalition. Existing single-record poison defenses miss this class. [CONFIRMED abstract]

### Steal

1. Audit persistent memory as a **set** (coalitions), not per-record Shannon heuristics
2. Reconstruct / validate memory before inject (extends MemHarness + STAIR)
3. Treat cross-session observe→summarize pipelines as an untrusted write path
4. Lab-only red-team against owned agents — no LIVE OpenClaw/third-party

## Snippets

> "multiple benign-looking memories may jointly induce unsafe behavior."
[Source: arXiv 2608.01637 abstract]
