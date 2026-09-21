---
title: "Available Guardrails — certifying selective prediction (arXiv 2609.22048)"
type: source
tags: [source, arxiv, agent-security, audit, guardrails, eval, k354]
keywords: [2609.22048, selective prediction, certified precision, abstention, tool-calling gate, availability]
related:
  - concepts/certified-selective-prediction-guardrails.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/chain-of-self-questioning-selective-abstention.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-21
phase_0_verdict: "REFERENCE 2026-09-21 — deployment certification methodology; no clone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K354)"
---

## Relations

- @concepts/certified-selective-prediction-guardrails.md — K354 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Available Guardrails: Certifying Selective Prediction across ML Systems |
| arXiv | 2609.22048 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.22048-available-guardrails-certifying-selective-predic.pdf |
| Retrieved | 2026-09-21 |
| Read status | read (abstract + triage) |

## Narrative

**Available Guardrails** treats selective predictors (abstain unless trustworthy) as **certified safety gates** at target precision per reporting unit (tool, policy label, patient subgroup). The central deployment question is often **availability**: finite calibration data may fail to certify some units at all as gates become safer or finer-grained. The paper makes availability computable via exact-binomial inversion and partition selection dynamic programming, exposing trade-offs among safety, granularity, and served traffic. Applies across LLM tool-calling, moderation, clinical routing, and recommendation. **K354** is an **audit/deployment methodology steal** — pairs K321 guardrail construct validity and K343 CoSQ abstention. Report certified availability and partition planning, not global precision alone.

## Snippets

> A gate trustworthy when precision of served traffic is certified from data — a single global guarantee may hide unsafe subgroups. [Source: arXiv 2609.22048 abstract]

> Finite-sample estimation nearly erases population opportunity — recovery from finite data is the central challenge. [Source: arXiv 2609.22048 abstract]
