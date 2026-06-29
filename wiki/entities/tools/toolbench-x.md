---
title: ToolBench-X
type: entity
tags: [tool, benchmark, agent-evaluation, tool-use, reliability]
keywords: [toolbench-x, foreverskyou, tool environment unreliability, hazard injection, 2606.25819]
related:
  - sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md
  - concepts/tool-environment-unreliability-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/seclaw-eval.md
  - concepts/llm-pentest-automation.md
  - concepts/mcp-security-posture.md
maturity: draft
created: 2026-06-27
updated: 2026-06-27
phase_0_verdict: "Reference 2026-06-27 — github.com/Foreverskyou/ToolBench-X 0★, LICENSE absent, README: full release organizing; re-audit on artifact drop"
---

## Relations

- @sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md — paper + benchmark design
- @concepts/tool-environment-unreliability-eval.md — when to use vs SeClaw / AgentDojo

## Raw Concept

Phase-0 audit 2026-06-27 on arXiv:2606.25819 linked repo [Foreverskyou/ToolBench-X](https://github.com/Foreverskyou/ToolBench-X).

## Narrative

Executable benchmark injecting **five recoverable hazard types** into deterministic tool environments (~1,106 tasks). Evaluates **task completion under P_h**, not function-call syntax alone.

### Phase-0 audit summary

| Check | Result |
|-------|--------|
| License | **None** (404 on LICENSE) |
| Maturity | 0★; README: "organizing the codebase… full release… soon" |
| vs SeClaw | ToolBench-X = **benign reliability** hazards; SeClaw = **security** trajectories |
| vs AgentDojo | ToolBench-X stresses **recovery** from tool faults; AgentDojo = injection attacks |

**Verdict: Reference** until LICENSE + benchmark tarball ship. Track repo for **CONDITIONAL-GO** re-audit.

See `briefs/2026-06-27_toolbench-x-prod-mcp-reliability-eval-checklist.md` for prod-mcp hazard-injection regression gates.

## Snippets

[Source: github.com/Foreverskyou/ToolBench-X + arxiv-2606.25819]
