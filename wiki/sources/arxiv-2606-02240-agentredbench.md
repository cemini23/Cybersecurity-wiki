---
title: "AgentRedBench — dynamic redteaming for SaaS-integrated LLM agents (arXiv:2606.02240)"
type: source
tags: [arxiv, agent-security, prompt-injection, red-team, benchmark, saas-integration, research-paper]
keywords: [agentredbench, agentredguard, indirect prompt injection, saas integration, underspecified authorization, stackone]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - entities/tools/agentredguard.md
  - entities/tools/airguard.md
  - entities/tools/defenseclaw.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
maturity: draft
read_status: read
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @concepts/agent-runtime-guardrails.md — integration read/write gap + dynamic redteam benchmark
- @concepts/llm-adversarial-fuzzing.md — dynamic LLM-driven attack generation vs static templates
- @concepts/llm-pentest-automation.md — enterprise agent copilot threat model
- @entities/tools/airguard.md — runtime authority guard comparison
- @entities/tools/defenseclaw.md — enterprise governance complement
- @sources/arxiv-2605-28914-airguard-guarding-agent-actions.md — authority confusion framing
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface eval hygiene

## Raw Concept

- **Title**: AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations
- **Authors**: Hiskias Dingeto, Will Leeney (StackOne)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2606.02240-agentredbench-dynamic-redteaming-and-integration.pdf`
- **URL**: https://arxiv.org/abs/2606.02240
- **Retrieved**: 2026-06-02
- **Read-status**: read

## Narrative

**AGENTREDBENCH**: 215 subtle **underspecified-authorization** scenarios across **24 enterprise integrations** (Gmail, Salesforce, Jira, etc.), five attack types, dynamic LLM redteaming (not fixed payload replay). Eight-model panel no-guard ASR **32–81%**. **AGENTREDGUARD** (trained on adversarial tool-response content) cuts panel ASR **69.9% → 2.4%** at **0.37% FPR**, beating Llama Guard / PromptGuard 2 / ProtectAI on integration-diverse holdouts.

Threat model: adversarial content via **read** on one integration, harm via **write** on another — production indirect prompt injection. Canonical scenarios released via maintainer-mediated channel (not full public scenario set) `[TENTATIVE]` for reproducibility claims.

**Reference tier** for wiki — benchmark + guard model; evaluate before adoption vs AIRGuard/DefenseClaw stack.

## Snippets

> "Every integration the agent reads from is a channel an external party can write into; every integration the agent can act through is a channel an attacker can hijack."

> "Existing guards … trained on chat-style dialogue, they are [blind to] tool-response content."
