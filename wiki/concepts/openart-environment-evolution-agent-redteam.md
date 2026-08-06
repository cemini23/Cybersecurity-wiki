---
title: OpenART — environment-evolution agent red teaming
type: concept
tags: [concept, agent-security, red-teaming, lab]
keywords: [OpenART, EMHA, stateful scenarios, MCP, 2608.00677]
related:
  - sources/arxiv-2608-00677-openart-agent-redteam-evolution.md
  - entities/tools/openart.md
  - concepts/gpt-red-self-play-red-teaming.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/cyber-capable-agent-evaluation-containment.md
  - concepts/ai-for-cybersecurity.md
  - concepts/red-team-operations.md
  - concepts/trident-agentic-drl-defense-redteam.md
  - sources/arxiv-2608-04317-trident-agentic-drl-redteam.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
maturity: draft
created: 2026-08-04
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2608-00677-openart-agent-redteam-evolution.md
- @entities/tools/openart.md
- @concepts/gpt-red-self-play-red-teaming.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/cyber-capable-agent-evaluation-containment.md
- @concepts/ai-for-cybersecurity.md
- @concepts/red-team-operations.md
- @concepts/trident-agentic-drl-defense-redteam.md
- @sources/arxiv-2608-04317-trident-agentic-drl-redteam.md
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md

## Raw Concept

Scale agent red teaming by evolving shared environment state under fixed safety contracts.

## Narrative

Static jailbreak benches miss cumulative tool/MCP state risks. OpenART + EMHA pattern: large scenario corpus → project to agent adapters → evolve environment with feedback while holding objectives constant. Lab posture only (AGPL; written auth). Pair with containment principles for cyber-capable agent evals. [CONFIRMED]
