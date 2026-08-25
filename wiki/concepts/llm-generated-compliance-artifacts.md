---
title: "LLM-generated compliance artifacts — candidates, not deliverables (K306)"
type: concept
tags: [concept, llm, compliance, gdpr, dpia, dpp, k306, watch]
keywords: [LLM compliance artifacts, DPIA, DPP, DBP, ESPR, GDPR, HITL, hallucination, schema-valid not correct]
related:
  - sources/arxiv-2608-21317-llm-regulatory-compliance-artifacts.md
  - concepts/compliance-detector-rule-blindness.md
  - concepts/llm-generated-dependency-breaking-tests.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K306)"
---

## Relations

- @sources/arxiv-2608-21317-llm-regulatory-compliance-artifacts.md
- @concepts/compliance-detector-rule-blindness.md — same lesson on the detection side: schema/format conformance ≠ semantic correctness
- @concepts/llm-generated-dependency-breaking-tests.md — LLM-generated artifacts are candidates, not a merge gate (K300 parallel)

## Raw Concept

Question this page answers: **can LLMs be trusted to draft regulatory compliance artifacts (DPIAs, Digital Product Passports), and what guardrails do you need around that?**

## Narrative

Compliance artifacts (GDPR DPIAs, ESPR Digital Product Passports / Digital Battery Passports) are hard to produce manually: heterogeneous industrial data, no standardized DPIA format, interdisciplinary expertise required. LLM-assisted generation is proposed, but the study (K306, 2608.21317) shows quality depends on **regulation strictness × prompt context**, not just model:

- **Vague standards (DPIA):** need **higher-context prompts** to stay consistent and complete — sparse instructions produce drift.
- **Strict formats (DBP):** consistent output regardless of context, but **more hallucinations** — the model confidently fills gaps in a rigid schema.
- Evaluated against manually-created **ground-truth schemas** across five models (GPT-4o, Claude 4.6 Sonnet, Llama-3.1-8B, Mistral-7B, Qwen2.5-7B).

**Operator steal (defensive / Watch):**
1. **LLM compliance artifacts are candidates, not deliverables.** Schema-valid and consistent ≠ legally or technically correct — exactly the `compliance-detector-rule-blindness` lesson (a guard that passes format checks can still miss the substance) and the `llm-generated-dependency-breaking-tests` lesson (generated artifacts review before they gate anything).
2. **Hallucination concentrates where confidence is highest** — strict-format artifacts are the *most* dangerous, because the output looks the most authoritative. Add a verification pass against ground-truth schemas / source data, not just a format check.
3. **Privacy: DPIA data is sensitive.** Do not send private-data context to third-party APIs for artifact generation; prefer isolated/local models (paper flags this; pairs `local-abliterated-llm-pentest-stack` isolation philosophy and `agent-vm-sandboxing`).
4. **HITL is non-negotiable** for anything that becomes a legal/regulatory record; the LLM drafts, a qualified human owns the artifact.
5. This is a **Watch** wire, not an adoption: no artifact templates for production use are filed from this source.

## Snippets

> Stricter guidelines … result in consistent results regardless of prompt context, but may lead to more hallucinations in the output. [Source: arXiv 2608.21317 abstract]
