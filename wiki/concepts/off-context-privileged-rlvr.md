---
title: Off-context privileged RLVR (OC-GRPO pattern)
type: concept
tags: [rlvr, training, reasoning]
keywords: [OC-GRPO, privileged guidance, importance correction, learning cliff]
related:
  - sources/arxiv-2607-19313-oc-grpo-off-context.md
  - entities/tools/oc-grpo.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/arxiv-2607-19313-oc-grpo-off-context.md
- @entities/tools/oc-grpo.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Hard RLVR problems yield zero reward → no learning. Privileged train-time guidance helps if the objective is importance-corrected back to the unguided prompt (OC-GRPO).

## Narrative

CCC/harness steal for hard-spot training. Not a runtime security control.
