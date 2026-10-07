---
title: "Secure speculative decoding for large language models"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.08678, k405]
related:
  - concepts/speculative-decoding-safety-asymmetry.md
  - concepts/fragtoken-inference-cost-amplification-lab.md
  - concepts/reliable-inference-procurement-routing.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/crescendo-multi-turn-jailbreak.md
maturity: draft
read_status: read
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K405)"
---

## Relations

## Relations

- @concepts/speculative-decoding-safety-asymmetry.md
- @concepts/fragtoken-inference-cost-amplification-lab.md
- @concepts/reliable-inference-procurement-routing.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/crescendo-multi-turn-jailbreak.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Secure speculative decoding for large language models |
| arXiv | 2610.08678 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.08678-secure-speculative-decoding-for-large-language-m.pdf |
| Retrieved | 2026-10-07 |
| Read status | read (deep-read) |

## Narrative

**K405 — an inference optimisation that silently weakens safety.** Speculative decoding speeds a **target** model by letting a smaller **draft** model propose tokens the target then verifies. Prior work studied only the efficiency–utility trade-off. This is the first systematic look at the **security** implications, and it finds a sharp **security–utility asymmetry**: swapping in a weaker draft model raises **attack success rates for jailbreak and prompt injection** substantially while barely moving utility — so the cost of the weakness is invisible on a quality benchmark. The mechanism is the **early tokens** the draft model generates, which the target's ordinary acceptance check waves through. **SecureSD** applies a **stricter verification criterion to draft-model tokens at early decoding positions**, cutting jailbreak and prompt-injection ASR by **up to 92.4%** while keeping **99.8%** of the decoding speedup and utility within **98.4%** of existing methods. Operator steal: **treat any inference-time optimisation as a safety-relevant change** — a draft model is part of the trusted computing base once it can put tokens in the output stream. Pairs the inference-cost thread (K376) and the IPI thread. Lab only, owned or procured models. **No jailbreak payloads or decoding exploits in wiki.**

## Snippets

> See arXiv 2610.08678 abstract. [Source: arXiv 2610.08678 (retrieved 2026-10-07)]
