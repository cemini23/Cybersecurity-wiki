---
title: Six-dimensional post-training adaptation taxonomy (arXiv 2608.06246)
type: source
tags: [source, arxiv, ai-governance, fine-tuning, unlearning, survey]
keywords: [2608.06246, post-training, taxonomy, PEFT, RAG, model editing, unlearning]
related:
  - concepts/post-training-adaptation-taxonomy.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/gradient-immunity-malicious-finetune.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-07
updated: 2026-08-07
phase_0_verdict: "REFERENCE 2026-08-07 — survey; no code artifact"
wire_status: wont_wire
wire_target: "vocabulary / governance docs only"
---

**Briefs:** `briefs/2026-08-07_k250-post-training-taxonomy-prod.md`

## Relations

- @concepts/post-training-adaptation-taxonomy.md
- @concepts/datashield-risky-finetune-data-filtering.md
- @concepts/gradient-immunity-malicious-finetune.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance |
| Authors | Fardin Afdideh, Fernando Seoane, Farhad Abtahi |
| arXiv | 2608.06246 |
| Code | none (survey) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.06246-a-six-dimensional-taxonomy-of-post-training-adap.pdf` |
| Retrieved | 2026-08-07 |

## Narrative

Survey taxonomy of post-training adaptation along **mechanism · goal · data requirement · persistence · structural scope · model type**. Separates fine-tuning vs RAG vs prompting; maps inheritance/hybrid stacks for documentation and governance. [CONFIRMED abstract]

### Steal

1. Document how a model was changed with the six axes — not a vague “we fine-tuned”
2. Pair with DataShield / Gradient Immunity when open weights leave your boundary
3. Abliteration / unlearning are first-class adaptation classes — track persistence

## Snippets

> "introduces a six-dimensional taxonomy organized by mechanism, goal, data requirement, persistence, structural scope, and model type."
[Source: arXiv 2608.06246 abstract]
