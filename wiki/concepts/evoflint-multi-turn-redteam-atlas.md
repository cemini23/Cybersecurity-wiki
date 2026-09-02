---
title: "EvoFlint multi-turn red-team atlas — search over conversation plans (K320)"
type: concept
tags: [concept, agent-security, red-team, multi-turn, lab-only, k320]
keywords: [EvoFlint, multi-turn ASR, evolutionary red team, MAP-Elites, phased conversation plans, HarmBench, quality-diversity archive]
related:
  - sources/arxiv-2609-00487-evoflint-multi-turn-redteam.md
  - concepts/psychological-multiturn-jailbreaks.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/gflowrl-distribution-matching-attacker-rl.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K320)"
---

## Relations

- @sources/arxiv-2609-00487-evoflint-multi-turn-redteam.md — EvoFlint (2609.00487)
- @concepts/psychological-multiturn-jailbreaks.md — multi-turn persuasion surface (K302)
- @concepts/faithful-agent-asr-measurement.md — report ASR with harness/judge configuration

## Raw Concept

Question: **how should we red-team gradual multi-turn harm, not only single-turn jailbreaks?**

## Narrative

Models may refuse a harmful one-shot prompt yet comply when intent arrives **across turns**. **EvoFlint (K320)** treats red-teaming as **quality-diversity search**: maintain an archive of **phased conversation plans**, evolve them, and map failures by **risk category** — not only maximize a scalar ASR.

**Operator steal:**
1. **Report multi-turn ASR with severity** — Pareto over success rate and peak harm; near-misses carry signal.
2. **Archive diversity matters** — one-off wins understate systematic gaps; category-indexed atlases support defense prioritization.
3. **Authorized lab only** — HF `reinforcelabs/EvoFlint` WATCH; no plan payloads in wiki.
4. Pairs K271 faithful ASR — label the judge, split, and adjudication configuration.

## Snippets

> We argue it is better framed as a search problem: discover, organize, and iteratively refine a diverse archive of attack strategies. [Source: arXiv 2609.00487 abstract, paraphrase]
