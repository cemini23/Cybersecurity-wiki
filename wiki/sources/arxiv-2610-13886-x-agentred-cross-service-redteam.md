---
title: "X-AgentRed: red-teaming personal agents in evolving multi-service ecosystems"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.13886, k423]
related:
  - concepts/cross-service-agent-compositional-harm.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/black-box-agentic-redteam-taxonomy.md
  - concepts/agentxploit-repository-runtime-red-teaming.md
  - concepts/task-conditioned-excess-authority.md
  - concepts/intent-governed-tool-authorization.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K423)"
---

## Relations

## Relations

- @concepts/cross-service-agent-compositional-harm.md
- @concepts/layer-paradigm-agent-red-teaming.md
- @concepts/black-box-agentic-redteam-taxonomy.md
- @concepts/agentxploit-repository-runtime-red-teaming.md
- @concepts/task-conditioned-excess-authority.md
- @concepts/intent-governed-tool-authorization.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | X-AgentRed: red-teaming personal agents in evolving multi-service ecosystems |
| arXiv | 2610.13886 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.13886-x-agentred-red-teaming-personal-agents-in-evolvi.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K423 — the harm is in the composition, not the call.** Personal agents connect to many services through tools, and when their **effects accumulate and interact across services**, a benign user request can produce a harmful outcome. Discovering those **cross-service paths** is hard because generation is biased toward tool combinations seen in training. **X-AgentRed** is a **self-evolving** red-teaming framework: it analyses each tool's **effects, potential harms, and execution preconditions** and builds a **directed graph** in which one tool's effects satisfy another's preconditions; it samples **recipes** from the graph, instantiates them as realistic scenarios, and uses **execution feedback** to diversify blocked paths by **tool substitution** and by **refining the preconditions** at failed steps.

Across **four frontier agentic models** it reaches **1.77x** the harmful-path rate of the **STAC** baseline and explores a more diverse tool set — **2.99x tool coverage** on average. Meta Research; **no public release** — this is attack tooling, **never clone**. Operator steal: the attack surface is the **graph of tool effects and preconditions**, not prompt-space patterns; a **feedback-driven, self-evolving** search finds novel cross-service chains that one-shot generation misses. Defend by bounding **combinations** — effect-aware, least-privilege tool gating — not by filtering each call. **No attack recipes or trajectories in wiki.**

## Snippets

> See arXiv 2610.13886 abstract. [Source: arXiv 2610.13886 (retrieved 2026-10-12)]
