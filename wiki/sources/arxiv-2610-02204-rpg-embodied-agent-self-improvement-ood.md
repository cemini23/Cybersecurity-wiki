---
title: "Reconstruct, practice, go real: guided self-improvement for embodied agents"
type: source
tags: [source, ood]
keywords: [2610.02204, ood]
related:
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - concepts/skill-misevolution.md
  - concepts/experience-driven-redteam-skill-evolution.md
  - concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md
maturity: draft
read_status: read
created: 2026-10-02
updated: 2026-10-02
phase_0_verdict: "REFERENCE 2026-10-02 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K390)"
---

## Relations

## Relations

- @concepts/cross-task-no-regression-skill-promotion-gate.md
- @concepts/skill-misevolution.md
- @concepts/experience-driven-redteam-skill-evolution.md
- @concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reconstruct, practice, go real: guided self-improvement for embodied agents |
| arXiv | 2610.02204 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.02204-reconstruct-practice-go-real-guided-self-improve.pdf |
| Retrieved | 2026-10-02 |
| Read status | read (deep-read via grok CLI) |

## Narrative

**K390 — OOD for security, in-scope for agent-harness evolution.** RPG improves a robot execution system **without updating model weights**: reconstruct practice tasks from an offline dataset, run them in simulation, diagnose failures with privileged simulator state plus video, then revise a shared **skill library and system prompt**. The transferable mechanism is the **promotion gate**: a candidate revision is eligible only if mean task success rises **and** no task drops more than one success in five, and merged revisions are retested under the same gate. Report: 28.6% → 95.0% over 15 rounds on 22 held-out tasks; 30/30 physical trials. Security relevance: **none** — no adversary or attack surface. Keep it as a **harness-evolution pattern** (gate skill/prompt writes on no-regression across tasks), which pairs with the validation-ratchet family. Project page `rpg-robot.github.io`, license not stated — no clone.

## Snippets

> See arXiv 2610.02204 abstract. [Source: arXiv 2610.02204 (retrieved 2026-10-02)]
