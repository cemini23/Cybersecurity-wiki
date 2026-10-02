---
title: "Hierarchical LLM cyber defense — planner vs executor (K387)"
type: concept
tags: [concept, agent-security, k387]
keywords: [2610.00590, K387]
related:
  - sources/arxiv-2610-00590-hierarchical-llm-cyber-defense.md
  - concepts/cyber-range-autonomous-incident-response-agents.md
  - concepts/sentinel-rl-soc-topological-reasoning.md
  - concepts/trident-agentic-drl-defense-redteam.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K387)"
---

## Relations

- @sources/arxiv-2610-00590-hierarchical-llm-cyber-defense.md
- @concepts/cyber-range-autonomous-incident-response-agents.md
- @concepts/sentinel-rl-soc-topological-reasoning.md
- @concepts/trident-agentic-drl-defense-redteam.md

## Raw Concept

Question: **Hierarchical LLM cyber defense — planner vs executor** — operator steal from arXiv 2610.00590?

## Narrative

Split an autonomous defender into a **planner** (which subnet to defend) and an **executor** (which action to take), then swap RL or a frozen LLM into each slot. The finding to carry: **replacing only the planner buys little**; the gain comes when the executor is strong too. Measure the whole stack across network scales — a controller that looks good at 15 hosts can fail at 1,010. Keep the **specialisation trap** in view: a cyber-tuned model can beat a general model at one scale and collapse at another. Defense-side lab only; no attack recipes.

## Snippets

> See arXiv 2610.00590 abstract. [Source: arXiv 2610.00590 (retrieved 2026-10-02)]
