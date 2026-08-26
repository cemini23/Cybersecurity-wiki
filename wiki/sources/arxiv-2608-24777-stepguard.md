---
title: "StepGuard — step-level agent guardrails with scalable supervision (arXiv 2608.24777)"
type: source
tags: [source, arxiv, agent-security, guardrail, tool-use, k307]
keywords: [2608.24777, StepGuard, StepGen, Balance-GRPO, step-level guard, pre-execution, agent guardrail, AgentDojo, AgentDyn]
related:
  - concepts/step-level-agent-guardrails.md
  - entities/tools/stepguard.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-26
updated: 2026-08-26
phase_0_verdict: "CONDITIONAL-GO 2026-08-26 — zheng977/StepGuard ~6MB; LICENSE re-hunt 2026-08-26 still NO-GO (null SPDX). scripts/stepguard_inventory.sh for adopt when SPDX lands."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc + mcp-tool-control.mdc (K307)"
---

## Relations

- @concepts/step-level-agent-guardrails.md — primary steal (pre-execution tool action guard)
- @entities/tools/stepguard.md — Phase-0 repo / model pointer

## Raw Concept

| Field | Value |
|-------|-------|
| Title | StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing |
| Authors | Zhijie Zheng et al. (Shanghai AI Lab / Beihang / Fudan / RUC / KAUST) |
| arXiv | 2608.24777 (29 pp, EMNLP 2026) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.24777-stepguard-learning-step-level-guardrails-with-sc.pdf` |
| Retrieved | 2026-08-26 |
| Read status | read (abstract + method + results + ablations) |
| Public code | `github.com/zheng977/StepGuard` (~6MB, **no LICENSE file** at hunt 2026-08-26) |
| Public weights | `huggingface.co/ninty-seven/StepGuard` (4B guard model) |

## Narrative

**Problem:** LLM agents invoke tools with real-world side effects. Many guardrails judge **completed trajectories**, so unsafe actions may execute before intervention. Guards also show **defense bias** — over-defense (utility loss) vs under-defense (ASR).

**StepGuard (4B):** audits completed trajectories **and** checks candidate tool actions **before execution** at each step.

**Training:**
- **StepGen** — synthetic safe/unsafe trajectories sharing the same prefix up to a risky step; ATBench-style tool/risk sampling; intermediate-prefix labels + benign tool reuse.
- **Balance-GRPO** — dynamic advantage reweighting from observed safe vs unsafe accuracy gap to balance safety–utility during RL.

**Results (paper claims):**
- Highest average step-level F1 among open-weight agent guards; competitive with GPT-5.4 on static benchmarks (83.0 acc / 83.3 F1 trajectory; 84.8 acc / 84.1 F1 step-level).
- Guarded-agent: mean ASR ↓ **77.3%** vs no guard on AgentDojo + AgentDyn; mean utility ↓ **2.8** points.
- AgentDojo: ASR 1.2, utility 90.7; AgentDyn: ASR 9.3, utility 66.7 (Qwen3.6-35B-A3B backbone).
- AgentHarm remains hard: malicious score 22.8→3.4 but task completion 70.9→52.8.

**Why filed (K307):** pre-execution **step-level** guard is the enforcement point for MCP/tool agents — pairs K239 execution fidelity (block before irreversible effect) and K276 withhold contract (machine-checkable gate). No runtime wire until LICENSE verified; no weight download in wiki ingest.

## Snippets

> StepGuard is a step-level guard model that checks candidate tool actions before execution and also audits completed trajectories. [Source: arXiv 2608.24777 abstract]

> When used to guard agents on AgentDojo and AgentDyn, StepGuard reduces mean ASR by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 points. [Source: arXiv 2608.24777 abstract]

> Existing guards often exhibit defense bias: some block too many benign actions, while others miss too many unsafe ones. [Source: arXiv 2608.24777 §1]
