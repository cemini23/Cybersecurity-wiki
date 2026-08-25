---
title: "Conditional safety adapter routing — selective safety intervention vs the alignment tax (K301)"
type: concept
tags: [concept, llm-safety, alignment, adapter-routing, k301, defensive]
keywords: [CLEAR, conditional safety, latent gate, safety LoRA, alignment tax, over-refusal, selective intervention]
related:
  - sources/arxiv-2608-21278-clear-latent-adapter-routing.md
  - concepts/reasoning-induced-misalignment.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/tripwire-safety-neuron-clamp.md
  - concepts/decoy-hardening-open-weight-abliteration.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K301)"
---

## Relations

- @sources/arxiv-2608-21278-clear-latent-adapter-routing.md
- @concepts/reasoning-induced-misalignment.md — the failure mode conditional routing tries to avoid (safety drift under fine-tuning)
- @concepts/local-abliterated-llm-pentest-stack.md — open-weight safety posture contrast; selective vs removed refusal
- @concepts/tripwire-safety-neuron-clamp.md — safety mechanisms on open weights, both are HITL-gated
- @concepts/decoy-hardening-open-weight-abliteration.md — safety-removal vs conditional-safety contrast on open weights
- @concepts/agent-runtime-guardrails.md — enforcement-layer context; gating telemetry feeds guardrail monitoring

## Raw Concept

Question this page answers: **can an LLM's safety behavior be applied selectively — only when harmful intent is detected — instead of globally, and what does that mean for lab/defensive stacks?**

## Narrative

Safety tuning is usually **global**: the same aligned parameters apply to harmful, benign, and safety-adjacent inputs, so improving refusal degrades benign responses (the **alignment tax**). CLEAR (K301, 2608.21278) is the conditional alternative: a **hidden-state gate** continuously controls the strength of a **safety LoRA** on a frozen backbone — h′ = (W + g·ΔW)h with g(x) ∈ [0,1]. The gate is learned jointly with the adapter (subtype-aware weighting + hard pairwise margin), so the model itself decides when to route in the safety intervention rather than relying on an external classifier.

**Paper-reported results [TENTATIVE]:** HarmBench ASR 32.3% → 0.5% on Llama-3-8B-Instruct with up to +7.1 pp GSM8K vs global SFT/LoRA; similar safety with higher retained utility on Gemma-2-2B-it (73.46% GSM8K retained).

**Operator steal (defensive):**
1. **A global safety LoRA/SFT is not a proof of safety** — it is a coarse knob that trades utility for refusal. If a stack must keep benign behavior intact, prefer *conditional* or *selective* intervention (gate, router, or input-conditioned adapter) and evaluate over-refusal explicitly (XSTest-style), not just ASR.
2. **Gating scores are telemetry**: in an agentic deployment, an input-conditioned safety gate gives a per-request "how much safety intervention fired" signal — useful for drift monitoring and incident forensics, analogous to guardrail verdict logging.
3. **Pairs with the reasoning-FT hazard (K304)**: global fine-tuning — even on harmless reasoning data — can shift safety representations; conditional routing is one mitigation direction, and any fine-tune of an aligned model should re-run safety evals.
4. No HF weight downloads; REFERENCE only (no public code at hunt 2026-08-25).

**Why this is a half-page without the defender side:** the attack-relevant reading is that refusal-based safety can be *tuned away* by anyone with fine-tuning access (see `reasoning-induced-misalignment`); the defense is to treat safety as an ongoing, measurable property of the deployed artifact, not a one-time alignment step.

## Snippets

> CLEAR performs input-conditioned adapter routing: benign prompts receive little or no adapter intervention, preserving the original model behavior, while harmful or adversarial prompts receive stronger safety-adapter activation. [Source: arXiv 2608.21278 abstract]
