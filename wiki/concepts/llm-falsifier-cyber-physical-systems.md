---
title: "LLM-Falsifier for cyber-physical systems (K350)"
type: concept
tags: [concept, ot, cyber-physical, eval, lab, k350]
keywords: [2609.20752, LLM-Falsifier, STL falsification, ARCH-COMP, robustness optimization, CPS]
related:
  - sources/arxiv-2609-20752-llm-falsifier-cyber-physical-systems.md
  - concepts/zero-trust-mission-critical-robotic-fleets.md
maturity: draft
created: 2026-09-20
updated: 2026-09-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K350)"
---

## Relations

- @sources/arxiv-2609-20752-llm-falsifier-cyber-physical-systems.md — LLM-Falsifier (2609.20752)

## Raw Concept

Question: **LLM-Falsifier for CPS** — what should OT/security operators steal?

## Narrative

**LLM-Falsifier** applies iterative LLM prompting to **STL falsification** — searching for counterexamples by minimizing robustness degree with semantic feedback (I/O names, trajectories, critical-time witnesses). Report **simulation budget**, spec coverage, and comparator tools — not a single win rate alone.

**Authorized OT/CPS lab only** on owned plants or written engagement scope. Pairs K339 zero-trust robotic fleets. Counterexamples inform safety testing; they are **not** permission to attack third-party infrastructure. No plant-specific attack recipes in wiki.

## Snippets

> LLM-driven falsification can reduce simulations needed for STL counterexamples when semantic feedback is available. [Source: arXiv 2609.20752 abstract]
