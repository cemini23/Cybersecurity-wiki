---
title: "Task-conditioned excess authority (eval axis)"
type: concept
tags: [concept, agent-security, least-privilege, mcp, ccc-k290]
keywords: [excess authority, sufficient-authority envelope, trajectory audit, 2608.18351]
related:
  - sources/arxiv-2608-18351-excess-authority-least-privilege.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-security-posture.md
  - concepts/lingering-authority-revocable-capabilities.md
  - concepts/intent-governed-tool-authorization.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (CCC K290 excess-authority)"
---

## Relations

- @sources/arxiv-2608-18351-excess-authority-least-privilege.md
- @concepts/agent-least-privilege-tool-selection.md — over-privileged tool *selection* vs excess *trajectory* authority
- @concepts/mcp-security-posture.md
- @concepts/lingering-authority-revocable-capabilities.md
- @concepts/intent-governed-tool-authorization.md

## Raw Concept

An agent can be correct on the task and still be over-authorized.

## Narrative

Score **trajectories**, not only final-answer correctness. Define a per-task sufficient-authority envelope (minimum tools / files / scopes). Audit each terminal or MCP action with a deterministic pre/post vector (completion, evidence, exact state, prohibited attempts, safe success, plus the paper's sixth risk dimension). Excess = authority beyond the envelope even when the task succeeds. [Source: arXiv 2608.18351]

Pairs: TOOLPRIVBENCH/OPUR (tool *choice*), PORTICO lingering authority (time), IGAC intent certificates (session narrowing), Mandato signed mandates (CCC K285). Post-training restraint is an extra layer, not a substitute for gates and sandboxing.

**Dual-ID:** this is CCC K290. Cybersec K290 remains CHIVE. Atto-priority for MCP proxy eval.

**Phase-0:** no exploit PoCs; authorized lab eval only; no clone.

## Snippets

> Traditional permission gating systems alone for validating agent environments are insufficient. [Source: arXiv 2608.18351 abstract]
