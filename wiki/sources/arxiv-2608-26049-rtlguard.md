---
title: "RTLGuard — teacher-student defense for poisoned RTL codegen (arXiv 2608.26049)"
type: source
tags: [source, arxiv, hardware-security, rtl, llm-supply-chain, defensive, k310]
keywords: [2608.26049, RTLGuard, hardware trojan, backdoor, poisoned RTL, teacher-student, knowledge distillation, feature alignment, ASR, Verilog, LLM supply chain]
related:
  - concepts/rtl-codegen-poison-defense.md
maturity: draft
read_status: read
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "REFERENCE 2026-08-28 — in-scope sanitize-before-trust defense pattern. No public paper repo at hunt (name-collision repos ≠ the paper). No clone; no RTL-trojan payload / no backdoor how-tos in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K310)"
---

## Relations

- @concepts/rtl-codegen-poison-defense.md — primary steal (sanitize-before-trust for RTL/codegen models)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models |
| Authors | Mahshid Rezakhani, Kimia Azar, Hadi Kamali (UCF ECE) |
| arXiv | 2608.26049 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.26049-rtlguard-a-lightweight-teacher-student-defense-f.pdf` |
| Retrieved | 2026-08-28 |
| Read status | read (abstract + method + results) |
| Public code | **none at hunt** — the name-collision repos (`kamatampadmasree56-ece/RTLGuardai`) are NOT this paper; no clone |

## Narrative

**Problem:** LLMs are shifting toward automated register-transfer-level (RTL) design — translating high-level specs into synthesizable hardware. Third-party **fine-tuned** RTL models are opaque (training data + adaptation process not visible), so an adversary (even a model provider) can embed a hidden **backdoor during fine-tuning**. At inference time a benign-looking prompt triggers malicious behavior — e.g. emitting a **hardware Trojan** in the generated RTL.

**RTLGuard (K310)** is a lightweight **teacher-student defense** that sanitizes a compromised RTL model without the prohibitive cost of full-parameter retraining:

1. Fine-tune a small, **clean** teacher on a limited set of **trusted RTL data**.
2. Guide the **poisoned target** model via a **composite teacher-student objective**.
3. Add **feature alignment** + **knowledge distillation** to suppress the malicious behavior.

**Result (paper claim):** across various LLM architectures, RTLGuard **significantly reduces the Attack Success Rate (ASR)** while preserving **functional correctness** and **synthesizability** of the generated RTL.

**Why filed (K310):** the hardware/IC supply chain is the same "trust the third-party fine-tune" problem as software LLM backdoors. The teacher-student + feature-alignment pattern is the **defensive** counterpart to the offensive "poisoned fine-tune" class — pairs `concepts/cweep-rtl-cwe-early-prevention` (early CWE lint) + Gradient Immunity / DataShield (subspace/consensus gates at release). **No public repo at hunt** → REFERENCE only, no clone, no trojan/PoC content.

## Snippets

> Adversaries (even model providers) may embed hidden backdoor threats during fine-tuning, allowing malicious behavior, e.g., hardware Trojans, to be triggered by seemingly benign prompts given by victim user at inference time. [Source: arXiv 2608.26049 abstract]

> Rather than prohibitive computational cost of full-parameter retraining, RTLGuard leverages a teacher-student framework designed to sanitize compromised RTL generation models. [Source: arXiv 2608.26049 abstract]

> Our experiments across various LLM architectures demonstrate that RTLGuard significantly reduces the Attack Success Rate (ASR) while preserving the functional correctness and synthesizability of the generated RTL code. [Source: arXiv 2608.26049 abstract]
