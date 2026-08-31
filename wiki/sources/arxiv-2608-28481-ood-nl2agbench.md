---
title: "OOD — NL2AGBench geometry auto-formalization for AlphaGeometry (arXiv 2608.28481)"
type: source
tags: [source, arxiv, ood, mathematics, auto-formalization, benchmark]
keywords: [2608.28481, NL2AGBench, AlphaGeometry, auto-formalization, geometry DSL, execution-based verification]
related:
  - concepts/nl-to-ltl-requirements-llm.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
phase_0_verdict: "OOD 2026-08-31 — Olympiad geometry NL→DSL benchmark; not cyber-primary. Steal: execution-based verification for formal translation (pairs NL→LTL HITL pattern). No cyber adopt."
wire_status: wont_wire
wire_target: "OOD — math formalization; contrast for nl-to-ltl-requirements-llm"
---

## Relations

- @concepts/nl-to-ltl-requirements-llm.md — parallel steal: NL→formal spec needs human/solver verify, not text similarity alone

## Raw Concept

| Field | Value |
|-------|-------|
| Title | NL2AGBench: Benchmarking LLM Auto-Formalization for AlphaGeometry |
| Authors | Samuel Xiao, Judy Song, Rory Hu, Ziliang Zong (Texas State University) |
| arXiv | 2608.28481 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.28481-nl2agbench-benchmarking-llm-auto-formalization-f.pdf |
| Retrieved | 2026-08-31 |
| Read status | **skimmed** — OOD |
| Public code | benchmark from JGEX/AlphaGeometry formalized problems; no cyber wire |

## Narrative

**NL2AGBench** evaluates LLMs translating English geometry problems into **AlphaGeometry's domain-specific language**, scored by **execution within AlphaGeometry** (not BLEU/text similarity). 48 problems from 231 manually formalized JGEX instances. Frontier closed-source models exceed **80%** executable translation; largest open-source models struggle (**<46%** even with optimized prompting). Error taxonomy: syntax vs logic failures.

**Why filed (OOD with one steal):** geometry auto-formalization is **not cyber-primary** (math/education/neuro-symbolic). One steal for this wiki: **execution-based verification beats textual similarity** for NL→formal pipelines — same pattern as `@concepts/nl-to-ltl-requirements-llm.md` (human + solver verify; do not treat single-shot NL formalization as authority). No clone; no weight downloads.

## Snippets

> NL2AGBench evaluates translation quality using execution-based verification within the AlphaGeometry framework rather than relying solely on textual similarity metrics. [Source: arXiv 2608.28481 abstract]
