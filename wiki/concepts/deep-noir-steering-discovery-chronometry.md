---
title: "Deep Noir steering discovery and security audit (K349)"
type: concept
tags: [concept, agent-security, interpretability, steering, audit, k349]
keywords: [2609.20722, Deep Noir, activation steering, architectural chronometry, logit lens, inference-time intervention]
related:
  - sources/arxiv-2609-20722-deep-noir-steering-discovery-chronometry.md
  - concepts/agent-runtime-guardrails.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-09-20
updated: 2026-09-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K349)"
---

## Relations

- @sources/arxiv-2609-20722-deep-noir-steering-discovery-chronometry.md — Deep Noir (2609.20722)

## Raw Concept

Question: **Deep Noir steering discovery** — what should security operators steal?

## Narrative

**Deep Noir** automates **activation steering** discovery using Logit Lens chronometry and causal head attribution. For security eval, treat steering as an **integrity boundary**: automated discovery improves utility tasks but **does not prove safety** without counterfactual tests (pairs K290 CHIVE, K318 J-lens). As steering integrates into agent stacks, audit **who can set steering vectors**, **persistence across sessions**, and **bypass of external StepGuard gates** (K307/K348).

**Audit-only** — no clamp recipes, no steering payload bodies in wiki. REFERENCE until public SPDX artifact verified.

## Snippets

> Automated steering discovery generalizes across tasks but security properties of steering interventions need explicit audit. [Source: arXiv 2609.20722 triage]
