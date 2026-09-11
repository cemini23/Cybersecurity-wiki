---
title: "Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence (arXiv 2609.05385)"
type: source
tags: [source, arxiv, agent-security, interpretability, audit, k337]
keywords: [2609.05385, necessary sufficient explanations, behavioural evidence, agent monitoring]
related:
  - concepts/llm-explanation-necessary-sufficient-audit.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — explanation behavioural audit; no enforcement claims from NL alone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K337)"
---

## Relations

- @concepts/llm-explanation-necessary-sufficient-audit.md — K337 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence |
| arXiv | 2609.05385 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.05385-necessary-or-sufficient-evaluating-llm-explanati.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

Operators may rely on LLM **named-factor explanations** for monitoring and escalation. **K337** tests **necessity** (changing a factor changes output) vs **sufficiency** (factor alone drives output) with behavioural counterfactuals. Explanations often fail both tests — pairs **K290 CHIVE** and **K308 decorative CoT**: explanation text is not evidence without behavioural verification.

## Snippets

> Behavioural counterfactual tests distinguish necessary vs sufficient LLM explanation factors for agent decisions. [Source: arXiv 2609.05385 abstract]
