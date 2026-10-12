---
title: "From identification to discovery: holistic RF fingerprinting via learning-aided quantization"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.05979, k419]
related:
  - concepts/holistic-rffi-open-world-discovery.md
  - concepts/horffi-high-openness-rffi.md
  - concepts/wifi-rf-fingerprinting-open-set.md
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/rf-fingerprint-temperature-drift.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K419)"
---

## Relations

## Relations

- @concepts/holistic-rffi-open-world-discovery.md
- @concepts/horffi-high-openness-rffi.md
- @concepts/wifi-rf-fingerprinting-open-set.md
- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/rf-fingerprint-temperature-drift.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From identification to discovery: holistic RF fingerprinting via learning-aided quantization |
| arXiv | 2610.05979 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.05979-from-identification-to-discovery-holistic-rf-fin.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K419 — one expandable representation for identify, reject, and discover.** Radio-frequency fingerprint identification (RFFI) authenticates a transmitter from hardware impairments in the analog waveform, but existing pipelines treat the three tasks as separate components: **closed-set identification** (name a registered device), **open-set recognition** (OSR — reject an unknown one), and **novel-class discovery** (NCD — organise rejected signals into new identities). The paper unifies them by casting RFFI as **vector quantization in a learned latent space**: registered devices are **labeled codewords**, closed-set is codeword assignment, OSR is an uncertainty from **codebook geometry**, and NCD reuses the **continuous** open-set score to cluster rejected samples into new devices.

Numbers (LoRa and Wi-Fi datasets): closed-set accuracy **97.9%** at ten devices; with **five unseen devices** it correctly associates **81.8%** of held-out samples to their new identities (vs **80.4%** for GCD and **18.6%** for OpenNCD); with **seven rogue transmitters** new-device accuracy **90.3%** (vs 78.7% / 40.0%); total accuracy after registration **91.1-92.6%**. It is cheap — **~5 MFLOPs/frame**, **>99.9%** in the convolutional feature extractor. Repo `github.com/omer-hazan/RFFI-with-GCD-via-VQVAE`; licence not stated.

The design lesson is the coupling: **binarising the OSR decision early destroys the information NCD needs.** Operator steal: an unauthorized-transmitter detector should keep the **continuous novelty score**, and a single codebook lets a system detect unknowns *and* name them as new devices without retraining. Authorized RF lab only.

## Snippets

> See arXiv 2610.05979 abstract. [Source: arXiv 2610.05979 (retrieved 2026-10-12)]
