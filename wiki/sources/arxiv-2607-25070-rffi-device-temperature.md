---
title: Device temperature effects on RF fingerprinting (arXiv 2607.25070)
type: source
tags: [source, arxiv, wireless, rf-fingerprint, authentication]
keywords: [2607.25070, RFFP, temperature drift, Oregon State, device auth]
related:
  - concepts/rf-fingerprint-temperature-drift.md
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/wireless-pentest.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-30
updated: 2026-07-30
phase_0_verdict: "REFERENCE 2026-07-30 — dataset at research.engr.oregonstate.edu/hamdaoui/datasets; no companion code repo"
---

**Briefs:** `briefs/2026-07-30_k225-rffi-temperature-prod.md`

## Relations

- @concepts/rf-fingerprint-temperature-drift.md
- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/wireless-pentest.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Characterizing and Mitigating the Effects of Device Temperature on RF Fingerprinting Accuracy |
| Authors | Albousayri, Hamdaoui (Oregon State) |
| arXiv | 2607.25070 |
| Data | research.engr.oregonstate.edu/hamdaoui/datasets |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.25070-characterizing-and-mitigating-the-effects-of-dev.pdf` |
| Retrieved | 2026-07-30 |

## Narrative

RFFP auth fails when classifiers ignore **device temperature** (internal + environmental). Temperature-aware models that concatenate temperature with feature embeddings outperform temperature-blind baselines, especially under unseen thermal conditions. Complements probe-point sensitivity (@concepts/rf-fingerprint-probe-point-benchmark.md).

### Steal

1. Lab RFFP evals must vary temperature — not just SNR/channel
2. Log temperature with enrollment + verification captures
3. Treat thermal drift as an attacker-controllable confounder (heat/cool target)

## Snippets

> "ignoring temperature information can lead to significant performance degradation, particularly under unseen conditions."
[Source: arxiv-2607.25070 conclusion]
