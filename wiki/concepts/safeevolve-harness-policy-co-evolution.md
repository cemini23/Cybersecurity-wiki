---
title: "SafeEvolve — harness-policy co-evolution for agent safety (K324)"
type: concept
tags: [concept, agent-security, harness, safety, skill-evolution, k324]
keywords: [SafeEvolve, harness-policy co-evolution, reversible harness artifacts, verifier rewards, skill misevolution defense]
related:
  - sources/arxiv-2609-02786-safeevolve-harness-policy-co-evolution.md
  - concepts/skill-misevolution.md
  - concepts/safety-harness-evolution.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/evoskill-injection-self-evolving-agents.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-09-03
updated: 2026-09-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K324)"
---

## Relations

- @sources/arxiv-2609-02786-safeevolve-harness-policy-co-evolution.md — SafeEvolve (2609.02786)
- @concepts/skill-misevolution.md — govern authoring / retrieval / execution gates

## Raw Concept

Question: **how do you evolve agent safety without harness-only or policy-only isolation?**

## Narrative

Agent safety depends on **both** the base model and the **harness** (prompts, skills, tool policy). **K324 (SafeEvolve)** proposes **experience-driven co-evolution**: trajectory-level safety evidence → **bounded, reversible harness component updates** + **policy training** that learns to use evolved harness artifacts under **verifier-decomposed RL rewards**.

**Harness steal:** component-level edits (not whole prompt dumps), auditable artifacts, rollback path. **Policy steal:** harness-use SFT bootstraps compliance; RL shapes multi-step safe exploration.

**Critical guardrail (wiki policy):** co-evolution is a **lab/defensive pattern** — **HITL before any prod harness/skill write**; never unattended auto-evolve `.cursor/skills` (pairs K237 misevolution). **Dual-ID:** Cybersec **K324 SafeEvolve** ≠ CCC **K324 RedEvoAgent** validation ratchet.

## Snippets

> SafeEvolve achieves a 3× ASR reduction on AgentDojo while improving benign utility for Qwen3.5-4B (paper claim). [Source: arXiv 2609.02786 abstract]
