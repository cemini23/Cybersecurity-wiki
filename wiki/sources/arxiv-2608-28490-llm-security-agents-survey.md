---
title: "LLM-Based Agents for Software and Systems Security — systematic review (arXiv 2608.28490)"
type: source
tags: [source, arxiv, agent-security, survey, software-security, k315]
keywords: [2608.28490, LLM agents, software security, systems security, systematic literature review, assessment, bounded authority, auditable behavior]
related:
  - concepts/security-agent-authority-auditability-slr.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-pentest-harness-landscape.md
maturity: draft
read_status: read
created: 2026-08-31
updated: 2026-08-31
phase_0_verdict: "REFERENCE 2026-08-31 — peer-reviewed SLR (100 papers, Jan 2023–Mar 2026); taxonomy + synthesis only; no tool clone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K315)"
---

## Relations

- @concepts/security-agent-authority-auditability-slr.md — primary steal (act but not bounded/auditable)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment |
| Authors | Jingjing Nie, Jiawei Guo, Krishna Meda, Haipeng Cai (University at Buffalo, SUNY) |
| arXiv | 2608.28490 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.28490-llm-based-agents-for-software-and-systems-securi.pdf |
| Retrieved | 2026-08-31 |
| Read status | read (abstract + contributions) |
| Public code | none — survey paper |

## Narrative

Systematic literature review of **100 peer-reviewed papers** (January 2023 – March 2026) on LLM-based agents for software and systems security. Three-axis taxonomy:

1. **Approach** — architecture, perception, memory, reasoning/planning, action space, orchestration, self-improvement
2. **Application** — vulnerability analysis, pentest, patching, SOC, malware/RE, fuzzing, access-control assessment, etc.
3. **Assessment** — datasets, outcome + trajectory metrics, safety measures, baselines, protocols

**Central synthesis:** the field has built agents **able to act**, but not yet agents whose **authority is bounded** or whose **behavior is auditable**. Final task success alone does not show faithful evidence use, scope adherence, hallucination avoidance, tool-permission respect, or cost.

**Why filed (K315):** vocabulary for comparing security-agent papers and benchmarks; pairs K271 faithful ASR, `@concepts/llm-pentest-automation.md`, `@concepts/agent-runtime-guardrails.md`. Survey REFERENCE only — no clone.

## Snippets

> The field has built agents able to act but not yet agents whose authority is bounded or whose behavior is auditable. [Source: arXiv 2608.28490 abstract]

> Assessment protocols are often incomparable; the term “agent” is applied inconsistently across papers. [Source: arXiv 2608.28490 abstract, paraphrase]
