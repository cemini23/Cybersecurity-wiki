---
title: CoGate confidence-gated secure code co-decoding
type: concept
tags: [concept, secure-coding, llm, decoding-time]
keywords: [CoGate, co-decoding, expert confidence, CWEval, 2607.28529]
related:
  - sources/arxiv-2607-28529-cogate-secure-code-codecoding.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
  - concepts/cweep-rtl-cwe-early-prevention.md
  - sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md
maturity: draft
created: 2026-07-31
updated: 2026-08-03
---

## Relations

- @sources/arxiv-2607-28529-cogate-secure-code-codecoding.md
- @concepts/llm-code-review-agent-security.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md
- @concepts/cweep-rtl-cwe-early-prevention.md
- @sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md

## Raw Concept

Security-expert co-decoding must gate on expert confidence — preference ≠ trustworthiness under OOD.

## Narrative

Unconfident security experts poison token choices. Gate with entropy-normalized confidence; eval on unseen CWEs. [CONFIRMED abstract; code closed]
