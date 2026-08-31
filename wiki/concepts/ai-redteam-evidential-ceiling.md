---
title: AI red-team evidential ceiling
type: concept
tags: [concept, llm-safety, evaluation, red-teaming]
keywords: [evidential ceiling, null result, harm rate, certification claim, 2607.21735]
related:
  - concepts/agent-safety-executable-evaluation.md
  - sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
  - entities/tools/ai-redteam-evidential-limits.md
  - sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/pair-prompt-pattern.md
  - sources/arxiv-2608-12996-atobench-deceptive-observations.md
  - concepts/atobench-verification-chain-deception.md
  - sources/arxiv-2608-15578-arena-audio-lalm-redteam.md
  - concepts/audio-grounded-lalm-redteaming.md
  - sources/arxiv-2608-16747-chive-counterfactual-explanations.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - entities/tools/chive.md
  - sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md
  - sources/arxiv-2608-17202-fools-gold-defensive-deception.md
  - concepts/decoy-hardening-open-weight-abliteration.md
  - sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md
  - sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md
  - concepts/compliance-detector-rule-blindness.md
  - concepts/psychological-multiturn-jailbreaks.md
  - concepts/trace-verified-ctf-agent-eval.md
  - concepts/security-agent-authority-auditability-slr.md
maturity: draft
created: 2026-07-29
updated: 2026-08-31
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
