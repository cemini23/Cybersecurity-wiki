---
title: "Distillation defenses easily break after reinforcement learning"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.35699, k381]
related:
  - concepts/distillation-defense-reinforcement-learning-threat-model.md
maturity: draft
read_status: read
created: 2026-09-29
updated: 2026-09-29
phase_0_verdict: "REFERENCE 2026-09-29 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K381)"
---

## Relations

- @concepts/distillation-defense-reinforcement-learning-threat-model.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Distillation defenses easily break after reinforcement learning |
| arXiv | 2609.35699 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.35699-distillation-defenses-easily-break-after-reinfor.pdf |
| Retrieved | 2026-09-29 |
| Read status | read (abstract + triage) |

## Narrative

**K381** — distillation-theft defenses are often scored **right after distillation**, which understates attackers who continue with **reinforcement learning**. Post-distill RL can restore reasoning that looked blocked at the distill checkpoint; simple trace collection from current APIs can match more elaborate hidden-trace theft once RL continues. Operator steal: threat models must include **post-distill RL**; re-eval defenses with **pre- and post-RL** metrics on **owned or procured** models. **No distillation attack recipes in wiki.** **Runtime:** `scripts/k381_distillation_defense_rl_precheck.py`.

## Snippets

> See arXiv 2609.35699 abstract. [Source: arXiv 2609.35699 (retrieved 2026-09-29)]
