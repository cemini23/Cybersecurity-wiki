---
title: Physical vs content danger — embodied / tool-acting agent safety
type: concept
tags: [concept, agent-safety, embodied, physical-danger, probing]
keywords: [physical danger, content danger, prism, before-execute monitor, psb-1k]
related:
  - sources/arxiv-2607-15218-prism-physical-vs-content-danger.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- @sources/arxiv-2607-15218-prism-physical-vs-content-danger.md — PRISM paper
- @concepts/cage-1-enterprise-agent-governance-eval.md — Prebind before binding actions
- @concepts/vulnerability-concept-graph-production-agent-red-teaming.md — enabling conditions for unsafe trajectories

## Raw Concept

Text moderation answers “is this wording harmful?” Embodied/tool agents also need “is this plan physically/causally unsafe if executed?”

## Narrative

| Class | Example | Visible in text? |
|-------|---------|------------------|
| **Content danger (CD)** | “ignite the curtain” | Yes |
| **Physical danger (PD)** | “microwave an egg” / metal in microwave | No — causality |

PRISM shows CD/PD are separable in hidden states and that a cheap probe beats LLM judges on false-positive rate for safe tasks. [CONFIRMED — abstract]

### Cemini pattern

For any agent that binds real actions (shell, Discord, robot, browser click):

1. Text guardrail (CD)
2. **Before-execute** causal/physical/policy monitor (PD) — Prebind sibling
3. Log enabling condition when denying

## Snippets

See source.
