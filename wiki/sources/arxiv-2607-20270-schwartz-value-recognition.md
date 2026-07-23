---
title: Which values do LLMs confuse? Schwartz recognition (arXiv 2607.20270)
type: source
tags: [source, arxiv, llm-eval, values, alignment]
keywords: [2607.20270, Schwartz, Acc@1, value recognition, Russian NLP]
related:
  - concepts/llm-schwartz-value-recognition.md
  - concepts/ethics-autonomous-offensive-ai-agents.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-23
phase_0_verdict: "REFERENCE 2026-07-23 — evaluation study; no code artifact located"
---

**Briefs:** `briefs/2026-07-23_k212-schwartz-value-recognition-prod.md`

## Relations

- @concepts/llm-schwartz-value-recognition.md
- @concepts/ethics-autonomous-offensive-ai-agents.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study |
| Authors | Chetvergov et al. (ISP RAS / RANEPA) |
| arXiv | 2607.20270 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20270-which-values-do-llms-confuse-a-schwartz-based-re.pdf` |
| Retrieved | 2026-07-23 |

## Narrative

Prerequisite for value-endorsement evals: can the model **recognize** which Schwartz basic value a situation expresses? 1,000 Russian situational texts × 10 values; 21 instruction-tuned runs.

### Headline [CONFIRMED from abstract]

| Metric | Value |
|--------|-------|
| Acc@1 (pooled) | **0.683** |
| Acc@3 | **0.892** |
| Adjacent-value errors | **50.9%** of semantic errors (vs 24.4% null) |
| Recurring directed confusions | e.g. Universalism→Benevolence, Tradition→Conformity, Security→Power (asymmetric) |

### Steal

1. Value-routing / policy labels need recognition-error analysis, not only endorsement scores
2. Asymmetric confusions can bias higher-order value profiles used in agent policy

## Snippets

> "Pooled Acc@1 is 0.683 and Acc@3 is 0.892… Adjacent values account for 50.9% of semantic errors"
[Source: arxiv-2607.20270 abstract]
