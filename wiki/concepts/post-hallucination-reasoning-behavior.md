---
title: "Does the model correct or commit? (K411)"
type: concept
tags: [concept, agent-security, k411]
keywords: [2610.10455, K411]
related:
  - sources/arxiv-2610-10455-phrbench-post-hallucination-reasoning.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/llm-explanation-necessary-sufficient-audit.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K411)"
---

## Relations

- @sources/arxiv-2610-10455-phrbench-post-hallucination-reasoning.md
- @concepts/chain-of-thought-decorative-reasoning-audit.md
- @concepts/llm-explanation-necessary-sufficient-audit.md
- @concepts/measurement-integrity-mcp-security-eval.md

## Raw Concept

Question: **Does the model correct or commit?** — operator steal from arXiv 2610.10455?

## Narrative

A hallucination is not a single wrong token — it is a premise the model then reasons from. PHRBench measures the aftermath: given a hallucinated premise, does the model **correct** or **commit**? Committing is the norm. Hallucinated premises cost **7.7 pp** of accuracy on average, more for **proprietary** models (11.0%) than open ones (6.1%), and **correction is rare** — only 11 of 18 models produce insightful trajectories above 10%.

The discriminating signal is **belief-update frequency**, not length: insightful paths run **0.68 vs 0.24** and carry ~35 more reasoning words, so a model that reasons *longer* around a wrong premise looks busy without being right. And not all bad premises are equal — a fluent **pseudoscientific** framing costs only **1.8 pp** while **state distortion** costs **9.4**. Operator rule: when auditing reasoning, ask whether the model **revises under contradiction** — pairs the K308 finding that chain-of-thought is not evidence.

## Snippets

> See arXiv 2610.10455 abstract. [Source: arXiv 2610.10455 (retrieved 2026-10-09)]
