---
title: "Passive RF UAV controller-only false confirmation (K364)"
type: concept
tags: [concept, agent-security, k364]
keywords: [2609.25294, K364]
related:
  - sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md
  - concepts/through-wall-detection-sdr-pca.md
  - concepts/wifi-har-privacy-perturbation-graw.md
maturity: validated
created: 2026-09-24
updated: 2026-09-24
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K364)"
---

## Relations

- @sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md
- @concepts/through-wall-detection-sdr-pca.md
- @concepts/wifi-har-privacy-perturbation-graw.md

## Raw Concept

Question: **Passive RF UAV controller-only false confirmation** — operator steal from arXiv 2609.25294?

## Narrative

Counter-UAV RF eval needs three cells: **ambient**, **controller-only** (powered RC, aircraft off), **linked**. High clutter/linked accuracy can **mask** controller-only false alarms — use **defer** when FCR constraints trade TPR for precision.
## Snippets

> Controller-only false confirmation: linked-UAV alarm with no aircraft present. [Source: arXiv 2609.25294; K364]