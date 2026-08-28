---
title: "RTL codegen poison defense — sanitize-before-trust (K310)"
type: concept
tags: [concept, hardware-security, rtl, llm-supply-chain, defensive, agent-security, k310]
keywords: [RTLGuard, poisoned fine-tune, hardware trojan, teacher-student, feature alignment, knowledge distillation, sanitize-before-trust, third-party model trust, ASR]
related:
  - sources/arxiv-2608-26049-rtlguard.md
  - concepts/cweep-rtl-cwe-early-prevention.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K310)"
---

## Relations

- @sources/arxiv-2608-26049-rtlguard.md — source paper (teacher-student sanitize)
- @concepts/cweep-rtl-cwe-early-prevention.md — same RTL-hardware-safety lane; design-time CWE lint vs post-hoc sanitize

## Raw Concept

Question: **how do you trust a third-party fine-tuned code/RTL model whose training data and adaptation process are opaque, when a backdoor can turn an innocent prompt into a malicious artifact?**

## Narrative

Any downstream consumer of an open-weight / third-party fine-tuned model inherits the provider's trust decisions. For **RTL**, the payoff is physical and hard to undo — a poisoned model can emit a **hardware Trojan** on a benign prompt, and the design may be manufactured before the trigger is caught.

**Sanitize-before-trust** is the pattern: instead of trusting the model's provenance, run a **cheap clean-teacher pass** that re-anchors the model's behavior. RTLGuard does this in three moves:

1. **Small clean teacher** — fine-tune on a small trusted RTL corpus.
2. **Composite teacher-student objective** — the poisoned target is guided toward the clean teacher's behavior.
3. **Feature alignment + knowledge distillation** — suppress the backdoor behavior directly (this is the mechanism that actually kills the malicious mapping, not just the trigger phrase).

This works without full-parameter retraining, and the paper reports it **lowers ASR while keeping the RTL functionally correct and synthesizable**. The same logic generalizes: **a poisoned / mislabeled fine-tune is a runtime-safety hazard that provenance alone cannot clear.** The defensive response is a post-hoc alignment / distillation pass against a trusted reference, not merely a scan for trigger strings.

**Operator steal (authorized lab / product pentest harness):**
1. **Treat any third-party fine-tune as possibly-poisoned** — do not gate a build on "the prompt looked benign"; the trigger is buried in the fine-tune.
2. **Sanitize-before-trust for codegen models** (RTL, firmware, HDL, anything synthesizable/compilable into a deployed artifact) using a small clean-teacher distillation pass on trusted data.
3. **Verify functional/synthesizable output**, not only a lower ASR — a sanitizer that breaks the artifact is not a defense.
4. **Pairs with release-time gates** — Gradient Immunity / DataShield-style subspace/consensus filters at publish, CWEEP-style CWE lint at design time. Defense-in-depth, not a single control.
5. **No clone, no trojan/PoC content in wiki** — document the defense pattern; keep payloads out. No public repo for this paper (name-collision repos `RTLGuardai`/`RTLGuard` are unrelated).

## Snippets

> A poisoned RTL generation model can trigger a hardware Trojan on a seemingly benign prompt; RTLGuard sanitizes the model with a clean teacher and feature alignment / knowledge distillation, lowering ASR while preserving functional correctness and synthesizability. [Source: arXiv 2608.26049 abstract]
