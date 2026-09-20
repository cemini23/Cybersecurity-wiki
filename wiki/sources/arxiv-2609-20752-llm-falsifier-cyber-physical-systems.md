---
title: "LLM-Falsifier — LLMs as falsifiers for cyber-physical systems (arXiv 2609.20752)"
type: source
tags: [source, arxiv, ot, cyber-physical, eval, lab, k350]
keywords: [2609.20752, LLM-Falsifier, STL, signal temporal logic, falsification, ARCH-COMP, CPS]
related:
  - concepts/llm-falsifier-cyber-physical-systems.md
maturity: draft
read_status: read
created: 2026-09-20
updated: 2026-09-20
phase_0_verdict: "REFERENCE 2026-09-20 — CPS falsification methodology; authorized OT lab only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K350)"
---

## Relations

- @concepts/llm-falsifier-cyber-physical-systems.md — K350 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Large Language Models as Falsifiers for Cyber-Physical Systems |
| arXiv | 2609.20752 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.20752-large-language-models-as-falsifiers-for-cyber-ph.pdf |
| Retrieved | 2026-09-20 |
| Read status | read (abstract + triage) |

## Narrative

**LLM-Falsifier** uses LLMs to minimize **STL robustness degree** when searching for counterexamples to formal CPS specifications. Semantic feedback (natural-language I/O names, trajectories, critical-time witnesses) improves sample efficiency vs black-box optimizers. On ARCH-COMP benchmarks, reported wins on 14/21 specs by simulation count — treat budget asymmetry as a measured caveat. **K350** is **authorized OT/CPS lab methodology** — pairs K339 zero-trust robotic fleets. No exploit payloads or plant-specific attack recipes in wiki.

## Snippets

> LLM-Falsifier falsifies STL specifications by minimizing robustness degree with semantic simulator feedback. [Source: arXiv 2609.20752 abstract]

> Outperforms several falsification paradigms on 14/21 ARCH-COMP specs by average simulations to counterexample. [Source: arXiv 2609.20752 abstract]
