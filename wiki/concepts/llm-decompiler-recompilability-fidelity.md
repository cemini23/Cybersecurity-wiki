---
title: "LLM decompiler recompilability vs semantic fidelity (K335)"
type: concept
tags: [concept, reverse-engineering, malware-analysis, llm, eval, k335]
keywords: [2609.05370, LLM decompiler, Ghidra, recompilability, vulnerability analysis, malware]
related:
  - sources/arxiv-2609-05370-llm-decompiler-fidelity.md
  - concepts/malware-analysis.md
  - concepts/exploit-development.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K335)"
---

## Relations

- @sources/arxiv-2609-05370-llm-decompiler-fidelity.md — When LLM Decompilers Recompile More and Preserve Less (2609.05370)

## Raw Concept

Question: **LLM decompiler recompilability vs semantic fidelity** — what should operators steal from this paper?

## Narrative

LLM decompilers produce clean, recompilable C while traditional tools expose unresolved artifacts — but **recompilability metrics can overstate fidelity**. **K335** shows LLM decompilers **recompile more yet preserve less** semantically vs Ghidra/Hex-Rays baselines. **Audit steal:** do not treat build+execute pass as ground truth for vuln/malware review; require semantic diff checks and analyst spot audits on security-critical paths.

## Snippets

> LLM decompilers score high on recompilability while losing semantic fidelity vs traditional decompilers. [Source: arXiv 2609.05370 abstract]
