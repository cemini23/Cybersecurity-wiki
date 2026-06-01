---
title: "Provably Secure Agent Guardrail (arXiv:2605.29251)"
type: source
tags: [arxiv, agent-security, guardrail, formal-methods, epca, smt, research-paper]
keywords: [epca, provably secure agent guardrail, executable proof-constrained action, smt, formal verification, semantic guardrail dilemma]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/defenseclaw.md
  - entities/tools/airguard.md
maturity: draft
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/agent-runtime-guardrails.md — anchor source for formal/ePCA guardrail paradigm
- @concepts/ai-for-cybersecurity.md — agent privilege inflation context (OpenClaw cited)
- @concepts/llm-adversarial-fuzzing.md — contrasts probabilistic jailbreak testing vs deterministic runtime enforcement
- @entities/tools/defenseclaw.md — enterprise runtime governance complement
- @entities/tools/airguard.md — empirical runtime authority control complement

## Raw Concept

- **Title**: Provably Secure Agent Guardrail
- **Authors**: Benlong Wu, Weiming Zhang, Kejiang Chen, Han Fang, Nenghai Yu (USTC)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2605.29251-provably-secure-agent-guardrail.pdf`
- **URL**: https://arxiv.org/abs/2605.29251
- **Retrieved**: 2026-06-01
- **Read-status**: deep-read (abstract + intro + problem formulation)

## Narrative

Proposes shifting agent defense from **empirical semantic guardrails** and LLM-as-Judge to **Executable Proof-Constrained Action (ePCA)**: agents must formalize action intentions as first-order logical constraints verified by an SMT solver before side effects execute. Unsafe transitions map to provable logical deadlocks (UNSAT). Evaluated on multi-step financial transfer and cross-domain exfiltration scenarios — reports 0% ASR and 0% FPR in evaluated settings with ~0.44 ms formal-check latency. `[TENTATIVE]` — claims are conditional on explicit system assumptions; full paper not lab-replicated in this wiki.

## Snippets

> "Existing defense architectures heavily rely on empirical semantic guardrails and probabilistic large model adjudicators, mechanisms that fail to provide deterministic security lower bounds when facing complex semantic symbol decoupling attacks."

> "Agents must use a Satisfiability Modulo Theories (SMT) solver … to automatically formalize their action intentions into mathematical constraints … the solver deterministically outputs an unsatisfiable (UNSAT) decision."
