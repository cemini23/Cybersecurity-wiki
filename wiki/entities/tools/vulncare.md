---
title: VulnCare
type: entity
category: tool
tags: [entity, tool, kubernetes, kspm, apache, go]
keywords: [VulnCare, Dynatrace, healthcare cluster, Trivy findings]
related:
  - sources/arxiv-2607-25995-kutie-topology-k8s-patches.md
  - concepts/topology-aware-k8s-llm-remediation.md
  - entities/tools/kutie-artifacts.md
  - concepts/container-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
phase_0_verdict: "GO 2026-07-29 — Apache-2.0; ~2.6MB; github.com/dynatrace-research/vulncare"
---

## Relations

- @sources/arxiv-2607-25995-kutie-topology-k8s-patches.md
- @concepts/topology-aware-k8s-llm-remediation.md
- @entities/tools/kutie-artifacts.md
- @concepts/container-security.md

**Local clone:** `raw-sources/repos/vulncare` (~2.6MB)
- @concepts/ai-for-cybersecurity.md

## Narrative

### Phase-0 (2026-07-29): GO

| Gate | Status |
|------|--------|
| License | **PASS** — Apache-2.0 |
| Size | **PASS** — ~2.6MB |
| Contents | chart/cluster fixtures, inject.sh, misconfigurations, Trivy secret fixtures |
| Verdict | **GO** — laptop lab for topology-dependent KSPM remediation eval |
