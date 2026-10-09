---
title: "Recursive safety improvement under a Pareto gate (K414)"
type: concept
tags: [concept, agent-security, k414]
keywords: [2610.12233, K414]
related:
  - sources/arxiv-2610-12233-resi-recursive-safety-improvement.md
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - concepts/defensive-sufficiency-feedback-loop.md
  - concepts/psychological-multiturn-jailbreaks.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K414)"
---

## Relations

- @sources/arxiv-2610-12233-resi-recursive-safety-improvement.md
- @concepts/cross-task-no-regression-skill-promotion-gate.md
- @concepts/defensive-sufficiency-feedback-loop.md
- @concepts/psychological-multiturn-jailbreaks.md

## Raw Concept

Question: **Recursive safety improvement under a Pareto gate** — operator steal from arXiv 2610.12233?

## Narrative

A safety-improvement loop is only safe for the product if it cannot quietly spend capability to buy safety. ReSI's structure is the steal: **each round is accepted only if it passes a Pareto gate on a benign cost budget**, and the loop **stops when no round passes**. That yielded X-Teaming ASR **31.45%** against an 86.01% backbone — better than the frontier model at 56.69% — with H-CoT dropping from 72–100% to 0–18%.

The honest cost: **−2.80 pp** benign full-compliance on two models and **−1.31 to −2.07 pp** IFEval. And note the loop self-terminated after **1–3 rounds** because the gate stopped passing — that termination is a feature, not a failure: it is the budget telling you the remaining safety gains cost more capability than they are worth. Generalise the shape: **gate, measure the benign cost, stop when the gate fails.**

## Snippets

> See arXiv 2610.12233 abstract. [Source: arXiv 2610.12233 (retrieved 2026-10-09)]
