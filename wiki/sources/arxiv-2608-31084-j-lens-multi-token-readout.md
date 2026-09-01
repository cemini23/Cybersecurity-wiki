---
title: "J-lens — verbalizing multi-token concepts for interpretability (arXiv 2608.31084)"
type: source
tags: [source, arxiv, interpretability, audit, agent-security, k318]
keywords: [2608.31084, J-lens, multi-token readout, first token clue, sparse autoencoder, SAE, Neuronpedia, concept verbalization]
related:
  - concepts/multi-token-concept-readout-audit.md
  - concepts/counterfactual-simulatability-llm-explanations.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
phase_0_verdict: "WATCH 2026-09-01 — Neuronpedia integration; audit/interpretability steal only. Not an enforcement boundary."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K318)"
---

## Relations

- @concepts/multi-token-concept-readout-audit.md — primary steal (first-token ≠ full concept)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The First Token Is a Clue: Verbalizing Multi-Token Concepts with J-Lens |
| Authors | (see PDF) |
| arXiv | 2608.31084 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.31084-the-first-token-is-a-clue-verbalizing-multi-toke.pdf |
| Retrieved | 2026-09-01 |
| Read status | read (abstract + method summary) |
| Public artifact | Neuronpedia J-lens integration (WATCH) |

## Narrative

**J-lens** extends sparse-autoencoder (SAE) feature verbalization to **multi-token concepts** by treating the **first generated token as a clue** and iteratively refining a natural-language description of the full concept the feature represents. Standard SAE readouts often collapse multi-token semantics into misleading single-token labels.

**Why filed (K318):** **audit/interpretability** for refusal and safety surfaces — pairs `@concepts/counterfactual-interpretability-audit.md` (K290 CHIVE) and Taboo-style refusal diagnostics. **Not enforcement** — decoded labels do not gate tool execution.

## Snippets

> The first token is a clue … verbalizing multi-token concepts. [Source: arXiv 2608.31084 title/abstract theme]
