---
title: CITADEL — CSI-based jamming detection for IIoT (arXiv 2606.22939)
type: source
tags: [source, arxiv, wireless, iiot, ot, jamming, tangential]
keywords: [2606.22939, citadel, csi, jamming detection, iiot, open-set classification]
related:
  - concepts/network-security.md
  - concepts/wireless-pentest.md
  - concepts/6g-cps-closed-loop-security.md
  - concepts/industrial-safety-security-convergence.md
  - sources/arxiv-2607-15840-io-link-wireless-pren-50742.md
maturity: draft
read_status: skimmed
created: 2026-06-23
updated: 2026-07-20
phase_0_verdict: "Archive-only 2026-06-23 — IIoT defensive RF ML; no GitHub artifact Phase-0'd; tangential to offensive wireless tradecraft"
---

## Relations

- @sources/arxiv-2607-15840-io-link-wireless-pren-50742.md
- @concepts/industrial-safety-security-convergence.md
- @concepts/network-security.md — IIoT / OT wireless availability threats
- @concepts/wireless-pentest.md — jamming as offensive vector (orthogonal defensive ML paper)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CITADEL: CSI-Based Jamming Detection and Open-Set Classification for IIoT Networks |
| Authors | Aymen Bouferrouma et al. (Inria, Luxembourg, Avignon) |
| arXiv | 2606.22939v1 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.22939-2606-22939v1-citadel-csi-based-jamming-detection.pdf` |
| Retrieved | 2026-06-23 |
| Read status | **skimmed** (abstract + intro) |

## Narrative

**Tangential ingest** — defensive IIoT wireless security. Two-stage CSI pipeline for jamming **detection + classification** including zero-day (open-set) attacks on commodity IIoT hardware.

Claims: 100% known-attack detection, 97.1% zero-day detection, 0.4% FPR; 14.2 ms inference on edge GPU. Relevant to **OT/IIoT blue team** monitoring, not WiFi pentest tradecraft on @concepts/wireless-pentest.md.

No deep-read unless IIoT engagement scope expands.

## Snippets

> "CITADEL is the first system to translate this insight into an end-to-end pipeline that jointly achieves closed-set classification of known attacks, open-set detection of zero-day attacks, and resistance to adversarial evasion."

[Source: arxiv-2606.22939-citadel-csi-jamming-iiot.pdf abstract]
