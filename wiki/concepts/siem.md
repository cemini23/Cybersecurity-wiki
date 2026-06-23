---
title: SIEM (Security Information and Event Management)
type: concept
tags: [siem, soc, blue-team, detection, log-management]
keywords: [siem, log management, correlation, detection engineering, splunk, qradar, wazuh]
related:
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - entities/tools/llm-defense-lattice.md
  - entities/tools/splunk.md
  - entities/tools/qradar.md
  - entities/tools/wazuh.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/linux-log-analysis-wazuh.md
  - sources/open-source-soc-guide.md
  - sources/soc-log-types.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
  - sources/threat-hunting-101.md
  - entities/tools/sysmon.md
  - entities/people/rajneesh-gupta.md
  - entities/people/ashish-m-kothekar.md
  - concepts/6g-cps-closed-loop-security.md
  - sources/arxiv-2606-08173-ai-native-closed-loop-6g-cps-security.md
  - sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md
  - entities/tools/defengraph.md
maturity: draft
created: 2026-05-16
updated: 2026-06-23
---

## Relations

- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @entities/tools/splunk.md
- @entities/tools/qradar.md
- @entities/tools/wazuh.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/next-gen-soc-ibm-qradar.md
- @sources/linux-log-analysis-wazuh.md
- @sources/open-source-soc-guide.md
- @sources/soc-log-types.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md
- @sources/threat-hunting-101.md
- @entities/tools/sysmon.md
- @entities/people/rajneesh-gupta.md
- @entities/people/ashish-m-kothekar.md
- @entities/tools/llm-defense-lattice.md
- @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). The corpus is SIEM-heavy —
Splunk query/command collections, a QRadar SOC book, and log-type / log-analysis references
— but no dedicated SIEM concept page existed; @concepts/soc-operations.md only mentioned it
in passing.

## Narrative

**SIEM** = the platform layer that centralizes log and event collection from disparate
sources (endpoints, servers, firewalls, IDS/IPS, cloud), normalizes and correlates them, and
surfaces alerts for SOC triage. It is the analytic backbone of a SOC (see
@concepts/soc-operations.md).

Core SIEM pipeline: log ingestion → parsing / normalization → correlation rules → alerting →
dashboards → threat hunting (see @concepts/threat-hunting.md). Detection content is written
in platform-specific query languages — SPL for Splunk, AQL for QRadar, KQL for Microsoft
Sentinel.

Common platforms: Splunk (@entities/tools/splunk.md), IBM QRadar (@entities/tools/qradar.md),
Wazuh (@entities/tools/wazuh.md, FOSS), Elastic, and Microsoft Sentinel. The corpus's
*Open-Source SOC* and *Low Cost SOC* material favours the FOSS path (Wazuh + Elastic). The
12 log types a SIEM ingests are catalogued in the corpus's *SOC logs* reference.

### Detection-as-code + BAS → Sigma (2026 research)

Breach-and-attack-simulation (BAS) findings describe **what monitoring missed**; operators traditionally hand-author Sigma YAML to close gaps. arXiv:2606.05252 shows a **deterministic** alternative when probes come from a **locked corpus** with stable `probe_id` + OWASP/MITRE tags:

```
BAS bypass finding → probe_id → OWASP category → Sigma template → starter rule (+ traceback URIs)
```

- **23-template library** (OWASP LLM + Web Top 10) — starter quality only; analyst review before prod.
- **Traceability**: emitted rules reference originating finding + MITRE technique; byte-stable re-derivation from published corpus.
- **Live replay**: OpenSearch SIEM fired on 30% AdvBench / 14% HarmBench held-out subsets (7.7% FP benign baseline) — not production coverage claims.

Pairs with @entities/tools/llm-defense-lattice.md (engine-side OWASP LLM attribution on the same locked 17-probe corpus). See @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md.

### Telco CDR analytics (6G CPS — 2606.08173)

Mobile-core SIEM differs from enterprise log correlation: **call-detail records (CDRs)** at minute scale plus **RAN/O-RAN telemetry** at sub-ms scale feed MEC anomaly detectors (statistical front-line + deep models on flagged segments). Threat hunts map to ATT&CK + CDR-observable features (signalling storms, silent-call campaigns, slice-hop slow attacks). See @concepts/6g-cps-closed-loop-security.md.
