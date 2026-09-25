---
title: "Agent execution trace tampering audit (K373)"
type: concept
tags: [concept, agent-security, k373]
keywords: [2609.30266, K373]
related:
  - sources/arxiv-2609-30266-llm-agents-trace-tampering.md
  - concepts/agent-execution-provenance.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/trace-verified-ctf-agent-eval.md
maturity: draft
created: 2026-09-25
updated: 2026-09-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K373)"
---

## Relations

- @sources/arxiv-2609-30266-llm-agents-trace-tampering.md
- @concepts/agent-execution-provenance.md
- @concepts/faithful-agent-asr-measurement.md
- @concepts/trace-verified-ctf-agent-eval.md

## Raw Concept

Question: **Agent execution trace tampering audit** — operator steal from arXiv 2609.30266?

## Narrative

Treat agent-visible log files as **untrusted**. Compliance and IR reconstructions need **append-only / out-of-band** trace capture with **integrity checks**. Report harness + model when citing tampering rates.

## Snippets

> Triage from arXiv 2609.30266 abstract. [Source: arXiv 2609.30266 (retrieved 2026-09-25)]
