---
title: Partition–Prompt–Aggregate — statistical self-consistency in LLMs (arXiv 2607.15277)
type: source
tags: [source, arxiv, evaluation, self-consistency, icl, ood-lite]
keywords: [2607.15277, macro fallacy, statistical self-consistency, persona prompting, mpi]
related:
  - concepts/llm-statistical-self-consistency-macro-fallacy.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/agent-completion-verification-gates.md"
maturity: draft
read_status: skimmed
created: 2026-07-17
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-17 — eval criterion; primary home CCC; cybersec light note only"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-17_statistical-self-consistency-ood-note.md`, `briefs/2026-07-17_k187-statistical-self-consistency-prod.md`

## Relations

- @concepts/llm-statistical-self-consistency-macro-fallacy.md — cybersec-relevant slice
- Primary methodology → CCC eval lane

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models |
| Authors | Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner |
| Affiliation | MPI-IS; ETH Zürich; ELLIS |
| arXiv | 2607.15277 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15277-partition-prompt-aggregate-statistical-self-cons.pdf` |
| Retrieved | 2026-07-17 |
| Read status | **skimmed** |

## Narrative

If ICL is conditional inference, estimates should obey the law of total probability across population partitions. Authors find widespread violations and the **macro fallacy**: fine-grained persona/subpopulation aggregates often match human references better than direct population prompts. Statistical self-consistency is proposed as a reference-free eval criterion. [Source: abstract]

### Cross-wiki

- **CCC:** primary — eval / persona / survey-simulation hygiene
- **Cybersec:** light — don’t trust single-shot population risk estimates from persona prompting without partition checks

### Phase-0

REFERENCE — no product install.

## Snippets

> "…estimates reconstructed from more fine-grained subpopulation responses are often better aligned with human reference data than direct population-level estimates."
[Source: arxiv-2607.15277 abstract]
