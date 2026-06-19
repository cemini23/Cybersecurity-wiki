---
title: TOOLPRIVBENCH — over-privileged tool selection benchmark
type: entity
tags: [tool, benchmark, agent-security, least-privilege, tool-selection]
keywords: [toolprivbench, opur, ped, 2606.20023, agent-tool-selection-bias]
related:
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/airguard.md
maturity: draft
created: 2026-06-19
updated: 2026-06-19
phase_0_verdict: "Reference 2026-06-19 — github.com/AISafetyHub/agent-tool-selection-bias: 0★, README MIT badge, gh api LICENSE null + LICENSE 404; use methodology until SPDX verified"
---

## Relations

- @sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md — paper provenance
- @concepts/agent-least-privilege-tool-selection.md — OPUR/PED concepts + mitigation ladder
- @concepts/mcp-security-posture.md — prod MCP eval complements K100 stack

## Raw Concept

| Field | Value |
|-------|-------|
| Name | TOOLPRIVBENCH |
| Repo | [AISafetyHub/agent-tool-selection-bias](https://github.com/AISafetyHub/agent-tool-selection-bias) |
| Paper | arXiv:2606.20023 |
| Scale | 544 scenarios · 8 domains · 5 risk types |
| License (claimed) | MIT (README badge) |
| License (verified) | **None on GitHub API 2026-06-19** — LICENSE file 404 |

## Narrative

Simulation benchmark for **privilege-sensitive tool selection** in LLM agents. Each scenario provides three lower-privilege and three higher-privilege tools, all independently sufficient for the user task, enabling measurement of **over-privilege preference** without capability confounds.

Reports **OPUR** (Over-Privileged Tool Use Rate) and **PED** (Pre-Escalation Exploration Depth). Supports multi-turn eval with injected transient failures on lower-privilege tools to study **premature escalation**.

**Steal-from:** eval protocol for prod-mcp agent configs — paired narrow/broad tool scenarios + 503 injection pattern. **Do not** clone repo into IP-sale surfaces until LICENSE file lands.

**Complements:** AgentHarm (harmful refusal), AIRGuard (runtime authority), SkillGuard (permission metadata) — TOOLPRIVBENCH tests whether agents pick minimally privileged tools among **authorized** options.

## Snippets

```text
# Eval dimensions (from paper)
Domains: Database, Business, Education, Coding, Gov, Health, Media, Infra
Risk types: Authority Escalation, Scope Expansion, Temporal Persistence,
            Safety Bypass, Data Over-Exposure
Turn cap: k=5 per scenario
```
