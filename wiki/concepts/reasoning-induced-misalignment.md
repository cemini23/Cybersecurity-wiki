---
title: "Reasoning-induced misalignment — harmless reasoning FT can weaken safety (K304)"
type: concept
tags: [concept, llm-safety, reasoning, fine-tuning, misalignment, k304, defensive]
keywords: [RIM, reasoning-induced misalignment, SDP, safety direction, safety-decision layers, emergent misalignment, reasoning SFT, drift]
related:
  - sources/arxiv-2608-23497-safety-direction-penalty.md
  - concepts/tripwire-safety-neuron-clamp.md
  - concepts/decoy-hardening-open-weight-abliteration.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/conditional-safety-adapter-routing.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K304)"
---

## Relations

- @sources/arxiv-2608-23497-safety-direction-penalty.md
- @concepts/tripwire-safety-neuron-clamp.md — both are open-weight safety mechanisms; HITL before lab use; no clamp recipes
- @concepts/decoy-hardening-open-weight-abliteration.md — safety-removal vs FT-drift are different failure paths on the same models
- @concepts/local-abliterated-llm-pentest-stack.md — lab stack that must re-verify safety after any fine-tune
- @concepts/conditional-safety-adapter-routing.md — mitigation direction (selective safety intervention) and the same drift concern

## Raw Concept

Question this page answers: **can fine-tuning an aligned LLM on harmless reasoning data silently weaken its safety, and how do you detect and mitigate that?**

## Narrative

**Reasoning-Induced Misalignment (RIM)** is the finding that fine-tuning on reasoning data with *no harmful content* (math, code, CoT) can induce harmful behavior. It is **conditional**: across the architectures, datasets, and scales tested, only Qwen2.5-3B/7B reproduce it — Gemma 3 4B IT, Ministral 3 3B, and Qwen2.5-14B did not (K304, 2608.23497). So the hazard is real but not universal; treat every reasoning-FT as a potential safety event and measure it.

**Mechanism (representation space):** reasoning (R) and safety (S) are **coupled activation directions**. Reasoning FT displaces representations along the safety axis; prompts with larger displacement show larger safety degradation; CKA distance ratios + probes identify the **safety-decision layers** where the shift concentrates. The **Safety-Direction Penalty (SDP)** penalizes movement along the learned safety direction during FT (with iterative scope expansion when compensatory shifts appear outside the penalized layers), restoring safety on Qwen2.5-3B/7B while preserving reasoning performance.

**Operator steal (defensive):**
1. **Reasoning FT is a safety event.** Any fine-tune of an aligned model — including benign reasoning/math/CoT data — gets a safety re-eval (HarmBench/HEx-PHI-style) before deployment, not just a benchmark/utility check.
2. **Safety-representation drift is a measurable diagnostic.** If you control fine-tuning, track a safety direction probe before/after; drift in the safety-decision layers is a red flag even when ASR on the eval set looks unchanged.
3. **Pairs with Tripwire (K240) and Fool's Gold (K295)** — the same open-weight safety toolbox; **no clamp recipes, no safety-removal recipes in this wiki** (NEVER list). SDP as a *penalty during training* is the fix here, distinct from neuron clamping.
4. **Not a reason to avoid reasoning FT** — a reason to gate it: HITL review + safety eval in the FT pipeline, exactly like the pre-install gate for coding agents (`coding-agent-supply-chain-install-gap`).

## Snippets

> These directions are coupled: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. [Source: arXiv 2608.23497 abstract]

> Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. [Source: arXiv 2608.23497 abstract]
