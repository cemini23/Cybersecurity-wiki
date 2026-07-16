---
title: GFlowRL — distribution-matching RL for LLMs (arXiv 2607.13394)
type: source
tags: [source, arxiv, rl, llm-post-training, red-teaming-eval, microsoft]
keywords: [2607.13394, gflowrl, gflownet, distribution matching, advbench, harmbench, microsoft research]
related:
  - concepts/gflowrl-distribution-matching-attacker-rl.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/agentic-online-rl-self-evolving-systems.md"
maturity: draft
read_status: skimmed
created: 2026-07-16
updated: 2026-07-16
phase_0_verdict: "NO-GO 2026-07-16 — github.com/microsoft/gflowrl 404 (promised release); REFERENCE for ASR attacker-diversity claims only"
---

**Briefs:** `briefs/2026-07-16_gflowrl-attacker-diversity-ood-note.md`, `briefs/2026-07-16_k178-gflowrl-attacker-rl-reference-prod.md`

## Relations

- @concepts/gflowrl-distribution-matching-attacker-rl.md — cybersec-relevant slice (red-team ASR)
- Primary RL methodology → CCC / research post-training lane

## Raw Concept

| Field | Value |
|-------|-------|
| Title | GFlowRL: Scaling Distribution-Matching RL to Large Language Models |
| Authors | Xiaodong Liu, Michael Xu, Jack W. Stokes, Paul Smolensky, Doug Burger, Jianfeng Gao |
| Affiliation | Microsoft Research |
| arXiv | 2607.13394 |
| Code | promised `github.com/microsoft/gflowrl` — **404 as of 2026-07-16** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.13394-gflowrl-scaling-distribution-matching-rl-to-larg.pdf` |
| Retrieved | 2026-07-16 |
| Read status | **skimmed** (abstract + cybersec-relevant ASR claims) |

## Narrative

GFlowRL replaces the learned GFlowNet partition function with an in-batch Monte Carlo estimate, adding importance-sampling correction and asymmetric flow-gap clipping. Primary claims are math/code post-training (Codeforces **2048** at 14B). Cybersec-relevant claim: highest average **ASR@1** on AdvBench and HarmBench vs prior multi-turn attacker SOTA, in a regime where FlowRL diverges. [Source: arXiv 2607.13394 abstract]

### Cross-wiki routing

- **Cybersec:** REFERENCE note — distribution-matching RL as attacker-diversity method; do not adopt training stack
- **CCC:** post-training / harness RL methodology (see CCC handoff)

### Phase-0 (2026-07-16)

| Gate | Status |
|------|--------|
| Repo | **FAIL** — 404 |
| Size/adopt | N/A |
| Verdict | **NO-GO** install; **REFERENCE** claims only |

## Snippets

> "…attaining the highest average ASR@1 on AdvBench and HarmBench, outperforming the previous SOTA multi-turn attacker…"
[Source: arxiv-2607.13394 abstract]
