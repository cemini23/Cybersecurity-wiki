---
title: "Reflections and fragments: securing LLMs against sequential mosaic attacks"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.05346, k400]
related:
  - concepts/mosaic-attack-bounded-window-insufficiency.md
  - concepts/non-decaying-loop-safety-state.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/linguistic-illegibility-llm-security.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K400)"
---

## Relations

## Relations

- @concepts/mosaic-attack-bounded-window-insufficiency.md
- @concepts/non-decaying-loop-safety-state.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/amt-x-phase-structured-multi-turn-red-teaming.md
- @concepts/linguistic-illegibility-llm-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reflections and fragments: securing LLMs against sequential mosaic attacks |
| arXiv | 2610.05346 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.05346-reflections-and-fragments-securing-llms-against.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K400 — the strongest theory result of the batch.** A **mosaic attack** is a multi-turn sequence whose individual fragments are innocuous in isolation and assemble into a harmful payload. The paper formalises mosaic defence as a finite extensive-form game with imperfect information and proves the result that matters operationally: **no fixed bounded window of recent prompts is sufficient in general** — safety-relevant information may sit arbitrarily far back. It then introduces a **watchman**, an online state mechanism carrying that information forward, and shows that under explicit assumptions it gives **zero-failure defence with positive benign helpfulness**, and under stronger conditions is optimal among zero-failure defenders. The cost is priced too: an exact watchman can need **exponentially many states**, and exact maliciousness detection **exponentially many queries** in an unstructured black-box model — though the construction behind the state bound is *efficiently learnable from labelled examples*, while certifying worst-case safety needs far more under restricted access. Also: **self-play equilibrium alone does not certify usefulness**, motivating a constrained formulation that maximises worst-case benign helpfulness among zero-failure defenders. Empirically, role-specific attacker/defender **LoRA adapters** over frozen LLMs trained by multi-turn self-play strengthen **both** roles, including against unseen objectives. Operator steal: **a bounded-window or per-turn session guard is not a defence** — this is the formal companion to K312's non-decaying loop state. Pairs K312, Crescendo, AMT-X. **No attack fragments or payloads in wiki.**

## Snippets

> See arXiv 2610.05346 abstract. [Source: arXiv 2610.05346 (retrieved 2026-10-06)]
