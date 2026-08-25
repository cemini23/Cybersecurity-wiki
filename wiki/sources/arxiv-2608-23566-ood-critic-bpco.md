---
title: "OOD — How to Train a Critic Stably and Efficiently / BPCO (arXiv 2608.23566)"
type: source
tags: [source, arxiv, ood, rl, critic, grpo, trainer, bpco]
keywords: [2608.23566, BPCO, golden_critic, GRPO alternative, critic-based RL, DPPO, length-adaptive GAE, single-rollout]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/ai-pentest-harness-landscape.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "OOD 2026-08-25 — RL-trainer paper (critic-based alternative to GRPO), not a cyber harness. golden_critic REFERENCE clone (Apache-2.0, ~14MB) under .local/adopts — wont_wire; no GRPO-style trainer wired as harness; no weight dumps."
wire_status: wont_wire
wire_target: "OOD — RL trainer; pairs existing no-GRPO-as-wired-harness policy"
---

## Relations

- @concepts/ai-for-cybersecurity.md — contrast only (RL training machinery, no cyber runtime)
- @concepts/ai-pentest-harness-landscape.md — harness-adoption contrast; this is a trainer, not a pentest harness

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How to Train a Critic Stably and Efficiently |
| Authors | Penghui Qi (NUS), Xiangxin Zhou (Tencent Hunyuan), Wee Sun Lee (NUS) |
| arXiv | 2608.23566 (12 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.23566-how-to-train-a-critic-stably-and-efficiently.pdf` |
| Retrieved | 2026-08-25 |
| Read status | **skimmed** — OOD |
| Public code | `github.com/QPHutu/golden_critic` — **Apache-2.0, ~14MB, shallow REFERENCE clone** `.local/adopts/golden_critic` (hunt 2026-08-25) |

## Narrative

**BPCO (Best-Practice Critic Optimization)** is a single-rollout critic-based RL recipe that addresses GRPO-style instability: it combines **DPPO** (clipping defined by the sampled token's probability change), **value predictions bounded to the reward range**, **Monte Carlo value targets**, **unnormalized policy advantages**, and **length-adaptive GAE**. Because the critic is discarded after training, BPCO can condition it on **privileged reward-defining information** (reference answer, grading rubric) hidden from the policy. Across math-reasoning tasks with models 1.5B → 30B-A3B MoE, BPCO improves the critic baseline consistently and **matches or exceeds a group-based (GRPO) baseline while sampling one response per prompt**.

**Why filed (OOD with a policy steal):** this is an **RL trainer**, not a cyber harness. The steal is a *policy confirmation*: it pairs the existing **no-GRPO-trainer-as-wired-harness** stance — the wiki does not wire group-relative or critic-based trainers into the agent-security harness. `golden_critic` is cloned as **REFERENCE only** (Apache-2.0, 14MB, within the <500MB + SPDX rule) with `wont_wire`; **no HF weight dumps**; no trainer runtime installed.

## Snippets

> BPCO matches or exceeds a group-based baseline while sampling one response per prompt. These results show that a carefully designed critic provides a reliable alternative to group-relative advantage estimation. [Source: arXiv 2608.23566 abstract]
