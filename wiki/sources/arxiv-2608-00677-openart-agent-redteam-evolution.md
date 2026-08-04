---
title: OpenART agent red-teaming via environment evolution (arXiv 2608.00677)
type: source
tags: [source, arxiv, agent-security, red-teaming, mcp, lab]
keywords: [2608.00677, OpenART, EMHA, agent red team, environment evolution]
related:
  - concepts/openart-environment-evolution-agent-redteam.md
  - entities/tools/openart.md
  - concepts/gpt-red-self-play-red-teaming.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/cyber-capable-agent-evaluation-containment.md
  - concepts/ai-for-cybersecurity.md
  - concepts/red-team-operations.md
maturity: draft
read_status: read
created: 2026-08-04
updated: 2026-08-04
phase_0_verdict: "CONDITIONAL-GO 2026-08-04 — AGPL-3.0; ~19MB; lab red-team only"
wire_status: deferred
wire_target: "lab sandbox only — AGPL; no host wire"
---

**Briefs:** `briefs/2026-08-04_k237-openart-prod.md`

## Relations

- @concepts/openart-environment-evolution-agent-redteam.md
- @entities/tools/openart.md
- @concepts/gpt-red-self-play-red-teaming.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/cyber-capable-agent-evaluation-containment.md
- @concepts/ai-for-cybersecurity.md
- @concepts/red-team-operations.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution |
| Authors | Chen, Wang, Wang, Liu, Li, Teng, et al. (Fudan / Shanghai AI Lab / XSafeAI) |
| arXiv | 2608.00677 |
| Code | https://github.com/AI45Lab/OpenART (AGPL-3.0) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.00677-openart-scaling-agent-red-teaming-via-open-ended.pdf` |
| Retrieved | 2026-08-04 |

## Narrative

Open-ended **arena** for agent red teaming by evolving environments (not just prompts). >10K validated stateful scenarios / 50 domains / >500K tools·MCPs·skills; median ~97 tool calls; unified eval across 75 agent–model configs. **EMHA** (Evolutionary Markov Hypergraph Attack) evolves environment state under fixed objectives/safety contracts. Surfaces long-horizon cumulative risks static benches miss (MCP capability rebinding, provenance composition, plan–referent drift, etc.). [CONFIRMED abstract + README]

### Steal

1. Red-team agents in **evolving stateful environments**, not only static prompts
2. Keep task objectives + safety contracts fixed while mutating environment state
3. Lab-only: AGPL + dual-use — owned sandboxes; no LIVE targets

## Snippets

> "Throughout evolution, task objectives and safety contracts remain fixed while only the environment state changes."
[Source: arXiv 2608.00677]
