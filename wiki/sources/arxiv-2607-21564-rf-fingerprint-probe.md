---
title: Where you tap matters — RF fingerprint probe-point benchmark (arXiv 2607.21564)
type: source
tags: [source, arxiv, wireless, rf-fingerprint, rffi]
keywords: [2607.21564, RFFI, open-set, BPSK, timing recovery, probe point]
related:
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-24
phase_0_verdict: "REFERENCE 2026-07-24 — benchmark/methodology; no public code located"
---

**Briefs:** `briefs/2026-07-24_k219-rf-fingerprint-probe-prod.md`

## Relations

- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Where You Tap Matters: A Probe-and-Model Benchmark for Open-Set RF Fingerprinting |
| Authors | Oligeri, Sciancalepore, Huso, Al-Mousawi (HBKU / TU/e) |
| arXiv | 2607.21564 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.21564-where-you-tap-matters-a-probe-and-model-benchmar.pdf` |
| Retrieved | 2026-07-24 |

## Narrative

Open-set reconstruction-error RFFI across **five probe points** on a BPSK receiver chain. RFFI is **strongly probe-dependent**: **timing recovery** (and carrier recovery somewhat) enable low false-acceptance; other stages often need FA ratio >0.1 for TA=0.9.

### Steal

1. Document **where** you tap the RX chain when claiming RFFI results
2. Prefer timing-recovery (and carefully carrier-recovery) probes for low-FA open-set ID
3. Wireless lab: standardize probe-point reporting in RF fingerprint evals

## Snippets

> "RFFI is strongly probe-dependent: timing recovery and, to a lesser extent, carrier recovery enable low false-acceptance operation"
[Source: arxiv-2607.21564 abstract]
