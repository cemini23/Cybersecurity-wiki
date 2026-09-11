---
title: "BlueSTAR tiered agentic cyber defense (K330)"
type: concept
tags: [concept, agent-security, blue-team, soc, architecture, k330]
keywords: [2609.11852, BlueSTAR, autonomous cyber defense, tiered agents, SOC telemetry]
related:
  - sources/arxiv-2609-11852-bluestar-tiered-cyber-defense.md
  - concepts/security-agent-authority-auditability-slr.md
  - concepts/sentinel-rl-soc-topological-reasoning.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K330)"
---

## Relations

- @sources/arxiv-2609-11852-bluestar-tiered-cyber-defense.md — BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense (2609.11852)

## Raw Concept

Question: **BlueSTAR tiered agentic cyber defense** — what should operators steal from this paper?

## Narrative

Automated attacks compress defender reaction time; LLMs can correlate heterogeneous evidence but raw security telemetry exceeds context and ingestion rates. **K330 (BlueSTAR)** proposes a **tiered agentic architecture** for autonomous cyber defense: specialized tiers for ingestion, reasoning, and action with bounded authority. **Audit steal:** demand auditable trajectories and bounded tool grants — terminal alert closure is not proof of faithful evidence use (pairs K315). REFERENCE only; no prod auto-contain without HITL.

## Snippets

> Tiered LLM agent architecture for autonomous cyber defense over high-volume security telemetry. [Source: arXiv 2609.11852 abstract]
