---
title: "SENTINEL-RL SOC topological reasoning offload (K336)"
type: concept
tags: [concept, soc, blue-team, agent, graph, k336]
keywords: [2609.04159, SENTINEL-RL, SOC, authentication graph, containment, RL]
related:
  - sources/arxiv-2609-04159-sentinel-rl-soc-topology.md
  - concepts/bluestar-tiered-agentic-cyber-defense.md
  - concepts/security-agent-authority-auditability-slr.md
  - concepts/soc-operations.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K336)"
---

## Relations

- @sources/arxiv-2609-04159-sentinel-rl-soc-topology.md — SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center (2609.04159)

## Raw Concept

Question: **SENTINEL-RL SOC topological reasoning offload** — what should operators steal from this paper?

## Narrative

SOC-scale authentication graphs exceed LLM context windows, and free-form containment recommendations may be **topologically inconsistent**. **K336 (SENTINEL-RL)** decouples **topological reasoning** (graph algorithms + RL) from LLM narrative/analysis layers. **Steal-from:** enforce graph-feasible containment actions outside the LLM; treat LLM output as untrusted planner input (pairs K288 ESTI / ADI).

## Snippets

> Agentic SOC architecture offloading graph-consistent containment reasoning from the LLM context window. [Source: arXiv 2609.04159 abstract]
