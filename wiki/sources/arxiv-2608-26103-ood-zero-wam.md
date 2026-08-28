---
title: "OOD — Zero-WAM in-context world-action modeling from human video (arXiv 2608.26103)"
type: source
tags: [source, arxiv, ood, robotics, icl, video-action]
keywords: [2608.26103, Zero-WAM, HumanGen, in-context learning, robotic manipulation, video-action model, cross-task generalization]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "OOD 2026-08-28 — robotics / vision-language-action paper. No cyber adopt; no trainer or agent wire."
wire_status: wont_wire
wire_target: "OOD — robotics; no cyber mapping"
---

## Relations

- @concepts/ai-for-cybersecurity.md — OOD contrast only (robot ICL; no cyber adopt)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization |
| Authors | Jiaming Zhou et al. (Robbyant / HKUST-GZ / HKUST) |
| arXiv | 2608.26103 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.26103-zero-wam-in-context-world-action-modeling-from-h.pdf` |
| Retrieved | 2026-08-28 |
| Read status | **skimmed** — OOD |
| Public code | `robbyant-research.github.io/Zero-WAM/` — project page; no cyber adopt |

## Narrative

**Zero-WAM** borrows the LLM in-context-learning paradigm for **robotic manipulation**: the task specification for a manipulation policy is a **human video** (rich visual cues, no parameter update). A **causal video-action model** executes unseen tasks by following in-context human-video guidance. To address scarce task-rich paired human-robot data, an automatic pipeline converts task-sampled robot trajectories into semantically matched human videos, yielding **HumanGen** — 74.2K human-robot ICL pairs across 8.6K tasks. An **in-context future chunk prediction (IFP)** objective suppresses shortcuts. On 7 unseen tasks in RoboTwin 2.0 simulation: **47.0% average success rate** (+29.5 pp over the strongest video-action baseline).

**Why filed (OOD, no cyber adopt):** robotics/vision-language-action domain. No security or agent-harness mapping for this batch.

## Snippets

> Zero-WAM, a causal video-action model that executes unseen tasks by following in-context human video guidance … on seven unseen tasks in RoboTwin 2.0 simulation, achieves a 47.0% average success rate. [Source: arXiv 2608.26103 abstract]
