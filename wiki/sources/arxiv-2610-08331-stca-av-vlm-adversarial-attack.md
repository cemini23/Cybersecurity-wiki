---
title: "STCA: transferable spatial-temporal adversarial attack on autonomous-driving VLMs"
type: source
tags: [source, routed]
keywords: [arXiv 2610.08331]
related:
  - concepts/vlm-perception-adversarial-robustness.md
  - concepts/adversarial-region-estimation-vs-single-example.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/vlm-perception-adversarial-robustness.md — K408-K417 ingest / 2026-10-09
- @concepts/adversarial-region-estimation-vs-single-example.md — K408-K417 ingest / 2026-10-09

## Raw Concept

| Field | Value |
|-------|-------|
| Title | STCA: transferable spatial-temporal adversarial attack on autonomous-driving VLMs |
| Identifier | arXiv 2610.08331 |
| Type | arXiv paper (routed from image-gen 2026-10-08) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-09 |
| Read status | read (routed brief) |

## Narrative

**A black-box transferable attack on vision-language models in a safety-critical perception stack.** The perturbation is visually mild — **SSIM falls only 0.93 → 0.82** — and beats PGD and FGSM baselines. Attack success rises sharply:

| Target | BDD100K ASR | nuScenes ASR |
|---|---|---|
| Video-LLaVA | 32.6% → **71%** | 57.6% → 83% |
| Qwen2.5-VL | 45% → **84.2%** | 64.7% → 96.5% |
| Dolphin | 46.9% → 46.2% | 37.6% → 47.1% |

**The most actionable defensive finding is in that last row:** the **domain-tuned Dolphin** model is markedly **more robust** than the general-purpose VLMs. Operator steal: **domain tuning bought adversarial robustness here; a general VLM in a safety-critical loop did not.** No GitHub, no repo, no weights, no dataset; uses public BDD100K and nuScenes; **no licence stated**. Authorized robustness lab only. **No perturbation recipes or attack code in wiki.**

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-09)]
