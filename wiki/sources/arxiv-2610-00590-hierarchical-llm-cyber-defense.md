---
title: "Towards hierarchical cyber defense with large language models: from planning to execution"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.00590, k387]
related:
  - concepts/hierarchical-llm-cyber-defense-planner-executor.md
  - concepts/cyber-range-autonomous-incident-response-agents.md
  - concepts/sentinel-rl-soc-topological-reasoning.md
  - concepts/trident-agentic-drl-defense-redteam.md
maturity: draft
read_status: read
created: 2026-10-02
updated: 2026-10-02
phase_0_verdict: "REFERENCE 2026-10-02 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K387)"
---

## Relations

## Relations

- @concepts/hierarchical-llm-cyber-defense-planner-executor.md
- @concepts/cyber-range-autonomous-incident-response-agents.md
- @concepts/sentinel-rl-soc-topological-reasoning.md
- @concepts/trident-agentic-drl-defense-redteam.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Towards hierarchical cyber defense with large language models: from planning to execution |
| arXiv | 2610.00590 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.00590-towards-hierarchical-cyber-defense-with-large-la.pdf |
| Retrieved | 2026-10-02 |
| Read status | read (deep-read via grok CLI) |

## Narrative

**K387** — an RL cyber defender is tied to the network it trained on; hierarchical RL splits strategic targeting from tactical execution but still retrains per scale. The authors ask whether **frozen zero-shot LLMs** give retraining-free control, and what changes when LLM control moves from planning to execution. Controller-agnostic planner-executor: the planner picks a subnet every k=5 steps, the executor picks a primitive action (deploy decoy / isolate host / nothing). Three configurations — **RL+RL, LLM+RL, LLM+LLM** — over six models (3B→70B, two cyber-specialised) on Cyberwheel at 15 / 100 / 1,010 hosts. **Planner-only substitution gives limited gains** as the network grows; extending control to execution is what helps. Llama-3.3-70B LLM+LLM holds lateral movement to ~1% of steps and impact near zero at all three scales **with one frozen weight set**, where RL+RL degrades with scale (impact 1.22% → 5.10% → 15.20%) and is retrained per scale. Operator steal: hierarchical separation is not enough on its own — a weak executor caps the planner's benefit; test the **whole stack** at each scale, not the planner alone. Counter-example worth keeping: Trendyol-Cybersecurity-70B collapses at the large scale (compromise 14.45%, defense 12.95%) where the general-purpose 70B holds — **security specialisation is not a cross-scale guarantee**. No repo (© 2026 IEEE). **No attack payloads in wiki.**

## Snippets

> See arXiv 2610.00590 abstract. [Source: arXiv 2610.00590 (retrieved 2026-10-02)]
