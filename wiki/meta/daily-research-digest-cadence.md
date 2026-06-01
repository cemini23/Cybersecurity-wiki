---
title: Daily research digest cadence (cybersec)
type: concept
tags: [meta, automation]
related:
  - concepts/threat-intelligence.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-06-01-daily.md
  - "@osint-wiki/concepts/federated-daily-research-digest.md"
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/threat-intelligence.md — digest topics include CVE feeds and offensive OSINT
- @sweeps/2026-06-01-daily.md — first federated digest output (agent security cluster)
- @osint-wiki/concepts/federated-daily-research-digest.md — parent federation pattern (K93 install)

## Narrative

Federated install from @osint-wiki/concepts/federated-daily-research-digest.md (K93 brief, 2026-06-01).

- **Script**: `scripts/daily_research_digest_run.py`
- **Config**: `scripts/daily_research_config.yaml` (topics: offensive OSINT, MCP red-team skills, CVE feeds, wireless)
- **Output**: `wiki/sweeps/YYYY-MM-DD-daily.md`
- **Scheduler**: LaunchAgent `com.cemini.daily-research-digest.cybersec` (08:15 daily; load manually with `launchctl load`)

Import boundary: laptop-only automation — digest fetches to `research to be indexed/`; human ingest workflow still required per CLAUDE.md.
