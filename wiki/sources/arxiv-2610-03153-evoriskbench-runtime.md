---
title: "EvoRiskBench: runtime risk across model x harness configurations"
type: source
tags: [source, routed, agent-security]
keywords: [arXiv 2610.03153]
related:
  - concepts/harness-vs-model-risk-share.md
  - concepts/cyber-capable-agent-evaluation-containment.md
  - concepts/agentic-containment-principles.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/harness-vs-model-risk-share.md
- @concepts/cyber-capable-agent-evaluation-containment.md
- @concepts/agentic-containment-principles.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EvoRiskBench: runtime risk across model x harness configurations |
| Identifier | arXiv 2610.03153 |
| Type | arXiv paper (routed by OSINT K282) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-07 |
| Read status | read (routed brief) |

## Narrative

**The number the federation did not have.** Nine model x harness configurations, indirect prompt injection arriving through **MCP tools, skills, and subagents** — the exact surfaces this federation ships. Aggregate attack success rate **37.46%**; worst configuration **68.44%** (DeepSeek-V4-Pro-0813 x Codex).

**The finding that matters for how we measure:** **model spread (54.37 pp) is far larger than harness spread (5.41 pp)**. So the harness is *not* where most of the variance lives — but 5 pp across harnesses is still a real, measurable difference, and it is the part an operator can change. Operator steal: when you report an agent-security number, **say which model and which harness produced it**; a model-only or harness-only claim is under-specified. Pairs K341 and the containment line. **Measurement recommendation, not an adoption.** Any run against our own harness is a scoped, authorised test. **No injection payloads in wiki.**

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-07)]
