---
title: "OOD — historical backtesting for scientific question discovery (arXiv 2608.16795)"
type: source
tags: [source, arxiv, ood, eval, astronomy, route]
keywords: [2608.16795, historical backtesting, LLM-judge kappa, temporal leakage, memorized relevance]
related:
  - sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "OOD 2026-08-18 — astronomy/science-eval protocol. Route to CCC science-eval. Do not clone astronomy corpora. Steal one sentence for cyber eval hygiene."
wire_status: wont_wire
wire_target: none (OOD pointer)
---

**Briefs:** `briefs/2026-08-18_ood-astronomy-backtesting-route.md`

## Relations

- @sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md — sibling OOD stub this batch
- @concepts/ai-redteam-evidential-ceiling.md — judge-agreement ≠ validity
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot |
| arXiv | 2608.16795 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.16795-historical-backtesting-for-scientific-question-d.pdf` |
| Retrieved | 2026-08-18 |
| Read status | read (skim + steal) |

## Narrative

**OOD.** Astronomy / science-eval protocol: freeze a historical cutoff, generate questions from pre-cutoff literature only, grade with post-cutoff literature the generator never saw. The protocol contains no question generator.

**Steal (one sentence).** LLM-judge agreement ≠ taxonomy validity (model–model agreement overstated reliability ~3× vs a seven-rater study); **memorized relevance ≠ foresight**. Temporal leakage is the eval bug.

No astronomy clone. CCC owns science-eval depth if they ingest. Cyber `wont_wire`.

## Snippets

> LLM-only generation shows memorized relevance without specific foresight. [Source: arXiv 2608.16795]
