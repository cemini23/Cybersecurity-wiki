---
title: LLM biosecurity red-teaming (early-warning posture)
type: concept
tags: [biosecurity, dual-use, llm-safety, red-team]
keywords: [Intern-BioBreaker, bio-risk ASR, synthesis screening, dual-use AI]
related:
  - sources/arxiv-2607-18056-intern-biobreaker-biosecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/responsible-disclosure.md
  - concepts/ai-for-cybersecurity.md
  - concepts/biosecbench-surveillance-verifiable-agent-eval.md
  - sources/arxiv-biosecbench-surveillance-2607.19262.md
maturity: draft
created: 2026-07-21
updated: 2026-07-22
---

## Relations

- @concepts/biosecbench-surveillance-verifiable-agent-eval.md
- @sources/arxiv-2607-18056-intern-biobreaker-biosecurity.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/responsible-disclosure.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Frontier models with scientific/bio capability create dual-use risk beyond chatbot jailbreaks. Early-warning evals couple model stress tests with (authorized) physical validation to show text safeguards can lag real-world hazard.

## Narrative

### Defensive posture [TENTATIVE — single-lab early warning]

| Control | Why |
|---------|-----|
| Domain bio red-team | Chat ASR ≠ bio-task ASR |
| Nucleic-acid synthesis screening | Model text can become DNA |
| Capability gating | Science models ≠ general chat policy |
| No public attack recipes in wiki | Dual-use hygiene |

### Out of scope for this wiki

Operational jailbreaks, sequences, or lab protocols — see source disclaimer; cite paper only.
