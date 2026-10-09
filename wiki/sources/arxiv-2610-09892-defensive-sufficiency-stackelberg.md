---
title: "Defensive sufficiency in a Stackelberg model of AI security"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.09892, k409]
related:
  - concepts/defensive-sufficiency-feedback-loop.md
  - concepts/cross-task-no-regression-skill-promotion-gate.md
  - concepts/local-suppression-vs-repair.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K409)"
---

## Relations

## Relations

- @concepts/defensive-sufficiency-feedback-loop.md
- @concepts/cross-task-no-regression-skill-promotion-gate.md
- @concepts/local-suppression-vs-repair.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Defensive sufficiency in a Stackelberg model of AI security |
| arXiv | 2610.09892 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.09892-defensive-sufficiency-in-a-stackelberg-model-of.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K409 — when does the test → repair → update loop actually give you security?** The paper answers with three conditions over a **finite attack surface**: every unresolved attack keeps a **persistent chance of discovery** (epsilon), **repairs are effective**, and **updates preserve earlier protection**. Under those, the surface is defended with probability 1 — **P(T > t) ≤ min{{1, N(1−epsilon)^t}}** and **E[T] ≤ N/epsilon**, so coverage time for probability 1−delta is **t ≥ log(N/delta)/epsilon**. The third condition is the one operators break: an update that fixes today's failure while reopening yesterday's resets the clock.

The second result is structural and surprising: **repair regions, not singletons.** Region-level expected completion time is **m·H_m** against **N·H_N** for singleton repairs (N = m·r, r > 1) — fixing a *class* of failures is asymptotically far cheaper than fixing each instance. The rest is an economic model (attacker cost kappa, discovery rate eta) for **when investing in the feedback loop is worth it at all**, with simulation matching the theory to within a fraction of a point. Operator steal: a red-team program is only a control if **findings persist, repairs hold, and updates do not regress** — and repairing a category beats repairing the case. Pairs K390 (the no-regression promotion gate) and K285-a (local suppression is not repair).

## Snippets

> See arXiv 2610.09892 abstract. [Source: arXiv 2610.09892 (retrieved 2026-10-09)]
