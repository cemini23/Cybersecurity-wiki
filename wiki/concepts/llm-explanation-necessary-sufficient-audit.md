---
title: "LLM explanation necessity vs sufficiency audit (K337)"
type: concept
tags: [concept, agent-security, interpretability, audit, k337]
keywords: [2609.05385, necessary sufficient explanations, behavioural evidence, agent monitoring]
related:
  - sources/arxiv-2609-05385-llm-explanation-necessary-sufficient.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/compliance-detector-rule-blindness.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K337)"
---

## Relations

- @sources/arxiv-2609-05385-llm-explanation-necessary-sufficient.md — Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence (2609.05385)

## Raw Concept

Question: **LLM explanation necessity vs sufficiency audit** — what should operators steal from this paper?

## Narrative

Operators may rely on LLM **named-factor explanations** for monitoring and escalation. **K337** tests **necessity** (changing a factor changes output) vs **sufficiency** (factor alone drives output) with behavioural counterfactuals. Explanations often fail both tests — pairs **K290 CHIVE** and **K308 decorative CoT**: explanation text is not evidence without behavioural verification.

## Snippets

> Behavioural counterfactual tests distinguish necessary vs sufficient LLM explanation factors for agent decisions. [Source: arXiv 2609.05385 abstract]
