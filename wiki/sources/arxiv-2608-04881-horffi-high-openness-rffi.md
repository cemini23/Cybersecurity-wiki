---
title: HoRFFI high-openness RF fingerprint identification (arXiv 2608.04881)
type: source
tags: [source, arxiv, wireless, rf-fingerprint, authentication]
keywords: [2608.04881, HoRFFI, RFFI, open-set, SVIB, LoRa, Wi-Fi]
related:
  - concepts/horffi-high-openness-rffi.md
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/rf-fingerprint-temperature-drift.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: "REFERENCE 2026-08-06 — no public code"
wire_status: wont_wire
wire_target: "REFERENCE"
---

**Briefs:** `briefs/2026-08-06_k245-horffi-prod.md`

## Relations

- @concepts/horffi-high-openness-rffi.md
- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/rf-fingerprint-temperature-drift.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | HoRFFI: High-Openness RF Fingerprint Identification with a Similarity-Enhanced Variational Information Bottleneck |
| Authors | Zeng, Shen, Zhang, Shen, Tan, Song |
| arXiv | 2608.04881 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.04881-horffi-high-openness-rf-fingerprint-identificati.pdf` |
| Retrieved | 2026-08-06 |

## Narrative

Practical RFFI must enroll new authorized devices and reject unknowns after training on only a few labeled base classes (**high-openness**). HoRFFI uses similarity-enhanced variational information bottleneck (SVIB) supervision with feature-space augmentation/clustering so embeddings transfer with less training-class diversity. Eval on public LoRa and Wi-Fi datasets. [CONFIRMED abstract]

### Steal

1. Open-set RFFI claims need few-shot + unknown-reject metrics — not closed-set accuracy alone
2. Pair with probe-point and temperature-drift findings before trusting RFFI in labs

## Snippets

> "supports scalable device identification and unknown-device rejection using only a small number of labeled training devices."
[Source: arXiv 2608.04881 abstract]
