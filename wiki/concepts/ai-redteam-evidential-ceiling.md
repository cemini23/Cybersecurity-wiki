---
title: AI red-team evidential ceiling
type: concept
tags: [concept, llm-safety, evaluation, red-teaming]
keywords: [evidential ceiling, null result, harm rate, certification claim, 2607.21735]
related:
  - sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
  - entities/tools/ai-redteam-evidential-limits.md
  - sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/pair-prompt-pattern.md
maturity: draft
created: 2026-07-29
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
- @entities/tools/ai-redteam-evidential-limits.md
- @sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md — faithful ASR as a measurement-condition tuple (K271)
- @concepts/faithful-agent-asr-measurement.md — exposure/execution/observation/adjudication decomposition (K271)
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/pair-prompt-pattern.md

## Raw Concept

What can a fixed-budget red-team eval actually prove — and when is a clean sheet stronger than one failure?

## Narrative

Evidential ceiling = max belief-update under fixed n. Crossing harm rate falls as 1/n. High-frequency harms: existing suites can certify. Rare/catastrophic: orders of magnitude short; below the rate, null results do not license safety claims. Discrimination between H0/H1 beats raw attack-success rate. [CONFIRMED abstract + companion MIT repo]
