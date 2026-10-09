---
title: "Cross-task no-regression skill promotion gate (K390)"
type: concept
tags: [concept, agent-security, k390]
keywords: [2610.02204, K390]
related:
  - sources/arxiv-2610-12233-resi-recursive-safety-improvement.md
  - sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md
  - concepts/recursive-safety-improvement-pareto.md
  - concepts/defensive-sufficiency-feedback-loop.md
  - sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md
  - concepts/skill-misevolution.md
  - concepts/experience-driven-redteam-skill-evolution.md
  - concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md
maturity: draft
created: 2026-10-02
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K390)"
---

## Relations

- @sources/arxiv-2610-12233-resi-recursive-safety-improvement.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md — K408-K417 ingest / 2026-10-09
- @concepts/recursive-safety-improvement-pareto.md — K408-K417 ingest / 2026-10-09
- @concepts/defensive-sufficiency-feedback-loop.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md
- @concepts/skill-misevolution.md
- @concepts/experience-driven-redteam-skill-evolution.md
- @concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md

## Raw Concept

Question: **Cross-task no-regression skill promotion gate** — operator steal from arXiv 2610.02204?

## Narrative

An agent files an update to its own **skill library or system prompt** only if a gate passes on **every** task in the suite: mean success must rise **and** no single task may fall more than a set margin. Merged revisions are retested under the same gate, so an integration that fixes one task but breaks another is rejected. This is the no-regression sibling of the validation ratchet — use it to bound **skill and prompt writes** in an owned harness. Domain is robot manipulation; the mechanism is harness-general. **No skill bodies in wiki.**

## Snippets

> See arXiv 2610.02204 abstract. [Source: arXiv 2610.02204 (retrieved 2026-10-02)]
