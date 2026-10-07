---
title: "Speculative decoding safety asymmetry (K405)"
type: concept
tags: [concept, agent-security, k405]
keywords: [2610.08678, K405]
related:
  - sources/arxiv-2610-08678-secure-speculative-decoding.md
  - concepts/fragtoken-inference-cost-amplification-lab.md
  - concepts/reliable-inference-procurement-routing.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/crescendo-multi-turn-jailbreak.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K405)"
---

## Relations

- @sources/arxiv-2610-08678-secure-speculative-decoding.md
- @concepts/fragtoken-inference-cost-amplification-lab.md
- @concepts/reliable-inference-procurement-routing.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/crescendo-multi-turn-jailbreak.md

## Raw Concept

Question: **Speculative decoding safety asymmetry** — operator steal from arXiv 2610.08678?

## Narrative

Speculative decoding lets a **small draft model** write tokens that a **large target model** verifies. The verification check is tuned for *distributional* agreement, not for safety — so a weak draft model can push jailbreak and prompt-injection content through early decoding positions while a utility benchmark shows almost nothing. That asymmetry is the finding: **the safety cost does not appear on the metric you are watching.** The defence is to tighten verification for draft-model tokens **at early positions** specifically (up to **92.4%** ASR reduction at **99.8%** of the speedup). Operator rule: an optimisation that adds a model to the token path **adds a model to the trusted computing base** — re-run the safety eval, not just the quality eval.

## Snippets

> See arXiv 2610.08678 abstract. [Source: arXiv 2610.08678 (retrieved 2026-10-07)]
