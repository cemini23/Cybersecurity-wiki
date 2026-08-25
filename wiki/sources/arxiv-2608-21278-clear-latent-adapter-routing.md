---
title: "CLEAR — Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment (arXiv 2608.21278)"
type: source
tags: [source, arxiv, llm-safety, alignment, adapter-routing, k301]
keywords: [2608.21278, CLEAR, latent adapter routing, safety LoRA, hidden-state gate, alignment tax, HarmBench, XSTest, GSM8K]
related:
  - concepts/conditional-safety-adapter-routing.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "REFERENCE 2026-08-25 — no public code repo found at GitHub hunt; no HF weight download. Defensive policy steal only (safety-utility conditional routing ≠ global LoRA as proof of safety)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K301)"
---

## Relations

- @concepts/conditional-safety-adapter-routing.md — primary steal (conditional safety adaptation)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment |
| Authors | Chengxiao Wang, Enyi Jiang, Xiaojing Liao (UIUC), Sanmi Koyejo (Stanford) |
| arXiv | 2608.21278 (14 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.21278-clear-continuous-latent-adapter-routing-for-util.pdf` |
| Retrieved | 2026-08-25 |
| Read status | read (abstract + mechanism + results sections) |
| Public code | none found at GitHub hunt 2026-08-25 |

## Narrative

**CLEAR (Continuous LatEnt Adapter Routing)** is a conditional safety-adaptation framework that attacks the **alignment tax**: globally applied safety tuning (SFT or plain LoRA) changes the model's behavior on *benign* inputs that merely resemble harmful requests, causing over-refusal and reasoning degradation. CLEAR freezes the backbone LLM and routes a **safety LoRA** whose activation strength is continuously controlled by a learned **hidden-state gate**: the gate predicts a routing score g(x) ∈ [0,1] and the model applies h′ = (W + g·ΔW)h — benign prompts get little or no adapter intervention, harmful/adversarial prompts get stronger safety activation.

The gate is **not** an external filter or post-hoc moderation module: it is jointly optimized with the safety adapter and directly controls intervention strength during generation. A **subtype-aware gate weighting** plus a **hard pairwise margin objective** explicitly separate harmful and benign prompts in the latent gating space.

**Key results (paper-reported, [TENTATIVE] — no local repro):**
- Llama-3-8B-Instruct: HarmBench ASR **32.3% → 0.5%**, retaining most base utility and up to **+7.1 pp GSM8K** vs globally applied SFT/LoRA.
- Gemma-2-2B-it: retains **73.46% GSM8K** (~7 pp above global SFT/LoRA) with HarmBench ASR down to **0.50%**.
- Safety eval: HarmBench + XSTest (over-refusal / unsafe-refusal); utility eval: GSM8K (5-shot), MMLU (5-shot), TruthfulQA (0-shot) via lm-eval-harness.

**Why filed (K301):** conditional safety routing is the training-side counterpart of the wiki's runtime guardrail work — it shows safety intervention can be *selective*, and it cautions against treating any global LoRA/SFT as a proof of safety. No weights downloaded; no code clone (none public at hunt). [Source: arXiv 2608.21278 PDF]

## Snippets

> CLEAR performs input-conditioned adapter routing: benign prompts receive little or no adapter intervention … while harmful or adversarial prompts receive stronger safety-adapter activation to encourage refusal-style responses. [Source: arxiv-2608.21278-clear PDF, §1]

> On Llama-3-8B-Instruct, CLEAR reduces HarmBench ASR from 32.3% to 0.5% … achieving up to 7.1 percentage points higher GSM8K accuracy than globally applied SFT or LoRA. [Source: arxiv-2608.21278-clear PDF, abstract]
