---
title: StepGuard (AgentDoG)
type: entity
tags: [entity, tool, agent-security, guardrail, k307]
keywords: [StepGuard, StepGen, Balance-GRPO, zheng977, ninty-seven, agent guard, EMNLP 2026]
related:
  - sources/arxiv-2608-24777-stepguard.md
  - concepts/step-level-agent-guardrails.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
phase_0_verdict: "CONDITIONAL-GO 2026-08-26 — github.com/zheng977/StepGuard ~6MB, LICENSE missing at hunt; re-check before clone. HF: ninty-seven/StepGuard. Runtime wont_wire until operator OK + SPDX."
wire_status: wont_wire
wire_target: "REFERENCE eval only after LICENSE; no default Cursor MCP"
---

## Relations

- @sources/arxiv-2608-24777-stepguard.md
- @concepts/step-level-agent-guardrails.md

## Raw Concept

StepGuard is a **4B step-level guard model** (Shanghai AI Lab AgentDoG team) for pre-execution tool-action checking and post-hoc trajectory audit. Training uses StepGen synthetic data + Balance-GRPO safety–utility balancing.

## Narrative

| Field | Value |
|-------|-------|
| Repo | `https://github.com/zheng977/StepGuard` |
| Model | `https://huggingface.co/ninty-seven/StepGuard` |
| License | **NOASSERTION** — no LICENSE file in repo at hunt 2026-08-26 |
| Size | ~6 MB repo (code + assets) |
| Verdict | **CONDITIONAL-GO** — methodology steal + optional REFERENCE clone after LICENSE verified; **no weight download** in wiki ingest; **wont_wire** as default harness MCP |

**Adoption gate:** verify SPDX in repo root before `.local/adopts/StepGuard` shallow clone. Do not curl|bash install scripts. Lab eval only on owned agent harnesses.

## Snippets

> StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. [Source: arXiv 2608.24777 abstract — verify locally before citing in engagements]
