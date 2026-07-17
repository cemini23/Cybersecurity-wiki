---
title: LLM statistical self-consistency — macro fallacy (cybersec slice)
type: concept
tags: [concept, evaluation, self-consistency, persona]
keywords: [macro fallacy, partition prompt aggregate, statistical self-consistency]
related:
  - sources/arxiv-2607-15277-partition-prompt-aggregate-self-consistency.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- @sources/arxiv-2607-15277-partition-prompt-aggregate-self-consistency.md — paper
- Primary home: CCC eval methodology

## Raw Concept

Population-level LLM estimates often disagree with aggregates of finer persona partitions (**macro fallacy**). Treat single-shot “what does the public/security community think” prompts as unreliable without partition checks.

## Narrative

Cybersec use: threat surveys, risk scoring, persona-based red-team planning — prefer partitioned aggregates + consistency checks over one global prompt. Full methodology lives in CCC.
