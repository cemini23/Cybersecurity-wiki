---
title: "OOD — self-prompting + cross-model consensus for literature extraction (arXiv 2608.19025)"
type: source
tags: [source, arxiv, ood, eval, science, route]
keywords: [2608.19025, self-prompting, cross-model consensus, HITL, literature extraction]
related:
  - sources/arxiv-2608-17067-ood-disco-t2i-defense.md
  - sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md
  - concepts/ai-redteam-evidential-ceiling.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "OOD 2026-08-20 — science literature extraction. No clone. Steal: consensus ≠ ground truth; HITL on disputed cases."
wire_status: wont_wire
wire_target: none (OOD science pointer)
---

**Briefs:** `briefs/2026-08-20_ood-self-prompting-consensus.md`

## Relations

- @sources/arxiv-2608-17067-ood-disco-t2i-defense.md — sibling OOD this batch
- @sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md — LLM-judge κ / memorized relevance
- @concepts/ai-redteam-evidential-ceiling.md — agreement is not validity

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models |
| Authors | Valentin Romanov, Monique Bax, Steven Niederer (Imperial / Cambridge / Stanford) |
| arXiv | 2608.19025 (cs.AI, v1 19 Aug 2026) CC BY 4.0 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.19025-self-prompting-and-cross-model-consensus-enable.pdf` |
| Retrieved | 2026-08-20 |

## Narrative

**OOD.** Cardiac / organoid literature extraction via browser-frontier LLMs. Four escalating workflows: expert prompt → self-authored prompts → autonomous literature discovery (misses/hallucinated refs) → guideline-driven new datasets that still need HITL. Cyber does not own the domain.

**Steal (one sentence).** Cross-model consensus is a **disagreement flag**, not a ground-truth certificate; experts specify the evidence standard and resolve disputed cases. Autonomous "deep research" agents missed or hallucinated references. Pairs astronomy-OOD (memorized relevance ≠ foresight) and evidential-ceiling. [Source: arXiv 2608.19025]

No clone. `wont_wire`.

## Snippets

> These findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases. [Source: arXiv 2608.19025 abstract]
