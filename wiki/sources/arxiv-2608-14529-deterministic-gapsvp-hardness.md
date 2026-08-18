---
title: "Deterministic poly-factor GapSVP NP-hardness (arXiv 2608.14529)"
type: source
tags: [source, arxiv, pqc, lattice, watch]
keywords: [2608.14529, GapSVP, SVP, Hair, Sahai, lattice PQC, NP-hardness]
related:
  - concepts/lattice-pqc-hardness-watch.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "WATCH 2026-08-18 — no repo URL; do not chase unlicensed clones. SEO K159 overflow routed here."
wire_status: wont_wire
wire_target: none (PQC hardness watch; no ADOPT artifact)
---

**Briefs:** `briefs/2026-08-17_k159-svp-hardness-from-seo.md`

## Relations

- @concepts/lattice-pqc-hardness-watch.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Polynomial-Factor Deterministic NP-Hardness for SVP in Every ℓp Norm with p > 2 |
| Authors | Isaac M Hair, Amit Sahai |
| arXiv | 2608.14529 |
| Code | none located |
| Retrieved | 2026-08-17 (SEO overflow brief); filed 2026-08-18 |

## Narrative

A **deterministic** polynomial-time reduction from 3SAT to M^ε-GapSVP_p for every constant 2 < p < ∞ (and p = ∞) in the stated ε ranges. Builds on OpenAI [Ope26] polynomial-gap CVP and Hair–Sahai [HS26b]. Framed against Ajtai / Regev / Peikert worst-case foundations of lattice PQC.

**Steal.** Removing randomness from the 3SAT → GapSVP reduction tightens the hardness *story* under lattice PQC — track as a watch item, **not an attack**. No clone.

## Snippets

> A deterministic polynomial-time reduction from 3SAT to M^ε-GapSVP_p for every constant 2 < p < ∞. [Source: briefs/2026-08-17_k159-svp-hardness-from-seo.md]
