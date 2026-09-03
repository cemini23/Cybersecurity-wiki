---
title: "WiFi RF fingerprinting — open-set recognition under environment shift (K326)"
type: concept
tags: [concept, wireless, rf-fingerprinting, iot, lab-only, k326]
keywords: [RF fingerprinting, OpenMax, WiFi CSI, open-set recognition, device authentication]
related:
  - sources/arxiv-2609-02007-c2t-openmax-wifi-rf-fingerprinting.md
  - concepts/wireless-pentest.md
  - concepts/horffi-high-openness-rffi.md
  - concepts/hardware-id-masking-opsec.md
maturity: draft
created: 2026-09-03
updated: 2026-09-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K326)"
---

## Relations

- @sources/arxiv-2609-02007-c2t-openmax-wifi-rf-fingerprinting.md — C²T-OpenMax (2609.02007)
- @concepts/wireless-pentest.md — contrast: offensive WLAN tradecraft vs device-auth ML

## Raw Concept

Question: **how does open-set RF fingerprinting behave when environments shift?**

## Narrative

**RF fingerprinting (RFF)** authenticates transmitters from hardware imperfections. Practical deployment needs **open-set** recognition across environments — unknown devices must be rejected, known devices recognized under location/channel drift.

**K326 (C²T-OpenMax)** refines OpenMax with **center-constrained learning** (tighter known-class geometry) and **confidence-guided tail modeling** (high-confidence logits for Weibull fits). Evaluated on public **WiFi CSI** data with strong open-set metrics vs augmented OpenMax.

**Operator steal:** useful for **owned-lab spectrum monitoring / device inventory** awareness — not a substitute for WPA cracking or rogue-AP pentest methodology. **Authorized RF lab only** on owned/authorized spectrum.

## Snippets

> C²T-OpenMax achieves highest open-set accuracy in seven of eight location groups on public WiFi CSI dataset. [Source: arXiv 2609.02007 abstract, paraphrase]
