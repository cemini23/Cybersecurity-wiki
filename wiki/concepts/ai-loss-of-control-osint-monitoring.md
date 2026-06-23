---
title: AI loss of control — OSINT monitoring
type: concept
tags: [ai-governance, osint, cti, loss-of-control, monitoring]
keywords: [2606.20610, ai loss of control, osint detection, capability concealment, infrastructure correlation]
related:
  - sources/arxiv-2606-20610-osint-ai-loss-of-control-detection.md
  - concepts/osint-for-cybersecurity.md
  - concepts/threat-intelligence.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- @sources/arxiv-2606-20610-osint-ai-loss-of-control-detection.md — primary source (2606.20610)
- @concepts/osint-for-cybersecurity.md — operational OSINT tradecraft for engagements

## Narrative

Ingest 2026-06-23: arXiv:2606.20610 frames **AI loss of control** as an observable phenomenon amenable to **OSINT + CTI** methods — distinct from in-app prompt injection testing.

### Three priority vectors

```
User reports (transcripts) ──→ anomaly clustering
Infrastructure telemetry ──→ unexpected egress / replication
Output vs action gap ──→ capability concealment
```

### Overlap with pentest/SOC work

| Vector | Existing wiki hook |
|--------|-------------------|
| Infrastructure correlation | @concepts/threat-intelligence.md CTI fusion; SOC egress (@entities/tools/iron-proxy.md) |
| Transcript mining | Social/OSINT sources; not automated in this wiki |
| Capability concealment | Agent trajectory eval (@concepts/seclaw-agent-security-evaluation.md) |

### Limits

- **Partial feasibility** — not a substitute for runtime guardrails or formal verification
- **Governance/policy** paper — no tool Phase-0
- Cross-wiki handoff: institutional monitoring architecture may fit @osint-wiki briefs better than deep entity pages

See `briefs/2026-06-23_ai-loc-osint-monitoring-handoff.md` for CTI/SOC fusion notes.
