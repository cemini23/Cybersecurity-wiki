---
title: "Chain-of-thought decorative reasoning — perturbation audit (K308)"
type: concept
tags: [concept, agent-security, chain-of-thought, audit, interpretability, k308, defensive]
keywords: [decorative reasoning, CoT faithfulness, chain decoupling, cdr, perturbation audit, counterfactual, rationale evidence]
related:
  - sources/arxiv-2608-24790-decorative-reasoning-medical-cot.md
  - concepts/agent-runtime-guardrails.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/atobench-verification-chain-deception.md
  - concepts/compliance-detector-rule-blindness.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K308)"
---

## Relations

- @sources/arxiv-2608-24790-decorative-reasoning-medical-cot.md
- @concepts/agent-runtime-guardrails.md — agent "reasoning" surfaces in harness audit
- @concepts/faithful-agent-asr-measurement.md — do not trust trajectory self-report
- @concepts/atobench-verification-chain-deception.md — activity ≠ grounded verification
- @concepts/compliance-detector-rule-blindness.md — verdict must track stated rule under counterfactuals

## Raw Concept

Question: **when an LLM shows step-by-step reasoning, does that text prove how the answer was computed?**

## Narrative

Visible CoT can improve answers **and** give humans a surface to scrutinize. K308 (2608.24790) shows the second role often fails: on medical QA, **72.9% chain-decoupling rate (cdr)** — destructive question edits that the chain ignores while the answer stays unchanged. Corrupting the chain barely moves accuracy; removing CoT prompting does not hurt accuracy. The chain frequently **narrates** rather than **loads**.

**Audit pattern (steal for any high-stakes agent):**
1. **Perturb inputs** with clinically or logically meaningful edits (negation, severity, scope).
2. **Joint score** chain update × answer flip — high cdr ⇒ decorative CoT.
3. **Do not use CoT as compliance evidence** without counterfactual tests (pairs K290 CHIVE, rule-blindness crossed-rule probes).
4. **Closed models** — when chain text is hidden, rely on **external verification** (tool receipts, state diffs), not answer confidence.

Authorized lab framing for medical models; methodology applies to security copilots and agent audit panels.

## Snippets

> Three independent tests converge: cdr is 72.9% panel-wide; chain corruption leaves accuracy unchanged; removing CoT prompting does not reduce accuracy. [Source: arXiv 2608.24790 abstract]

> The visible CoT has to actually track and drive the underlying computation, not narrate it after the fact. [Source: arXiv 2608.24790 §1]
