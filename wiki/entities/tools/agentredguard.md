---
title: "AgentRedGuard — integration-aware guard for SaaS LLM agents (Reference)"
type: entity
tags: [tool, ai-security, agent-guard, benchmark, saas, reference]
keywords: [agentredguard, agentredbench, stackone, indirect prompt injection, tool-response guard]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/airguard.md
  - entities/tools/defenseclaw.md
  - entities/tools/seclaw-eval.md
  - sources/arxiv-2606-02240-agentredbench.md
maturity: draft
created: 2026-06-02
updated: 2026-06-04
phase_0_verdict: "Reference 2026-06-02 — paper-reported guard; compare vs AIRGuard on integration-diverse lab replay before adopt."
---

# AgentRedGuard — integration-aware guard for SaaS LLM agents

## Relations

- @concepts/agent-runtime-guardrails.md — AGENTREDBENCH + AGENTREDGUARD in SaaS integration threat model
- @concepts/llm-adversarial-fuzzing.md — dynamic redteam benchmark vs static jailbreak fuzzing
- @entities/tools/airguard.md — runtime authority control (complementary evaluation target)
- @entities/tools/defenseclaw.md — enterprise-scale governance
- @sources/arxiv-2606-02240-agentredbench.md — paper provenance

## Raw Concept

Ingested from arXiv:2606.02240 (2026-06-02 daily digest). Guard model shipped with **AgentRedBench** (StackOne). Trained on adversarial **tool-response** content across enterprise integrations.

## Narrative

Addresses the gap where chat-trained guards miss **indirect prompt injection** delivered through Gmail/Slack/Jira/etc. tool returns. Paper claims ASR reduction 69.9% → 2.4% at 0.37% FPR on eight-model panel vs open-source baselines.

**Import boundary**: Reference until Phase-0 lab replay on your MCP/SaaS stack; scenarios not fully public (maintainer-mediated eval channel).

## Snippets

Paper-reported panel ASR: 32% (Claude Sonnet 4.6) to 81% (Gemini 3 Flash) without guard. `[TENTATIVE]` — re-verify on current model IDs.

## Dead Ends

- **Chat-only guards for agent copilots** — paper shows large blind spot on tool-response injections.
- **Single-integration benchmarks** — under-measures production multi-integration read→write chains.
