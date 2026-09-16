---
title: "When should LLMs abstain? Chain-of-self-questioning for selective risk control (arXiv 2609.17516)"
type: source
tags: [source, arxiv, agent-security, abstention, safety, eval, k343]
keywords: [2609.17516, CoSQ, abstention, selective risk control, TruthfulQA, grounded commitment]
related:
  - concepts/chain-of-self-questioning-selective-abstention.md
maturity: draft
read_status: read
created: 2026-09-16
updated: 2026-09-16
phase_0_verdict: "REFERENCE 2026-09-16 — selective abstention eval; not a production safety certificate alone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K343)"
---

## Relations

- @concepts/chain-of-self-questioning-selective-abstention.md — K343 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control |
| arXiv | 2609.17516 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.17516-when-should-llms-abstain-chain-of-self-questioni.pdf |
| Retrieved | 2026-09-16 |
| Read status | read (abstract + triage) |

## Narrative

Models may answer fluently when factual support is weak. **K343 (Chain-of-Self-Questioning, CoSQ)** makes answer commitment conditional on explicit self-assessment of information sufficiency — a **prompt-only selective risk control** framework. Grounded-CoSQ can reduce unconditional wrong answers at calibrated abstention thresholds. **Steal-from:** pair abstention policies with **machine-checkable withhold contracts** (K276) — verbalized self-questioning is not enforcement alone (pairs K314).

## Snippets

> CoSQ defers answers until self-assessed information sufficiency; Grounded-CoSQ reduces wrong answers at high abstention thresholds. [Source: arXiv 2609.17516 abstract]
