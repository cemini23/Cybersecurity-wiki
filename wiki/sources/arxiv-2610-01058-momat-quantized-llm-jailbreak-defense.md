---
title: "MOMAT: mixture of multiple atlases for low-power jailbreak defense of quantized LLMs"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.01058, k389]
related:
  - concepts/quantized-llm-jailbreak-defense-atlas.md
  - concepts/defender-centric-jailbreak-utility.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/instruction-hierarchy-conflict-benchmark.md
maturity: draft
read_status: read
created: 2026-10-02
updated: 2026-10-02
phase_0_verdict: "REFERENCE 2026-10-02 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K389)"
---

## Relations

## Relations

- @concepts/quantized-llm-jailbreak-defense-atlas.md
- @concepts/defender-centric-jailbreak-utility.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/instruction-hierarchy-conflict-benchmark.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MOMAT: mixture of multiple atlases for low-power jailbreak defense of quantized LLMs |
| arXiv | 2610.01058 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.01058-momat-mixture-of-multiple-atlases-for-low-power.pdf |
| Retrieved | 2026-10-02 |
| Read status | read (deep-read via grok CLI) |

## Narrative

**K389** — **quantization weakens alignment safeguards**, and the effect is **scale-dependent**: Llama2-13B shows negligible ASR change under W4A8 (Δ −0.7% AdvBench / −2.0% Malicious Instruct) while **Llama2-7B rises** (Δ **+4.4%** / **+3.0%**). The 7B model is the one that compresses to 3.76 GB and is therefore the realistic edge deployment — so **the compression that makes a model deployable is the compression that erodes its safety**. **MOMAT** organises safety knowledge into domain-localised **atlases** (semantic clusters of harmful/benign samples + policy templates), retrieves top-k per atlas, and scores with a lightweight MoE detector, with a compute-in-memory similarity engine. Results on W4A8 quantised models: **ASR 0.00** on both AdvBench and Malicious Instruct for **Llama2-7B** (undefended 32.5% / 28.0%) and **Mistral-7B** (undefended 68.2% / 67.5%), with **FRR unchanged** (+0.0) — no benign overkill. Architecture: a **frozen** `BAAI/bge-large-en-v1.5` encoder (0.3B, 1024-dim) embeds the prompt — the protected model does not build it — a CiM engine returns top-k (k=10) from every atlas, and a **1.03M-parameter** MoE detector (K=3-5 experts) produces the harmfulness score; above threshold the system serves a safe template instead of generating. CiM retrieval cuts a 100-query batch from 15,052.44 ms to 3,207.21 ns and energy from 8.1e7 µJ to 3.32 µJ. Operator steal: **do not assume a safety-tuned model stays aligned after quantisation** — re-measure ASR *and* FRR at the shipped precision, and report both. 223.2k-sample dataset promised. **No jailbreak payloads in wiki.**

## Snippets

> See arXiv 2610.01058 abstract. [Source: arXiv 2610.01058 (retrieved 2026-10-02)]
