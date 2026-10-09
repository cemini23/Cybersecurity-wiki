---
title: "Adversarial robustness of VLM perception (K-av1)"
type: concept
tags: [concept, agent-security, k-av1]
keywords: [arXiv 2610.08331, K-av1]
related:
  - sources/arxiv-2610-08331-stca-av-vlm-adversarial-attack.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/adversarial-region-estimation-vs-single-example.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K-av1)"
---

## Relations

- @sources/arxiv-2610-08331-stca-av-vlm-adversarial-attack.md — K408-K417 ingest / 2026-10-09
- @concepts/llm-adversarial-fuzzing.md — K408-K417 ingest / 2026-10-09
- @concepts/adversarial-region-estimation-vs-single-example.md — K408-K417 ingest / 2026-10-09

## Raw Concept

Question: **Adversarial robustness of VLM perception** — operator steal from the inbound brief (arXiv 2610.08331)?

## Narrative

A vision-language model in a **safety-critical perception loop** is an adversarial target, and a **black-box transferable** perturbation does not have to look dramatic. On two autonomous-driving datasets the attack lifted ASR from **32.6% to 71%** (Video-LLaVA) and **45% to 84.2%** (Qwen2.5-VL) while **SSIM only fell 0.93 to 0.82** — a change a human reviewer would wave through.

The actionable half is the failure to generalise in the other direction: a **domain-tuned** model (Dolphin) barely moved (46.9% → 46.2%), while the general VLMs collapsed. So **domain tuning bought adversarial robustness here** — worth weighing against the usual assumption that a bigger general model is the safer one. For any VLM sitting in a control or triage path, ask what it was tuned on and test transfer, not just accuracy. Pairs K403's region-estimation rule: measure the failure surface, not one example.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-09)]
