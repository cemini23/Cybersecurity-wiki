---
title: "Constrained-action SOC remediation (K410)"
type: concept
tags: [concept, agent-security, k410]
keywords: [2610.09906, K410]
related:
  - sources/arxiv-2610-09906-constrained-action-ai-remediation-siem.md
  - concepts/step-level-agent-guardrails.md
  - concepts/non-decaying-loop-safety-state.md
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K410)"
---

## Relations

- @sources/arxiv-2610-09906-constrained-action-ai-remediation-siem.md
- @concepts/step-level-agent-guardrails.md
- @concepts/non-decaying-loop-safety-state.md
- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md

## Raw Concept

Question: **Constrained-action SOC remediation** — operator steal from arXiv 2610.09906?

## Narrative

Let an LLM triage SIEM/XDR alerts, but never let it act unconstrained: put a **rail** between the model and the effect so it can only emit schema-valid remediation. Measured on 200 injection variants, that rail took recall from **25.0% to 94.5%** at 0.1% false-positive rate — but cost **14.14 s** median against a 0.31 s bare call.

The design lesson is the **cascade**: a deterministic **Tier-0 gate** in front gives 58% recall at **0.00% FPR in 0.18 s with no LLM calls at all**, and catches content the LLM rail misses. Then the rail, then **manual approval on every action** — in live testing 41 action records were produced from 54 injected alerts and **none were dispatched**. Two rules generalise: **order the cheap deterministic check first**, and **validate the arguments, not just the intent** (the schema check rejected an action whose target came from attacker-controlled metadata).

## Snippets

> See arXiv 2610.09906 abstract. [Source: arXiv 2610.09906 (retrieved 2026-10-09)]
