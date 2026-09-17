---
title: "ASLEval — measuring privacy exposure displacement in LLM agent sessions (arXiv 2609.18864)"
type: source
tags: [source, arxiv, agent-security, privacy, eval, audit, k347]
keywords: [2609.18864, ASLEval, privacy exposure displacement, agent sessions, authorization-aware eval]
related:
  - concepts/asleval-privacy-exposure-displacement.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
phase_0_verdict: "REFERENCE 2026-09-17 — session-level privacy eval; no extraction payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K347)"
---

## Relations

- @concepts/asleval-privacy-exposure-displacement.md — K347 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions |
| arXiv | 2609.18864 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.18864-asleval-measuring-privacy-exposure-displacement.pdf |
| Retrieved | 2026-09-17 |
| Read status | read (abstract + triage) |

## Narrative

Agent privacy evals often inspect a **local proxy** (final response, single action, attacker report) and miss unauthorized exposure elsewhere in a multi-step session. **K347 (ASLEval)** defines **privacy exposure displacement** — mismatch between local proxy and **target-grounded session exposure** — and provides an **authorization-aware** framework with pre-registered hidden targets and measurement of all declared visible exits. Pairs K298 covert-channel eval and K271 faithful ASR (session-level, not terminal-only).

## Snippets

> ASLEval measures privacy exposure displacement when local eval proxies miss multi-step session leaks. [Source: arXiv 2609.18864 abstract]
