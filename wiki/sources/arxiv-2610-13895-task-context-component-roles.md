---
title: "Task context shapes component roles in language models"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.13895, k424]
related:
  - concepts/task-dependent-component-roles.md
  - concepts/late-attention-entity-token-copying-interpretability.md
  - concepts/deep-noir-steering-discovery-chronometry.md
  - concepts/countersteer-activation-steering-ipi-defense.md
  - concepts/probe-internal-recognition-sandbagging-audit.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K424)"
---

## Relations

## Relations

- @concepts/task-dependent-component-roles.md
- @concepts/late-attention-entity-token-copying-interpretability.md
- @concepts/deep-noir-steering-discovery-chronometry.md
- @concepts/countersteer-activation-steering-ipi-defense.md
- @concepts/probe-internal-recognition-sandbagging-audit.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Task context shapes component roles in language models |
| arXiv | 2610.13895 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610-13895-task-context-shapes-component-roles-in-language.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K424 — a shared attention head is not a fixed feature; its role is task-conditional.** Circuit analysis shows LLMs **reuse the same attention heads across tasks**, but identifying a shared head does not explain what it does differently in each. This work compares **identical graph facts** across tasks and measures two things per component: **influence** (how an intervention on a head changes later layers) and **importance** (the effect on the answer). Task changes **redistribute influence** across five open-weight models (four families, 1.5-14B).

The concrete demonstration: in **Gemma-2-9B** and **Qwen3-14B**, a single **activation edit** switches **which fact the model reads** while the written instruction stays fixed — the same heads then respond to different facts and influence later components differently. The authors build two **linear response maps** (before and after the edit), and for a **separate factual intervention** the condition-matched map reduces **mean squared prediction error by 53.6%** in Gemma and **5.0%** in Qwen against the average of the two maps. No code release.

Operator steal for the security/interpretability lane: **a head's role is a function of task context**, so an interpretability finding does not transfer as a fixed label, and any steering or intervention meant to change one behaviour while preserving others must be **re-validated per task**. Pairs K318 (multi-token SAE readout), K349 (Deep Noir steering), K383 (CounterSteer).

## Snippets

> See arXiv 2610.13895 abstract. [Source: arXiv 2610.13895 (retrieved 2026-10-12)]
