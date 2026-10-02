---
title: "KaliBench — NL-to-CLI tool-use evaluation (K391)"
type: concept
tags: [concept, agent-security, k391]
keywords: [2610.02206, K391]
related:
  - concepts/k278-security-wave.md
  - sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md
  - concepts/secure-ai-powered-pentest-agents.md
  - concepts/privescalate-llm-linux-privilege-escalation.md
  - concepts/security-agent-authority-auditability-slr.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K391)"
---

## Relations

- @concepts/k278-security-wave.md — K278 wave aggregation page
- @sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md
- @concepts/secure-ai-powered-pentest-agents.md
- @concepts/privescalate-llm-linux-privilege-escalation.md
- @concepts/security-agent-authority-auditability-slr.md

## Raw Concept

Question: **KaliBench — NL-to-CLI tool-use evaluation** — operator steal from arXiv 2610.02206?

## Narrative

Score an agent's tool invocation against a **fixed reference command**, not against its own account of what it ran. KaliBench does this **without executing** anything: canonicalise the command, then match tool name, alias-aware optional flags, and ordered positional arguments. The split worth reusing is **tool selection vs argument construction** — selection nearly resolves when the candidate set is narrowed, while exactness does not move until the arguments are pinned down. Report both, never a single 'tool accuracy' figure. Caveat: ground truth comes from manuals captured at build time, so flags drift. Licence claim unverified — no clone, no dataset download.

## Snippets

> See arXiv 2610.02206 abstract. [Source: arXiv 2610.02206 (retrieved 2026-10-02)]
