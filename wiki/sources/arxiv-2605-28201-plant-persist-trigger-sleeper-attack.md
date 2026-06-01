---
title: "Plant, Persist, Trigger: Sleeper Attack on LLM Agents (arXiv:2605.28201)"
type: source
tags: [arxiv, agent-security, prompt-injection, sleeper-attack, adversarial, research-paper]
keywords: [sleeper attack, plant persist trigger, agent memory, mcp context, multi-turn attack]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - entities/tools/nvidia-skillspector.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/agent-runtime-guardrails.md — sleeper attack as multi-interaction external threat
- @concepts/llm-adversarial-fuzzing.md — extends single-turn injection testing scope
- @concepts/crescendo-multi-turn-jailbreak.md — multi-turn adversarial pattern (different threat class)
- @entities/tools/nvidia-skillspector.md — poisoned skills as persist target

## Raw Concept

- **Title**: Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents
- **Authors**: Yongxiang Li et al. (USTC, NUS, SMU, Shanghai AI Lab)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2605.28201-plant-persist-trigger-sleeper-attack-on-large-la.pdf`
- **URL**: https://arxiv.org/abs/2605.28201
- **Retrieved**: 2026-06-01
- **Read-status**: read

## Narrative

**Sleeper Attack**: adversarial content in external observations (tool returns, webpages, MCP context) **persists** in agent state (session context, memory, reusable skills), stays dormant across benign interactions, then activates on a later benign user query. Benchmark: 1,896 instances, six harmful outcomes, three attack strategies, three persist targets. Seven LLMs remain vulnerable even when single-interaction ASR is low. `[TENTATIVE]` — anonymous code URL in paper; reproduce before engagement claims.

## Snippets

> "Adversarial content may persist in the agent state, remain dormant across interactions, and later be activated by a benign user query."

> Persist targets: "session context, memory, and reusable skills."
