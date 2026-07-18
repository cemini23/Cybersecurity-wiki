---
title: CLAWAUDIT
type: entity
tags: [tool, agent-security, static-analysis, openclaw, benchmark]
keywords: [clawaudit, srestlabub, openclawbench, semgrep, codeql, 2606.21071]
related:
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - concepts/local-agent-runtime-audit.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/ai-infra-guard.md

maturity: draft
created: 2026-06-24
updated: 2026-07-18
phase_0_verdict: "CONDITIONAL-GO 2026-06-24 — github.com/SRestLabUB/ClawAudit 0★, gh api LICENSE null + LICENSE 404; Semgrep/CodeQL rules + OPENCLAWBENCH usable for audit methodology after manual triage gate"
---

## Relations

- @sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md — paper + benchmark provenance
- @concepts/local-agent-runtime-audit.md — methodology synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Name | CLAWAUDIT |
| Repo | [SRestLabUB/ClawAudit](https://github.com/SRestLabUB/ClawAudit) |
| Benchmark | OPENCLAWBENCH (446 OpenClaw advisories, 217 held-out test) |
| Backends | 47 Semgrep YAML + 30 CodeQL queries |
| License (verified) | **None on GitHub API 2026-06-24** — LICENSE 404 |

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/ClawAudit` (~1.0MB, shallow). **No LICENSE file** — methodology/rules only; no code import into prod without SPDX.


Static auditing framework for **local LLM agent runtime source** — STRIDE-derived rules targeting prompt builder, parser, dispatcher, skill loader, memory writer, network client, permission gate boundaries.

**Held-out recall lift:** Semgrep 21.7%→66.8%; CodeQL 13.8%→75.1%.

**Steal-from:** agent-runtime Semgrep/CodeQL rule pack pattern for OpenClaw forks. **Do not** auto-fail CI on raw findings — paper notes recall-oriented rules need semantic filtering / manual triage.

**Layer with:** SkillSpector + DefenseClaw (pre-install), SeClaw (behavioral), AIRGuard (runtime).

## Snippets

```text
# Phase-0 checklist
- LICENSE: missing on API — treat rules as reference until SPDX filed
- Maturity: 0★, academic artifact (UB SUNY)
- Failure mode: implementation-level runtime weaknesses missed by black-box eval
- GO: CONDITIONAL — run on OpenClaw fork; human triage before CI gate
```
