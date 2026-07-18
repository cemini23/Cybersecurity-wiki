---
title: ARMOR++ — agentic black-box attacks on deepfake detectors (arXiv 2607.15246)
type: source
tags: [source, arxiv, deepfake, adversarial-ml, agentic, black-box]
keywords: [2607.15246, armor++, aadd-2025, deepfake detector, transferable attack, qwen]
related:
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agentic-hard-example-synthesis-content-safety.md
  - "@ccc-wiki/sources/arxiv-armor-plusplus-deepfake-agentic-attacks-2607.15246.md"
maturity: draft
read_status: read
created: 2026-07-17
updated: 2026-07-18
phase_0_verdict: "REFERENCE 2026-07-18 — no public code; steal agentic orchestration of attack primitives + residual detector reliability gap"
---

**Briefs:** `briefs/2026-07-18_armor-plusplus-deepfake-handoff.md`, `briefs/2026-07-18_k188-armor-plusplus-deepfake-prod.md`

## Relations

- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md — synthesis
- CCC REFERENCE route only (orchestration pattern already covered)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ARMOR++: Agentic Reasoning for Method Orchestration and Reparameterization in Transferable Black-Box Attacks on Deepfake Detectors |
| Authors | Christos Korgialas, Gabriel Jun Rong Lee, Dion Jia Xu Ho, Pai Chet Ng, Xiaoxiao Miao, Konstantinos N. Plataniotis |
| arXiv | 2607.15246 |
| Venue | IEEE Transactions on Reliability (preprint) |
| Code | **none found** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15246-armor-plusplus-deepfake-agentic-attacks.pdf` |
| Retrieved | 2026-07-18 |
| Read status | **read** (AADD results + agent stack) |

## Narrative

Multi-agent VLM/LLM framework (Qwen2.5-VL + Qwen3) orchestrates **five** attack primitives (dense opt, saliency, spatial, frequency/SSA, block/BSR) with adaptive reparameterization for **no-query** black-box transfer onto deepfake detectors.

### Headline ASR [CONFIRMED — Tables II/III narrative]

| Regime | Target | ARMOR++ ASR | vs ARMOR | vs AA-PGD |
|--------|--------|-------------|----------|-----------|
| AADD-LQ | ViT-B/16 | **0.443** | +4.7 pp | +24.7 pp |
| AADD-LQ | Swin-B | **0.408** | +3.7 pp | +22.5 pp |
| AADD-HQ | ViT-B/16 | **0.321** | +3.8 pp | +17.2 pp |
| AADD-HQ | Swin-B | **0.287** | +2.8 pp | +15.6 pp |

Residual reliability gap: even SOTA detectors remain substantially evadeable under agentic transfer.

### Steal

1. Deepfake detector evals must include **agentic multi-primitive** transfer, not only FGSM-class
2. Agentic orchestration of heterogeneous primitives beats single-primitive pipelines
3. No local adopt — GPU/Qwen-heavy research stack; REFERENCE only

### Phase-0

REFERENCE — no public repo; do not attempt local adopt under 500MB budget (model weights alone exceed).

## Snippets

> "These findings highlight a significant residual reliability gap in current deepfake detector deployments…"
[Source: arxiv-2607.15246 abstract]
