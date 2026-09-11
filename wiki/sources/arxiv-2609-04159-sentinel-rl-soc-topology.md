---
title: "SENTINEL-RL — offloading topological reasoning from SOC LLM agents (arXiv 2609.04159)"
type: source
tags: [source, arxiv, soc, blue-team, agent, graph, k336]
keywords: [2609.04159, SENTINEL-RL, SOC, authentication graph, containment, RL]
related:
  - concepts/sentinel-rl-soc-topological-reasoning.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — SOC graph-reasoning offload pattern; no clone until SPDX verified."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K336)"
---

## Relations

- @concepts/sentinel-rl-soc-topological-reasoning.md — K336 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center |
| arXiv | 2609.04159 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.04159-sentinel-rl-offloading-topological-reasoning-fro.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

SOC-scale authentication graphs exceed LLM context windows, and free-form containment recommendations may be **topologically inconsistent**. **K336 (SENTINEL-RL)** decouples **topological reasoning** (graph algorithms + RL) from LLM narrative/analysis layers. **Steal-from:** enforce graph-feasible containment actions outside the LLM; treat LLM output as untrusted planner input (pairs K288 ESTI / ADI).

## Snippets

> Agentic SOC architecture offloading graph-consistent containment reasoning from the LLM context window. [Source: arXiv 2609.04159 abstract]
