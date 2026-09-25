---
title: "Learning the cost of reliable inference"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.28322, k366]
related:
  - concepts/reliable-inference-procurement-routing.md
  - concepts/certified-selective-prediction-guardrails.md
maturity: validated
read_status: deep-read
created: 2026-09-24
updated: 2026-09-24
phase_0_verdict: "REFERENCE 2026-09-24 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K366)"
---

## Relations

- @concepts/reliable-inference-procurement-routing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Learning the cost of reliable inference |
| arXiv | 2609.28322 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.28322-learning-the-cost-of-reliable-inference.pdf |
| Retrieved | 2026-09-24 |
| Read status | deep-read (2026-09-25) |

## Narrative

**K366** (MPI-SWS) — **procurement platform** for LLM routing: **reverse second-price auction** with truthful cost bids; platform learns provider quality and routes to the **cheapest qualified** provider for a user’s quality threshold. Experiments (Llama/Qwen on math + QA benches): winner **pricing margin 10–71%** vs fixed per-token markets — quality tier and task shape matter.

Audit steal for **OpenRouter / routing marketplaces**: report **quality floor + $/task**, not flat token price alone (pairs K354). REFERENCE economics; not a security boundary.
## Snippets

> "The pricing margin of the most cost-competitive provider varies significantly—from 10% to 71%—depending on the task and quality threshold." [Source: arXiv 2609.28322 abstract]