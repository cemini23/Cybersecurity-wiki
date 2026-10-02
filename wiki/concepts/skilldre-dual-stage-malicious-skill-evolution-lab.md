---
title: "SkillDRE dual-stage malicious skill evolution (K378)"
type: concept
tags: [concept, agent-security, k378]
keywords: [2609.32400, K378]
related:
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md
  - sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md
  - concepts/agent-skill-injection.md
  - concepts/skill-misevolution.md
  - concepts/evoskill-injection-self-evolving-agents.md
  - concepts/skill-cascading-attacks-skill-based-agents.md
maturity: draft
created: 2026-09-29
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K378)"
---

## Relations

- @concepts/cross-task-no-regression-skill-promotion-gate.md — K390 cross-task no-regression promotion gate (sibling of the validation ratchet)
- @sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md — K387-K391 ingest source page
- @sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md
- @concepts/agent-skill-injection.md
- @concepts/skill-misevolution.md
- @concepts/evoskill-injection-self-evolving-agents.md
- @concepts/skill-cascading-attacks-skill-based-agents.md

## Raw Concept

Question: **SkillDRE dual-stage malicious skill evolution** — operator steal from arXiv 2609.32400?

## Narrative

Pre-execution scan and runtime defense are **different gates**. Lab eval of skill evolution must close the loop across both stages and keep a **benign-task** metric alongside attack success. HITL before evolving skills in an owned harness. **Do not clone** null-SPDX SkillDRE. **No skill payloads in wiki.**

## Snippets

> Triage from arXiv 2609.32400 abstract. [Source: arXiv 2609.32400 (retrieved 2026-09-29)]
