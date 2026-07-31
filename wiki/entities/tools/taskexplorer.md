---
title: "TaskExplorer — Windows kernel process introspection"
type: entity
tags: [tool, windows-kernel, process-introspection, gpl-3, defensive-security, sysinternals-alternative]
keywords: [taskexplorer, windows kernel, process introspection, gpl-3, sysinternals alternative]
related:
  - "@osint-wiki/entities/tools/taskexplorer.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - concepts/malware-analysis.md
maturity: draft
created: 2026-05-12
updated: 2026-07-31
osint_eval_origin: doc1-url-7 (cross-routed; cybersec primary)
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- `@osint-wiki/entities/tools/taskexplorer.md` — OSINT cross-route
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 7)
- @concepts/malware-analysis.md — kernel process introspection for malware behavior analysis
## Raw Concept

- **License**: GPL-3.0
- **Tier**: Reference / Adopt-candidate for Windows IR

## Narrative

Open-source Windows kernel-mode process explorer. Use cases: incident response on Windows hosts, malware behavior analysis, process-hollowing / injection detection. GPL-3.0 — acceptable for IR-team-internal use; not embeddable in commercial products.

### Phase-0 audit pending

Verify driver signing situation, Win10/11 + Server compat, last-commit recency, alternative comparison (Process Hacker, System Informer).
