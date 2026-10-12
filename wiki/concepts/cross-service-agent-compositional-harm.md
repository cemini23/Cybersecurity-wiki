---
title: "Harm emerges from the composition of benign tool calls (K423)"
type: concept
tags: [concept, agent-security, k423]
keywords: [2610.13886, K423]
related:
  - sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/black-box-agentic-redteam-taxonomy.md
  - concepts/agentxploit-repository-runtime-red-teaming.md
  - concepts/task-conditioned-excess-authority.md
  - concepts/intent-governed-tool-authorization.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K423)"
---

## Relations

- @sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md
- @concepts/layer-paradigm-agent-red-teaming.md
- @concepts/black-box-agentic-redteam-taxonomy.md
- @concepts/agentxploit-repository-runtime-red-teaming.md
- @concepts/task-conditioned-excess-authority.md
- @concepts/intent-governed-tool-authorization.md

## Raw Concept

Question: **Harm emerges from the composition of benign tool calls** — operator steal from arXiv 2610.13886?

## Narrative

A personal agent invokes individually-benign tools across services, and their **effects accumulate and interact** — information, permissions, and state propagate — so a benign request can end in a harmful outcome. That makes the unit of risk the **combination**, not the call, and it means a per-call filter is looking in the wrong place.

X-AgentRed operationalises the search over combinations: build a **directed graph of tool effects and preconditions** (one tool's effect can enable another), sample recipes, instantiate scenarios, and **self-improve from execution feedback** by substituting tools and refining preconditions at blocked steps. It achieves **1.77x** the harmful-path rate and **2.99x** tool coverage of a strong baseline across four frontier models. `github.com/CHATS-lab/ToolShield` and `github.com/ZJU-LLM-Safety/TRACE` are cited **prior work**, not a release of this system.

The operator consequence: **defend the composition.** Effect-aware, least-privilege tool gating — what a *sequence* of authenticated calls may collectively do — is the lever, not prompt filtering of single messages. Pairs K327 (black-box agentic red-team taxonomy), K375 (AgentXploit repo-to-runtime), and the intent-governed tool authorization line. Defensive lab only; no attack recipes in wiki.

## Snippets

> See arXiv 2610.13886 abstract. [Source: arXiv 2610.13886 (retrieved 2026-10-12)]
