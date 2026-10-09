---
title: "background-agents — sandboxed background coding agents"
type: entity
tags: [entity, tool, agent-security]
keywords: [github.com/ColeMurray/background-agents, K285-c]
related:
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/agentic-containment-principles.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "EXTRACT K285 — MIT, sandboxed delegation. Needs a container runtime; single-tenant only. No clone this batch."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K285-c)"
---

## Relations

- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md — K408-K417 ingest / 2026-10-09
- @concepts/coding-agent-supply-chain-install-gap.md — K408-K417 ingest / 2026-10-09
- @concepts/agentic-containment-principles.md — K408-K417 ingest / 2026-10-09

## Raw Concept

background-agents — sandboxed background coding agents — evaluated from the inbound routed brief (github.com/ColeMurray/background-agents).

## Narrative

**MIT, 3,345 stars.** An open-source **background agents** coding system: **sandboxed `spawn-child` delegation** plus **managed skills**. Already an Extract in K283 for GuruWatcher; recorded here for the **local lab**.

**Play:** a **background binary-auditing agent** that runs in an isolated container without blocking the operator. **Constraint:** needs a container runtime (Modal / Daytona / Docker) and enforces a **single-tenant** organizational boundary — keep it inside the lab. Pairs the K421 containment line: delegation is only safe when the child is sandboxed and bounded.

## Snippets

> Verified from the routed brief, not a first-hand repo audit. [Source: `briefs/` inbound route (2026-10-09)]
