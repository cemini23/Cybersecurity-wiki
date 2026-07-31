---
title: Notes to Self — experiential abstractions for LLMs (arXiv 2607.20372)
type: source
tags: [source, arxiv, llm-memory, abstractions, rl]
keywords: [2607.20372, Notes-to-self, experiential abstractions, MATH-500, GRPO]
related:
  - concepts/experiential-abstraction-memory.md
  - entities/tools/notes-to-self.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-07-23 — github.com/ChangLiu-DrPatient/Notes-to-self ~16MB; Apache-2.0 via vendored verl/LICENSE; root LICENSE absent"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

**Briefs:** `briefs/2026-07-23_k214-notes-to-self-experiential-prod.md`

## Relations

- @concepts/experiential-abstraction-memory.md
- @entities/tools/notes-to-self.md
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Notes to Self: Can LLMs Benefit from Experiential Abstractions? |
| Authors | Chang Liu, Xinyu Li, Artur Dubrawski (CMU Auton Lab) |
| arXiv | 2607.20372 |
| Code | [github.com/ChangLiu-DrPatient/Notes-to-self](https://github.com/ChangLiu-DrPatient/Notes-to-self) |
| Local clone | `raw-sources/repos/Notes-to-self` (~16MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20372-notes-to-self-can-llms-benefit-from-experiential.pdf` |
| Retrieved | 2026-07-23 |

## Narrative

Extract natural-language **experiential abstractions** (strategies / cautions) from MATH training traces into a retrievable library. Modes: (1) inference-time retrieval, (2) RL with abstraction-augmented prompts. Self-extracted ≈ teacher-extracted; transfers across datasets/models.

### Steal (cyber/agent ops)

1. Distill engagement/lab failures into short **caution notes** retrieved into agent context — not full traces
2. Score-gate retrieval to avoid prompt bloat (cf. context pruning)
3. Lab: clone is Apache via `verl/LICENSE`; add root LICENSE note if redistributing

### Phase-0

| Gate | Status |
|------|--------|
| License | **PASS** — Apache-2.0 in `verl/LICENSE` (vendored); root LICENSE missing |
| Size | **PASS** — ~16MB |
| Verdict | **CONDITIONAL-GO** lab (memory/abstraction pipeline) |

## Snippets

> "Self-extracted abstractions match teacher-extracted ones, and our abstraction usage framework can transfer to other datasets and models."
[Source: arxiv-2607.20372 abstract]
