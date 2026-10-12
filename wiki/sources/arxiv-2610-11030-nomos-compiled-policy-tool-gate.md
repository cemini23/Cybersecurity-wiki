---
title: "NOMOS: compiling a written agent policy into a deterministic runtime tool-call gate"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.11030, k288]
related:
  - concepts/nomos-compiled-policy-enforcement.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K288 inbound)"
---

## Relations

## Relations

- @concepts/nomos-compiled-policy-enforcement.md
- @concepts/intent-governed-tool-authorization.md
- @concepts/mcp-execution-control-invariants.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | NOMOS: compiling a written agent policy into a deterministic runtime tool-call gate |
| arXiv | 2610.11030 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.11030-nomos-compiled-policy-to-tool-gate.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K288 (inbound, OSINT brief) — compile the policy, gate the call.** NOMOS turns a **written agent policy** into a **deterministic, LLM-free runtime tool-call gate**, and it is the strongest published counter-argument to prompt-level guardrails. Four passes: **PARSE → EXTRACT** (the only LLM pass; N=5 majority vote) **→ RESOLVE** (deterministic static checks: self-blocking reachability, argument-signature consistency, domain satisfiability, state contradictions, write-scope correctness) **→ MATERIALIZE**. The runtime gate evaluates each proposed tool call against **facts taken only from real tool results and user turns** (structural fact provenance) and returns allow/block in **microseconds with zero LLM**.

Results: violations among state-changing calls **66.3% → 2.6%** (airline) and **30.8% → 6.9%** (retail) — **26x** and **4.5x**; **AgentDojo banking ASR 0.0%** (288 pairs) against **46.5% undefended** (a tool filter alone leaves 11.8%); **Pass^5 / Pass^1 0.51 → 0.67**, so the policy does not break the agent. A prompt-level PolicyGuard reimplementation costs **+74% wall-clock and 347 LLM calls** against **3 us/call and zero**. It reproduces on **Llama-3.3-70B** (86.9% → 7.1%) and the compiler runs **on-premise** on gemma-4-26B.

**The caution that matters:** RESOLVE **repairs 37% and rejects 13%** of extracted rules — the generated policy is wrong **about a third of the time**, so policy extraction must be **statically verified, never trusted**. Operator steal: **an LLM-written policy is an input to a checker, not a control.** Artifact DOI `10.5281/zenodo.22123419`; **implementation proprietary, not released.** **No PoC or exploit steps.**

## Snippets

> See arXiv 2610.11030 abstract. [Source: arXiv 2610.11030 (retrieved 2026-10-12)]
