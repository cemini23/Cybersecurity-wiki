---
title: "A component's role is a function of task context (K424)"
type: concept
tags: [concept, agent-security, k424]
keywords: [2610.13895, K424]
related:
  - sources/arxiv-2610-13895-task-context-component-roles.md
  - concepts/late-attention-entity-token-copying-interpretability.md
  - concepts/deep-noir-steering-discovery-chronometry.md
  - concepts/countersteer-activation-steering-ipi-defense.md
  - concepts/probe-internal-recognition-sandbagging-audit.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K424)"
---

## Relations

- @sources/arxiv-2610-13895-task-context-component-roles.md
- @concepts/late-attention-entity-token-copying-interpretability.md
- @concepts/deep-noir-steering-discovery-chronometry.md
- @concepts/countersteer-activation-steering-ipi-defense.md
- @concepts/probe-internal-recognition-sandbagging-audit.md

## Raw Concept

Question: **A component's role is a function of task context** — operator steal from arXiv 2610.13895?

## Narrative

Mechanistic interpretability often treats a discovered circuit as a fixed label: 'this head does X'. K424 shows the label is **task-conditional**. Hold the input facts identical and change only the task, and **influence redistributes** — the same attention heads respond to **different facts** and change later computation **differently**. In Gemma-2-9B and Qwen3-14B a single **activation edit** flips **which fact the model reads** while the written instruction is unchanged, and a **condition-specific linear response map** predicts a later head's response far better than the average of the two maps — **53.6%** lower MSE in Gemma, **5.0%** in Qwen.

The operator rule matters for safety interventions: **an interpretability result does not transfer across tasks as a static fact**, so a steering edit or activation clamp validated on one behaviour must be **re-validated for the behaviour you intend to preserve**. This is the mechanistic counterpart to the wiki's measurement-integrity line — a component-level claim is only as strong as the task surface it was measured on. Pairs K318, K349, K383, K337.

## Snippets

> See arXiv 2610.13895 abstract. [Source: arXiv 2610.13895 (retrieved 2026-10-12)]
