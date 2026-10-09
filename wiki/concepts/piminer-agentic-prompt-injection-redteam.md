---
title: PIMiner — agentic prompt-injection red teaming
type: concept
tags: [concept, agent-security, prompt-injection, red-teaming, lab]
keywords: [PIMiner, strategy library, IPIArena, AgentDojo, 2608.05108]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/llm-adversarial-fuzzing.md
  - sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md
  - concepts/test-time-training-redteam-attacker.md
  - sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md
  - sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md
  - concepts/countersteer-activation-steering-ipi-defense.md
  - concepts/finrt-amortized-redteam-generator.md
  - sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
  - entities/tools/piminer.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/openart-environment-evolution-agent-redteam.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
  - concepts/aria-instruction-backdoor-redteam.md
  - sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md
maturity: draft
created: 2026-08-06
updated: 2026-10-09
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — K408-K417 ingest / 2026-10-09
- @concepts/llm-adversarial-fuzzing.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md — K398-K402 ingest source page
- @concepts/test-time-training-redteam-attacker.md — K399 attacker weights are not frozen at test time
- @sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md — K382–K386 ingest source page
- @sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md — K382–K386 ingest source page
- @concepts/countersteer-activation-steering-ipi-defense.md — K383 inference-time steering defense against IPI
- @concepts/finrt-amortized-redteam-generator.md — K382 amortized generator red-team
- @sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
- @entities/tools/piminer.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/openart-environment-evolution-agent-redteam.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/ai-for-cybersecurity.md
- @concepts/aria-instruction-backdoor-redteam.md
- @sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md

## Raw Concept

Agent-vs-agent prompt-injection red team that learns a transferable strategy library instead of per-target RL.

## Narrative

Lab tool for evaluating Cemini/friend agent harnesses under indirect prompt injection. Complements OpenART (env evolution) and detector calibration. Authorized sandboxes only. [CONFIRMED]
