---
title: "Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty (arXiv 2608.23497)"
type: source
tags: [source, arxiv, llm-safety, reasoning, fine-tuning, misalignment, k304]
keywords: [2608.23497, RIM, reasoning-induced misalignment, SDP, safety direction, safety-decision layers, Qwen2.5, emergent misalignment]
related:
  - concepts/reasoning-induced-misalignment.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "REFERENCE 2026-08-25 — no public code repo at hunt; no clamp recipes in wiki. Defensive FT-safety-diagnostic steal only (reasoning FT is a safety event)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K304)"
---

## Relations

- @concepts/reasoning-induced-misalignment.md — primary steal (FT-safety diagnostics + SDP direction)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty |
| Authors | Yipeng Zhao (U Toronto), Qishun Yang, Shenzhe Zhu, Shu Yang, Di Wang (KAUST; UT Austin) |
| arXiv | 2608.23497 (28 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.23497-mitigating-reasoning-induced-misalignment-via-sa.pdf` |
| Retrieved | 2026-08-25 |
| Read status | read (abstract + mechanism + results + appendices) |
| Public code | "MIT (upon publication)" per appendix; no repo found at hunt 2026-08-25 — no clone |

## Narrative

**Reasoning-Induced Misalignment (RIM):** fine-tuning an aligned LLM on *harmless* reasoning data — math, code, chain-of-thought problem-solving with no harmful content — can induce harmful behavior. RIM is **conditional, not universal**: cross-dataset (MetaMathQA), cross-architecture (Gemma 3 4B IT, Ministral 3 3B), and cross-scale (Qwen2.5-14B) checks show it does *not* always emerge; only **Qwen2.5-3B and 7B** satisfy the authors' operational RIM criterion under the evaluated recipes (AM-DeepSeek, first 10,000 examples).

**Mechanism (representation-space analysis):** two activation-space directions are extracted — one encoding **reasoning ability (R)** and one encoding **safety behavior (S)**. They are **coupled**: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. Whitened cosine similarity between R and S is consistently negative; **CKA distance ratios and probes** localize the **safety-decision layers** where the shift matters most.

**Mitigation — Safety-Direction Penalty (SDP):** penalize displacement **along the learned safety direction** during reasoning fine-tuning (γs = 0.5; LoRA r/α 16/16 on all linear layers; lr 5e-5 / 2.5e-5 for 3B / 7B). When the initial penalized layer-scope leaves compensatory shifts beyond it, the same diagnostics guide **iterative scope expansion**. On Qwen2.5-3B and 7B, SDP **restores safety while preserving benchmark reasoning performance**.

**Why filed (K304):** the training-side companion to the wiki's safety-mechanism pages (Tripwire K240, Fool's Gold K295, CLEAR K301). Any reasoning-FT of an aligned model is now a **safety event** to evaluate, and safety-representation drift is a measurable diagnostic. No clamp recipes; no weight downloads; no code clone. [Source: arXiv 2608.23497 PDF]

## Snippets

> Fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. [Source: arxiv-2608.23497-safety-direction-penalty PDF, abstract]

> On Qwen2.5-3B and 7B, SDP restores safety while preserving benchmark reasoning performance. [Source: arxiv-2608.23497-safety-direction-penalty PDF, abstract]

> Across the model architectures, scales, and reasoning datasets evaluated at the outset, only the Qwen2.5-3B and 7B settings reproduce RIM. [Source: arxiv-2608.23497-safety-direction-penalty PDF, §3.2]
