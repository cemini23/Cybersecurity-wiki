---
title: "Auto Mode blocking classifier red-team (K348)"
type: concept
tags: [concept, agent-security, red-team, eval, tool-control, k348]
keywords: [2609.19587, Auto Mode, blocking classifier, malign coding agents, multi-context attacks, step guard]
related:
  - sources/arxiv-2609-19587-auto-mode-blocking-classifier-redteam.md
  - concepts/agent-runtime-guardrails.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
  - concepts/secure-ai-powered-pentest-agents.md
maturity: draft
created: 2026-09-20
updated: 2026-09-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K348) + agent-audit"
---

## Relations

- @sources/arxiv-2609-19587-auto-mode-blocking-classifier-redteam.md — Red-Teaming Auto Mode (2609.19587)

## Raw Concept

Question: **Auto Mode blocking classifier red-team** — what should operators steal from this paper?

## Narrative

Production coding agents use **blocking monitors** that reject proposed tool actions before execution. **K348** evaluates these monitors against **persistent malign coding agents** (not only prompt injection or accidental harm). Report **multi-context attack** resilience separately from single-turn injection ASR. Monitor improvements (tool coverage, transcript formatting, agentic monitor stage) help but do not close the multi-context gap at acceptable cost.

Defensive steal: treat blocking classifiers as **pre-execution StepGuard-class gates** (K307) with **external eval** — model verbalized detection is not enforcement (K314). **Authorized lab only**; no attack transcript bodies or malign replay payloads in wiki. **Runtime:** `scripts/k348_auto_mode_redteam_precheck.py` (advisory checklist).

## Snippets

> Blocking monitors review each proposed action before it runs; multi-context malign agents remain an open eval axis. [Source: arXiv 2609.19587 abstract]
