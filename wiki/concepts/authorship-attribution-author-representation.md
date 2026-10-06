---
title: "Authorship attribution needs an author representation (K395)"
type: concept
tags: [concept, agent-security, k395]
keywords: [2610.03531, K395]
related:
  - sources/arxiv-2610-03531-authorship-attribution-zero-shot-representations.md
  - concepts/osint-for-cybersecurity.md
  - concepts/threat-hunting.md
  - concepts/linguistic-illegibility-llm-security.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K395)"
---

## Relations

- @sources/arxiv-2610-03531-authorship-attribution-zero-shot-representations.md
- @concepts/osint-for-cybersecurity.md
- @concepts/threat-hunting.md
- @concepts/linguistic-illegibility-llm-security.md

## Raw Concept

Question: **Authorship attribution needs an author representation** — operator steal from arXiv 2610.03531?

## Narrative

Asking an LLM 'who wrote this, from these names?' is near-chance and gets worse as the candidate list grows. What moves the number is the **representation of each candidate author**: writing samples, an LLM-written style description, or a style embedding. Style embeddings with a **two-stage** reduce-then-select step scored best (56.6%). Carry two cautions: **model choice matters more than prompt wording** (36.6 pp vs 16.6 pp spread), and models concentrate predictions on a few candidates as the task hardens — a confident label from a flat-looking distribution can still be selection bias, not evidence. Use for OSINT attribution support, not as a forensic conclusion.

## Snippets

> See arXiv 2610.03531 abstract. [Source: arXiv 2610.03531 (retrieved 2026-10-06)]
