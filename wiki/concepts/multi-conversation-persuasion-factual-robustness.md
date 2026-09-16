---
title: "Multi-conversation persuasion factual robustness (K342)"
type: concept
tags: [concept, agent-security, eval, persuasion, multi-turn, lab-only, k342]
keywords: [2609.16777, persuasion attacks, refusal inertia, factual robustness, multi-turn eval]
related:
  - sources/arxiv-2609-16777-multi-conversation-persuasion-robustness.md
  - concepts/psychological-multiturn-jailbreaks.md
  - concepts/evoflint-multi-turn-redteam-atlas.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-09-16
updated: 2026-09-16
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K342)"
---

## Relations

- @sources/arxiv-2609-16777-multi-conversation-persuasion-robustness.md — Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion (2609.16777)

## Raw Concept

Question: **Multi-conversation persuasion factual robustness** — what should operators steal from this paper?

## Narrative

Persuasion benchmarks that keep **full conversation history** can inflate robustness via **refusal inertia** — an initial refusal propagates even when later turns supply misinformation pressure. **K342** introduces **multi-conversation persuasion** eval to measure factual robustness without that artifact. **Lab eval only** — no persuasion recipes in wiki (pairs K302 PsychJail pattern). Report per-turn and cross-conversation metrics separately.

## Snippets

> Multi-conversation persuasion benchmark addresses refusal-inertia bias in full-history red-teaming. [Source: arXiv 2609.16777 abstract]
