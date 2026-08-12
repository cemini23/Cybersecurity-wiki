---
title: Cross-lingual safety transfer illusion in low-resource languages
type: concept
tags: [concept, llm-safety, multilingual, jailbreak-surface, low-resource, evaluation]
keywords: [cross-lingual safety, LRL, LoDNA, refusal direction, literal vs localized, latent geometric framework, English-centric alignment]
related:
  - sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md
  - concepts/multilingual-long-horizon-agent-evaluation.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K272)"
---

## Relations

- @sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md
- @concepts/multilingual-long-horizon-agent-evaluation.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

LLM safety alignment is built and measured in English, but low-resource-language (LRL) deployments inherit almost none of the English refusal signal. Oppong et al. 2608.11146 show English refusal directions retain **<10%** in Twi/Hausa/Amharic/Swahili even when literal and culturally localized prompts are semantically aligned (cosine 0.95–0.996) — models encode harm concepts but never route them to the safety mechanism.

## Narrative

**Cybersec takeaway:** English-only safety evaluation is a **false assurance** for any deployment that serves non-English users. For red-team / eval work in the lab:

1. **Use culturally localized prompts, not literal translations.** Literal-translation benchmarks measure the English filter's shadow; localized idioms and coded language are the actual jailbreak surface (`llm-adversarial-fuzzing`).
2. **Prefer representational probes over generation-based evals when available.** The Latent Geometric Framework (residual-stream probing of the refusal direction, drift metrics) detects that safety features are present-but-unrouted — a failure mode generation tests can miss entirely.
3. **Report the language dimension.** A model's ASR in English says nothing about its ASR in a low-resource language; eval/lab runs should cover target languages or explicitly scope to English-only.
4. **Defender angle:** safety tuning must add LRL-specific refusal coverage; a universal harm-manifold assumption is unsupported for the studied languages.

Authorized lab only — generating harmful content in target languages for eval is a scoped red-team activity (`local-abliterated-llm-pentest-stack`), not a deployment experiment. No public LoDNA data at Phase-0 → REFERENCE.

## Snippets

> Because models often process safety logic via internal English translation, cultural nuances lost in this latent translation bypass alignment entirely, creating structural mapping errors that bad actors can exploit using adversarial metaphors as universal jailbreaks. [Source: arXiv:2608.11146 §1]

## Dead Ends

- LoDNA not yet released; the <10% retention figure is paper-reported for 7B–8B open models only.
- Probing-based eval requires access to model weights (residual-stream hooks) — not applicable to API-only victims.
