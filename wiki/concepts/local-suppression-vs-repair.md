---
title: "Local suppression is not repair (K285-a)"
type: concept
tags: [concept, agent-security, k285-a]
keywords: [arXiv 2610.10276 / 2610.10345, K285-a]
related:
  - sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md
  - sources/arxiv-2610-10345-sldr-signed-layer-safety-repair.md
  - sources/arxiv-2610-10276-patchbench-local-suppression-vs-repair.md
  - sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md
  - concepts/defensive-sufficiency-feedback-loop.md
  - concepts/conditional-memory-knowledge-editing.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/speculative-decoding-safety-asymmetry.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K285-a)"
---

## Relations

- @sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-10345-sldr-signed-layer-safety-repair.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-10276-patchbench-local-suppression-vs-repair.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md — K408-K417 ingest / 2026-10-09
- @concepts/defensive-sufficiency-feedback-loop.md — K408-K417 ingest / 2026-10-09
- @concepts/conditional-memory-knowledge-editing.md — K408-K417 ingest / 2026-10-09
- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
- @concepts/speculative-decoding-safety-asymmetry.md — K408-K417 ingest / 2026-10-09

## Raw Concept

Question: **Local suppression is not repair** — operator steal from the inbound brief (arXiv 2610.10276 / 2610.10345)?

## Narrative

When a model refusal is 'fixed' by activation patching, two very different things may have happened: the harmful behaviour was **selectively repaired**, or a broad neighbourhood was **suppressed** — which also damages benign behaviour that happened to sit nearby.

Measure it **locally**, not globally: generate neighbours of the failure and score **harmful-neighbour correction** against **benign-neighbour preservation**. PatchBench's numbers show why a global benchmark is not enough — **MMLU moved −0.07 while BNPS fell 26.3**. The constructive counterpart is SLDR: safety sensitivity across layers is **signed**, so repair the extreme layers and **route only the affected traffic**, giving Harmful Score **11.54 → 0.08** at near-zero accuracy cost. Rule: **a repair claim needs a neighbourhood test, and the narrowest repair is usually the right one.**

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-09)]
