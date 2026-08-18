---
title: Differential fault injection for LLM code validation (CCC-primary stub)
type: concept
tags: [concept, stub, fault-injection, llm-code, cross-wiki]
keywords: [differential fault injection, FTINJ, off-nominal fidelity, silent data corruption, LLM modernization]
related:
  - concepts/llm-code-review-agent-security.md
  - "@ccc-wiki/concepts/differential-fault-injection-llm-modernization.md"
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@concepts/llm-code-review-agent-security.md` — LLM code-review security posture
- `@ccc-wiki/concepts/differential-fault-injection-llm-modernization.md` — **primary**
- `@ccc-wiki/sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md`

## Raw Concept

Cross-wiki stub for off-nominal validation of LLM-transformed code (differential fault injection, arXiv 2608.14527). Verification depth lives in CCC.

## Narrative

Differential fault injection validates LLM-modernized code beyond nominal tests: inject identical deterministic faults into original and modernized implementations at shared driver sites and compare paired responses. Surfaces silent-data-corruption, false convergence under reduced precision, and rank-local parallel deadlocks. Transferable lesson for security tooling: nominal test suites don't exercise off-nominal fault response; match harness + compiler config to avoid false diffs. **NO-GO** deepen here — follow CCC K284. [Source: arXiv:2608.14527]
