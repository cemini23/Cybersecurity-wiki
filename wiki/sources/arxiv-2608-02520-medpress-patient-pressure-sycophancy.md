---
title: MedPRESS patient-pressure medical sycophancy (arXiv 2608.02520)
type: source
tags: [source, arxiv, llm-safety, multi-turn, sycophancy]
keywords: [2608.02520, MedPRESS, medical sycophancy, multi-turn pressure]
related:
  - concepts/multi-turn-pressure-sycophancy.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-04
updated: 2026-08-04
phase_0_verdict: "REFERENCE 2026-08-04 — no public code; medical eval bench"
wire_status: wont_wire
wire_target: "REFERENCE — pattern steal only"
---

**Briefs:** `briefs/2026-08-04_k239-medpress-prod.md`

## Relations

- @concepts/multi-turn-pressure-sycophancy.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/social-engineering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MedPRESS: A Multi-turn Benchmark for Patient-Pressure-Induced Medical Sycophancy in LLMs |
| Authors | Saman Sarker Joy, Niloy Farhan |
| arXiv | 2608.02520 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.02520-medpress-a-multi-turn-benchmark-for-patient-pres.pdf` |
| Retrieved | 2026-08-04 |

## Narrative

600 five-turn medically grounded dialogues (medication demand, self-care, triage resistance). Escalation: personal experience → social proof → external evidence claims → direct adversarial challenge. 20 LLMs evaluated; models often shift to unsafe agreement under repeated pressure; anti-sycophancy prompts help but do not eliminate. [CONFIRMED abstract]

### Steal

1. Multi-turn **pressure ladders** (not single prompts) for safety/sycophancy eval — same shape as Crescendo
2. Domain knowledge ≠ pressure robustness
3. Cybersec transfer: engagement/report agents under client pressure to soften findings

## Snippets

> "safe medical knowledge is not enough unless models can maintain it under conversational pressure."
[Source: arXiv 2608.02520 abstract]
