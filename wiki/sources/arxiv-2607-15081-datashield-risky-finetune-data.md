---
title: DataShield — risky fine-tuning data via consensus subspace (arXiv 2607.15081)
type: source
tags: [source, arxiv, llm-safety, fine-tuning, data-centric, alignment]
keywords: [2607.15081, datashield, fine-tuning safety, consensus subspace, asr, zju]
related:
  - concepts/datashield-risky-finetune-data-filtering.md
  - entities/tools/datashield.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/crescendo-multi-turn-jailbreak.md
maturity: draft
read_status: read
created: 2026-07-17
updated: 2026-07-17
phase_0_verdict: "CONDITIONAL-GO 2026-07-17 — github.com/ZJU-LLM-Safety/DataShield MIT ~3MB; lab fine-tune filtering only"
---

**Briefs:** `briefs/2026-07-17_datashield-risky-finetune-handoff.md`, `briefs/2026-07-17_k184-datashield-risky-finetune-prod.md`

## Relations

- @concepts/datashield-risky-finetune-data-filtering.md — synthesis
- @entities/tools/datashield.md — Phase-0 + local clone

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment |
| Authors | Zefeng Wu, Weiwei Qi, Jielong Chen, Tianhang Zheng, et al. |
| Affiliation | Zhejiang University; Shanghai AI Lab; ECNU; UESTC |
| arXiv | 2607.15081 |
| Code | [github.com/ZJU-LLM-Safety/DataShield](https://github.com/ZJU-LLM-Safety/DataShield) (MIT) |
| Local clone | `raw-sources/repos/DataShield` (~3MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15081-datashield-uncovering-risky-fine-tuning-data-acr.pdf` |
| Retrieved | 2026-07-17 |
| Read status | **read** (framework + ASR claims) |

## Narrative

Benign task fine-tuning can weaken LLM safety. DataShield estimates risk by aligning samples/segments to **consensus unsafe vs safe subspaces** derived from multiple safety-aligned models (semantic spectral decomposition), avoiding single-model mean-vector fragility.

### Headline results [CONFIRMED from abstract]

| Method | ASR reduction vs SOTA baselines |
|--------|----------------------------------|
| Sample filtering | **−14.6%** ASR |
| Segment masking | **−32.3%** ASR |

Preserves downstream utility; risk scores are not target-model-specific.

### Steal for Cemini

1. Before any domain fine-tune of a safety-aligned model: run DataShield-style filter/mask on the dataset
2. Prefer multi-model consensus safety directions over single-tokenizer mean vectors
3. Segment masking > sample drop when utility matters

### Phase-0 (2026-07-17)

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Size | **PASS** — ~3MB shallow clone |
| Maturity | **WATCH** — 4★, pushed 2026-07-16 (new) |
| Failure mode | Needs multi-LLM embeddings / GPU for full pipeline — lab only |
| Verdict | **CONDITIONAL-GO** |

## Snippets

> "DataShield reduces ASR by 14.6% with sample filtering and 32.3% with segment masking, while preserving downstream utility…"
[Source: arxiv-2607.15081 abstract]
