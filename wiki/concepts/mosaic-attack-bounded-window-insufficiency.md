---
title: "Mosaic attacks defeat bounded-window defenses (K400)"
type: concept
tags: [concept, agent-security, k400]
keywords: [2610.05346, K400]
related:
  - sources/arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense.md
  - concepts/non-decaying-loop-safety-state.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/linguistic-illegibility-llm-security.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K400)"
---

## Relations

- @sources/arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense.md
- @concepts/non-decaying-loop-safety-state.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/amt-x-phase-structured-multi-turn-red-teaming.md
- @concepts/linguistic-illegibility-llm-security.md

## Raw Concept

Question: **Mosaic attacks defeat bounded-window defenses** — operator steal from arXiv 2610.05346?

## Narrative

The operator rule: **a defence that looks at only the last N turns is not a defence.** For mosaic attacks — each fragment benign alone, harmful assembled — the paper proves no fixed bounded window suffices, because the safety-relevant fragment can be arbitrarily far back. What is required is an **online state mechanism** (a watchman) that carries the distinction forward. Price it honestly: an exact watchman can need exponentially many states, and detecting completeness can need exponentially many black-box queries — but that construction is learnable from labelled examples, so a learned watchman is the practical route. Do not treat **self-play equilibrium** as proof of usefulness; it says nothing about worst-case benign helpfulness. This is the theory under K312's non-decaying loop state.

## Snippets

> See arXiv 2610.05346 abstract. [Source: arXiv 2610.05346 (retrieved 2026-10-06)]
