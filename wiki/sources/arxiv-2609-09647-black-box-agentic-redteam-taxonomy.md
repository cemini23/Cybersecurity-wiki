---
title: "Black-Box Red Teaming of Agentic AI — taxonomy-driven risk discovery (arXiv 2609.09647)"
type: source
tags: [source, arxiv, agent-security, red-team, eval, taxonomy, lab-only, k327]
keywords: [2609.09647, black-box red team, agentic AI, seven-domain taxonomy, multi-step eval]
related:
  - concepts/black-box-agentic-redteam-taxonomy.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — taxonomy-driven black-box agent eval; no public repo at hunt."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K327)"
---

## Relations

- @concepts/black-box-agentic-redteam-taxonomy.md — K327 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Black-Box Red Teaming of Agentic AI: A Taxonomy-Driven Framework for Automated Risk Discovery |
| arXiv | 2609.09647 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.09647-black-box-red-teaming-of-agentic-ai-a-taxonomy-d.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

Production agentic systems read untrusted inputs, call privileged tools, and act over multiple steps — yet many evals remain single-turn. **K327** presents a **black-box**, taxonomy-driven framework requiring only basic system descriptions: a **seven-domain taxonomy** maps observable behaviors to risk classes, enabling automated multi-step risk discovery. **Operator steal:** report ASR as `(harness, judge, taxonomy domain, verification mode)`; prefer state-grounded verification over trajectory self-report (pairs K271/K315). **Authorized lab only**; no attack payloads or exploit templates in wiki.

## Snippets

> Seven-domain taxonomy for risk-aware black-box agent evaluation beyond single-turn chat probes. [Source: arXiv 2609.09647 abstract]
