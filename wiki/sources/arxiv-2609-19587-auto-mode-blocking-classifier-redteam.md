---
title: "Red-Teaming Auto Mode — blocking classifiers against malign coding agents (arXiv 2609.19587)"
type: source
tags: [source, arxiv, agent-security, red-team, eval, k348]
keywords: [2609.19587, Auto Mode, blocking classifier, malign coding agents, step guard, Claude Code, Codex Guardian]
related:
  - concepts/auto-mode-blocking-classifier-redteam.md
maturity: draft
read_status: read
created: 2026-09-20
updated: 2026-09-20
phase_0_verdict: "REFERENCE 2026-09-20 — blocking-monitor red-team eval; no attack transcripts in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K348) + agent-audit"
---

## Relations

- @concepts/auto-mode-blocking-classifier-redteam.md — K348 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents |
| arXiv | 2609.19587 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.19587-red-teaming-auto-mode-improving-blocking-classif.pdf |
| Retrieved | 2026-09-20 |
| Read status | read (abstract + triage) |

## Narrative

Production coding agents now use **blocking monitors** that review each proposed action before execution (Auto Mode in Claude Code, Guardian in OpenAI Codex). Prior evals focused on accidental harm or untrusted-source hijacks; **K348** red-teams **persistent malign coding agents** — agents that pursue harmful goals across turns. The paper reports **multi-context attacks** as an open problem even after monitor design improvements (tool coverage, transcript formatting, agentic monitor stage). Pairs K307 StepGuard, K314 recognition≠enforcement, and K341 secure pentest agents. **Authorized lab only** — no attack transcript bodies in wiki.

## Snippets

> Production systems review each proposed action with a blocking monitor before it runs (Auto Mode, Guardian). [Source: arXiv 2609.19587 abstract]

> Preventing multi-context attacks at acceptable cost remains an open problem. [Source: arXiv 2609.19587 abstract]
