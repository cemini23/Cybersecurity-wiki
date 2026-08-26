---
title: "Prompt structure redistributes LLM codegen security weaknesses (arXiv 2608.24857)"
type: source
tags: [source, arxiv, agent-security, secure-coding, prompt-engineering, k309]
keywords: [2608.24857, prompt engineering, Bandit, CodeQL, secure codegen, CWE redistribution, GPT-4o, LLaMA]
related:
  - concepts/llm-codegen-prompt-security-redistribution.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-26
updated: 2026-08-26
phase_0_verdict: "REFERENCE 2026-08-26 — empirical study; no tool repo. Policy: structured prompts improve compliance but do not substitute SAST/review."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K309)"
---

## Relations

- @concepts/llm-codegen-prompt-security-redistribution.md — primary steal

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code |
| Authors | Maitreyee Das Urmi et al. (Toronto Metropolitan U / Colorado State U) |
| arXiv | 2608.24857 (11 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.24857-prompt-structure-redistributes-not-reduces-an-em.pdf` |
| Retrieved | 2026-08-26 |
| Read status | read (abstract + methodology + severity/CWE analysis) |
| Public code | none at retrieval |

## Narrative

424 security-sensitive Python tasks; GPT-4o and LLaMA 3.1-8B; five prompt variants adding structure + security guidance; evaluated with **Bandit** and **CodeQL**.

**Compliance:** structured prompts cut refusals/invalid outputs sharply (GPT-4o invalid 338/424 → 37–52), enabling large-scale static analysis.

**Security:** stronger prompts do **not** consistently reduce overall weakness prevalence. For GPT-4o, risk **redistributes**: high-severity Bandit findings **20.8% → 13.6%** while low-severity **32% → 43.5%**. Dominant CWE classes (CWE-78 OS command injection, CWE-502 deserialization) **persist** across prompt variants. Some classes (CWE-94/95 dynamic code) shift more than others.

**Semantic drift:** stricter prompts may silently remove or rewrite explicitly requested unsafe constructs — compliance without honoring task intent.

**Why filed (K309):** agent codegen harnesses must not treat "security prompt" as a control — SAST + human review remain gates (pairs K300 BreakGuard dependency tests as candidates, not deploy gates).

## Snippets

> Structured prompting substantially reduces refusals … but security-oriented refinements do not consistently reduce overall weakness prevalence. [Source: arXiv 2608.24857 abstract]

> For GPT-4o, stronger prompts primarily redistribute risk: high-severity findings fall while low-severity findings rise. [Source: arXiv 2608.24857 abstract]

> Prompt structure improves compliance but is an unreliable substitute for robust security controls in LLM-assisted development. [Source: arXiv 2608.24857 abstract]
