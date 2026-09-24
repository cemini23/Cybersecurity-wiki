---
title: "Through-wall detection via ambient WiFi CSI (K344)"
type: concept
tags: [concept, wireless, rf, lab-only, defensive, k344]
keywords: [2609.12443, through-wall detection, SDR, CSI, PCA, ambient WiFi]
related:
  - sources/arxiv-2609-12443-through-wall-detection-sdr-pca.md
  - concepts/wifi-rf-fingerprinting-open-set.md
  - concepts/side-sensor-impersonation-edge-detection.md
  - concepts/horffi-high-openness-rffi.md
  - concepts/wifi-har-privacy-perturbation-graw.md
  - sources/arxiv-2609-24173-graw-wifi-har-privacy-perturbation.md
  - concepts/passive-rf-uav-controller-only-false-confirmation.md
  - sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md
maturity: draft
created: 2026-09-17
updated: 2026-09-17
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K344)"
---

## Relations

- @sources/arxiv-2609-12443-through-wall-detection-sdr-pca.md — Through-Wall Detection using Software-Defined Radio based on adaptive Principal Component Analysis (2609.12443)

## Raw Concept

Question: **Through-wall detection via ambient WiFi CSI** — what should operators steal from this paper?

## Narrative

**Through-wall detection (TWD)** using ambient WiFi CSI enables non-invasive sensing for security and rescue. **K344** extracts CSI from ambient packets via **software-defined radio (Bluebottle)** without controlling the transmitter, using **adaptive PCA** to select motion-relevant principal components. **Authorized RF lab / owned spectrum only** — not unauthorized eavesdrop tradecraft; pairs open-set RF identity research (K326).

## Snippets

> Ambient WiFi CSI + adaptive PCA on SDR enables through-wall motion detection without AP control. [Source: arXiv 2609.12443 abstract]
