---
title: "Test-time training for a red-team attacker (K399)"
type: concept
tags: [concept, agent-security, k399]
keywords: [2610.05282, K399]
related:
  - sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K399)"
---

## Relations

- @sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/piminer-agentic-prompt-injection-redteam.md

## Raw Concept

Question: **Test-time training for a red-team attacker** — operator steal from arXiv 2610.05282?

## Narrative

A red-team attacker with frozen weights cannot accumulate anything about the behaviour it is attacking — every signal stays in the prompt. Letting it **train at test time** on the current behaviour beats a budget-matched search baseline (**72.4% vs 55.9%** ASR at 120 samples), needs only sampling access to the victim, and needs no pipeline change. The second, quieter steal is the **objective**: red-teaming success is the *single best* sample, not the average, so a training objective borrowed from alignment work is the wrong shape. Authorised lab only, owned or procured models; no attack code or jailbreak bodies in the wiki.

## Snippets

> See arXiv 2610.05282 abstract. [Source: arXiv 2610.05282 (retrieved 2026-10-06)]
