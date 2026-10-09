---
title: "When the test-repair loop is actually a control (K409)"
type: concept
tags: [concept, agent-security, k409]
keywords: [2610.09892, K409]
related:
  - sources/arxiv-2610-12233-resi-recursive-safety-improvement.md
  - concepts/recursive-safety-improvement-pareto.md
  - sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - concepts/local-suppression-vs-repair.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K409)"
---

## Relations

- @sources/arxiv-2610-12233-resi-recursive-safety-improvement.md — K408-K417 ingest / 2026-10-09
- @concepts/recursive-safety-improvement-pareto.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md
- @concepts/cross-task-no-regression-skill-promotion-gate.md
- @concepts/local-suppression-vs-repair.md

## Raw Concept

Question: **When the test-repair loop is actually a control** — operator steal from arXiv 2610.09892?

## Narrative

Red-teaming and incident feedback only produce security under three conditions: **every unresolved attack keeps a persistent chance of being discovered**, **repairs work**, and **updates preserve earlier protection**. Drop the third and the loop churns — you fix one thing and reopen another, and the completion clock never runs down. Given all three, a finite surface is covered with probability 1, with expected time bounded by **N/epsilon** and coverage time **log(N/delta)/epsilon**.

The second, cheaper rule: **repair regions, not singletons** — **m·H_m** against **N·H_N** — so a fix that closes a *class* of failure beats a pile of per-case fixes. And the loop is an investment: when the attacker's cost is high enough, **deterrence** (no new capability needed) beats buying more detection. Ask of any security program: **do findings persist, do repairs hold, and do updates stop regressing?**

## Snippets

> See arXiv 2610.09892 abstract. [Source: arXiv 2610.09892 (retrieved 2026-10-09)]
