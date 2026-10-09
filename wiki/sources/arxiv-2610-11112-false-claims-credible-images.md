---
title: "False claims, credible images: a red-teaming benchmark for commercial image generators"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.11112, k413]
related:
  - concepts/verification-generation-gap.md
  - concepts/compliance-verdict-rule-invariance.md
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K413)"
---

## Relations

## Relations

- @concepts/verification-generation-gap.md
- @concepts/compliance-verdict-rule-invariance.md
- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | False claims, credible images: a red-teaming benchmark for commercial image generators |
| arXiv | 2610.11112 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610-11112-false-claims-credible-images-a-red-teaming-bench.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K413 — the model knows the claim is false and renders it anyway.** The paper names a **verification-generation gap**: a commercial image model can label a claim as misinformation under verification and still produce it as **credible visual evidence**. The numbers make the gap explicit — **FCR (false-claim rejection) = 100.00% while ASR = 77.01%** on GPT-Image-2 (delta +22.99) and **100.00% vs 55.82%** on Nano Banana 2 (delta +44.18). Knowing is not acting.

**EPIREAL-BENCH** is 10,000 verified prompts and 10,000 selected images over 10 claim categories and 10 credible visual formats; **EPIREAL-ATTACK** is a skill-guided black-box search over a Pareto set of validity / misinformation realization / visual credibility. Direct prompting already yields **above 70% average ASR** (GPT-Image-2 77.01, Grok Imagen 2.0 89.43, Seedream 5.0 Flash 73.20, Nano Banana 2 55.82); the attack pushes every model past **95%**. Input-level filters do not hold — keyword filter, NSFW classifier, and a prompt checker all sit under 38% interception on every model.

**The constructive result:** **Verification-Guided Prompting (VGP)** — ask the same model to check the claim before generating it, with **no retrieval and no weight change** — lifts interception from 10.70% to **76.20%** (GPT-Image-2) and 32.40% to **93.00%** (Nano Banana 2). Benign factual prompts still resolve at 92.8-99.1%. Repo `github.com/Ye-ze-yu/EpiReal-Bench`; licence not stated. Operator steal: **a capability the model demonstrably has in one mode is not a control in another** — if you need the check to bind, make it a step in the pipeline. Pairs K415/K416 (the same stated-versus-operative gap) and the deepfake-detection line. **No misinformation prompts or generated examples in wiki.**

## Snippets

> See arXiv 2610.11112 abstract. [Source: arXiv 2610.11112 (retrieved 2026-10-09)]
