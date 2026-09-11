---
title: "BlueSTAR — tiered agentic architecture for autonomous cyber defense (arXiv 2609.11852)"
type: source
tags: [source, arxiv, agent-security, blue-team, soc, architecture, k330]
keywords: [2609.11852, BlueSTAR, autonomous cyber defense, tiered agents, SOC telemetry]
related:
  - concepts/bluestar-tiered-agentic-cyber-defense.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — tiered defensive agent architecture; no clone until SPDX verified."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K330)"
---

## Relations

- @concepts/bluestar-tiered-agentic-cyber-defense.md — K330 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense |
| arXiv | 2609.11852 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.11852-bluestar-tiered-agentic-architecture-for-autonom.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

Automated attacks compress defender reaction time; LLMs can correlate heterogeneous evidence but raw security telemetry exceeds context and ingestion rates. **K330 (BlueSTAR)** proposes a **tiered agentic architecture** for autonomous cyber defense: specialized tiers for ingestion, reasoning, and action with bounded authority. **Audit steal:** demand auditable trajectories and bounded tool grants — terminal alert closure is not proof of faithful evidence use (pairs K315). REFERENCE only; no prod auto-contain without HITL.

## Snippets

> Tiered LLM agent architecture for autonomous cyber defense over high-volume security telemetry. [Source: arXiv 2609.11852 abstract]
