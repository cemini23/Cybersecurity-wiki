---
title: "Through-wall detection using SDR and adaptive PCA (arXiv 2609.12443)"
type: source
tags: [source, arxiv, wireless, rf, lab-only, defensive, k344]
keywords: [2609.12443, through-wall detection, SDR, CSI, PCA, ambient WiFi]
related:
  - concepts/through-wall-detection-sdr-pca.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
phase_0_verdict: "REFERENCE 2026-09-17 — TWD defensive sensing; authorized RF lab only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K344)"
---

## Relations

- @concepts/through-wall-detection-sdr-pca.md — K344 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Through-Wall Detection using Software-Defined Radio based on adaptive Principal Component Analysis |
| arXiv | 2609.12443 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.12443-through-wall-detection-using-software-defined-ra.pdf |
| Retrieved | 2026-09-17 |
| Read status | read (abstract + triage) |

## Narrative

**Through-wall detection (TWD)** using ambient WiFi CSI enables non-invasive sensing for security and rescue. **K344** extracts CSI from ambient packets via **software-defined radio (Bluebottle)** without controlling the transmitter, using **adaptive PCA** to select motion-relevant principal components. **Authorized RF lab / owned spectrum only** — not unauthorized eavesdrop tradecraft; pairs open-set RF identity research (K326).

## Snippets

> Ambient WiFi CSI + adaptive PCA on SDR enables through-wall motion detection without AP control. [Source: arXiv 2609.12443 abstract]
