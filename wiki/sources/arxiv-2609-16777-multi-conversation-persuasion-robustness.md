---
title: "Benchmarking factual robustness via multi-conversation persuasion (arXiv 2609.16777)"
type: source
tags: [source, arxiv, agent-security, eval, persuasion, multi-turn, lab-only, k342]
keywords: [2609.16777, persuasion attacks, refusal inertia, factual robustness, multi-turn eval]
related:
  - concepts/multi-conversation-persuasion-factual-robustness.md
maturity: draft
read_status: read
created: 2026-09-16
updated: 2026-09-16
phase_0_verdict: "REFERENCE 2026-09-16 — persuasion eval methodology; authorized lab only; no wiki payloads."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K342)"
---

## Relations

- @concepts/multi-conversation-persuasion-factual-robustness.md — K342 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion |
| arXiv | 2609.16777 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.16777-benchmarking-factual-robustness-of-llms-via-mult.pdf |
| Retrieved | 2026-09-16 |
| Read status | read (abstract + triage) |

## Narrative

Persuasion benchmarks that keep **full conversation history** can inflate robustness via **refusal inertia** — an initial refusal propagates even when later turns supply misinformation pressure. **K342** introduces **multi-conversation persuasion** eval to measure factual robustness without that artifact. **Lab eval only** — no persuasion recipes in wiki (pairs K302 PsychJail pattern). Report per-turn and cross-conversation metrics separately.

## Snippets

> Multi-conversation persuasion benchmark addresses refusal-inertia bias in full-history red-teaming. [Source: arXiv 2609.16777 abstract]
