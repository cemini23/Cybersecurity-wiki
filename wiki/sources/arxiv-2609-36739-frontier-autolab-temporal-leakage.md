---
title: "Frontier Autolab: organizational memory, adversarial dissent and temporal leakage in multi-agent LLM firms"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.36739, k384]
related:
  - concepts/frontier-autolab-organizational-memory-leakage.md
  - concepts/trajectory-context-control.md
  - concepts/salami-collusive-memory-poisoning.md
maturity: draft
read_status: read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: "REFERENCE 2026-09-30 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K384)"
---

## Relations

## Relations

- @concepts/frontier-autolab-organizational-memory-leakage.md
- @concepts/trajectory-context-control.md
- @concepts/salami-collusive-memory-poisoning.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Frontier Autolab: organizational memory, adversarial dissent and temporal leakage in multi-agent LLM firms |
| arXiv | 2609.36739 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.36739-frontier-autolab-organizational-memory-adversari.pdf |
| Retrieved | 2026-09-30 |
| Read status | read (abstract + triage) |

## Narrative

**K384** — multi-agent LLM systems are structured like firms but evaluated on minute-long tasks. **Frontier Autolab** runs one simulated firm (16 personas + a Red Team) through nine temporally gated eras, 1990–2040; a historian-judge reveals outcomes and scores a five-dimension rubric; lessons enter a persistent Playbook. Across four trajectories (36 era decisions, 180 subscores): a **foresight–commitment gap** in **24/24** historically scored eras (mean gap **1.88**, SD 0.80) — the judge rated recognition of the coming shift above the choice of where to build. Design shaped character: a Red Team with numeric **kill gates** produced fifty simulated years of gated pilots and **no product**, yet scored the highest. The paper also shows why the numbers are hard to trust: published totals rise across eras while the judge's own hindsight subscore falls (within-run **r = −0.58**), confounding apparent learning with recall of history. Operator steal: report a **leakage measure**, **separate the briefing author from the scorer**, compute totals **in code**, and fix the rubric's treatment of **caution** in advance. Repo `github.com/LoopGlitch26/Frontier-Autolab` is **MIT** — REFERENCE (testbed, not a security tool; no clone this batch). **Runtime:** `scripts/k384_frontier_autolab_leakage_precheck.py`. Pairs GT-MCP trajectory-context-control and K238 memory poisoning.

## Snippets

> See arXiv 2609.36739 abstract. [Source: arXiv 2609.36739 (retrieved 2026-09-30)]
