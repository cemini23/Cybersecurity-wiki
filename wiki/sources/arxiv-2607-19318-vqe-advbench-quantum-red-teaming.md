---
title: VQE-AdvBench — SoK adversarial robustness of VQE via red-teaming (arXiv 2607.19318)
type: source
tags: [source, arxiv, quantum, red-team, sok, cloud]
keywords: [2607.19318, VQE-AdvBench, QTrojan, QDoor, QNBAD, ZNE]
related:
  - concepts/quantum-vqe-adversarial-robustness.md
  - concepts/ai-for-cybersecurity.md
  - concepts/cloud-pentest.md
maturity: draft
read_status: skimmed
created: 2026-07-22
updated: 2026-07-22
phase_0_verdict: "REFERENCE 2026-07-22 — SoK/benchmark paper; no public code at ingest; steal cloud VQE-as-a-service threat model"
---

**Briefs:** `briefs/2026-07-22_k203-vqe-advbench-quantum-redteam-prod.md`

## Relations

- @concepts/quantum-vqe-adversarial-robustness.md
- @concepts/ai-for-cybersecurity.md
- @concepts/cloud-pentest.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SoK: Adversarial Robustness of the Variational Quantum Eigensolver via Red-Teaming |
| Authors | Ahmed Azaz Humdoon, Cheng Chu, Lei Jiang, Qian Lou, Mengxin Zheng |
| arXiv | 2607.19318 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.19318-sok-adversarial-robustness-of-the-variational-qu.pdf` |
| Retrieved | 2026-07-22 |
| Public code | None found |

## Narrative

**VQE-AdvBench** unifies black/gray/white-box attacks on cloud VQE-as-a-service (QTrojan, QDoor, FGSM/PGD adaptations, QNBAD noise variants) on H₂ / H₃⁺ across five IBM noise-calibrated backends. Severity ordering highlights **noise-induced attacks that manipulate Zero-Noise Extrapolation (ZNE)** as especially severe.

### Steal

1. Treat cloud quantum pipelines as multi-tenant/transpilation attack surfaces
2. Prefer unified energy-error metrics when comparing VQE attacks
3. Watch ZNE / error-mitigation pipeline integrity

### Phase-0

| Verdict | **REFERENCE** |
