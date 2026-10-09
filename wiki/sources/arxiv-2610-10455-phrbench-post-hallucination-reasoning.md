---
title: "PHRBench: a behavioral evaluation of post-hallucination reasoning in LLMs"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.10455, k411]
related:
  - concepts/post-hallucination-reasoning-behavior.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/llm-explanation-necessary-sufficient-audit.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K411)"
---

## Relations

## Relations

- @concepts/post-hallucination-reasoning-behavior.md
- @concepts/chain-of-thought-decorative-reasoning-audit.md
- @concepts/llm-explanation-necessary-sufficient-audit.md
- @concepts/measurement-integrity-mcp-security-eval.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PHRBench: a behavioral evaluation of post-hallucination reasoning in LLMs |
| arXiv | 2610.10455 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.10455-phrbench-a-behavioral-evaluation-of-pos.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K411 — what a model does *after* it hallucinates matters more than that it hallucinated.** PHRBench feeds models a premise containing a hallucination and measures subsequent **reasoning behaviour**, not just answer accuracy. Across 18 models, hallucinated premises cost **7.7 percentage points** of accuracy on average — and the drop is **larger for proprietary models (11.0%) than open-source (6.1%)**, with GPT-5.2 falling 16.9 points. It is not one domain: Biomedicine 8.34 pp, Physics 7.12, Code Generation 6.89 (17 of 18 models drop there).

The taxonomy is the reusable part. **Hallucination Compliance** versus **Heuristic Correction** — and correction is rare: Qwen2.5 7.58% at 1.5B rising to 26.48% at 72B; GLM-4-9B 1.98%; GPT-5.2 3.69%. Only **11 of 18** models produce **insightful trajectories** above 10%. Insightful paths show **more reasoning words (~+34.7)** and a much higher **belief-update frequency (0.68 vs 0.24)** — the model actually revises, rather than reasoning longer around a wrong premise. Augmentation type matters: State Distortion costs 9.4 pp, Rule Contradiction 7.4, **Pseudoscientific Entanglement only 1.8** — a fluent pseudo-scientific framing barely moves the score. Operator steal: **test whether a model corrects or commits**, and prefer belief-update frequency over output length as the signal. Pairs K308 (decorative reasoning) and K337 (explanation necessity).

## Snippets

> See arXiv 2610.10455 abstract. [Source: arXiv 2610.10455 (retrieved 2026-10-09)]
