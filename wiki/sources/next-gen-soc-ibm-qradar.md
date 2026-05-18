---
title: "Building a Next-Gen SOC with IBM QRadar.pdf"
type: source
tags: [soc, siem, qradar, blue-team, book, ibm]
keywords: [ibm qradar, siem, next-gen soc, correlation, offenses, ariel, aql, dsm, eps, fpm, wincollect]
related:
  - entities/tools/qradar.md
  - entities/tools/splunk.md
  - entities/tools/wazuh.md
  - entities/tools/sysmon.md
  - entities/people/ashish-m-kothekar.md
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/endpoint-detection-response.md
maturity: validated
read_status: skimmed
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: Building a Next-Gen SOC with IBM QRadar
- **Author**: Ashish M Kothekar (see @entities/people/ashish-m-kothekar.md)
- **Publisher**: Packt Publishing, 2023
- **ISBN**: 978-1-80107-602-9
- **Type**: PDF (12 chapters, ~165 body pages, 3 parts)
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs)
- **Retrieved**: 2026-05-16
- **Deep-read**: 2026-05-17 (Ch 1-4 only — extraction gap documented below)
- **Read-status**: skimmed (NOT read — Ch 5-12 are TOC-only)

## Narrative

A 2023 Packt operator-focused reference on **IBM QRadar SIEM**, organized into three
parts:

1. **Part I — Foundations** (Ch 1-2): introduction to QRadar; architecture, services,
   the Console + managed-host model; the two databases (Ariel for events/flows,
   Postgres for config); core concepts (event, flow, log source, DSM, offense, building
   block, rule, reference set).
2. **Part II — Detection + tuning** (Ch 3-7): deployment topologies, sizing, license
   model; event + flow ingestion pipelines; coalescing; traffic analysis; AQL search;
   rule writing; one end-to-end example (Linux SSH brute-force).
3. **Part III — Apps + operations** (Ch 8-12): UBA, Watson Advisor, Use Case Manager,
   NTA, DSM Editor, app marketplace, WinCollect, troubleshooting + tuning playbook.

The synthesis is in @entities/tools/qradar.md (promoted draft → validated 2026-05-17).
Cross-corpus: paired with @entities/tools/splunk.md and @entities/tools/wazuh.md for
SIEM comparison; cited from @concepts/siem.md as the QRadar primary reference.

### Extraction gap (honest disclosure)

The PDF is 126,426 characters — too large to inline-read — and was extracted via a
subagent that fully covered Ch 1-4 (~36% of the body) and gave only TOC summaries for
Ch 5-12. Adopted into the wiki:

| Coverage | Topic | Adopted into entity? |
|----------|-------|----------------------|
| ✅ Full | QRadar architecture (Console + managed hosts) | yes |
| ✅ Full | Component taxonomy (EP, EC, FP, QFlow, Data Node, QNI, QRIF, QPCAP, QVM, QRM, App Host, DLC) | yes |
| ✅ Full | Two-database model (Ariel + Postgres) | yes |
| ✅ Full | Core concepts (event, flow, log source, DSM, offense, BB, rule, reference set, coalescing, traffic analysis) | yes |
| ✅ Full | Ingestion protocols (active + passive) | yes |
| ✅ Full | Flow capture + Superflow types A/B/C | yes |
| ✅ Full | Deployment topologies + Community Edition | yes |
| ✅ Full | EPS/FPM licensing model + 7.4 transition + sizing math | yes |
| ✅ Full | Upgrade pitfalls + operator foot-guns | yes |
| ✅ Full | One CRE detection example (SSH brute force) | yes |
| ⚠️ TOC | AQL syntax + canonical idioms | `[NEEDS VERIFICATION 2026-05-17]` |
| ⚠️ TOC | Rule wizard UI walkthrough | `[NEEDS VERIFICATION 2026-05-17]` |
| ⚠️ TOC | UBA / Watson Advisor / Use Case Manager / NTA | `[NEEDS VERIFICATION 2026-05-17]` |
| ⚠️ TOC | WinCollect deep-dive | `[NEEDS VERIFICATION 2026-05-17]` |
| ⚠️ TOC | Troubleshooting + tuning playbook | `[NEEDS VERIFICATION 2026-05-17]` |

**Next-extraction priority** (highest value): WinCollect (Ch 12) — Windows event
ingestion is the dominant blue-team use case. Second: rule-wizard + AQL idioms
(Ch 5-7) — needed for a rule-pattern catalog comparable to the Splunk SPL catalog
already in @entities/tools/splunk.md.

## Relations

- @entities/tools/qradar.md
- @entities/tools/splunk.md
- @entities/tools/wazuh.md
- @entities/tools/sysmon.md
- @entities/people/ashish-m-kothekar.md
- @concepts/siem.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/endpoint-detection-response.md
