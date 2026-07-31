---
title: CRAFT — clustering rubrics to diagnose weak LLM capabilities (arXiv 2607.16122)
type: source
tags: [source, arxiv, llm-eval, fine-tuning, rubrics, scale-ai]
keywords: [2607.16122, CRAFT, EvalTree, capability tree, rubric clustering, Scale AI]
related:
  - concepts/rubric-capability-tree-diagnosis.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-15081-datashield-risky-finetune-data.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-20 — Scale AI method paper; no public code at ingest; steal rubric→capability-tree→targeted-SFT pattern"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-20_k195-craft-capability-diagnosis-prod.md`; CCC primary; poker steal

## Relations

- @concepts/rubric-capability-tree-diagnosis.md — synthesis
- @concepts/datashield-risky-finetune-data-filtering.md — adjacent post-training data hygiene
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data |
| Authors | Vipul Gupta, Zihao Wang, Razvan-Gabriel Dumitru, MohammadHossein Rezaei, Aakash Sabharwal, Yunzhong He |
| Affiliation | Scale AI |
| arXiv | 2607.16122 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.16122-craft-clustering-rubrics-to-diagnose-weak-llm-ca.pdf` |
| Retrieved | 2026-07-20 |
| Read status | **read** |
| Public code | None found (method paper) |

## Narrative

Most eval pipelines say **where** a model fails (prompt/topic), not **why** (failed answer requirement). CRAFT treats each **rubric criterion** as a capability probe: extract capability descriptions → hierarchical cluster tree → score model at every node → select weakest nodes at clearest granularity → generate targeted SFT data.

Compared to **EvalTree** (prompt-level trees) and untargeted random generation on four open models, finance + legal domains, **13 held-out** benchmarks. CRAFT strongest finance average for all four models; strongest legal for 3/4 (4th within variance of best baseline).

### Steal (harness / security model FT)

1. Prefer **criterion-level** weakness diagnosis over category averages before collecting FT data
2. Pair with DataShield (@entities/tools/datashield.md): CRAFT targets capability gaps; DataShield filters risky FT samples
3. Poker / decide() eval: cluster rubric fails into a capability tree before rewriting prompts or SFT

### Phase-0

| Gate | Status |
|------|--------|
| Code | **Missing** — no public repo |
| Verdict | **REFERENCE** — pattern only |

## Snippets

> "Diagnosing weaknesses at the level of rubric criteria, rather than prompts or categories, thus yields both a sharper picture of what a model cannot do and measurably better models after fine-tuning on that diagnosis."
[Source: arxiv-2607.16122 abstract]
