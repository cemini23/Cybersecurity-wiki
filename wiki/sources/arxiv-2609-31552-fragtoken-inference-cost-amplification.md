---
title: "FragToken: amplifying LLM inference costs through noncanonical token generation"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.31552, k376]
related:
  - concepts/fragtoken-inference-cost-amplification-lab.md
  - concepts/reliable-inference-procurement-routing.md
maturity: draft
read_status: read
created: 2026-09-28
updated: 2026-09-28
phase_0_verdict: "REFERENCE 2026-09-28 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K376)"
---

## Relations

- @concepts/fragtoken-inference-cost-amplification-lab.md
- @concepts/reliable-inference-procurement-routing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FragToken: amplifying LLM inference costs through noncanonical token generation |
| arXiv | 2609.31552 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.31552-fragtoken-amplifying-llm-inference-costs-through.pdf |
| Retrieved | 2026-09-28 |
| Read status | read (abstract + triage) |

## Narrative

**K376** — tokenizer **decode is not injective**: the same visible text can map to a **longer noncanonical token sequence**, so decoding steps (and billable tokens) can rise without a matching visible-length increase. Paper frames a **training-time / third-party model** supply-chain threat (TIR **1.99–2.46** on four models; utility mostly held). Operator steal: on **owned or procured** models, report **token count vs visible length**; treat unexpected inflation as a **provenance** signal for fine-tunes. **Do not train FragToken. No fragmentation recipes in wiki.** **Runtime:** `scripts/k376_fragtoken_cost_precheck.py`. Pairs K366 reliable-inference procurement.

## Snippets

> See arXiv 2609.31552 abstract. [Source: arXiv 2609.31552 (retrieved 2026-09-28)]
