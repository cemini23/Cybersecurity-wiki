---
title: "Labels are not endpoints — measurement integrity in MCP security eval (2608.12880)"
type: source
tags: [source, arxiv, mcp, evaluation, measurement, k277]
keywords: [2608.12880, labels not endpoints, integrity chain, treatment-blind grading, MCP eval]
related:
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/mcp-security-posture.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: skimmed
---

## Relations

- @concepts/measurement-integrity-mcp-security-eval.md — cyber synthesis
- @concepts/mcp-security-posture.md — MCP eval claims must bind treatment bytes + outcome rule
- @ccc-wiki/sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md — primary ingest (CCC K277)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12880 — labels ≠ behavioral endpoints in MCP security evaluation |
| Retrieved | 2026-08-14 via CCC → `briefs/2026-08-14_k277-k281-from-ccc.md` |
| Dual-ID | CCC **K277**; Cybersec **K277** is RSM (2608.12311) — resolve by file+wiki |

## Narrative

A security-eval label ("attack") is a claim over **treatment bytes, executed behavior, authorization, outcome rule, and analysis unit**. Bind all five before interpreting rates. Treatment-blind grading is necessary, not sufficient — codebook ambiguity survives it. Seven-link Integrity Chain: a failed link halt-closes the stated inference. A campaign measurement audit is not a population attack-rate, model-ranking, defense-efficacy, or causal estimate. Pairs faithful ASR (K271) and ATOBench process-level evidence (Cybersec K278). [Source: arXiv:2608.12880]
