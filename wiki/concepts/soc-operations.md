---
title: SOC Operations
type: concept
tags: [soc, blue-team, siem, detection]
keywords: [soc, siem, monitoring, wazuh, elk, splunk]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/incident-response.md
  - concepts/purple-team-operations.md
  - concepts/threat-hunting.md
  - concepts/zero-trust.md
  - entities/people/joas-a-santos.md
  - entities/tools/wazuh.md
  - sources/100-security-operation-center-tools.md
  - sources/interview-question-tips-pentest-red-team-appsec-and-blue-team.md
  - sources/low-cost-soc-tools-2.md
  - sources/low-cost-soc.md
  - sources/red-team-and-blue-team-labs-and-ctf.md
  - sources/security-operation-center-40-tools.md
  - sources/security-operation-center-and-analysis.md
  - sources/security-operation-center-open-source-pt-en.md
  - sources/security-operation-center-open-source.md
  - sources/security-operation-center-operations-development.md
  - sources/security-operation-center-study-and-career-2022.md
  - sources/soc-analyst-career.md
  - sources/soc-open-source-tools.md
  - sources/2025-cybersecurity-attacks-playbooks.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - concepts/siem.md
  - concepts/endpoint-detection-response.md
  - entities/tools/splunk.md
  - entities/tools/qradar.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/basic-network-sniffer.md
  - sources/blue-team-handbook.md
  - sources/blue-team-notes.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/cybersecurity-blue-team-strategies.md
  - sources/top-50-cybersecurity-interview-questions.md
  - sources/edr-tools-overview.md
  - sources/effective-threat-investigation-soc-analysts.md
  - sources/linux-log-analysis-wazuh.md
  - sources/mitre-attack-framework-soc.md
  - sources/open-source-soc-guide.md
  - sources/ransomware-investigation-runbook.md
  - sources/soc-analyst-book.md
  - sources/soc-log-types.md
  - sources/soc-red-blue-team-drills.md
  - sources/50-free-online-tools-soc-analysts.md
  - sources/soc-top-30-interview-questions.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
  - sources/threat-hunting-101.md
  - entities/tools/sysmon.md
  - concepts/ransomware.md
  - concepts/threat-intelligence.md
  - entities/frameworks/cyber-kill-chain.md
  - concepts/phishing-investigation.md
  - entities/people/mostafa-yahia.md
  - entities/people/rajneesh-gupta.md
  - entities/people/ashish-m-kothekar.md
  - entities/tools/grex.md
  - entities/tools/vanguard.md
  - concepts/6g-cps-closed-loop-security.md
  - sources/arxiv-2606-08173-ai-native-closed-loop-6g-cps-security.md
  - sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md
  - entities/tools/defengraph.md
maturity: validated
created: 2026-05-12
updated: 2026-06-23
---

## Relations

- @concepts/ai-for-cybersecurity.md
- @concepts/incident-response.md
- @concepts/purple-team-operations.md
- @concepts/threat-hunting.md
- @concepts/zero-trust.md
- @entities/people/joas-a-santos.md
- @entities/tools/wazuh.md
- @sources/100-security-operation-center-tools.md
- @sources/interview-question-tips-pentest-red-team-appsec-and-blue-team.md
- @sources/low-cost-soc-tools-2.md
- @sources/low-cost-soc.md
- @sources/red-team-and-blue-team-labs-and-ctf.md
- @sources/security-operation-center-40-tools.md
- @sources/security-operation-center-and-analysis.md
- @sources/security-operation-center-open-source-pt-en.md
- @sources/security-operation-center-open-source.md
- @sources/security-operation-center-operations-development.md
- @sources/security-operation-center-study-and-career-2022.md
- @sources/soc-analyst-career.md
- @sources/soc-open-source-tools.md


- @sources/2025-cybersecurity-attacks-playbooks.md
- @concepts/siem.md
- @concepts/endpoint-detection-response.md
- @entities/tools/splunk.md
- @entities/tools/qradar.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/basic-network-sniffer.md
- @sources/blue-team-handbook.md
- @sources/blue-team-notes.md
- @sources/next-gen-soc-ibm-qradar.md
- @sources/cybersecurity-blue-team-strategies.md
- @sources/top-50-cybersecurity-interview-questions.md
- @sources/edr-tools-overview.md
- @sources/effective-threat-investigation-soc-analysts.md
- @sources/linux-log-analysis-wazuh.md
- @sources/mitre-attack-framework-soc.md
- @sources/open-source-soc-guide.md
- @sources/ransomware-investigation-runbook.md
- @sources/soc-analyst-book.md
- @sources/soc-log-types.md
- @sources/soc-red-blue-team-drills.md
- @sources/50-free-online-tools-soc-analysts.md
- @sources/soc-top-30-interview-questions.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md
- @sources/threat-hunting-101.md
- @entities/tools/sysmon.md
- @concepts/ransomware.md
- @concepts/threat-intelligence.md
- @entities/frameworks/cyber-kill-chain.md
- @concepts/phishing-investigation.md
- @entities/people/mostafa-yahia.md
- @entities/people/rajneesh-gupta.md
- @entities/people/ashish-m-kothekar.md

## Raw Concept

11+ corpus PDFs scope into SOC operations, plus the 2025 Basta et al. Wiley textbook (@sources/open-source-soc-guide.md) which structures SOC theory around five pillars.

## Narrative

**Security Operations Center** = the people + processes + tooling that detect, triage, and respond to security events 24×7. Tiered analyst model: **Tier-1** (alert triage), **Tier-2** (incident analysis), **Tier-3** (threat hunting + IR + advanced reverse engineering). Tooling stack: SIEM (Wazuh / Splunk / Elastic / Sentinel / QRadar), SOAR (Cortex XSOAR / Tines), EDR (CrowdStrike / Defender for Endpoint / SentinelOne), threat-intel (MISP / OpenCTI). The corpus's *Low Cost SOC* PDFs explicitly cover the FOSS path: Wazuh + Elastic + TheHive + MISP + Velociraptor. See @entities/tools/wazuh.md, @concepts/threat-hunting.md, @concepts/threat-intelligence.md.

### Five pillars (Basta et al. 2025)

Traditional people / processes / technology is now usually extended with **governance** + **data** as first-class pillars:

| Pillar | What it covers | Failure mode if neglected |
|--------|----------------|---------------------------|
| **People** | Analyst tiers, on-call rotations, training, retention | Burnout, alert fatigue, brain-drain |
| **Processes** | Runbooks, escalation paths, IR playbooks, post-incident reviews | Inconsistent response, repeat incidents |
| **Technology** | SIEM, EDR, SOAR, sandbox, ticketing, CTI platform | Tool sprawl, integration gaps, blind spots |
| **Governance** | Policies, regulatory mapping, metrics, audit, board reporting | No mandate, no budget, no accountability |
| **Data** | Collection, normalization, retention, integrity, privacy | Every downstream control degrades — bad data = bad detections |

[CONFIRMED — Basta et al., Open-Source SOC, Ch 1 [Source: open-source-soc-guide.pdf]]

### Three SOC operating models

| Model | Description | Best fit |
|-------|-------------|----------|
| **In-house** | Owned + staffed by the org | Large enterprises, regulated industries, high control-need |
| **Co-managed** | Shared between in-house team + MSSP | Mid-market, need 24×7 coverage but want control over IR + tuning |
| **MSSP** (Managed Security Service Provider) | Fully outsourced | SMB, no in-house security team, cost-sensitive |

**7 decision criteria** for choosing among them: budget, expertise, regulatory, infrastructure complexity, threat landscape, scalability, control + visibility. [Source: open-source-soc-guide.pdf Ch 1]

### Alert-volume reality

The math that justifies SOAR + ML-based prioritization:

> A company with 20,000 endpoints can generate up to 500,000 alerts per day. An analyst could get 1000 alerts per day, but only 10 of them may represent genuine hazards. — Basta et al. [Source: open-source-soc-guide.pdf Ch 1]

Implication: ~99% of alert volume is noise. The 1% genuine signal is buried unless you have:
- Tuned SIEM correlation (kill alert-class duplicates at source)
- Risk-based prioritization (entity-context scoring, e.g. Splunk RBA)
- SOAR auto-triage for known-benign patterns
- Threat-hunting program to find what alerts miss entirely (see @concepts/threat-hunting.md)

### Cyber Kill Chain — 7-stage reference

Used by Basta et al. as the SOC's intrusion-narrative framework alongside MITRE ATT&CK:

| # | Stage | Adversary activity | Defender signal |
|---|-------|-------------------|-----------------|
| 1 | Reconnaissance | Recon, target selection | DNS recon, scanning logs, social-media monitoring |
| 2 | Weaponization | Payload prep | Offline to defender — usually invisible |
| 3 | Delivery | Phishing email, drive-by, USB | Email-sec gateway, proxy, USB-control logs |
| 4 | Exploitation | CVE / macro / social-eng trigger | EDR exploit-detect, browser sandbox alerts |
| 5 | Installation | Malware drop, persistence | Sysmon EID 1+11+12-14, autoruns delta |
| 6 | Command & Control | Beacon to attacker infra | DNS, proxy, NetFlow C2 signals |
| 7 | Actions on Objectives | Exfil, encryption, sabotage | DLP, mass-file-mod, abnormal data-volume |

[Source: Lockheed-Martin original; cited in Basta et al. Ch 1 [Source: open-source-soc-guide.pdf]]

ATT&CK + Kill Chain pair: ATT&CK = unordered technique matrix; Kill Chain = ordered narrative. SOC playbooks usually carry both notations. See @entities/frameworks/mitre-attack.md, @entities/frameworks/cyber-kill-chain.md.

### Zero-trust adoption signal

> 76% of firms have at least begun to execute a zero-trust approach. — Nispel (2023), cited in Basta et al. [Source: open-source-soc-guide.pdf Ch 1]

Treat as the default network-design assumption when modeling modern SOC scope. See @concepts/zero-trust.md.

### Distributed / MEC-tier SOC (6G CPS — 2606.08173)

Enterprise tier-1/2/3 SOC model assumes central correlation latency. **6G CPS** (URLLC slices) needs **edge sense→detect→mitigate** inside p99 tail bounds — CDR slow-path + RAN fast-path at MEC, actuation via O-RAN RIC xApps/SDN, retrain via federated learning. Complements but does not replace central SOC for enterprise IT; see @concepts/6g-cps-closed-loop-security.md. [TENTATIVE] — telco survey, not laptop SOC lab validated here.
