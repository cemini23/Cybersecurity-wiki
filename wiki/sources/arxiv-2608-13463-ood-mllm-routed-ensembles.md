---
title: "OOD — MLLM-routed heterogeneous ensembles for cross-dataset image classification (arXiv 2608.13463)"
type: source
tags: [source, arxiv, ood, image-classification, mllm, routing, generative-ai]
keywords: [2608.13463, ARMDIL, MLLM router, cross-dataset classification, ResNet, DINO, CLIP, ensemble routing, image-domain]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "OOD 2026-08-14 — MLLM-routed heterogeneous image-classification ensemble (ARMDIL). Routed to image-gen wiki. Not cybersec harness wire."
wire_status: wont_wire
wire_target: "OOD — route to image-gen wiki"
---

**Briefs:** `briefs/2026-08-14_ood-mllm-routed-ensembles-route.md`

## Relations

- @concepts/ai-for-cybersecurity.md — general AI-research adjacency only (digest-cycle continuity; fetched in the llm-security paper lane)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification |
| Authors | Daniel Perkins, John Squires, Janou Milligan, Chandra Raskoti, Linda Ungerboeck (UT Knoxville) |
| arXiv | 2608.13463 (cs.CV, v1 13 Aug 2026) |
| Code | None public at retrieval |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.13463-mllm-routed-heterogeneous-ensembles-for-robust-c.pdf` |
| Retrieved | 2026-08-14 |
| Read status | skimmed — OOD |

## Narrative

ARMDIL (Adaptive Router for Multi-Domain Image classification with LLMs): a Gemma-4-12B MLLM agent dynamically routes each image to a specialized vision backbone (ResNet, DINO SSL, CLIP VLM) across five domain aliases (GENERAL/FACIAL/GEOGRAPHIC/MEDICAL/UNSURE) with a unified 38-class head. No cybersec application in scope — cross-domain image classification routing.

**Routed to image-gen wiki** as the primary owner (image classification / model routing / visual-domain ensemble). Cyber holds OOD stub only, `wont_wire`.

## Snippets

> ARMDIL is an ensemble that uses a multi-modal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. [Source: arXiv 2608.13463 abstract]
