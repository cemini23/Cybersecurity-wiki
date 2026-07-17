---
title: AMT-X — phase-structured multi-turn red-teaming with checklist-gated dual ASR
type: concept
tags: [concept, llm-security, multi-turn, red-teaming, evaluation, jailbreak]
keywords: [amt-x, overall asr, full asr, phase state machine, checklist gate, multi-role jury]
related:
  - sources/arxiv-2607-11151-amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/pair-prompt-pattern.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/fuzzyai.md
  - concepts/gflowrl-distribution-matching-attacker-rl.md
  - sources/arxiv-2607-13394-gflowrl-distribution-matching-rl.md
  - concepts/agentic-hard-example-synthesis-content-safety.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - sources/arxiv-2607-14256-agentic-hard-example-synthesis.md
  - sources/arxiv-2607-15218-prism-physical-vs-content-danger.md
maturity: draft
created: 2026-07-16
updated: 2026-07-17
---

## Relations

- @sources/arxiv-2607-11151-amt-x-phase-structured-multi-turn-red-teaming.md — primary paper
- @concepts/crescendo-multi-turn-jailbreak.md — ad hoc multi-turn baseline AMT-X makes reproducible
- @concepts/vulnerability-concept-graph-production-agent-red-teaming.md — complementary: chat ASR gating vs production-agent mechanism graphs

## Raw Concept

How do we measure multi-turn jailbreaks so that "model said something vaguely useful" is not scored the same as "complete operational procedure"? AMT-X answers with phase structure + dual ASR.

## Narrative

### Phase machine (P0–P4)

Attack is an explicit state machine, not free-form Crescendo improvisation. Phases bind a **31-technique library**; transitions use checklist completeness, semantic readiness, early disclosure, then turn budget (priority-ordered). Attacker runs **semantic simulation** before emit — revise if predicted reply looks like refusal.

### Dual metric (steal)

| Metric | Meaning | Use |
|--------|---------|-----|
| Overall ASR | Any critical actionability item | Upper-bound / regression smoke |
| Full ASR | All critical items pass (complete + real + operational) | Production triage / patch acceptance |

Reporting only overall ASR overstates risk; only full ASR understates partial leaks. **Report both** and the gap. [CONFIRMED — paper 6×7 grid]

### Vs prior wiki patterns

| Pattern | Granularity | Reproducibility |
|---------|-------------|-----------------|
| PAIR | Single-turn refine | High |
| Crescendo | Multi-turn escalate | Low (improvised) |
| AMT-X | Multi-phase state machine | High (phase + technique IDs) |

### Defender note

Stateful conversation re-eval and actionability-aware judges shrink the overall→full gap. Single-turn classifiers remain insufficient (same lesson as Crescendo).

## Snippets

See source page for abstract quote + Algorithm 1/2 paraphrases.
