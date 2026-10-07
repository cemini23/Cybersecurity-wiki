---
title: "Separate model risk from harness risk (K282-b)"
type: concept
tags: [concept, agent-security, k282-b]
keywords: [arXiv 2610.03153, K282-b]
related:
  - sources/arxiv-2610-03153-evoriskbench-runtime.md
  - concepts/cyber-capable-agent-evaluation-containment.md
  - concepts/agentic-containment-principles.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K282-b)"
---

## Relations

- @sources/arxiv-2610-03153-evoriskbench-runtime.md
- @concepts/cyber-capable-agent-evaluation-containment.md
- @concepts/agentic-containment-principles.md

## Raw Concept

Question: **Separate model risk from harness risk** — operator steal from the inbound brief (arXiv 2610.03153)?

## Narrative

An agent-security number is produced by a **model running in a harness**. EvoRiskBench measured nine combinations and found **model spread 54.37 pp against harness spread 5.41 pp** — most of the variance is the model, but the harness contributes a real, repeatable 5 pp, and that is the part an operator can actually change (tool gating, sandboxing, egress rules).

So: always report **model x harness** together, and when you harden the harness, expect a **single-digit** improvement, not a transformation — the rest is the model. Injection arrives through tools, skills, and subagents, so those are the surfaces to instrument. This is the measurement counterpart to the K421 containment rule.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-07)]
