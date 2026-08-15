---
title: Measurement integrity in MCP security eval — labels are not endpoints
type: concept
tags: [concept, mcp, evaluation, measurement, agent-security]
keywords: [labels not endpoints, integrity chain, treatment-blind grading, scope honesty, MCP eval]
related:
  - sources/arxiv-2608-12880-labels-not-endpoints.md
  - concepts/mcp-security-posture.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/atobench-verification-chain-deception.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/measurement-integrity-mcp-security-eval.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (CCC K277 dual-ID note)"
---

## Relations

- @sources/arxiv-2608-12880-labels-not-endpoints.md — primary paper
- @concepts/faithful-agent-asr-measurement.md — do not collapse exposure/execution/observation/adjudication
- @concepts/atobench-verification-chain-deception.md — ATOBench: activity ≠ verification
- @concepts/mcp-security-posture.md — MCP security claims inherit this measurement rule

## Raw Concept

When an MCP/agent security paper reports an "attack success rate," what exactly was measured — and what inference does that number *not* support?

## Narrative

**Labels are not behavioral endpoints.** Bind: (1) treatment bytes, (2) executed behavior, (3) authorization, (4) outcome rule, (5) analysis unit. Graders must not see treatment metadata when assigning outcome classes. Use a seven-link Integrity Chain with fail-closed conditions. **Scope honesty:** campaign counts are not population rates, model rankings, defense-efficacy, or causal estimates. Dual-ID: CCC board K277; Cybersec K277 remains RSM. [Source: arXiv:2608.12880]
