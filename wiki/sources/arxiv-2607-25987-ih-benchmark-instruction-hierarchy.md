---
title: IH-Benchmark instruction-hierarchy robustness (arXiv 2607.25987)
type: source
tags: [source, arxiv, instruction-hierarchy, agent-security, prompt-injection]
keywords: [2607.25987, IH-B, S≻U, U≻T, HiddenLayer, tool output conflict]
related:
  - concepts/instruction-hierarchy-conflict-benchmark.md
  - concepts/system-prompt-leakage.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-29
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-29 — release at anonymouslink; wait for public corpus"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-29_k223-ih-benchmark-prod.md`

## Relations

- @concepts/instruction-hierarchy-conflict-benchmark.md
- @concepts/system-prompt-leakage.md
- @concepts/mcp-security-posture.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications |
| Authors | McCauley, Kan, Martin (HiddenLayer) |
| arXiv | 2607.25987 |
| Code | anonymouslink (preprint) — watch for public release |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.25987-textsc-ih-benchmark-a-conflict-centered-benchmar.pdf` |
| Retrieved | 2026-07-29 |

## Narrative

**IH-B**: 2,336 scenarios — S≻U (734) + U≻T (1,602); 44 constraint families; predicate DSL + category-scoped LLM judges. Across 37 models, compliance **98.2% → 20.5%**. Strong S≻U ≠ U≻T robustness. Constraint hardening fixes some failures, not others. Subtle failures (injected disclaimers, small factual distortions) often beat overtly dangerous ones.

### Steal

1. Eval **tool-output conflicts** separately from user jailbreaks
2. Do not use S≻U scores as proxy for MCP/tool robustness
3. Harden for subtle tool-injected instruction overrides, not only purchases/bulk actions

## Snippets

> "strong S ≻ U compliance is not a reliable proxy for U ≻ T robustness"
[Source: arxiv-2607.25987 abstract]
