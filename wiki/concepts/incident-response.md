---
title: Incident Response
type: concept
tags: [dfir, blue-team, response]
keywords: [incident response, ir, dfir, ecir]
related:
  - concepts/malware-analysis.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - entities/frameworks/cyber-kill-chain.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/lockbit.md
  - entities/tools/wazuh.md
  - sources/elearnsecurity-certified-incident-response-ecir-guide-study-to-exam.md
  - sources/incident-response-overview.md
  - sources/incident-response-simulation-1.md
  - entities/tools/cua.md
  - concepts/agent-vm-sandboxing.md
  - sources/2025-cybersecurity-attacks-playbooks.md
  - concepts/defense-in-depth.md
  - entities/tools/grex.md
  - entities/tools/vanguard.md
  - concepts/linux-security.md
  - concepts/endpoint-detection-response.md
  - sources/blue-team-handbook.md
  - sources/blue-team-notes.md
  - sources/cybersecurity-blue-team-strategies.md
  - sources/effective-threat-investigation-soc-analysts.md
  - sources/open-source-soc-guide.md
  - sources/ransomware-investigation-runbook.md
  - sources/soc-analyst-book.md
  - sources/soc-top-30-interview-questions.md
  - concepts/ransomware.md
  - concepts/threat-intelligence.md
  - concepts/phishing-investigation.md
  - entities/people/mostafa-yahia.md
  - entities/tools/splunk.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/splunk-siem-soc2-use-cases.md
  - entities/tools/qradar.md
  - sources/next-gen-soc-ibm-qradar.md
  - entities/tools/cve-mcp-server.md
  - concepts/exceptional-access-risk-quantification.md
  - sources/arxiv-2606-19106-exceptional-access-compromise-risk-quantification.md
maturity: validated
created: 2026-05-12
updated: 2026-06-18
---

## Relations

- @concepts/malware-analysis.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @entities/frameworks/cyber-kill-chain.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/lockbit.md
- @entities/tools/wazuh.md
- @sources/elearnsecurity-certified-incident-response-ecir-guide-study-to-exam.md
- @sources/incident-response-overview.md
- @sources/incident-response-simulation-1.md
- @entities/tools/cua.md
- @concepts/agent-vm-sandboxing.md


- @sources/2025-cybersecurity-attacks-playbooks.md
- @concepts/defense-in-depth.md
- @concepts/linux-security.md
- @concepts/endpoint-detection-response.md
- @sources/blue-team-handbook.md
- @sources/blue-team-notes.md
- @sources/cybersecurity-blue-team-strategies.md
- @sources/effective-threat-investigation-soc-analysts.md
- @sources/open-source-soc-guide.md
- @sources/ransomware-investigation-runbook.md
- @sources/soc-analyst-book.md
- @sources/soc-top-30-interview-questions.md
- @concepts/ransomware.md
- @concepts/threat-intelligence.md
- @concepts/phishing-investigation.md
- @entities/people/mostafa-yahia.md
- @entities/tools/splunk.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/splunk-siem-soc2-use-cases.md
- @entities/tools/qradar.md
- @sources/next-gen-soc-ibm-qradar.md
- @entities/tools/cve-mcp-server.md — CVE/KEV/EPSS rapid-enrichment during containment/eradication triage

## Raw Concept

Three corpus PDFs anchor (Incident response - overview, Incident Response Simulation 1, eCIR Guide).

## Narrative

Incident Response (IR) is the structured process for detecting → containing → eradicating → recovering from → learning from a security incident. The two canonical lifecycles are: [Source: Incident response - overview.pdf]

### NIST SP 800-61r2 (4-phase canonical)

1. **Preparation** — IR plan, runbooks, tooling, jump bags, communication tree, retainer contracts. Done *before* an incident — the largest payoff phase.
2. **Detection & Analysis** — alert triage, scope determination, severity classification, initial containment decision.
3. **Containment, Eradication & Recovery** — short-term + long-term containment; evict the threat actor; restore from clean state; harden against re-entry.
4. **Post-Incident Activity** — lessons-learned meeting (within 2 weeks ideal), root-cause analysis, runbook updates, detection-engineering tickets.

[NIST SP 800-61r2 — the canonical reference](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)

### SANS PICERL (6-phase variant)

**P**reparation → **I**dentification → **C**ontainment → **E**radication → **R**ecovery → **L**essons Learned. Splits NIST's combined "Containment, Eradication & Recovery" into three distinct steps. Functionally equivalent to NIST; teams typically pick one vocabulary and stick.

### SOC vs CSIRT — terminology [CONFIRMED]

These get conflated; they're distinct functions. [Source: Incident response - overview.pdf]

- **SOC** (Security Operations Center) — continuous detection + first-line response. Tiered analyst structure. Always-on.
- **CSIRT** (Computer Security Incident Response Team) — formal incident handlers + investigators. Engaged for confirmed incidents (typically by the SOC handing off). May be permanent in-house, or summoned from a retainer firm. Often has charter authority the SOC lacks (legal hold, executive escalation, evidence chain-of-custody).

Smaller orgs collapse these into one team. Larger orgs (banks, telcos, governments) keep them separate with formal handoff criteria.

### DFIR — the forensic + IR fusion

**DFIR** = Digital Forensics and Incident Response. Forensic readiness = the deliberate pre-arrangement so that if/when an incident hits, evidence survives in chain-of-custody-quality state (centralized logs with WORM storage, EDR with tamper-proof telemetry, MFA logs retained ≥90 days, image-acquisition tooling pre-deployed). [Source: Incident response - overview.pdf]

Tooling cited in the corpus:

- **[DFIR-ORC](https://dfir-orc.github.io/)** — Microsoft's open-source forensic collection framework (Windows)
- **[DFIRTrack](https://github.com/dfirtrack/dfirtrack)** — incident-tracking app for analysts
- **[FIR (Fast Incident Response)](https://github.com/certsocietegenerale/FIR)** — Société Générale's open-source case-management app
- **[IPED](https://github.com/sepinf-inc/IPED)** — Brazilian Federal Police forensic processing tool (open-source)
- **[Kuiper](https://github.com/DFIRKuiper/Kuiper)** — Mac+Linux+Windows forensic-artifact parser
- **[awesome-incident-response](https://github.com/meirwah/awesome-incident-response)** — curated list of IR resources
- **[awesome-forensics](https://github.com/cugu/awesome-forensics)** — curated forensics tooling

### Windows event-log triage toolchain

Per @sources/effective-threat-investigation-soc-analysts.md (Yahia Ch 3) — the canonical live-vs-offline EVTX investigation stack for Windows-host IR:

| Tool | Use case | Cost |
|------|----------|------|
| **Event Viewer** (built-in) | Live host, GUI; exports CSV/EVTX/TXT/XML | Free / built-in |
| **PsLogList** (Sysinternals) | Live host, CLI; dumps logs to TXT/CSV/EVTX | Free |
| **Event Log Explorer** | Offline EVTX, GUI; free for personal use | Free (personal) / paid (commercial) |
| **EvtxECmd** (Eric Zimmerman) | Offline EVTX, CLI; outputs CSV/XML/JSON; scripts well | Free |
| **HELK** (Cyb3rWard0g) | Open-source SIEM lab — Elastic + Kafka + ELK on Ubuntu | Free |
| **Mordor datasets** | Pre-recorded adversarial-technique EVTX corpora at [securitydatasets.com](https://securitydatasets.com/) | Free |

Default Windows log path: `C:\Windows\System32\winevt\Logs`. Relocate via `HKLM\SYSTEM\CurrentControlSet\Services\EventLog\<LogName>` registry hive. A pure Windows 11 install ships with **336 log files** by default [Source: yahia ch 3 p. 52]. Six Security-log event categories: logon, logon validation, object access, account management, privilege use, process tracking.

### IR playbook libraries — community canonical

- [PagerDuty Incident Response Docs](https://github.com/PagerDuty/incident-response-docs) — runbook templates (more SRE-flavored but adaptable)
- [Counteractive incident-response-plan-template](https://github.com/counteractive/incident-response-plan-template)
- [GuardSight SOC playbooks](https://github.com/guardsight/gsvsoc_cybersecurity-incident-response-plan)
- [Austinsonger Incident-Playbook](https://github.com/austinsonger/Incident-Playbook) — per-incident-type runbooks

### Cross-link

- @concepts/malware-analysis.md — when the incident involves a malware-driven intrusion
- @concepts/soc-operations.md — where IR teams typically live organizationally
- @concepts/threat-hunting.md — proactive cousin of IR
- @entities/frameworks/cyber-kill-chain.md — narrative structure for incident write-ups

### Platform master-key compromise (OTT-EA analogue)

When signing keys, vault encryption keys, or KMS master material is exfiltrated (Storm-0558, LastPass 2022 patterns), IR must assume **retrospective decryption** of all historical traffic/data protected under that key — not just ongoing sessions. Playbook deltas vs standard endpoint breach:

1. **Immediate key revocation** — invalidate all tokens/certs derived from compromised material; assume attacker already forged credentials.
2. **Scope as temporal, not spatial** — "what was encrypted under this key since issuance?" not "which hosts are affected?"
3. **No clean recovery narrative** — key exfiltration is irreversible; comms to stakeholders must not imply patch-and-forget.
4. **Cross-store correlation** — check whether data stores AND key-management layers were hit in same campaign (P3·P4 chain in EA models).

See @concepts/exceptional-access-risk-quantification.md for the structured risk framework; carrier/LI incidents (Salt Typhoon) follow the T-EA variant with LI target-list exfil as primary impact.
