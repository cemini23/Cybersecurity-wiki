---
title: "ASLEval privacy exposure displacement (K347)"
type: concept
tags: [concept, agent-security, privacy, eval, audit, k347]
keywords: [2609.18864, ASLEval, privacy exposure displacement, agent sessions, authorization-aware eval]
related:
  - sources/arxiv-2609-18864-asleval-privacy-exposure-displacement.md
  - concepts/agent-runtime-guardrails.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/inadvertent-context-leakage.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/inference-time-covert-agentic-communication.md
maturity: draft
created: 2026-09-17
updated: 2026-09-17
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K347)"
---

## Relations

- @sources/arxiv-2609-18864-asleval-privacy-exposure-displacement.md — ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions (2609.18864)

## Raw Concept

Question: **ASLEval privacy exposure displacement** — what should operators steal from this paper?

## Narrative

Agent privacy evals often inspect a **local proxy** (final response, single action, attacker report) and miss unauthorized exposure elsewhere in a multi-step session. **K347 (ASLEval)** defines **privacy exposure displacement** — mismatch between local proxy and **target-grounded session exposure** — and provides an **authorization-aware** framework with pre-registered hidden targets and measurement of all declared visible exits. Pairs K298 covert-channel eval and K271 faithful ASR (session-level, not terminal-only).

## Snippets

> ASLEval measures privacy exposure displacement when local eval proxies miss multi-step session leaks. [Source: arXiv 2609.18864 abstract]
