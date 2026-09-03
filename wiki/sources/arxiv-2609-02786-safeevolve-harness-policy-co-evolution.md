---
title: "SafeEvolve — harness-policy co-evolution for agent safety (arXiv 2609.02786)"
type: source
tags: [source, arxiv, agent-security, harness, safety, k324]
keywords: [2609.02786, SafeEvolve, harness-policy co-evolution, skill evolution, agent safety alignment]
related:
  - concepts/safeevolve-harness-policy-co-evolution.md
maturity: draft
read_status: read
created: 2026-09-03
updated: 2026-09-03
phase_0_verdict: "REFERENCE 2026-09-03 — no unattended prod harness/skill auto-evolve; HITL required."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K324)"
---

## Relations

- @concepts/safeevolve-harness-policy-co-evolution.md — defensive co-evolution pattern

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment |
| arXiv | 2609.02786 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.02786-safeevolve-harness-policy-co-evolution-from-agen.pdf |
| Retrieved | 2026-09-03 |
| Read status | read (abstract + method) |

## Narrative

**SafeEvolve** loops **on-policy trajectory safety evidence** into **bounded harness updates** (safety prompt + hierarchical skills) and **policy SFT-RL** (harness-use SFT then harness-augmented RL with verifier-decomposed rewards). Reports stronger safety–utility tradeoff on agentic safety benches (e.g. 3× ASR reduction on AgentDojo for Qwen3.5-4B with utility lift). **Defensive pattern only** — pairs skill misevolution gates; never unattended auto-evolve prod `.cursor/skills`.

## Snippets

> Harness-side updates are component-level, auditable, and reversible; policy-side uses two-stage SFT-RL with verifier-decomposed rewards. [Source: arXiv 2609.02786 abstract, paraphrase]
