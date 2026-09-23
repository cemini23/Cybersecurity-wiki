---
title: "LLM vulnerability repair metrics audit (K363)"
type: concept
tags: [concept, agent-security, k363]
keywords: [2609.26749, K363]
related:
  - sources/arxiv-2609-26749-llm-vulnerability-repair-metrics-failure.md
  - concepts/llm-decompiler-recompilability-fidelity.md
  - concepts/llm-codegen-prompt-security-redistribution.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K363)"
---

## Relations

- @sources/arxiv-2609-26749-llm-vulnerability-repair-metrics-failure.md
- @concepts/llm-decompiler-recompilability-fidelity.md
- @concepts/llm-codegen-prompt-security-redistribution.md

## Raw Concept

Question: **LLM vulnerability repair metrics audit** — what should operators steal from arXiv 2609.26749?

## Narrative

LLM patch benchmarks that reward **compilable but wrong** fixes inflate progress. **K363** requires **change-aware** validation and semantic checks before treating repair ASR as meaningful. HITL before shipping auto-patch pipelines in prod or client engagements.

## Snippets

> Triage from arXiv 2609.26749 abstract. [Source: arXiv 2609.26749 (retrieved 2026-09-23)]
