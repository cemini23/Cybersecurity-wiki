---
title: ai-redteam-evidential-limits
type: entity
category: tool
tags: [entity, tool, mit, llm-safety, evaluation, go]
keywords: [hackwither, evidential ceiling, HarmBench, AdvBench]
related:
  - concepts/llm-adversarial-fuzzing.md
  - sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-29
updated: 2026-10-09
phase_0_verdict: "GO 2026-07-29 — MIT; ~528KB; github.com/hackwither/ai-redteam-evidential-limits"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @concepts/llm-adversarial-fuzzing.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/ai-for-cybersecurity.md

**Local clone:** `raw-sources/repos/ai-redteam-evidential-limits` (~528KB)

## Narrative

### Phase-0 (2026-07-29): GO

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Size | **PASS** — ~528KB |
| Contents | analysis + docs + tests for evidential-ceiling math |
| Verdict | **GO** — lab reproduce null-result ceilings on HarmBench/AdvBench-class suites |
