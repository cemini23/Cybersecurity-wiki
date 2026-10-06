---
title: "Author representation strategies for zero-shot authorship attribution"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.03531, k395]
related:
  - concepts/authorship-attribution-author-representation.md
  - concepts/osint-for-cybersecurity.md
  - concepts/threat-hunting.md
  - concepts/linguistic-illegibility-llm-security.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K395)"
---

## Relations

## Relations

- @concepts/authorship-attribution-author-representation.md
- @concepts/osint-for-cybersecurity.md
- @concepts/threat-hunting.md
- @concepts/linguistic-illegibility-llm-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Author representation strategies for zero-shot authorship attribution |
| arXiv | 2610.03531 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.03531-author-representation-strategies-for-zero-shot-a.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K395** — authorship attribution (stylometry) asks who wrote a text, from style alone. In the **zero-shot** setting — no task-specific training, just candidate labels — it largely fails: a label-only prompt scores at chance and **degrades as candidates grow** (df3 30.0/43.3/30.0% for Mixtral/Gemma/Qwen, down to df15 **3.3/8.0/7.3%**). The paper's finding is that what matters is the **author representation**, not the prompt: representative writing samples reach **43.3%**, LLM-generated style descriptions **33.3%** (much more compact), and a **two-stage LISA style-embedding** framework **56.6%** (candidate-space reduction k=2 + embedding-dimension selection N=35, P+A) against a 36.6% single-stage baseline. Two operator steasl: **model choice dominates prompt choice** (max prompt spread 16.6 pp vs max model spread 36.6 pp), and LLMs show **selection bias** — with 15 candidates, predictions collapse onto a few authors while others get almost none. Attribution framing only: useful for OSINT / threat-actor writing attribution, and for knowing when a stylometric claim is not supportable. No repo. **No de-anonymisation recipes in wiki.**

## Snippets

> See arXiv 2610.03531 abstract. [Source: arXiv 2610.03531 (retrieved 2026-10-06)]
