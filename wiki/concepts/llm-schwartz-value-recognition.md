---
title: LLM Schwartz value recognition (and directed confusions)
type: concept
tags: [concept, llm-eval, values, alignment]
keywords: [Schwartz, Acc@1, value recognition, directed confusion, 2607.20270]
related:
  - sources/arxiv-2607-20270-schwartz-value-recognition.md
  - concepts/ethics-autonomous-offensive-ai-agents.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- @sources/arxiv-2607-20270-schwartz-value-recognition.md
- @concepts/ethics-autonomous-offensive-ai-agents.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Can models **recognize** which Schwartz basic value a situation expresses before we trust endorsement/profile scores?

## Narrative

Pooled Acc@1 ~0.68; Acc@3 ~0.89. Errors cluster on **adjacent** values; several directed confusions are asymmetric (e.g. Security→Power). For agent policy / routing that uses value labels, treat recognition error as a first-class risk. [CONFIRMED abstract]

Russian-language eval set — cross-lingual transfer [NEEDS VERIFICATION 2026-07-23].
