---
title: "EngramEdit: decoupled knowledge updates in LLMs through conditional memory"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.10533, k412]
related:
  - concepts/conditional-memory-knowledge-editing.md
  - concepts/local-suppression-vs-repair.md
  - concepts/agent-execution-provenance.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K412)"
---

## Relations

## Relations

- @concepts/conditional-memory-knowledge-editing.md
- @concepts/local-suppression-vs-repair.md
- @concepts/agent-execution-provenance.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EngramEdit: decoupled knowledge updates in LLMs through conditional memory |
| arXiv | 2610.10533 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.10533-engramedit-decoupled-knowledge-updates-in-llms-t.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K412** — knowledge editing usually fights the model's weights. EngramEdit instead puts updates in a **conditional memory** and reads them back at inference, leaving the base model alone. On CounterFact (2,000 sequential edits) **Efficacy 99.5** and **Generalization 97.0** against pre-edit 9.5 / 11.2, with **Utility 93.9** versus 35.8 — and it beats MoEEdit on Generalization (97.0 vs 67.1) and Memory-FT on Utility.

The most useful result is the **memory-disable test**: after 2,000 edits, disabling the fact-related updated embeddings (~4.7 per fact) turns **89.4%** of previously successful prompts into failures and moves the edit margin from **15.5 to −5.9**, while **matched random disabling** causes **0 failures** and moves the margin by −0.0003. That is a clean demonstration that the edit lives in the **memory**, not in a prompt-level artefact — the control an editing claim usually lacks. Multi-hop is where it gets honest: on MQuAKE **CoT accuracy 25.2** vs 8.5 for fine-tuning, but 2-hop 36.92 falls to 15.09 at 4-hop, and **8.66% of facts sharing an n-gram account for 97.96% of Efficacy failures**. Operator steal: for any model-update claim, **demand a disable test with a random-disabling control** — and expect n-gram collisions to be the failure mode. Pairs K285-a (local suppression is not repair).

## Snippets

> See arXiv 2610.10533 abstract. [Source: arXiv 2610.10533 (retrieved 2026-10-09)]
