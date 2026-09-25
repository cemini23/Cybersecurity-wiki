---
title: "LLM agents can easily tamper with their own traces"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.30266, k373]
related:
  - concepts/agent-execution-trace-tampering-audit.md
  - concepts/agent-execution-provenance.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-09-25
updated: 2026-09-25
phase_0_verdict: "REFERENCE 2026-09-25 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K373)"
---


## Relations

- @concepts/agent-execution-trace-tampering-audit.md
- @concepts/agent-execution-provenance.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | LLM agents can easily tamper with their own traces |
| arXiv | 2609.30266 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609-30266-llm-agents-can-easily-tamper-with-their-own-trac.pdf |
| Retrieved | 2026-09-25 |
| Read status | read (abstract + triage) |

## Narrative

**K373** — local coding agents (multiple harnesses tested) can **delete or alter execution traces** on request; **external attackers** can induce deletion; **reward-seeking** can elicit tampering without explicit ask. **Muse Code** exception noted in paper triage. Audit steal: **independent interception logging** outside agent write path — trajectory self-report ≠ evidence (pairs K271/K278). **Runtime:** `scripts/k373_agent_trace_tampering_precheck.py`.

## Snippets

> See arXiv 2609.30266 abstract. [Source: arXiv 2609.30266 (retrieved 2026-09-25)]
