---
title: "Linguistic illegibility — security floor below NL self-report (K325)"
type: concept
tags: [concept, agent-security, audit, interpretability, sandbox, k325]
keywords: [linguistic illegibility, CoT monitoring limits, taint tracking, sandbox floor, activation probing]
related:
  - sources/arxiv-2609-02852-linguistic-illegibility-llm-security.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - concepts/agentic-containment-principles.md
maturity: draft
created: 2026-09-03
updated: 2026-09-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K325)"
---

## Relations

- @sources/arxiv-2609-02852-linguistic-illegibility-llm-security.md — linguistic illegibility (2609.02852)
- @concepts/chain-of-thought-decorative-reasoning-audit.md — visible CoT ≠ evidence (K308)

## Raw Concept

Question: **when can linguistic monitoring never be a complete security boundary?**

## Narrative

**Linguistic illegibility (K325)** is the claim that an LLM's **natural-language outputs and linguistically-defined probes** may fail to represent internal computation — because core reasoning lives in activation space with lossy translation at the boundaries.

**Security implication:** mechanisms that depend on **linguistic self-reporting** (CoT monitors, constitutional self-critique, SAE labels keyed on NL concepts) need an **external floor** — e.g. **taint tracking** on system state, robust VM/container isolation, third-party sandbox config audit — whose guarantees do **not** require trusting the model's prose.

Pairs K308 (decorative CoT), K314 (recognition ≠ enforcement), K290 CHIVE (counterfactual explanations). **Not** a license to skip monitoring — a limit on what monitoring alone can prove.

## Snippets

> Taint tracking can define a priori which system state must never be influenced by model-produced data, regardless of linguistic self-report. [Source: arXiv 2609.02852 abstract, paraphrase]
