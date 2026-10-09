---
title: "PatchBench: activation patching, local suppression vs selective repair"
type: source
tags: [source, routed]
keywords: [arXiv 2610.10276]
related:
  - concepts/local-suppression-vs-repair.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/speculative-decoding-safety-asymmetry.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/local-suppression-vs-repair.md — K408-K417 ingest / 2026-10-09
- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
- @concepts/speculative-decoding-safety-asymmetry.md — K408-K417 ingest / 2026-10-09

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PatchBench: activation patching, local suppression vs selective repair |
| Identifier | arXiv 2610.10276 |
| Type | arXiv paper (routed by OSINT K285) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-09 |
| Read status | read (routed brief) |

## Narrative

**A global metric can hide a large local regression.** Activation patching 'repairs' a jailbreak refusal; PatchBench asks whether that is a **selective repair** or **broad local suppression**. It generates **29 neighbours per failure** (paraphrase, translation, punctuation, spelling; benign structural/lexical) and measures two axes: **HNCS** (harmful-neighbour correction) and **BNPS** (benign-neighbour preservation).

**Findings.** AST-style patching gains HNCS but **loses large BNPS** — Qwen-3B **+3.1 HNCS over AlphaSteer yet −27.4 BNPS**; Gemma-4B **58.3 lower BNPS**. And the headline: **MMLU can be flat while local regression is severe** — CAST on Llama-8B shows **MMLU −0.07** but **BNPS −26.3**. Operator steal: **audit the change set, not the metric.** A repair that passes an aggregate benchmark can still have broken a neighbourhood you never measured. Pairs K396 (report sensitivity) and K405 (a change invisible on the quality metric).

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-09)]
