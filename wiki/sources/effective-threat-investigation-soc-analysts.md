---
title: "Effective Threat Investigation for SOC Analysts.pdf"
type: source
tags: [soc, threat-investigation, log-analysis, book, phishing, windows-event-logs]
keywords: [threat investigation, security logs, attacker techniques, soc analyst, mostafa yahia, packt, helk, evtx, spf dkim dmarc, mxtoolbox]
related:
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/threat-intelligence.md
  - concepts/phishing-investigation.md
  - concepts/phishing.md
  - concepts/social-engineering.md
  - entities/people/mostafa-yahia.md
  - entities/tools/sysmon.md
  - entities/tools/splunk.md
maturity: draft
read_status: skimmed
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: Effective Threat Investigation for SOC Analysts.pdf
- **Author**: [Mostafa Yahia](../entities/people/mostafa-yahia.md) (Egyptian MSSP SOC lead, GCFA / GCIH / IBM QRadar; YouTube channel)
- **Publisher**: Packt, August 2023 (ISBN 978-1-83763-478-1)
- **Type**: PDF (textbook, 4 parts / 15 chapters, ~280 pages)
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs) (fileId `19kYHrfybBmTgrwUrPlUjcNdByhD0AGq9`)
- **Retrieved**: 2026-05-16
- **Pages**: ~280
- **Read-status**: **skimmed** — Part 1 (Ch 1-3) fully extracted; Chapters 4-15 TOC-only

## Narrative

Packt 2023 SOC textbook by Mostafa Yahia, structured in 4 parts: **email investigation** (Ch 1-2), **Windows event-log investigation** (Ch 3-7), **firewall + proxy log investigation** (Ch 8-11), **other threats + external sources** (Ch 12-15). Yahia's signature is concrete per-log-source field/event-ID reference tables paired with investigation walkthroughs.

**[NEEDS VERIFICATION 2026-05-17]** — only Chapters 1-3 + first paragraph of Ch 4 were extractable in the current ingest pass. Ch 4-15 body text was truncated in the file-read stream (the highest-value content — Windows Security Event ID tables, NTLM Event IDs p.71, Kerberos Event IDs p.72, firewall + proxy field tables — is not yet readable). Re-extraction via `pdftotext` against a downloaded copy required before this source can be promoted to `read`.

### What was extracted (Ch 1-3)

**Part 1 — Email investigation (Ch 1-2):**

- Phishing accounts for **41% of initial-access attempts** per IBM X-Force [Source: p. 4]. Phishing vs spearphishing distinction (mass vs targeted), Business Email Compromise (BEC), blackmail/sextortion.
- **Phishing attachment types** that survive AV: weaponized Office docs (VBA macros), malicious PDFs (embedded JS), compressed archives (.rar/.7z/.zip — block AV scanning), **ISO images** (bypass file filters), HTML files (impersonate login pages).
- **Sandbox evasion tradecraft**: malware sleep (up to 3 min) to outlast sandbox runtime; encrypted attachments with password in email body (sandbox can't decrypt non-interactively); VM/sandbox-environment discovery; only responding to victim-environment IPs.
- **Investigation workflow**: each suspicious email passes through 5 sub-investigations — sender reputation, spoofing validation, sender behavior, subject/filename keyword hunt, content (URL/attachment) analysis.
- **Spoofing validation**: compare `Return-Path` vs `From:`; resolve sender domain MX records via [MxToolbox](https://mxtoolbox.com/); WHOIS the actual sending SMTP IP to confirm legitimacy. Fedex-spoof case study (Ch 1, pp. 18-20) walks through this end-to-end.
- **Email authentication trio (Ch 2):** full SPF/DKIM/DMARC reference. Headers analyzed bottom-to-top (chronological order through hop chain).

**Part 2 — Windows event logs intro (Ch 3):**

- Default log path `C:\Windows\System32\winevt\Logs`; relocate via `HKLM\SYSTEM\CurrentControlSet\Services\EventLog\<LogName>` registry hive.
- Windows 11 ships with **336 default log files** [Source: p. 52].
- **Investigation toolchain**: Event Viewer (built-in GUI, live host); PsLogList (Sysinternals CLI, live host); Event Log Explorer (third-party GUI, offline EVTX); EvtxECmd (Eric Zimmerman CLI, EVTX → CSV/JSON); HELK (Cyb3rWard0g — Elastic+Kafka+Logstash open-source SIEM lab); Mordor datasets (pre-recorded adversarial-technique EVTX corpora at securitydatasets.com).
- Six Windows Security event categories: logon events, logon validation events, object access events, account management events, privilege use events, process tracking events.

### What is in the TOC but not extracted

Chapters 4-15 cover (per TOC pp. vii-xii): NTLM + Kerberos login-validation Event IDs (p. 71-72); Windows process-tracking events + LOTL parent-child relationships; PowerShell execution tracking + fileless tradecraft; persistence (Run keys / scheduled tasks / services / WMI event subscription) + lateral movement (RDP / admin shares / PsExec / PSRemoting); firewall log anatomy (14 fields) + reconnaissance / lateral movement / C2 / DNS tunneling / exfiltration investigations; proxy log anatomy (15 fields) + C2 investigation by user-agent / referer / port / bytes; web attack detection (cmd injection / SQLi / path traversal / XSS / WAF logs); network flows + IDS/IPS + EDR alerts; threat-intel pivots (VirusTotal / IBM X-Force Exchange / AbuseIPDB / Google); malware sandbox build-out (YARA / PEStudio / EXEinfo / FakeNet / ProcMon / ProcDot / RegShot / Autoruns).

### Adoption decisions

- **NEW `concepts/phishing-investigation.md`** (validated) — primary home for Ch 1-2 content. Phishing attachment-type table, attacker email-security evasion tradecraft, common phishing subject/filename keywords, Yahia's 5-step investigation workflow, full SPF/DKIM/DMARC reference, Fedex spoof case study.
- **NEW `entities/people/mostafa-yahia.md`** (draft) — author entity mirroring [Joas A. Santos](../entities/people/joas-a-santos.md). Egyptian SOC lead, MSSP, GCFA/GCIH/IBM QRadar.
- **`concepts/incident-response.md`** — updated with the Ch 3 Windows-event-log triage toolchain (Event Viewer / PsLogList / Event Log Explorer / EvtxECmd / HELK + Mordor).
- **`concepts/threat-intelligence.md`** — updated with Ch 14 confirmed pivots (VirusTotal, IBM X-Force Exchange, AbuseIPDB, Google) as the named-entity OSINT-TI pivot stack.
- **NOT YET CREATED** — `concepts/windows-event-log-investigation.md`, `concepts/powershell-attack-detection.md`, `concepts/lateral-movement-detection.md`, `concepts/firewall-log-investigation.md`, `concepts/proxy-log-investigation.md`, `concepts/dns-tunneling.md`, `concepts/c2-detection.md`, `concepts/waf-investigation.md`, `concepts/malware-sandboxing.md`. These chapters exist in Yahia's TOC but their body text + tables were not extracted; deferring until re-extraction.

## Snippets

### Ch 1 — Investigating Email Threats

> As per the IBM Security X-Force report, 41% of the attackers prefer phishing techniques to gain initial access to the victim's environment, either by sending a weaponized document or a malicious link to the target victims. — Yahia Ch 1 p. 4

> Phishing emails are mass email attacks that are sent to a randomly large number of people. In contrast, spearphishing emails are much more targeted and personalized. They are specifically crafted to target a particular individual or group of individuals, such as employees of a particular company or members of a specific organization. — Yahia Ch 1 p. 6

> Recently, we observed a notable increase in the use of .iso files to deliver malware to target recipients. Attackers depend on ISO image files because they are like disc images; hence, they can be used to bypass file filters and evade antivirus detection. — Yahia Ch 1 p. 7

> To evade detection from sandbox analysis, an attacker can take precautions by, for example, incorporating a sleep time of up to three minutes in their malware code after execution, thereby delaying the start of any malicious activity until after the sandbox analysis has been completed. — Yahia Ch 1 p. 11

> Try to observe the most common attacker keywords used in the subject lines of phishing emails, such as RE:, FW:, Invoice, Missing Inv, New Message from, New scanned, You have a New Message, New message from, Verification Required, and Action Required. Also, attackers use common keywords in filenames, such as invoice, order, contract, payment, offer, planning, and SWIFT. — Yahia Ch 1 p. 21

### Ch 2 — Email Flow + Header Analysis

> The user submits the email by using his MUA, which, by design, is connected to the MSA server, which then forwards it to MTAs so that it can be routed to the recipient's domain MX server. Finally, after being successfully authenticated by the recipient to the MDA server, they will be able to read the email. — Yahia Ch 2 p. 27

> There is a field called Return-Path that specifies the email address where bounce messages and errors are sent if the email can't be delivered. This header value contains the email address of the sender's mailbox. When an email is received, the sender's mailbox address is compared with the Return-Path header address; if they do not match, this could indicate a spoofed email. — Yahia Ch 2 p. 35

### Ch 3 — Intro to Windows Event Logs

> By default, since Windows Vista and onward, Microsoft event logs are stored in the C:\\Windows\\System32\\winevt\\Logs path; however, this location can be changed by modifying the file registry key located under the HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\EventLog\\<EventLogName> registry hive. — Yahia Ch 3 pp. 49-50

> In a pure installation of the Windows 11 OS, the number of Windows log files is 336. — Yahia Ch 3 p. 52

### Reference fragments

**SPF qualifier semantics (Ch 2 p. 40):**

```
v=spf1 ip4:192.168.1.0/24 -all
```

| Suffix | Effect on fail |
|--------|----------------|
| `-all` | Hard fail (reject) |
| `~all` | Soft fail (mark spam) |
| `?all` | Neutral |
| `+all` | Pass any sender — insecure, never use |

**DMARC record (Ch 2 p. 43):**

```
v=DMARC1; p=reject; pct=100; rua=mailto:postmaster@example.com
```

## Dead Ends

- **Direct `read_file_content` of the 13.3 MB Yahia PDF** returned ~140 KB of text covering only the front matter + Ch 1-3 + first paragraph of Ch 4 before the body stream terminated; remaining ~210 pages collapse into a bare hyperlink/index dump. The book's highest-value content (Windows Event ID + Sysmon + firewall + proxy field tables) is page-numbered in the TOC (pp. 71, 72, 87-88, 149-153, 176-184) but the body text is not in the MCP-returned stream. Path forward: download the PDF locally via `download_file_content`, run `pdftotext -layout` against the file, chunk by chapter, then resume the deep-read.
- **Creating stub tool entities for every named tool in Ch 1-3** (MxToolbox, URLscan, ANY.RUN, HELK, Mordor datasets, EvtxECmd, Event Log Explorer, PsLogList, CyberChef) was considered and deferred. These tools are cited inline in `concepts/phishing-investigation.md` + `concepts/incident-response.md` without per-tool stubs — creating 9 empty stubs adds maintenance burden without commensurate content. Stubs to be created lazily as future deep-reads add substantive content.

## Relations

- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/threat-intelligence.md
- @concepts/phishing-investigation.md
- @concepts/phishing.md
- @concepts/social-engineering.md
- @entities/people/mostafa-yahia.md
- @entities/tools/sysmon.md
- @entities/tools/splunk.md
