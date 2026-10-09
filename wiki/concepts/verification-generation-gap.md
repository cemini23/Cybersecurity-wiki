---
title: "Knowing a claim is false is not refusing to render it (K413)"
type: concept
tags: [concept, agent-security, k413]
keywords: [2610.11112, K413]
related:
  - sources/arxiv-2610-11112-false-claims-credible-images.md
  - concepts/compliance-verdict-rule-invariance.md
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K413)"
---

## Relations

- @sources/arxiv-2610-11112-false-claims-credible-images.md
- @concepts/compliance-verdict-rule-invariance.md
- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md

## Raw Concept

Question: **Knowing a claim is false is not refusing to render it** — operator steal from arXiv 2610.11112?

## Narrative

A model can **verify** that a claim is misinformation and still **generate** it as credible visual evidence. The measured gap is stark: **FCR 100.00% against ASR 77.01%** on one commercial generator, **100.00% vs 55.82%** on another. The capability exists; it simply does not gate the output.

This is the third instance in this wiki of the same shape — K415 (a compliance verdict invariant to the rule) and K416 (a citation that is not a consultation). **Stated knowledge and operative behaviour are different objects**, and the instrument that reveals the difference is a **perturbation**, not the model's own account.

The constructive finding is that the gate can be made to bind: **asking the same model to verify before generating**, with no retrieval and no weight change, took interception from 10.70% to **76.20%** and from 32.40% to **93.00%** on two models, at no cost to benign prompts (92.8-99.1%). Operator rule: **do not assume a check the model can perform is a check that constrains it — put it in the pipeline as a step.**

## Snippets

> See arXiv 2610.11112 abstract. [Source: arXiv 2610.11112 (retrieved 2026-10-09)]
