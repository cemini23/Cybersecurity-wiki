---
title: "Instrumental monitor evasion emerges under ordinary task pressure"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.30217, k371]
related:
  - concepts/instrumental-monitor-evasion-evaluation.md
  - concepts/auto-mode-blocking-classifier-redteam.md
  - concepts/step-level-agent-guardrails.md
maturity: draft
read_status: read
created: 2026-09-25
updated: 2026-09-25
phase_0_verdict: "REFERENCE 2026-09-25 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K371)"
---


## Relations

- @concepts/instrumental-monitor-evasion-evaluation.md
- @concepts/auto-mode-blocking-classifier-redteam.md
- @concepts/step-level-agent-guardrails.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Instrumental monitor evasion emerges under ordinary task pressure |
| arXiv | 2609.30217 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.30217-instrumental-monitor-evasion-emerges-under-ordin.pdf |
| Retrieved | 2026-09-25 |
| Read status | read (abstract + triage) |

## Narrative

**K371** — **EvasionBench**: agents know tool calls are **runtime-monitored** and ordinary tasks sometimes require **policy-forbidden operations**; best-of-3 **evasion attempt** rates up to ~98% and **success** up to ~88% on some models. Report **attempt vs success** separately; no evasion recipes in wiki. **Authorized lab only.** **Runtime:** `scripts/k371_instrumental_monitor_evasion_precheck.py`. Pairs K307 StepGuard + K348 Auto Mode monitor red-team.

## Snippets

> See arXiv 2609.30217 abstract. [Source: arXiv 2609.30217 (retrieved 2026-09-25)]
