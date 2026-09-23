---
title: "Certified selective prediction guardrails (K354)"
type: concept
tags: [concept, agent-security, audit, guardrails, abstention, eval, k354]
keywords: [2609.22048, selective prediction, certified availability, abstention gate, tool-calling, partition planning]
related:
  - sources/arxiv-2609-22048-available-guardrails-selective-prediction.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/chain-of-self-questioning-selective-abstention.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - sources/arxiv-2609-01519-guardrail-construct-validity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/genai-access-control-policy-enforcement.md
maturity: draft
created: 2026-09-21
updated: 2026-09-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K354)"
---

## Relations

- @sources/arxiv-2609-22048-available-guardrails-selective-prediction.md — Available Guardrails (2609.22048)

## Raw Concept

Question: **Certified selective prediction guardrails** — what should operators steal from this paper?

## Narrative

Agent deployments increasingly use **selective predictors** — act only when prediction appears reliable (tool-call gates, moderation auto-block, clinical routing). **K354** adds **certified availability** as a first-class deployment metric: for each reporting unit (tool, category, subgroup), can finite calibration data support a target-precision certificate at all?

Audit steal:

- Report **per-unit certified availability**, not fleet-mean precision alone.
- Plan reporting partitions with explicit safety–granularity–traffic trade-offs.
- Separate **population-optimal** from **finite-sample** coverage — naive estimators can erase most gains.
- Pair with K321 construct validity before welfare/safety lift claims; verbalized abstention alone is not enforcement (K343/K314).

Audit-only this batch — no runtime precheck script.

## Snippets

> Certified availability determines when a safety gate can be certified, at what granularity, and over how much traffic. [Source: arXiv 2609.22048 abstract]
