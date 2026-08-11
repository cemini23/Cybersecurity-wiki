---
title: "Decoding-Level Taboo: a diagnostic stress test for LLM robustness (arXiv 2608.09900)"
type: source
tags: [source, arxiv, llm-eval, decoding, robustness, diagnostic]
keywords: [2608.09900, Taboo, logit masking, injected surprisal, off-path robustness, circumlocution]
related:
  - concepts/decoding-level-taboo-diagnostic.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/safety-harness-evolution.md
maturity: draft
read_status: read
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "REFERENCE 2026-08-11 — Zenodo CC-BY-4.0 taboo-decoder.zip (~234KB); no clone (not MIT/Apache). K269 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit (K269)"
---

**Briefs:** `briefs/2026-08-11_k269-taboo-decoding-diagnostic.md`

## Relations

- @concepts/decoding-level-taboo-diagnostic.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md
- @concepts/safety-harness-evolution.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness |
| Authors | Kamijo (Univ. Ryukyus), Rottenstreich (Technion), Conde, Martínez, Reviriego (UPM) |
| arXiv | 2608.09900 |
| Code | https://doi.org/10.5281/zenodo.21761445 → zenodo.org/records/21761446 (`taboo-decoder.zip`, CC-BY-4.0, ~234KB, anonymous) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.09900-decoding-level-taboo-a-diagnostic-stress-test-fo.pdf` |
| Retrieved | 2026-08-11 |
| Read status | read (19 pp) |

## Narrative

Taboo is a **zero-prompt** diagnostic stress test that intervenes directly in logit space during autoregressive decoding. Holding the prompt fixed, it masks the top-`i` candidate tokens at **word-initial** steps (`Mt,j = −∞` for `j ∈ Top-i(zt)` when `W=1`), forcing the model into machine circumlocution. Mid-word subword continuations are never masked, isolating semantic stress from tokenization corruption (mid-word masking collapses GSM8K accuracy to 0.01–0.05 even at small width).

Quantified dose: **Injected Surprisal** `∆S_t = −log₂ P(x*_t|x_<t) + log₂ P(x_nom_t|x_<t)`, summed over word-boundary interventions → `S_total` and normalized to Mean Injected Surprisal Per Intervention `∆S̄`. Implemented as a `TabooLogitsProcessor` for HF transformers; per-step cost negligible; generations lengthen ~1.4× at i=1.

Key results (four open-weight families, 0.5B–72B, four benchmarks):
- **Off-path robustness is scale×alignment compounded.** GSM8K conditional retention at i=1: Qwen2.5-32B-instruct 93% (vs 6% at 0.5B base); Gemma-3-12B 25%→90%; alignment widens with scale.
- **Task-specific:** big effect on generative multi-step reasoning (GSM8K), not MMLU (collapses to the MCQ floor — the single-letter answer is inherently word-initial) and small on TriviaQA (high lexical redundancy).
- **Family-dependent:** Llama-3.1-8B shows no base-instruct gap (14%→16%) — its instruct next-token distribution is not sharpened; the gain reappears at 70B (36%→75%) without distribution sharpening, a mechanistically distinct route.
- **Formal syntax bound:** HumanEval collapses to ~0 Pass@1 — reserved keywords/operators at word starts have no valid off-path substitutes (negative control).
- 4-bit quantization matches bf16 within sampling variance (median |Δacc| 0.03; one 14B cell anomalous, 8-bit recovers it).

Broader applications: non-destructive **safety-audit** (mask refusal tokens — if policy-violating content emerges, the alignment is superficial), synthetic **CoT trajectory discovery**, zero-training **structured-output stress testing** (JSON/function-call schema probing), and **taboo-guided alignment** (add Taboo sampling to verifier-based RL rollout so policies learn off-path robustness).

`[CONFIRMED]` from paper tables + figures; no local repro run.

## Snippets

> By dynamically masking primary candidate tokens at word boundaries, Taboo forces machine circumlocution. [Source: arXiv:2608.09900 abstract]

> Aligned checkpoints absorb a larger effective perturbation yet retain far more of their multi-step reasoning. An effect that widens with scale, is family-dependent … task-specific … and bounded by formal syntax (HumanEval collapses to zero). [Source: arXiv:2608.09900 abstract]

## Dead Ends

- Not a prompt-injection or jailbreak tool — it is a *decoding-time* diagnostic; don't confuse logit-space stress with input-surface attacks.
- Zenodo deposit is CC-BY-4.0 (data/software license) — **REFERENCE**, no clone into `raw-sources/repos/`; re-check for a later Apache/MIT GitHub release before adopting as a lab tool.
- Single-run marginal-retention figures at n=100 for the ≥32B ladder; Llama transition point between 8B and 70B is not located.
