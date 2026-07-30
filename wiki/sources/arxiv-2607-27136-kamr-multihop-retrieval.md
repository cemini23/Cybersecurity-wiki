---
title: KAMR knowledge-aligned multi-hop retrieval (arXiv 2607.27136)
type: source
tags: [source, arxiv, rag, knowledge-graph, grounding]
keywords: [2607.27136, KAMR, multi-hop, GRAG, anchor triplets, COLM 2026]
related:
  - concepts/kamr-knowledge-aligned-multihop-retrieval.md
  - concepts/ai-for-cybersecurity.md
  - concepts/evidence-aware-long-context-grounding.md
maturity: draft
read_status: read
created: 2026-07-30
updated: 2026-07-30
phase_0_verdict: "REFERENCE 2026-07-30 — github.com/XiaochenWang-PSU/KAMR has NO LICENSE; do not adopt"
---

**Briefs:** `briefs/2026-07-30_k228-kamr-prod.md`

## Relations

- @concepts/kamr-knowledge-aligned-multihop-retrieval.md
- @concepts/ai-for-cybersecurity.md
- @concepts/evidence-aware-long-context-grounding.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | KAMR: Grounding Generation via Knowledge-Aligned Multi-hop Retrieval |
| Authors | Wang, Zhong, Wang, Wang, Ma (Penn State / Albany / Stony Brook) |
| arXiv | 2607.27136 |
| Code | github.com/XiaochenWang-PSU/KAMR — **NO LICENSE** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.27136-kamr-grounding-generation-via-knowledge-aligned.pdf` |
| Retrieved | 2026-07-30 |

## Narrative

Multi-hop GRAG: distinguish **anchor** triplets (query-constrained) from **connected** triplets (structurally linked, weakly aligned). Partial-alignment pretraining via triplet masking + LLM query generation. Full-model accuracy cited ~75.86 on eval table; ablations show pretraining matters.

### Steal

1. For threat-intel / genealogy KGs: retrieve anchors first, then expand structurally
2. Do not rank multi-hop facts by global semantic match alone
3. Wait for LICENSE before any code adoption

## Snippets

> "distinguishes anchor triplets that are strongly constrained by the query from connected triplets that are weakly aligned yet structurally linked to the anchors."
[Source: arxiv-2607.27136 abstract]
