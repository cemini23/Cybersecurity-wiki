---
title: "Right Diagnoses, Decorative Reasoning — medical CoT perturbation audit (arXiv 2608.24790)"
type: source
tags: [source, arxiv, agent-security, chain-of-thought, medical-ai, audit, k308]
keywords: [2608.24790, decorative reasoning, chain decoupling, cdr, CoT faithfulness, medical QA, perturbation audit]
related:
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-26
updated: 2026-08-26
phase_0_verdict: "REFERENCE 2026-08-26 — audit framework + cdr metric; no attack code; clinical eval only. CoT text is not evidence without counterfactual perturbation."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K308)"
---

## Relations

- @concepts/chain-of-thought-decorative-reasoning-audit.md — primary steal (CoT ≠ faithful evidence)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Right Diagnoses, Decorative Reasoning: A Perturbation Audit of Medical Chain-of-Thought |
| Authors | Mengzhu Xu et al. (TU Eindhoven / Dana-Farber) |
| arXiv | 2608.24790 (20 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608-24790-right-diagnoses-decorative-reasoning-a-perturbat.pdf` |
| Retrieved | 2026-08-26 |
| Read status | read (abstract + method + joint analysis + clinician validation) |
| Public code | none cited at retrieval |

## Narrative

Clinicians treat visible chain-of-thought (CoT) as **auditable evidence** of medical reasoning. This paper tests whether the chain **tracks and drives** computation or **documents after the fact**.

**Method:** 30-operator perturbation battery on question + chain (severity reversal, negation flip, demographic swap, evidence ablation, chain truncate/delete/substitute/insert/reorder). **Chain-Decoupling Rate (cdr)** = share of destructive edits where the chain does not register the edit **and** the answer does not flip.

**Results (14 LLMs, four medical QA benchmarks):**
- Panel-wide **cdr 72.9%** on clinically meaningful destructive edits (M-block).
- Chain corruption (F-block) leaves accuracy **≈ unchanged** (median ΔAcc ≈ 0 pp; 11/14 within ±1.6 pp).
- Removing CoT prompting does not reduce accuracy — chain often **decorative**.
- Two board-certified clinicians re-annotated N=197 perturbed items; **98.5%** gold answers remain defensible after destructive edits.
- Closed-source tier: answer-side signals consistent with decoupling when chain text unavailable.

**Why filed (K308):** pairs K290 CHIVE — **CoT / review narratives are not evidence** unless counterfactual-tested. Applies to agent audit, SOC copilots, and pentest report "reasoning" sections, not only clinical QA.

## Snippets

> The Chain-Decoupling Rate (cdr) is 72.9% panel-wide on clinically meaningful destructive edits. [Source: arXiv 2608.24790 abstract]

> Chain corruption leaves accuracy unchanged, and removing CoT prompting does not reduce accuracy. [Source: arXiv 2608.24790 abstract]

> A clinician who cannot inspect the rationale has no signal that a confidently delivered answer is wrong for the wrong reasons. [Source: arXiv 2608.24790 §1]
