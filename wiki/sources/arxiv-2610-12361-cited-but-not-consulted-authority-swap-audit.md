---
title: "Cited but not consulted: a counterfactual audit of legal authority use"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.12361, k416]
related:
  - concepts/citation-is-not-consultation.md
  - concepts/compliance-verdict-rule-invariance.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K416)"
---

## Relations

- @concepts/citation-is-not-consultation.md — K408-K417 ingest / 2026-10-09
## Relations

- @concepts/compliance-verdict-rule-invariance.md
- @concepts/compliance-boundary-adjacent-pair-search.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cited but not consulted: a counterfactual audit of legal authority use |
| arXiv | 2610.12361 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.12361-cited-but-not-consulted-a-counterfactual-audit-o.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K416 — the citation is not the consultation.** Models justify legal decisions by **naming the statute or precedent**, and that naming is treated as evidence the decision follows from it. The audit substitutes the named authority for an **unrelated one**, holds the case facts fixed, and **decodes the verdict from hidden states** rather than waiting for the output. Across seven open-weight models (8B–70B) and four benchmarks spanning judicial and contractual reasoning, the verdict often does not track the swapped authority. Same lab as K415 (Lexsi Labs) and the same shape of finding: the **stated ground** and the **operative ground** are different things. Operator steal: **never accept a citation as proof of reliance** — perturb the cited authority and watch the decision, and prefer a hidden-state read over the model's own account of why. Pairs K415, K398 and K396. Research and audit framing only.

## Snippets

> See arXiv 2610.12361 abstract. [Source: arXiv 2610.12361 (retrieved 2026-10-09)]
