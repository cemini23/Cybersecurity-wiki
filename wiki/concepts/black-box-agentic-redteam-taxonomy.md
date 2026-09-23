---
title: "Black-box agentic red-team taxonomy (K327)"
type: concept
tags: [concept, agent-security, red-team, eval, taxonomy, lab-only, k327]
keywords: [2609.09647, black-box red team, agentic AI, seven-domain taxonomy, multi-step eval]
related:
  - sources/arxiv-2609-09647-black-box-agentic-redteam-taxonomy.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/security-agent-authority-auditability-slr.md
  - concepts/evoflint-multi-turn-redteam-atlas.md
  - concepts/agent-runtime-guardrails.md
  - concepts/secure-ai-powered-pentest-agents.md
  - concepts/cross-dimensional-agentic-ai-security-taxonomy.md
  - sources/arxiv-2609-23894-agentic-ai-cross-dimensional-taxonomy.md
maturity: draft
created: 2026-09-11
updated: 2026-09-16
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K327)"
---

## Relations

- @sources/arxiv-2609-09647-black-box-agentic-redteam-taxonomy.md — Black-Box Red Teaming of Agentic AI: A Taxonomy-Driven Framework for Automated Risk Discovery (2609.09647)

## Raw Concept

Question: **Black-box agentic red-team taxonomy** — what should operators steal from this paper?

## Narrative

Production agentic systems read untrusted inputs, call privileged tools, and act over multiple steps — yet many evals remain single-turn. **K327** presents a **black-box**, taxonomy-driven framework requiring only basic system descriptions: a **seven-domain taxonomy** maps observable behaviors to risk classes, enabling automated multi-step risk discovery. **Operator steal:** report ASR as `(harness, judge, taxonomy domain, verification mode)`; prefer state-grounded verification over trajectory self-report (pairs K271/K315). **Authorized lab only**; no attack payloads or exploit templates in wiki.

## Snippets

> Seven-domain taxonomy for risk-aware black-box agent evaluation beyond single-turn chat probes. [Source: arXiv 2609.09647 abstract]
