---
title: "Decoy hardening (Fool's Gold) vs safety-removal on open weights"
type: concept
tags: [concept, llm-security, defensive-deception, abliteration, k295]
keywords: [decoy hardening, Fool's Gold, abliterated honeypot, denial of trust]
related:
  - sources/arxiv-2608-17202-fools-gold-defensive-deception.md
  - concepts/conditional-safety-adapter-routing.md
  - concepts/psychological-multiturn-jailbreaks.md
  - concepts/reasoning-induced-misalignment.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/tripwire-safety-neuron-clamp.md
  - concepts/ai-redteam-evidential-ceiling.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K295)"
---

## Relations

- @sources/arxiv-2608-17202-fools-gold-defensive-deception.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/tripwire-safety-neuron-clamp.md
- @concepts/ai-redteam-evidential-ceiling.md

## Raw Concept

The question: if refusal can be stripped from released weights, what remaining control does a weight publisher have?

## Narrative

**Defensive deception inside the weights.** Classic honeypot / honeyfile tradition applied to the abliterated state: the attacked model is the honeypot. Hazardous operational requests draw confident answers with falsified critical specifics. The defender's goal is **denial of trust** in the unlocked artifact — not durable refusal. Clean-state behavior is supposed to stay pinned (refusal pin + benign leash). [Source: arXiv 2608.17202]

**What this is not.** It is not a jailbreak recipe, not an abliteration how-to, and not a reason to auto-clamp path-A lab models (see Tripwire). It does not cover in-context jailbreaks. Community abliterated rebuilds of *undefended* bases remain the usual local-lab path; do not assume a random HF abliterated slug is Fool's Gold-defended.

**Lab implication for Cemini / friend path-A.** Abliteration removes refusal; it does not certify correctness. Consensus across samples is not a label-free oracle (paper: element-wise consensus at K=64 still leaves a reconstruction residual and no label-free separator). Smoke-test dual-use answers against **your** ground truth, not fluency. [TENTATIVE]

**Phase-0:** no clone; no CBRNE / payload appendices in wiki.

## Snippets

> The abliterated model is itself the honeypot. [Source: arXiv 2608.17202 §I]
