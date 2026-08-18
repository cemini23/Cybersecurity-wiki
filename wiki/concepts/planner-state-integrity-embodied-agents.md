---
title: "Planner-state integrity for embodied agents (ESTI)"
type: concept
tags: [concept, methodology, agent-security, embodied, planner-integrity, k288]
keywords: [planner-state integrity, ESTI, schema-preserving false records, P-ASR, E-ASR, state producer]
related:
  - sources/arxiv-2608-16806-esti-state-semantic-injection.md
  - concepts/esti-state-semantic-injection-stub.md
  - entities/tools/esti-bench.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/agent-runtime-guardrails.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - concepts/mcp-security-posture.md
  - concepts/agent-data-injection-attacks.md
  - "@ccc-wiki/concepts/planner-state-semantic-integrity-attack-surface.md"
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemini-cybersec-mcp-tool-control.mdc (K288)"
---

## Relations

- @sources/arxiv-2608-16806-esti-state-semantic-injection.md
- @concepts/esti-state-semantic-injection-stub.md — pointer / CCC concurrent
- @entities/tools/esti-bench.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/agent-runtime-guardrails.md
- @concepts/physical-vs-content-danger-embodied-agents.md — content-danger vs physical consequence
- @concepts/mcp-security-posture.md — tool-return / env-state as untrusted planner input
- @concepts/agent-data-injection-attacks.md — ADI trusted vs untrusted data
- @ccc-wiki/concepts/planner-state-semantic-integrity-attack-surface.md — CCC K288 (same paper)

## Raw Concept

Is planner-facing environment state an integrity boundary? Schema-valid records can still be semantically false.

## Narrative

LLM-driven embodied agents treat scene objects, relations, affordances, task-stage, and execution feedback as **trusted facts**. ESTI shows that a single compromised state producer can inject **schema-preserving false records** that the planner adopts without any change to the user instruction, planner, or executor.

**Steal.**
1. Treat tool-return / env-state / execution-feedback as untrusted planner input (pairs ADI).
2. Schema-valid ≠ semantically true.
3. Report **P-ASR and E-ASR separately** — planning deviation is not physical success.
4. Conditional on write access to one producer; do not convert bench lifts into a probability of obtaining that access.
5. Runtime re-grounding was a small ablation effect vs carrier compatibility + representation consistency.

Authorized embodied/sim lab only. No injection payloads. **K288** is shared with CCC (cyber-primary).

## Snippets

> We study the complementary, conditional question after delivery: if exactly one planner-facing state producer is compromised, can a schema-preserving false record be adopted by the planner and realized as a targeted final-state consequence? [Source: arXiv 2608.16806 abstract]
