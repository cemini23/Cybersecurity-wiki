---
title: "Logit-tilting rare-behaviour audit — multi-turn elicitation without training (K319)"
type: concept
tags: [concept, agent-security, audit, red-team, lab-only, k319]
keywords: [BLOOM-WILT, LogitTilt, behaviour elicitation, automated auditing, multi-turn audit, rare behaviours, decoding-time steering]
related:
  - sources/arxiv-2608-31105-bloom-wilt-logit-tilting-audit.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/psychological-multiturn-jailbreaks.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K319)"
---

## Relations

- @sources/arxiv-2608-31105-bloom-wilt-logit-tilting-audit.md — BLOOM-WILT (2608.31105)
- @concepts/ai-redteam-evidential-ceiling.md — deployment scale exceeds pre-release eval
- @concepts/faithful-agent-asr-measurement.md — score behaviours in transcripts with explicit rubrics

## Raw Concept

Question: **how do you find realistic multi-turn examples of rare model behaviours for audit?**

## Narrative

Pre-deployment tests see far fewer interactions than production. **BLOOM-WILT (K319)** combines scenario-based **multi-turn auditing** (BLOOM) with optimization at **both ends**: auditor strategy refinement (input) and **LogitTilt** on target decoding (output) using only the target's **next-token logits** — no fine-tuning, no weight access.

**Operator steal:**
1. Prefer **multi-turn behaviour presence** metrics over single-turn compliance ASR for deployment-relevant failures.
2. **Elicitation–plausibility trade-off is tunable** (β hyperparameter) — trace Pareto frontier, not one operating point.
3. **Authorized lab only** — behaviour descriptions can surface harmful content; no elicitation recipes in wiki.
4. **`AdrSkapars/bloom-wilt` HOLD** until SPDX — REFERENCE pattern steal only.

## Snippets

> Methods like BLOOM lack optimisation pressure … their hit rate remains low. [Source: arXiv 2608.31105 §1, paraphrase]
