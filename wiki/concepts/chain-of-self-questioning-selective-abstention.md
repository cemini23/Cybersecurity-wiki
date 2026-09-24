---
title: "Chain-of-self-questioning selective abstention (K343)"
type: concept
tags: [concept, agent-security, abstention, safety, eval, k343]
keywords: [2609.17516, CoSQ, abstention, selective risk control, TruthfulQA, grounded commitment]
related:
  - sources/arxiv-2609-17516-chain-of-self-questioning-abstention.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/conditional-safety-adapter-routing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/compliance-detector-rule-blindness.md
  - concepts/certified-selective-prediction-guardrails.md
  - sources/arxiv-2609-22048-available-guardrails-selective-prediction.md
  - concepts/reliable-inference-procurement-routing.md
maturity: draft
created: 2026-09-16
updated: 2026-09-16
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K343)"
---

## Relations

- @sources/arxiv-2609-17516-chain-of-self-questioning-abstention.md — When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control (2609.17516)

## Raw Concept

Question: **Chain-of-self-questioning selective abstention** — what should operators steal from this paper?

## Narrative

Models may answer fluently when factual support is weak. **K343 (Chain-of-Self-Questioning, CoSQ)** makes answer commitment conditional on explicit self-assessment of information sufficiency — a **prompt-only selective risk control** framework. Grounded-CoSQ can reduce unconditional wrong answers at calibrated abstention thresholds. **Steal-from:** pair abstention policies with **machine-checkable withhold contracts** (K276) — verbalized self-questioning is not enforcement alone (pairs K314).

## Snippets

> CoSQ defers answers until self-assessed information sufficiency; Grounded-CoSQ reduces wrong answers at high abstention thresholds. [Source: arXiv 2609.17516 abstract]
