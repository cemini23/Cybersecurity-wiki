---
title: Tool-Guard
type: entity
tags: [tool, agent-security, defense, mcp, tool-poisoning]
keywords: [tool-guard, shishishi123, isolated planning, icml 2026, 2606.20922]
related:
  - sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
maturity: draft
created: 2026-06-24
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-06-24 — github.com/shishishi123/Tool-Guard MIT, 0★, last push 2026-05-25; ICML 2026 artifact — lab-validate ASR/utility on prod-mcp tool catalog before enforcement"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
---

## Relations

- @sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md — paper provenance
- @concepts/cross-tool-description-poisoning.md — threat model

## Raw Concept

| Field | Value |
|-------|-------|
| Name | Tool-Guard |
| Repo | [shishishi123/Tool-Guard](https://github.com/shishishi123/Tool-Guard) |
| Paper | arXiv:2606.20922 / ICML 2026 |
| License | MIT (GitHub API 2026-06-24) |
| Stars | 0 (2026-06-24) |

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/Tool-Guard` (~6.2MB, shallow). Lab-only until ASR/utility validated on prod-mcp catalog.


System-level defense implementing **isolated planning** against cross-tool description poisoning. Flagged tools move to an **influenced list** — excluded from planning context, still invokable if needed.

**AgentDojo (GPT-4o):** ASR 43.30% → **2.06%**; benign utility 76.29% → 72.16%.

**Steal-from:** influenced-list quarantine pattern for prod-mcp harness — do not require deleting tools from allowlist. **Lab-validate** latency (~3.7×) and token overhead (~1.4×) before default-on.

**Complements:** DefenseClaw/DCI scan (pre-connect), AIRGuard (execution-time authority) — Tool-Guard addresses **persistent metadata in planner context**.

## Snippets

```text
# Phase-0 checklist
- LICENSE: MIT ✓
- Maturity: 0★, single-maintainer ICML artifact
- Failure mode: cross-tool description poisoning in static MCP catalogs
- GO: CONDITIONAL — reproduce AgentDojo slice on local MCP gateway first
```
