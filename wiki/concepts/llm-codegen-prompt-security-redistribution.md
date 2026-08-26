---
title: "LLM codegen prompt security — redistribution not reduction (K309)"
type: concept
tags: [concept, agent-security, secure-coding, prompt-engineering, sast, k309, defensive]
keywords: [prompt structure, Bandit, CodeQL, CWE redistribution, secure codegen, semantic drift, compliance vs security]
related:
  - sources/arxiv-2608-24857-prompt-structure-security-redistribution.md
  - concepts/nl-security-rules-vs-builtin-deny.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K309)"
---

## Relations

- @sources/arxiv-2608-24857-prompt-structure-security-redistribution.md
- @concepts/nl-security-rules-vs-builtin-deny.md — NL security guidance ≠ enforcement
- @concepts/coding-agent-supply-chain-install-gap.md — generated code still needs verify gates
- @concepts/agent-runtime-guardrails.md — agent codegen is a side-effect surface
- @sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md — LLM-generated tests are candidates (K300)

## Raw Concept

Question: **does adding security structure to codegen prompts make the output safer, or just change which findings static analysis reports?**

## Narrative

K309 (2608.24857) tests five prompt variants on 424 security-sensitive Python tasks (GPT-4o, LLaMA 3.1-8B) with Bandit + CodeQL.

**Compliance wins:** structured prompts produce valid code far more often — fewer refusals and malformed outputs.

**Security nuance:** overall weakness **prevalence** often stays flat; **severity and CWE mix shift**. GPT-4o moves findings from HIGH toward LOW severity under stronger prompts while dominant classes (CWE-78 injection, CWE-502 deserialization) remain common. Stricter prompts can also **silently drop** requested unsafe constructs (semantic drift).

**Operator steal:**
1. **Do not count fewer HIGH findings as "secure"** without checking total prevalence and CWE mix.
2. **Keep SAST + human review in the loop** for agent-generated code — prompts are not a substitute (pairs K303 prose ≠ deny).
3. **Watch semantic drift** — the model may comply with "be safe" by deleting requested functionality; verify against the spec.
4. **Model-dependent** — LLaMA showed weaker, less monotonic severity shifts than GPT-4o.

## Snippets

> The dominant effect is not reduction but redistribution. [Source: arXiv 2608.24857 §I]

> CWE-78 and CWE-502 remain highly prevalent regardless of prompt structure. [Source: arXiv 2608.24857 §results]
