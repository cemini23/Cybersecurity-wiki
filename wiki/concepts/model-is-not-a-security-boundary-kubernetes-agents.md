---
title: "The model is not a security boundary (Kubernetes agents) (K421)"
type: concept
tags: [concept, agent-security, k421]
keywords: [arXiv 2610.02861, K421]
related:
  - @ccc-wiki/concepts/model-is-not-a-security-boundary.md
  - sources/arxiv-2610-02861-kubernetes-agent-containment.md
  - concepts/agentic-containment-principles.md
  - concepts/cyber-capable-agent-evaluation-containment.md
  - concepts/coding-agent-supply-chain-install-gap.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K421)"
---

## Relations

- @@ccc-wiki/concepts/model-is-not-a-security-boundary.md — CCC harness-side statement of the same rule (K421)
- @sources/arxiv-2610-02861-kubernetes-agent-containment.md
- @concepts/agentic-containment-principles.md
- @concepts/cyber-capable-agent-evaluation-containment.md
- @concepts/coding-agent-supply-chain-install-gap.md

## Raw Concept

Question: **The model is not a security boundary (Kubernetes agents)** — operator steal from the inbound brief (arXiv 2610.02861)?

## Narrative

Start from one sentence: **prompts and classifiers lower the probability of misbehaviour and guarantee nothing**, and their failure modes are discoverable by an adversary. So an agent that can act on infrastructure gets secured the way any multi-tenant workload is — **assume compromise and bound reach, action, and egress.**

The specific failure to design against is the collapse of **data/control separation**: anything the agent *reads* (a log line, an annotation, a ticket field, **a third-party MCP tool description**) can become an instruction it executes with its own credentials.

The most portable rule is to **never combine untrusted input + sensitive access + external egress** — the lethal trifecta. In Kubernetes the controls are ordinary platform controls: audience-bound ServiceAccount tokens, CEL admission policy for object-level validation, sandboxed runtimes, **FQDN-aware egress**, a tool gateway that applies policy to tool **arguments**, eBPF runtime enforcement, and audit logs. Enforcement lives **outside** the model. Same statement as the federation invariant "gate the tool step; model self-arbitration is not a boundary", applied to a cluster.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-07)]
