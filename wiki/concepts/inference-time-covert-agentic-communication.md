---
title: "Inference-time covert agentic communication (K359)"
type: concept
tags: [concept, agent-security, k359]
keywords: [2609.24994, K359]
related:
  - sources/arxiv-2609-24994-feedback-coding-covert-agentic-communication.md
  - concepts/inadvertent-context-leakage.md
  - concepts/asleval-privacy-exposure-displacement.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K359)"
---

## Relations

- @sources/arxiv-2609-24994-feedback-coding-covert-agentic-communication.md
- @concepts/inadvertent-context-leakage.md
- @concepts/asleval-privacy-exposure-displacement.md

## Raw Concept

Question: **Inference-time covert agentic communication** — what should operators steal from arXiv 2609.24994?

## Narrative

Multi-agent and tool-using deployments must treat **public-facing model outputs** as potential **covert channels**. Feedback coding enables inference-time signaling without white-box shared statistics. Defensive steal: monitor **benign-output predicates** and channel capacity under realistic agent loops — not refusal alone. **Runtime:** `scripts/k359_covert_agentic_comm_precheck.py`. Lab only.

## Snippets

> Triage from arXiv 2609.24994 abstract. [Source: arXiv 2609.24994 (retrieved 2026-09-23)]
