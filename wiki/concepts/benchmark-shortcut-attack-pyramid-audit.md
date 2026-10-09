---
title: "Benchmark shortcut attack pyramid (K388)"
type: concept
tags: [concept, agent-security, k388]
keywords: [2610.00960, K388]
related:
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/adversarial-region-estimation-vs-single-example.md
  - sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md
  - sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md
  - sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-10-02
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K388)"
---

## Relations

- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
- @concepts/adversarial-region-estimation-vs-single-example.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md — K403-K407 ingest source page
- @sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md — K395-K397 ingest source page
- @sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

Question: **Benchmark shortcut attack pyramid** — operator steal from arXiv 2610.00960?

## Narrative

Audit a benchmark by attacking it at nested levels of access: **options only → question text → other items in the pool → a single frame or captions → shuffled or truncated video**. Report the **breaking level** — the first level where the shortcut beats the reference margin — beside the headline score. Apply it to **agent-security** evals the same way: if a blind or option-only attacker already scores near the reported number, the score certifies nothing. Watch **near-duplicate items** and **effective size** (a 200-item draw can hold ~32 effective items). Audit-only.

## Snippets

> See arXiv 2610.00960 abstract. [Source: arXiv 2610.00960 (retrieved 2026-10-02)]
