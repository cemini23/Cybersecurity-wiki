---
title: Gradient Immunity null-space resistance to malicious fine-tuning (arXiv 2608.05045)
type: source
tags: [source, arxiv, llm-safety, fine-tuning]
keywords: [2608.05045, Gradient Immunity, USG, PPOW, malicious fine-tuning, null space]
related:
  - concepts/gradient-immunity-malicious-finetune.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - entities/tools/datashield.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: "REFERENCE 2026-08-06 — github.com/OpenCausaLab/Gradient-Immunity is empty (README only; no LICENSE)"
wire_status: wont_wire
wire_target: "REFERENCE — no clone until code+LICENSE land"
---

**Briefs:** `briefs/2026-08-06_k246-gradient-immunity-prod.md`

## Relations

- @concepts/gradient-immunity-malicious-finetune.md
- @concepts/datashield-risky-finetune-data-filtering.md
- @entities/tools/datashield.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning |
| Authors | Huang, Zeng, Zheng, Lu |
| arXiv | 2608.05045 |
| Code | https://github.com/OpenCausaLab/Gradient-Immunity — **empty / no LICENSE** (2026-08-06) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.05045-gradient-immunity-null-space-resistance-to-malic.pdf` |
| Retrieved | 2026-08-06 |

## Narrative

Open-weight aligned models remain vulnerable to **malicious downstream fine-tunes**. Setting: provider-controlled partially protected open-weight (PPOW) — most weights trainable, small safety-critical component preserved. **Unidirectional Safety Gate (USG)** = Null Space Cubic Layer + Inverse Adapter after final Transformer layer; blocks/suppresses gradients from harmful samples in a calibrated protected region while restoring forward behavior. Across six model-dataset settings, post-finetune ASR stays near pre-release under a fixed release threshold. [CONFIRMED abstract]

### Steal

1. DataShield filters training data; USG/Gradient Immunity protects a **weight subspace** at release — complementary
2. Friend/local abliterated path A: expect malicious FT still works unless provider-style PPOW gates exist
3. Skip clone until real code + SPDX appear

## Snippets

> "a provider controlled partially protected open-weight (PPOW) release setting in which most weights remain trainable while a small safety-critical component is preserved at release."
[Source: arXiv 2608.05045 abstract]
