---
title: "Decoding-level taboo diagnostic — logit-space off-path robustness stress testing"
type: concept
tags: [methodology, llm-eval, decoding, robustness, diagnostic]
keywords: [taboo decoding, logit masking, injected surprisal, off-path robustness, circumlocution, refusal auditing]
related:
  - sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/safety-harness-evolution.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit (K269)"
---

# Decoding-level taboo diagnostic — logit-space off-path robustness stress testing

## Relations

- @sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md
- @concepts/llm-adversarial-fuzzing.md — complements input-side fuzzing: measures resilience *inside* the decoder, holding the prompt fixed
- @concepts/agent-runtime-guardrails.md — refusal/guardrail auditing at decoding time (mask refusal tokens → test if alignment is surface-level)
- @concepts/ai-for-cybersecurity.md — pre-deployment audit for agent/LLM lanes
- @concepts/safety-harness-evolution.md — taboo-guided alignment pairs with harness evolution as an active robustness regularizer
- @concepts/llm-pentest-automation.md — diagnostic, not an attack; keep scoped as an eval/audit tool

## Raw Concept

Benchmarks measure nominal-condition capability; production deployments constantly push models off their preferred decoding path (system prompts, guardrails, JSON schemas, negative constraints). This page captures Taboo (2608.09900): a zero-prompt, runtime logit-space diagnostic that quantifies whether an LLM's multi-step reasoning stays intact when forced off-path.

## Narrative

### The diagnostic primitive

At each decoding step where the nominal top candidate starts a new word (`W=1`), mask the top-`i` logits to `−∞` and re-select greedy. The model must construct semantically valid alternatives on the fly — machine circumlocution. The **injected surprisal** `∆S` (bits) is the dose; `∆S̄` normalizes across architectures/tokenizers.

Word-initial-only masking is essential: masking mid-word subwords corrupts tokenization (accuracy → 0.01–0.05), whereas word-initial masking at a *higher* intervention preserves reasoning (Gemma-3-12B 0.81). So Taboo isolates semantic stress from tokenization artifacts.

### What the results mean

- **Robustness is learned, not given.** Instruction-tuned checkpoints retain far more of their baseline-correct items than base checkpoints — but only on multi-step generative reasoning, and only in some families.
- **Scale compounds alignment.** Qwen2.5-32B-instruct retains 93% at i=1; base collapses. Largest base models are not the most robust (72B-base < 32B-base on GSM8K).
- **Family recipes differ mechanistically.** In Qwen/OLMo/Gemma, instruct absorbs *more* surprisal per intervention (sharper next-token distribution) yet retains more; Llama-3's instruct does not sharpen its distribution, and only acquires taboo-robustness at 70B — a dissociation that marks post-training recipe as the driver.
- **Formal syntax is a hard bound.** Reserved keywords have no synonyms; HumanEval → ~0. Use this as the "do not overclaim off-path capability" control.

### Use cases for the lab

1. **Refusal-surface audit** — mask top refusal tokens on an adversarial prompt; if the model immediately emits policy-violating content, alignment is a shallow top-token preference, not latent safety.
2. **Pre-deployment reliability check** — run Taboo across the prompt/system/JSON constraints a lane actually uses; a model that derails (repetition loops, no-termination, confident-wrong) under dose is fragile in production.
3. **Synthetic CoT diversity** — Taboo sampling yields diverse, logically coherent off-path trajectories for distillation/verifier-RL (taboo-guided GRPO regularizer).
4. **Structured-output stress testing** — semi-structured formats have lexical redundancy; mask preferred top tokens inside a schema to test genuine schema understanding vs memorized templates.

### Caveats

- Taboo is a **diagnostic/eval primitive**, not an attack or a fix. It reveals fragility; taboo-guided alignment is the fix direction, not the mask itself.
- MMLU-style multiple choice is a format artifact (single-letter answers are word-initial); don't read robustness conclusions from MCQ-only results.
- Keep as a scoped eval in the authorized lab; do not use as a generic "safety benchmark" for pass/fail release gates without the task-specific controls (negative-control HumanEval, MCQ-floor MMLU).

## Snippets

> Operating directly within the generation pipeline via runtime logit-space intervention enables precise, unconfounded probing of model health. [Source: arXiv:2608.09900 p.2]

> If suppressing primary refusal tokens causes the model to immediately emit policy-violating content, the alignment is superficial; if the model instead re-routes to alternative safe phrasings or valid policy rationales, the safety guardrail is structurally robust. [Source: arXiv:2608.09900 §5.1]

## Dead Ends

- **Treating Taboo as a jailbreak** — it holds the prompt fixed and never searches for a harmful input; it measures decoder resilience, not input-surface exploitability.
- **Over-reading MCQ results** — the single-letter answer being word-initial means Taboo directly masks the model's primary choice; retention there is a format artifact.
