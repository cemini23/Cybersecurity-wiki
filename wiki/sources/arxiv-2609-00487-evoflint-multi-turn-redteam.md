---
title: "EvoFlint — evolutionary atlas of multi-turn LLM vulnerabilities (arXiv 2609.00487)"
type: source
tags: [source, arxiv, agent-security, red-team, multi-turn, lab-only, k320]
keywords: [2609.00487, EvoFlint, multi-turn red team, MAP-Elites, quality-diversity, HarmBench, phased conversation plans]
related:
  - concepts/evoflint-multi-turn-redteam-atlas.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
phase_0_verdict: "REFERENCE 2026-09-02 — HF space reinforcelabs/EvoFlint WATCH; no attack conversation plans in wiki. Authorized-lab eval only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit.mdc (K320)"
---

## Relations

- @concepts/evoflint-multi-turn-redteam-atlas.md — primary steal (search over strategy archive, not one-off prompts)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities |
| Authors | Feitong Qiao et al. |
| arXiv | 2609.00487 |
| Location | inbox `research to be indexed/arxiv-2609.00487-evoflint-an-evolutionary-atlas-of-multi-turn-llm.pdf` (archive pending) |
| Retrieved | 2026-09-02 |
| Read status | read (abstract + method) |
| Public artifact | HF space `reinforcelabs/EvoFlint`; paper repo at release — WATCH |

## Narrative

**EvoFlint** reframes multi-turn LLM red-teaming as a **search problem**: evolve a **diverse archive** of phased conversation plans (not raw one-off prompts) via LLM-driven mutation/crossover, Pareto fitness over **ASR + peak severity**, and NSLC-nested MAP-Elites over strategy embeddings. A generation-level memory feeds target-model insights back into strategy generation.

**Results (HarmBench-test split, paper):** ASR up to 35.8% Claude Sonnet 4.6, 59.7% GPT-5.4, 94.3% Qwen3-32B; archive organized by risk category exposes coverage gaps in safety training.

**Why filed (K320):** complements single-turn and persuasion evals — multi-turn gradual intent is a distinct failure mode. **Authorized lab only**; no conversation-plan payloads in wiki; pairs `@concepts/psychological-multiturn-jailbreaks.md`, `@concepts/ai-redteam-evidential-ceiling.md`.

## Snippets

> Frontier models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns. [Source: arXiv 2609.00487 abstract]
