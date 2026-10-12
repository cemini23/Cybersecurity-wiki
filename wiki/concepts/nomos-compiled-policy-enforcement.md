---
title: "Compile the policy once; enforce it in code (K288)"
type: concept
tags: [concept, agent-security, k288]
keywords: [2610.11030, K288]
related:
  - sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K288 inbound)"
---

## Relations

- @sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md
- @concepts/intent-governed-tool-authorization.md
- @concepts/mcp-execution-control-invariants.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md

## Raw Concept

Question: **Compile the policy once; enforce it in code** — operator steal from arXiv 2610.11030?

## Narrative

Prompt-level guardrails ask the model to police itself. NOMOS takes the opposite path: **compile a written policy into a deterministic runtime gate** so enforcement is code, not an LLM judgement. The LLM appears in exactly one pass — **EXTRACT**, with an N=5 majority vote — and the **RESOLVE** pass then verifies the extracted rules **statically**; the runtime evaluates each proposed tool call against facts drawn from real tool results and user turns and allows or blocks in **microseconds with zero LLM**.

The measured effect is large: state-changing violations fall **66.3% → 2.6%** and **30.8% → 6.9%** (**26x / 4.5x**), AgentDojo banking **ASR 0.0%** against 46.5% undefended, and **Pass^5 0.51 → 0.67** — the gate does not break the agent. The cost is negligible where it matters: **3 us/call and zero LLM calls** against a prompt-level baseline's **+74% wall-clock and 347 calls**.

The load-bearing caveat is the reason to pair it with a static checker: **RESOLVE repairs 37% and rejects 13% of extracted rules**, so **the generated policy is wrong about a third of the time.** Operator rule: **treat an LLM-written policy as an input to a checker, never as the control itself** — extract with a model, verify statically, enforce deterministically. Pairs K249/intent-governed tool authorization (IGAC) and the MCP execution-control invariants line. Artifact DOI `10.5281/zenodo.22123419`; implementation proprietary.

## Snippets

> See arXiv 2610.11030 abstract. [Source: arXiv 2610.11030 (retrieved 2026-10-12)]
