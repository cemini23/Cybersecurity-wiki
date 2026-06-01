---
title: "ChainCaps: Composition-Safe Tool-Using Agents (arXiv:2605.26542)"
type: source
tags: [arxiv, agent-security, mcp, information-flow, composition-safety, research-paper]
keywords: [chaincaps, permission laundering, monotonic capability attenuation, mcp proxy, sink-specific budget]
related:
  - concepts/agent-runtime-guardrails.md
  - entities/tools/chaincaps.md
  - concepts/llm-pentest-automation.md
  - entities/tools/nvidia-skillspector.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/agent-runtime-guardrails.md — permission laundering + composition-safety invariant
- @entities/tools/chaincaps.md — MCP proxy implementation concept
- @concepts/llm-pentest-automation.md — MCP tool chains in pentest agents
- @entities/tools/nvidia-skillspector.md — supply-chain preflight vs runtime flow enforcement

## Raw Concept

- **Title**: ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation
- **Authors**: Xiaochong Jiang et al. (AIWILD @ ICML 2026 workshop)
- **Type**: arXiv preprint / workshop paper
- **Location**: `raw-sources/arxiv-2605.26542-chaincaps-composition-safe-tool-using-agents-via.pdf`
- **URL**: https://arxiv.org/abs/2605.26542
- **Retrieved**: 2026-06-01
- **Read-status**: read

## Narrative

**Permission laundering**: per-tool checks pass but composed workflow violates policy (read confidential doc → summarize → email externally). ChainCaps attaches **sink-specific capability budgets** to values; composition propagates by **intersection** — authority can only attenuate, never amplify. Implemented as transparent **MCP proxy** (no agent/tool-server changes). 82-task suite: ASR 25–68% → 0–4.8%; 96–100% benign completion. **Manifest quality** is deployment bottleneck (expert 100% block vs naive 27.3%).

## Snippets

> "We call this failure mode permission laundering."

> "Composition can preserve or reduce a value's downstream authority, but it cannot widen what the value may do next."
