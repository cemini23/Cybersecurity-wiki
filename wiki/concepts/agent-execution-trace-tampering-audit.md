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
maturity: validated
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

Assume **agent-writable trace files are untrusted** for IR, compliance, and async monitoring. Mitigations: **out-of-band append-only** capture, **tool-call execution attestation** (not API log alone), monitor **skill-install** paths, and test **model downgrade** paths that bypass premium guardrails. **Muse-style immutable-trace reminders** are a partial harness control, not a complete boundary.
## Snippets

> "Even when an agent has full access to perform its task, it must not be able to edit the traces used to monitor and evaluate it." [Source: arXiv 2609.30266; K373]