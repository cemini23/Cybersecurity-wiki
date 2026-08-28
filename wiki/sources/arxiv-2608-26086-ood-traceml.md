---
title: "OOD — TraceML human-agent planning in ML development (arXiv 2608.26086)"
type: source
tags: [source, arxiv, ood, ml-dev, agent-planning, process-trace, bench]
keywords: [2608.26086, TraceML, Kaggle, human-agent planning, process traces, narrow loop, ML development, outcome bench]
related:
  - concepts/trace-verified-ctf-agent-eval.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "OOD 2026-08-28 — ML-development process study, not a security paper. No cyber adopt. Steal: outcome benches hide process. HF dataset `jerryyan/TraceML` — do NOT download."
wire_status: wont_wire
wire_target: "OOD — ML-dev; process-trace contrast for trace-verified eval"
---

## Relations

- @concepts/trace-verified-ctf-agent-eval.md — contrast steal: outcome benches hide the development process

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development |
| Authors | Jiarui Yan, Weiwei Sun, Sijie Li, Wenhan Li, Yiming Yang (CMU) |
| arXiv | 2608.26086 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.26086-traceml-an-empirical-analysis-of-human-agent-pla.pdf` |
| Retrieved | 2026-08-28 |
| Read status | **skimmed** — OOD |
| Public code | HF dataset `huggingface.co/datasets/jerryyan/TraceML` — **do not download** |

## Narrative

**Problem:** outcome-based benchmarks grade the final submission and discard the development process, so they record the human-vs-agent gap but not its cause. **TraceML** pairs human and agent work on the same competitions under a single version-level schema: **4,465 human Kaggle trajectories across 134 competitions**, plus 430 paired human + 207 agent trajectories from two scaffolds. Every code version carries score, timestamp, action, intent, edit size, and score effect.

**Finding:** experts **alternate** data work / validation / model changes / ensembling and **return to set-aside approaches**; each agent scaffold instead **collapses into a narrow loop** (Codex re-weights ensembles; MLE-volve mutates in place) and neither pivots nor reopens abandoned work at the human rate. A **short planning prompt** moves the named behaviors toward the human profile and lifts scores, but the effort profile stays agent-shaped — **instruction closes only the part of the gap that reduces to instructions**.

**Why filed (OOD with one steal):** **outcome benches hide process.** The same critique applies to agentic security evals — a score/flag says nothing about the agent's *process evidence* (pairs the trace-verified CTF-eval concept). **No cyber adopt** — ML-development domain.

## Snippets

> Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. [Source: arXiv 2608.26086 abstract]

> Each agent scaffold instead collapses into a narrow loop … instruction closes only the part of the gap that reduces to instructions. [Source: arXiv 2608.26086 abstract]
