---
title: DrawnApart — remote GPU fingerprinting (NDSS 2022)
type: source
tags: [source, arxiv, gpu, browser-fingerprint, privacy]
keywords: [2201.09956, DrawnApart, GPU execution units, NDSS 2022, Laperdrix]
related:
  - concepts/hardware-id-masking-opsec.md
  - sources/arxiv-1905-01051-browser-fingerprinting-survey.md
  - "@osint-wiki/entities/tools/fingerprint-suite.md"
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — attack paper; GitHub artifact exists; NO-GO clone (tracker, not OPSEC tool)"
wire_status: wont_wire
wire_target: "Do not clone drawnapart/drawnapart — steal the lesson only"
---

## Relations

- @concepts/hardware-id-masking-opsec.md — manufacturing variation survives software ID changes
- @sources/arxiv-1905-01051-browser-fingerprinting-survey.md — browser-fingerprint context
- @osint-wiki/entities/tools/fingerprint-suite.md — adjacent web-fingerprint lane

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DRAWN APART: A Device Identification Technique based on Remote GPU Fingerprinting |
| Authors | Laor, Mehanna, Durey, Dyadyuk, Laperdrix, Maurice, Oren, Rouvoy, Rudametkin, Yarom |
| arXiv | 2201.09956 |
| Venue | NDSS 2022 |
| Code | https://github.com/drawnapart/drawnapart (do not adopt) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2201.09956-drawn-apart-gpu-fingerprinting.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

Unprivileged JavaScript times GPU execution units; manufacturing differences distinguish **nominally identical** hardware/software configs that ordinary browser fingerprints collapse. Crowd-sourced ~2,500 devices / months of data: up to **67%** boost in median tracking duration vs Vastel et al. S&P 2018 linking. [CONFIRMED abstract]

OPSEC steal: two “identical” lab laptops are not identical to a website. Changing MachineGuid does not change GPU EU timing. Do not clone the artifact into the operator toolkit.

## Snippets

> "we show that variations in speed among the multiple execution units that comprise a GPU can serve as a reliable and robust device signature, which can be collected using unprivileged JavaScript."
[Source: arxiv-2201.09956 abstract]
