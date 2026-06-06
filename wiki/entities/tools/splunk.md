---
title: Splunk
type: entity
tags: [siem, soc, log-analysis, detection-engineering, commercial]
keywords: [splunk, spl, siem, search processing language, soc, detection, soc 2, detection engineering, threat hunting, dashboards, alerts]
related:
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/endpoint-detection-response.md
  - concepts/ransomware.md
  - concepts/phishing-investigation.md
  - concepts/threat-intelligence.md
  - entities/tools/qradar.md
  - entities/tools/wazuh.md
  - entities/tools/sysmon.md
  - entities/frameworks/mitre-attack.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
  - sources/effective-threat-investigation-soc-analysts.md
  - sources/open-source-soc-guide.md
  - sources/soc-analyst-book.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - entities/people/rajneesh-gupta.md
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
- @concepts/ransomware.md
- @concepts/phishing-investigation.md
- @concepts/threat-intelligence.md
- @entities/tools/qradar.md
- @entities/tools/wazuh.md
- @entities/tools/sysmon.md
- @entities/frameworks/mitre-attack.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md
- @sources/effective-threat-investigation-soc-analysts.md
- @sources/open-source-soc-guide.md
- @sources/soc-analyst-book.md
- @sources/next-gen-soc-ibm-qradar.md
- @entities/people/rajneesh-gupta.md

## Raw Concept

Stub originally created during the BlueTeam Kit 26-PDF ingest (2026-05-16). Promoted to `validated` on 2026-05-17 after deep-reads of three corpus PDFs: a 110-query SPL detection catalog (@sources/100-splunk-queries-soc-analyst.md), an alphabetical SPL command reference (@sources/splunk-commands-reference.md), and 24 SOC-2-mapped SPL use cases by Rajneesh Gupta (@sources/splunk-siem-soc2-use-cases.md). Splunk is the de-facto reference SIEM in the corpus; supporting context from @sources/effective-threat-investigation-soc-analysts.md and @sources/soc-analyst-book.md.

## Narrative

**Splunk** is a commercial SIEM and machine-data analytics platform — it ingests, indexes, and searches logs and events at scale using **SPL** (Search Processing Language). In SOC work (@concepts/soc-operations.md) it underpins detection engineering, alerting, dashboards, incident-response timelines, and threat hunting (@concepts/threat-hunting.md). Detection content is written as SPL searches; the corpus's query collections are essentially reusable SPL detection libraries.

Splunk sits alongside @entities/tools/qradar.md (IBM) and @entities/tools/wazuh.md (FOSS) as the standard SIEM choices in the corpus. See @concepts/siem.md for the broader platform category.

### SPL primer — pipeline mental model

SPL searches read **left-to-right as a pipeline**: source events → filter → transform → aggregate → visualize. Every command after the first `|` operates on the rolling event stream.

```
index=auth sourcetype=linux_secure "Failed password"
| stats count by src_ip
| where count > 10
| sort -count
```

This pattern — `search → stats by field → threshold → sort` — is the spine of most detection queries in the corpus. [CONFIRMED — @sources/100-splunk-queries-soc-analyst.md, recurring pattern across all ~110 queries]

### Detection-query catalog — 110-query taxonomy

Synthesized from @sources/100-splunk-queries-soc-analyst.md. Each row is a hunt class with a representative SPL idiom; the source has multiple variants per class.

#### Authentication + access (28 queries)

| Hunt | Representative SPL | ATT&CK tactic |
|------|---------------------|----------------|
| Failed logins (Linux) | `index=auth sourcetype=linux_secure "Failed password" \| stats count by src_ip` | TA0006 Credential Access |
| Failed logins (Windows) | `index=wineventlog EventCode=4625 \| stats count by Account_Name, src_ip` | TA0006 |
| Successful logins (audit baseline) | `EventCode=4624 \| stats count by Account_Name, Logon_Type` | TA0001 Initial Access |
| Privilege escalation (Linux) | `index=auth sourcetype=linux_secure ("sudo" OR "su") \| stats count by user, command` | TA0004 PrivEsc |
| Privilege use (Windows) | `EventCode=4672 \| stats count by Account_Name` | TA0004 |
| Brute-force SSH | `"Failed password" \| stats count by src_ip \| where count > 10` | T1110 Brute Force |
| Brute-force RDP | `EventCode=4625 Logon_Type=10 \| stats count by src_ip \| where count > 10` | T1110.001 |
| Brute-force MSSQL / MySQL / FTP / SNMP / mail | `index=<svc> "auth fail*" \| stats count by src_ip` (per protocol) | T1110.003 |
| Account lockout | `EventCode=4740 \| stats count by Account_Name` | T1110 (failed) |
| New account creation | `EventCode=4720 \| table _time, Account_Name, Caller_User` | T1136 Create Account |
| Group-membership change | `EventCode IN (4728, 4732, 4756) \| table _time, Target_Account, Group_Name` | T1098 Account Manipulation |
| Audit-policy change | `EventCode=4907 \| stats count by Subject_User_Name` | T1562 Impair Defenses |

#### Process + endpoint behavior (18 queries)

| Hunt | Representative SPL | ATT&CK |
|------|---------------------|--------|
| Suspicious process spawn | `EventCode=4688 New_Process_Name IN ("*\\powershell.exe", "*\\cmd.exe", "*\\wscript.exe") \| stats count by Creator_Process_Name, New_Process_Name` | TA0002 Execution |
| PowerShell encoded-command | `EventCode=4688 Process_Command_Line="*-EncodedCommand*" \| table _time, Account_Name, Process_Command_Line` | T1059.001 |
| PowerShell script-block | `EventCode=4104 \| search ScriptBlockText="*Invoke-Mimikatz*" OR ScriptBlockText="*DownloadString*"` | T1059.001 |
| PowerShell Empire pattern | `EventCode=4104 ScriptBlockText IN ("*System.Net.WebClient*", "*[System.Convert]::FromBase64String*")` | S0363 Empire |
| Service install (persistence) | `EventCode=4697 \| table _time, Service_Name, Service_File_Name` | T1543.003 |
| Scheduled task | `EventCode=4698 \| table _time, Task_Name, Subject_User_Name` | T1053.005 |
| WMI persistence | `EventCode=5861 \| table _time, User, Operation` | T1546.003 |
| Defender malware detection | `EventCode=1116 \| stats count by Threat_Name, host` | TA0005 Defense Evasion |

#### Lateral movement (8 queries)

| Vector | Representative SPL | Notes |
|--------|---------------------|-------|
| SMB share access | `EventCode=5140 \| stats count by Share_Name, Account_Name, src_ip` | Watch for new tuples |
| RDP interactive | `EventCode=4624 Logon_Type=10 \| stats count by Account_Name, src_ip` | Logon_Type 10 = RDP |
| WMI remote exec | `EventCode=5861` | WMI eventing |
| WinRM | `EventCode=146` | WinRM operational log |
| DCOM | `EventCode=10009` | DCOM-via-RPC |
| NetBIOS | `EventCode=5719` | Trust failures |
| PsExec | `New_Process_Name="*\\PSEXESVC.exe"` | Sysmon `1` / 4688 |
| Remote registry | `EventCode=4663 Object_Name="*\\REGISTRY\\*" Object_Server="RemoteRegistry"` | Requires reg auditing |

Baseline tuples of `(host, account, src_ip)` and alert on new combinations — see @concepts/threat-hunting.md Hunt 6. [CONFIRMED]

#### Network anomalies + C2 + exfil (15 queries)

| Hunt | Representative SPL |
|------|---------------------|
| Port scan | `\| stats dc(dest_port) as ports by src_ip \| where ports > 100` |
| DNS tunneling | `sourcetype=dns \| eval qlen=len(query) \| where qlen > 50` |
| Long-domain DNS lookup | `sourcetype=dns query="*.????????????????.*"` |
| Outbound DNS bypass | `sourcetype=dns dst_ip!=<internal_resolver>` |
| C2 beaconing | `\| stats count by src_ip, dest_ip, dest_port \| where count > 100` (regular cadence) |
| Large outbound transfer | `\| stats sum(bytes_out) as bo by src_ip, dest_ip \| where bo > 100000000` |
| Outbound to known TOR | `dest_ip IN ([\| inputlookup tor_exit_nodes])` |
| Suspicious URL on web access | `sourcetype=access_combined uri_path IN ("/cmd.php", "/shell.jsp", "*webshell*")` |

#### Web-app attacks (6 queries)

| Hunt | Representative SPL |
|------|---------------------|
| SQL injection | `sourcetype=access_combined uri_query="*UNION*SELECT*" OR uri_query="*' OR 1=1*"` |
| Command injection | `uri_query="*;cat /etc/passwd*" OR uri_query="*\|whoami*"` |
| XSS | `uri_query="*<script>*" OR uri_query="*onerror=*"` |
| Web shell | `uri_path IN ("*.jsp", "*.php") status=200 method=POST \| stats count by uri_path` |
| Path traversal | `uri_query="*../../*"` |

#### Ransomware (5 queries)

| Hunt | Representative SPL |
|------|---------------------|
| Mass file rename | `sourcetype=WinEventLog:Security EventCode=4663 Access_Mask="0x10000" \| stats count by Account_Name \| where count > 100` |
| Ransom-note extensions | `Object_Name IN ("*.locked", "*.encrypted", "*.crypt", "*.ryk", "*.lockbit") \| stats count by host, Account_Name` |
| Shadow-copy deletion | `Process_Command_Line="*vssadmin delete shadows*" OR Process_Command_Line="*wmic shadowcopy delete*"` |
| Defender disable | `EventCode=4688 Process_Command_Line="*Set-MpPreference*DisableRealtimeMonitoring*"` |
| BitLocker abuse | `Process_Command_Line="*manage-bde*"` |

See @concepts/ransomware.md.

#### Reconnaissance + CVE exploitation (8 queries)

| Hunt | Representative SPL |
|------|---------------------|
| Nmap-style scan | `\| stats dc(dest_port) as ports by src_ip \| where ports > 50` |
| Suspicious User-Agent | `http_user_agent IN ("nikto", "sqlmap", "nmap", "curl", "wget")` |
| Log4Shell exploit | `\| search "\${jndi:ldap" OR "\${jndi:rmi"` |
| Spring4Shell | `Process_Command_Line="*class.module.classLoader*"` |
| ProxyShell / ProxyLogon | `sourcetype=iis cs_uri_stem="*autodiscover*" OR cs_uri_stem="*owa*"` |
| CVE generic | per-CVE pattern; high false-positive rate on naked CVE numbers — use POC payload patterns instead |

#### Phishing + email (3 queries)

| Hunt | Representative SPL |
|------|---------------------|
| Bulk-attachment delivery | `sourcetype=email \| stats count by sender, attachment_hash \| where count > 5` |
| Phishing-domain lookalike | `sourcetype=dns query="*microsoft-*" OR query="*-google.*"` (typosquat patterns) |
| Spoofed sender | `sourcetype=email From!=<authoritative SPF/DKIM domain>` |

See @concepts/phishing-investigation.md.

#### Data integrity + DDoS + account takeover (remaining queries)

| Hunt | Representative SPL |
|------|---------------------|
| DDoS volumetric | `\| stats count by src_ip \| where count > 10000` |
| Account takeover (impossible travel) | `EventCode=4624 \| iplocation src_ip \| stats values(Country) as countries by Account_Name \| where mvcount(countries) > 1` |
| Off-hours admin | `EventCode=4672 \| eval hour=strftime(_time, "%H") \| where hour < 6 OR hour > 22` |
| File-integrity change | `sourcetype=fim_audit \| stats count by file_path, action` |

### SPL command reference — the high-value subset

Synthesized from @sources/splunk-commands-reference.md. The full source covers ~100+ commands alphabetically; the table below is the **subset that recurs across the 110-query catalog**.

| Command | Purpose | Example |
|---------|---------|---------|
| `search` | Filter events | `search EventCode=4625 src_ip=10.*` |
| `stats` | Aggregate (count, sum, avg, values, dc) | `stats count by src_ip` |
| `eval` | Compute new fields | `eval risk_score = count * 2` |
| `where` | Post-filter on computed fields | `where count > 10` |
| `rex` | Regex-extract a field | `rex field=raw "user=(?<user>\w+)"` |
| `table` | Project columns | `table _time, user, action` |
| `sort` | Order results | `sort -count` (descending) |
| `dedup` | Remove duplicates | `dedup src_ip` |
| `top` / `rare` | Most / least common | `top limit=10 src_ip` |
| `timechart` | Time-bucketed aggregation | `timechart count by src_ip` |
| `chart` | Pivot aggregation | `chart count over src_ip by status` |
| `lookup` | Enrich from CSV | `lookup threat_intel src_ip OUTPUT category` |
| `iplocation` | Geo-enrich IPs | `iplocation src_ip` |
| `transaction` | Group events into sessions | `transaction src_ip maxspan=30m` |
| `streamstats` | Running aggregations | `streamstats count by user` |
| `eventstats` | Aggregate without collapsing | `eventstats avg(bytes) as avg_b` |
| `join` | SQL-style join across searches | `join src_ip [search ...]` (avoid — expensive) |
| `append` / `appendcols` | Concat results | for multi-source aggregation |
| `makeresults` | Synthesize events | testing without data |
| `inputlookup` / `outputlookup` | Read / write CSV | maintain hot watchlists |

**Performance rule**: `stats` scales; `join` and `transaction` do not. The corpus consistently prefers `stats` + lookup over `join`. [CONFIRMED — recurring pattern in @sources/100-splunk-queries-soc-analyst.md]

### SOC 2 use-case mapping (Rajneesh Gupta — 24 use cases)

From @sources/splunk-siem-soc2-use-cases.md ("24 Use Cases SPLUNK SIEM for SOC 2 Compliance" by Rajneesh Gupta, @rajneeshcyber). Maps SPL detection content to SOC 2 Trust Service Criteria. SOC 2 mapping matters because audit-driven SIEM deployments often need a control-traceability artifact, not just queries.

| TSC | Control | Splunk use cases (count) |
|-----|---------|--------------------------|
| **CC6.1** Logical Access | Authentication + authorization | 13 use cases: unauthorized access, privilege escalation, brute force, account lockout, dormant-account access, MFA bypass, shared-credential use, SSH key abuse, etc. |
| **CC6.6** Change Management | Authorized changes only | 1 use case: configuration change tracking |
| **CC6.7** System Operations | Monitoring + response | 8 use cases: malware detection, file-integrity, data exfil, abnormal network traffic, system errors, service availability, performance anomalies, log-source health |
| **CC6.8** Risk Mitigation | Vulnerability handling | 2 use cases: vulnerability-scanner integration, patch-compliance tracking |

Each Gupta use case is `(narrative scenario → SPL query → expected outcome → SOC-2 control reference)`. Same pattern as the 110-query catalog but with audit framing.

### Pitfalls + cost discipline

- **License cost is volumetric** — Splunk's pricing historically scales with daily-ingest GB. Index discipline matters: don't ingest verbose logs (e.g. DNS query logs at firehose volume) without a budget and a use case. The corpus reference (@sources/open-source-soc-guide.md) covers Wazuh + Elastic as no-license alternatives for budget-constrained SOCs.
- **`join` is a foot-gun** — use `stats` + `lookup` instead; `join` doesn't distribute across indexers and degrades quickly at scale.
- **Time-window default** — most SPL queries above assume the user's chosen time picker; in production-detection content, always pin `earliest=-24h latest=now` or similar.
- **Field-naming sprawl** — `Account_Name` vs `user` vs `src_user` will silently mismatch across sourcetypes. Use the **Common Information Model (CIM)** field normalization, or maintain a per-sourcetype lookup. [TENTATIVE — CIM mentioned in @sources/soc-analyst-book.md but not deep-extracted; recommend ingest before claiming validated]
- **Encoded-PowerShell hunting requires `4104`** — `4688` shows the command line but base64-encoded; `4104` (PowerShell Script Block Logging) decodes it. Both are needed. [CONFIRMED — cross-referenced with @concepts/threat-hunting.md Hunt 3]

### Comparison with peers

| Capability | Splunk | @entities/tools/qradar.md | @entities/tools/wazuh.md |
|------------|--------|---------------------------|---------------------------|
| License | Commercial — per-ingest-GB | Commercial — per-EPS | FOSS (Elastic-licensed) |
| Query language | SPL (proprietary, pipeline) | AQL (SQL-like) | Elasticsearch DSL + Wazuh rules (XML) |
| Detection-content ecosystem | Largest of the three; Splunkbase + ESCU | IBM-curated content packs | Community + commercial wazuh-rules |
| Best for | High-volume enterprise SOC with budget | Compliance-heavy regulated industries | Budget-constrained / FOSS-only / homelab |
| Corpus weight | 3 dedicated PDFs | 1 dedicated PDF | 1 dedicated PDF + open-source-soc-guide |

## Snippets

> **Failed-login brute-force baseline** [Source: 100+ Splunk Queries for SOC Analyst.pdf]
>
> ```
> index=auth sourcetype=linux_secure "Failed password"
> | stats count by src_ip
> | where count > 10
> | sort -count
> ```

> **PowerShell-Empire pattern** [Source: 100+ Splunk Queries for SOC Analyst.pdf]
>
> ```
> index=wineventlog EventCode=4104
> | search ScriptBlockText="*System.Net.WebClient*" OR ScriptBlockText="*FromBase64String*"
> | table _time, Computer, UserID, ScriptBlockText
> ```

> **Ransomware mass-rename detection** [Source: 100+ Splunk Queries for SOC Analyst.pdf]
>
> ```
> index=wineventlog EventCode=4663 Access_Mask="0x10000"
> | stats count by Account_Name, host
> | where count > 100
> ```

> **Lateral-movement (new (host, account, src) tuple)** [Source: 100+ Splunk Queries for SOC Analyst.pdf]
>
> ```
> index=wineventlog EventCode=4624 Logon_Type IN (3, 10)
> | stats values(src_ip) by Computer, Account_Name
> ```

> **SOC 2 CC6.1 — Brute-force authentication use case** [Source: splunk SOC .pdf (Gupta) — Use Case 2]
>
> *Scenario*: detect repeated failed authentication against any AD account → ATT&CK T1110.
> *Query*: `EventCode=4625 | stats count by Account_Name, src_ip | where count > 5`
> *Outcome*: alert routes to Tier-1 SOC for triage; raised to Tier-2 if MFA bypass / privileged account.

> **SPL pipeline canonical idiom** [Source: Splunk Commands.pdf, pattern from `stats` + `where` + `sort` chapters]
>
> ```
> <search> | <filter> | stats <agg> by <field> | where <threshold> | sort -<metric>
> ```

## Dead Ends

- **Hash-based detection** — corpus emphasizes SPL on behavioral fields (process command-line, parent process, event patterns) over hash matching. Same reason as @concepts/threat-hunting.md Hunt 1: hashes rotate trivially, behavior is sticky. [CONFIRMED]
- **`join` for large-table correlation** — see Pitfalls. Use `stats` + `lookup` instead. [CONFIRMED]
- **Pure CVE-number string-match for vulnerability detection** — high false-positive rate (CVE numbers appear in scan logs, patch logs, chat references). Hunt POC payload patterns or post-exploitation behavior instead. Acknowledged on @sources/100-splunk-queries-soc-analyst.md.
- **Encoded-PowerShell hunting on `4688` alone** — `4688` shows the encoded blob but doesn't decode it. Always pair with `4104` (Script Block Logging) for full visibility. [CONFIRMED]
