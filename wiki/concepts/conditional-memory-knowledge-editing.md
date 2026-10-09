---
title: "Conditional memory, and the disable test (K412)"
type: concept
tags: [concept, agent-security, k412]
keywords: [2610.10533, K412]
related:
  - sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md
  - concepts/local-suppression-vs-repair.md
  - concepts/agent-execution-provenance.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K412)"
---

## Relations

- @sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md
- @concepts/local-suppression-vs-repair.md
- @concepts/agent-execution-provenance.md

## Raw Concept

Question: **Conditional memory, and the disable test** — operator steal from arXiv 2610.10533?

## Narrative

Updating a model's knowledge by rewriting weights damages everything around the edit. Putting the update in **conditional memory** instead keeps the base model intact — **Efficacy 99.5 / Generalization 97.0** with **Utility 93.9** after 2,000 sequential edits.

The transferable method is the **evidence**, not the architecture: **disable the fact-related memory and see if the behaviour reverts.** It does — **89.4%** of successes become failures and the margin flips from +15.5 to −5.9 — while **random disabling** changes nothing (−0.0003, zero failures). That control separates a real memory edit from a prompt artefact, and it is rare in editing papers. Two caveats to carry: multi-hop degrades with depth (36.92% at 2-hop to 15.09% at 4-hop), and **n-gram collisions** concentrate the failures — 8.66% of facts carry 97.96% of them.

## Snippets

> See arXiv 2610.10533 abstract. [Source: arXiv 2610.10533 (retrieved 2026-10-09)]
