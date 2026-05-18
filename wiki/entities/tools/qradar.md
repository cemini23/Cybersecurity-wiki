---
title: IBM QRadar
type: entity
tags: [siem, soc, log-analysis, ibm, commercial, blue-team]
keywords: [qradar, ibm qradar, siem, soc, offense, correlation, aql, ariel, dsm, eps, fpm, ecs, qflow]
related:
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/endpoint-detection-response.md
  - entities/tools/splunk.md
  - entities/tools/wazuh.md
  - entities/tools/sysmon.md
  - entities/people/ashish-m-kothekar.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/soc-red-blue-team-drills.md
  - sources/open-source-soc-guide.md
maturity: validated
created: 2026-05-16
updated: 2026-05-17
---

## Relations

- @concepts/siem.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/endpoint-detection-response.md
- @entities/tools/splunk.md
- @entities/tools/wazuh.md
- @entities/tools/sysmon.md
- @entities/people/ashish-m-kothekar.md
- @sources/next-gen-soc-ibm-qradar.md
- @sources/soc-red-blue-team-drills.md
- @sources/open-source-soc-guide.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). Promoted to validated on
2026-05-17 after a deep-read pass over **Building a Next-Gen SOC with IBM QRadar** (Packt
2023, Ashish M Kothekar — see @entities/people/ashish-m-kothekar.md). The book is a 12-chapter
~165-page operator-focused architecture + deployment + tuning reference. **Extraction
coverage on this entity ≈ 36% — Chapters 1-4 (architecture, components, deployment,
ingestion) are fully synthesized; Chapters 5-12 (rule-writing patterns, AQL syntax, apps:
UBA / Watson Advisor / Use Case Manager / NTA, WinCollect, troubleshooting) are TOC-summary
only.** Gaps are tagged `[NEEDS VERIFICATION 2026-05-17]` in the relevant sections.

Cross-corpus: also the detection platform in the corpus's SOC drill notes
(@sources/soc-red-blue-team-drills.md) and contrasts with the FOSS path
(Wazuh, see @entities/tools/wazuh.md) discussed in @sources/open-source-soc-guide.md.

## Narrative

IBM QRadar is a **commercial SIEM** — it aggregates security telemetry from logs and
network flows, normalizes them into events, correlates them via a Custom Rule Engine
into **offenses**, and applies analytics + ML for detection and reporting. It has been
a long-standing leader in the SIEM market segment (alongside Splunk and Microsoft
Sentinel). Detection content is expressed in QRadar's query language (**AQL — Ariel
Query Language**) and the rule wizard. Compare @entities/tools/splunk.md (SPL/commercial)
and the FOSS @entities/tools/wazuh.md; see @concepts/siem.md for the category and
@concepts/soc-operations.md for the SOC context.

### Architecture overview

QRadar is built as a **Console + N managed hosts** distributed cluster. The Console is
the only host with a UI; everything else is a worker.

| Role | Component | What it does |
|------|-----------|--------------|
| Brain | **Console** | Web UI (Tomcat), config DB, orchestration, license server |
| Event side | **Event Processor (EP)** | Correlates events, runs rules, writes to Ariel |
| Event side | **Event Collector (EC)** | Receives + parses raw log sources, forwards to EP |
| Flow side | **Flow Processor (FP)** | Correlates flows (NetFlow / IPFIX / sFlow), feeds offenses |
| Flow side | **Flow Collector (QFlow)** | Captures network flows from taps / SPANs / NetFlow |
| Scale | **Data Node** | Adds storage + query horsepower to an EP/FP cluster |
| Deep packet | **QNI (Network Insights)** | Layer-7 metadata extraction from raw packets |
| Forensics | **QRIF (Incident Forensics)** | Indexed full-packet search over historical PCAP |
| Capture | **QPCAP** | Standalone full-packet capture appliance |
| Vuln | **QVM (Vulnerability Manager)** | Built-in vuln scanner, correlates findings into risk |
| Risk | **QRM (Risk Manager)** | Network topology + firewall-rule modeling (uses Ziptie Server) |
| App | **App Host** | Docker-based runtime for QRadar apps (UBA, Watson, etc.) |
| Edge | **DLC (Disconnected Log Collector)** | Standalone collector for air-gapped / remote sites |

[Source: next-gen-soc-ibm-qradar.pdf Ch 1-2 — Kothekar 2023]

### Console + EP subservices

On any node you can list subservices via `/opt/qradar/bin/`-installed scripts:

- **tomcat** — Web UI + REST API (Console only)
- **hostcontext** — node-management daemon (all hosts)
- **hostservices** — supervisor for the per-host service tree (all hosts)
- **ecs-ec-ingress** — raw-event ingress (on Event Collector)
- **ecs-ec** — Event Collector pipeline (parse + normalize + coalesce)
- **ecs-ep** — Event Processor pipeline (correlate + write Ariel)
- **qflow** — flow capture daemon (Flow Collector)
- **accumulator** — pre-aggregates events for dashboards / time series
- **ariel proxy** + **ariel query** — Ariel DB read/write path

[Source: next-gen-soc-ibm-qradar.pdf Ch 1 — Kothekar 2023]

### The two databases

QRadar splits state across two stores with very different semantics — confusing the two
is a common operator mistake:

| DB | What lives there | Replication | Query path |
|----|------------------|-------------|------------|
| **Ariel** | Events + flows (time-series, hierarchical partitions) | Local to each EP/FP/Data Node | AQL via ariel-proxy/ariel-query |
| **Postgres** | Configuration: rules, log sources, users, building blocks, reference sets | Replicated from Console → all managed hosts | UI + REST API |

Implication: **edit a rule on the Console** → Postgres replicates → managed hosts pick it
up. **Search historical events** → query goes against Ariel on whichever EP/Data Node
owns the time range. Ariel is *not* replicated; losing a Data Node loses its slice of
event history.

[Source: next-gen-soc-ibm-qradar.pdf Ch 2 — Kothekar 2023]

### Core concepts

| Concept | Definition | Where it lives |
|---------|------------|----------------|
| **Event** | A normalized log entry (post-DSM) | Ariel |
| **Flow** | A summarized network conversation (NetFlow / packet-derived) | Ariel |
| **Log Source** | A configured ingestion endpoint (e.g. *Cisco ASA on 10.0.0.5/UDP-514*) | Postgres |
| **DSM (Device Support Module)** | A parser plug-in per device-vendor / log-format pair | `/opt/qradar/dsms/` |
| **Offense** | A correlated incident — bundles related events/flows under one ID | Postgres + Ariel pointers |
| **Building Block** | A named reusable filter (e.g. *BB:NetworkDefinition: Trusted Networks*) | Postgres |
| **Rule (CRE)** | Logic in the Custom Rule Engine — triggers offenses, anomalies, behavioral matches | Postgres |
| **Reference Set** | Named list (IPs, hashes, usernames) — populated manually, by API, or by rule | Postgres |
| **Coalescing** | EC-side merge: ≥3 events with same QID / src-IP / dst-IP / user within 10s collapse to 1 | Event Collector |
| **Traffic Analysis** | Auto-discovers + auto-creates log sources from unrecognized inbound feeds | Event Collector |

[Source: next-gen-soc-ibm-qradar.pdf Ch 2-3 — Kothekar 2023]

### Ingestion: protocols + log sources

- **Active protocols** (QRadar reaches out): JDBC (DB tables), WMI, OPSEC LEA (Check Point), SDEE (Cisco IPS), MS Exchange, SMB/CIFS pulls, REST API pulls
- **Passive protocols** (data arrives): Syslog (UDP-514, TCP-514, TLS-6514), SNMP traps, log-file uploads, Windows Event Forwarding via WinCollect

**WinCollect** is the QRadar agent for Windows event collection — managed (Console-controlled)
or standalone — and is the recommended path for ingesting Windows Security / Sysmon / PowerShell
logs at scale. WinCollect details are TOC-only in the extraction. [NEEDS VERIFICATION
2026-05-17 — WinCollect config / pipeline]

### Flow capture

QFlow can derive flows from raw packets, NetFlow v5/v9, IPFIX, sFlow, JFlow, Packeteer.
A known foot-gun: **qflow keeps only the first 64 bytes of packet payload** for derived
flows by default — anything deeper requires QNI for L7 metadata or QRIF for full-PCAP
indexing. UDP flow sources have no delivery guarantee and frequently underreport in
high-bandwidth links.

**Superflows** are bandwidth-saving aggregates of conversation patterns:

| Type | Pattern | Detection use |
|------|---------|---------------|
| **A** | 1 source → many destinations | Port-scanning, internal reconnaissance |
| **B** | Many sources → 1 destination | DDoS, broad authentication brute-force |
| **C** | Many sources → many destinations on the same port | Worm propagation, P2P, scanning sweep |

[Source: next-gen-soc-ibm-qradar.pdf Ch 4 — Kothekar 2023]

### Custom Rule Engine (CRE)

The CRE evaluates every event/flow against the active rule set. Rule kinds:

- **Event rule** — pattern on a single event or sequence of events
- **Flow rule** — pattern on a single flow or sequence of flows
- **Common rule** — operates on the event+flow union
- **Offense rule** — fires when an existing offense matches criteria (escalation logic)
- **Anomaly rule** — statistical (z-score / threshold over time window)
- **Behavioral rule** — learned-baseline deviation

Rule actions can: create an offense, modify an offense, add to a reference set,
trigger an email / SNMP / syslog notification, or push to an external SOAR via API.
The rule wizard itself + advanced AQL patterns are TOC-only in the extraction.
[NEEDS VERIFICATION 2026-05-17 — rule wizard UI walkthrough + canonical AQL idioms]

### Example detection — Linux SSH brute force

The book walks one full detection end-to-end (Ch 4) for SSH brute force on Linux:

1. **Log source**: Linux syslog (passive, UDP-514) → DSM = *Linux OS DSM* parses
   `Failed password for invalid user` events to QID 5000132
2. **Building Block**: `BB:CategoryDefinition: Authentication Failures`
3. **Rule (event rule)**: when ≥5 events match BB above with the same `Source IP` over
   3 minutes → create offense indexed by `Source IP`
4. **Tuning**: add a reference set `IP_Whitelist_Pentest` to exclude known scanners
5. **Tuning**: increase coalescing window or threshold if SSH-bastion volume produces FP

This is the canonical CRE pattern — most authentication / brute-force / scan rules follow
the same `Log source → DSM → BB → event-count rule → indexed offense → reference-set tuning`
shape. [Source: next-gen-soc-ibm-qradar.pdf Ch 4 — Kothekar 2023]

### AQL — Ariel Query Language

AQL is QRadar's SQL-like query language over Ariel. Surface syntax resembles SQL
(`SELECT ... FROM events WHERE ... LAST N MINUTES`) but with QRadar-specific functions
for category/QID/offense lookup. **Detailed AQL syntax + canonical idioms are NOT
extracted** — Ch 5-6 (search + AQL) and Ch 7 (rule writing) are TOC-only.
[NEEDS VERIFICATION 2026-05-17 — AQL syntax + idioms]

### Licensing — EPS + FPM

QRadar's commercial model is **EPS** (Events Per Second) + **FPM** (Flows Per Minute):

- Licenses apply to **processors** (Event Processor / Flow Processor), not collectors —
  EC + QFlow forward unlimited; the EP/FP enforces the cap
- Pre-7.4: separate EPS-per-EP licenses, awkward to redistribute
- **7.4+**: single **Capacity License** — pool of total EPS/FPM redistributed across all
  EP/FP nodes from the Console
- Hardware/appliance license is separate from EPS/FPM (you license boxes AND throughput)
- Over-cap traffic: QRadar **buffers + drops oldest** during sustained over-cap; spikes
  buffer to disk first

**Sizing example** (from book): 2 TB/day of events with an average event size of
500 bytes ≈ **46,296 EPS** sustained — you license for peak (commonly 1.5-2× sustained
to absorb bursts), not average.

[Source: next-gen-soc-ibm-qradar.pdf Ch 3 — Kothekar 2023]

### Deployment topologies

| Topology | Spec | Best fit |
|----------|------|----------|
| **All-in-one** | Console + EP + FP + EC + QFlow on a single appliance | Lab, PoC, ≤2,500 EPS |
| **Distributed** | Console + dedicated EP/FP + N Data Nodes + remote EC + QFlow | Production, multi-region, ≥5,000 EPS |
| **HA** | Each managed host paired with a passive HA partner via DRBD | Regulated environments, RPO≈0 requirement |
| **DR** | Cross-site cluster with async Ariel replication | DR-mandate environments |

**Community Edition** is a free non-production all-in-one with capped EPS / retention —
useful for hands-on labs and rule-writing practice. [Source: next-gen-soc-ibm-qradar.pdf
Ch 3 — Kothekar 2023]

### Upgrade pitfalls

- **GlusterFS → DRBD** transition at 7.3 → 7.4: HA-pair rebuild required, not a
  rolling upgrade
- **"Patch All" UI button** — avoid for clusters >4 managed hosts; serialize manually,
  one host at a time, validating EPS recovery before the next
- App-Host Docker images sometimes drift from Console version after patching → recheck
  app health (UBA, Watson) post-upgrade
- DSM auto-updates can change parsing behavior silently → review change log and re-test
  affected rules

[Source: next-gen-soc-ibm-qradar.pdf Ch 3 — Kothekar 2023]

### Operator foot-guns

- **JDBC log-source marker-file corruption** — manifests as silent ingestion stoppage
  on a single log source; fix is to rebuild the marker file and re-ingest from a known
  timestamp
- **Time-zone drift** between log source and EC — events land in the wrong Ariel
  partition and rule windows miss matches; always force UTC on Linux EC + on JDBC
  connection strings
- **qflow 64-byte payload limit** (above) — surprises operators expecting L7 visibility
  without QNI
- **UDP-514 syslog** — silent loss under congestion; prefer TCP-6514 (TLS) for
  security-relevant feeds; budget ~5× the obvious throughput for syslog UDP buffering
- **App Host is mandatory** for UBA, Watson Advisor, Use Case Manager — these are not
  available on a Console-only deploy

### Apps + extensions (TOC-only in extraction)

- **User Behavior Analytics (UBA)** — ML / heuristic anomaly scoring per user
- **Watson Advisor** — IBM cloud-hosted threat-intel context lookup on events
- **Use Case Manager (UCM)** — MITRE ATT&CK mapping + rule-coverage gap visualization
- **Network Threat Analytics (NTA)** — anomaly detection on QNI/Flow data
- **DSM Editor** — UI for building custom DSMs without writing parser code
- **App Marketplace** — IBM X-Force, community apps, MITRE Navigator, etc.

[NEEDS VERIFICATION 2026-05-17 — UBA / Watson / UCM detail (Ch 8-11 not extracted)]

### Comparison vs Splunk + Wazuh

| Dimension | QRadar | Splunk (@entities/tools/splunk.md) | Wazuh (@entities/tools/wazuh.md) |
|-----------|--------|------------------------------------|----------------------------------|
| Cost model | EPS/FPM capacity license | Ingest-volume (GB/day) | FOSS |
| Query language | AQL (SQL-ish) | SPL (pipe DSL) | OpenSearch DSL + custom rules |
| Detection primitive | Offense (auto-correlated) | Notable Event / Risk Object | Alert |
| Strength | Built-in rule library, flow correlation, offense lifecycle | Query expressiveness, app ecosystem | Cost, integrated EDR (FIM, agentless) |
| Friction | Closed-source, complex licensing math, app-host dependency | Cost at scale, no native offense object | Less polished UI, more assembly required |

## Snippets

```
> A company with 20,000 endpoints can generate up to 500,000 alerts per day. An analyst
> could get 1000 alerts per day, but only 10 of them may represent genuine hazards.
[Source: open-source-soc-guide.pdf Ch 1 — Basta et al. 2025; quoted in @concepts/soc-operations.md to motivate offense-correlation tools like QRadar]
```

```
Coalescing default: ≥3 events sharing (QID, src-IP, dst-IP, username) within 10 seconds
are collapsed into a single event-with-count at the Event Collector before they reach
the Event Processor.
[Source: next-gen-soc-ibm-qradar.pdf Ch 2 — Kothekar 2023]
```

```
Sizing rule of thumb: 2 TB/day × (1 event / 500 bytes) / 86,400 s ≈ 46,296 EPS sustained.
License for peak ≈ 1.5-2× sustained to absorb bursts.
[Source: next-gen-soc-ibm-qradar.pdf Ch 3 — Kothekar 2023]
```

## Dead Ends

- **AQL syntax + canonical idioms**: not extracted (Ch 5-6 are TOC-only). Filling this
  gap needs a second extraction pass on the QRadar PDF or external IBM doc ingestion.
- **Rule-writing patterns**: Ch 7 is TOC-only — beyond the single SSH brute-force walk
  in Ch 4, there is no curated rule-pattern catalog yet.
- **UBA / Watson Advisor / Use Case Manager / NTA**: app coverage is TOC-only (Ch 8-11) —
  cannot yet meaningfully compare to e.g. Splunk's Enterprise Security app.
- **WinCollect deep-dive + troubleshooting playbook**: TOC-only (Ch 12) — Windows
  ingestion is the dominant blue-team use case so this is the highest-value next
  extraction target.
