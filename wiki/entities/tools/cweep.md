---
title: CWEEP
type: entity
category: tool
tags: [entity, tool, hardware-security, rtl, apache, conditional-go]
keywords: [CWEEP, Verible, RTL lint, CWE, bryan-kwan]
related:
  - sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md
  - concepts/cweep-rtl-cwe-early-prevention.md
  - concepts/ai-for-cybersecurity.md
  - concepts/chiplet-llm-hardware-security.md
  - sources/arxiv-2608-05063-chiplet-llm-hardware-security.md
maturity: draft
created: 2026-08-03
updated: 2026-08-06
phase_0_verdict: "CONDITIONAL-GO 2026-08-03 — Apache-2.0; ~15MB; github.com/bryan-kwan/cweep"
wire_status: deferred
wire_target: "owned RTL lab only — no Cursor alwaysApply / MCP"
---

## Relations

- @sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md
- @concepts/cweep-rtl-cwe-early-prevention.md
- @concepts/ai-for-cybersecurity.md

**Local clone:** `raw-sources/repos/cweep` (~15MB)
- @concepts/chiplet-llm-hardware-security.md
- @sources/arxiv-2608-05063-chiplet-llm-hardware-security.md

## Narrative

### Phase-0 (2026-08-03): CONDITIONAL-GO

| Gate | Status |
|------|--------|
| License | **PASS** — Apache-2.0 (Verible fork) |
| Size | **PASS** — ~15MB shallow |
| Contents | CWE lint rules in `verible/verilog/analysis/checkers` |
| Verdict | **CONDITIONAL-GO** — lab RTL only; build via bazel; `--autofix=patch` optional |

Usage sketch (owned lab): `verible-verilog-lint <file> -ruleset=none -rules=<cwe-rule>`.
