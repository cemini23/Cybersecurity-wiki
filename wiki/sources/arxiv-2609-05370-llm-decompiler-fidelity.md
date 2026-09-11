---
title: "When LLM Decompilers Recompile More and Preserve Less (arXiv 2609.05370)"
type: source
tags: [source, arxiv, reverse-engineering, malware-analysis, llm, eval, k335]
keywords: [2609.05370, LLM decompiler, Ghidra, recompilability, vulnerability analysis, malware]
related:
  - concepts/llm-decompiler-recompilability-fidelity.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — decompiler eval discipline; no exploit payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K335)"
---

## Relations

- @concepts/llm-decompiler-recompilability-fidelity.md — K335 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When LLM Decompilers Recompile More and Preserve Less |
| arXiv | 2609.05370 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.05370-when-llm-decompilers-recompile-more-and-preserve.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

LLM decompilers produce clean, recompilable C while traditional tools expose unresolved artifacts — but **recompilability metrics can overstate fidelity**. **K335** shows LLM decompilers **recompile more yet preserve less** semantically vs Ghidra/Hex-Rays baselines. **Audit steal:** do not treat build+execute pass as ground truth for vuln/malware review; require semantic diff checks and analyst spot audits on security-critical paths.

## Snippets

> LLM decompilers score high on recompilability while losing semantic fidelity vs traditional decompilers. [Source: arXiv 2609.05370 abstract]
