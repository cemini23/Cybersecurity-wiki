---
title: "ReSI: recursive safety improvement toward resistant and resilient AI"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.12233, k414]
related:
  - concepts/recursive-safety-improvement-pareto.md
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - concepts/defensive-sufficiency-feedback-loop.md
  - concepts/psychological-multiturn-jailbreaks.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K414)"
---

## Relations

## Relations

- @concepts/recursive-safety-improvement-pareto.md
- @concepts/cross-task-no-regression-skill-promotion-gate.md
- @concepts/defensive-sufficiency-feedback-loop.md
- @concepts/psychological-multiturn-jailbreaks.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ReSI: recursive safety improvement toward resistant and resilient AI |
| arXiv | 2610.12233 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610-12233-resi-recursive-safety-improvement-towar.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K414 — a post-training loop that beats frontier models on safety at a few points of benign cost.** ReSI runs a **recursive** improvement loop with a **Pareto gate**: a round is accepted only if it improves safety without breaking the benign budget, and the loop stops when no round passes. X-Teaming ASR falls to **31.45%** against a backbone mean of **86.01%** (−54.56 pp) — better than **GPT-5.6-Luna at 56.69%**, and frontier models sit at 56.69–84.85%. The hardest slice moves most: **H-CoT ASR 72–100% → 0–18%**.

The cost is stated honestly: benign full-compliance drops **2.80 pp** on two of four models and **IFEval loose accuracy falls 1.31–2.07 pp**; GPQA-Diamond and MMLU-Pro move within about ±2 pp. Accepted rounds were few — 1 to 3 per model, each loop then stopping because **the next round had no Pareto-gate pass**. Operator steal: **gate every safety round on a benign cost budget and stop when the gate stops passing** — that is what keeps a safety loop from trading capability away silently. Pairs K390 (the no-regression promotion gate) and K409 (defensive sufficiency).

## Snippets

> See arXiv 2610.12233 abstract. [Source: arXiv 2610.12233 (retrieved 2026-10-09)]
