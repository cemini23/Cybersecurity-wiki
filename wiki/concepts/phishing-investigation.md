---
title: Phishing Investigation (SOC Workflow)
type: concept
tags: [soc, phishing, incident-response, email-security, threat-hunting]
keywords: [phishing, spearphishing, bec, sextortion, email investigation, spoofing, spf, dkim, dmarc, mxtoolbox, urlscan, any.run, return-path, mostafa yahia]
related:
  - concepts/phishing.md
  - concepts/social-engineering.md
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/threat-hunting.md
  - concepts/threat-intelligence.md
  - concepts/malware-analysis.md
  - entities/people/mostafa-yahia.md
  - sources/effective-threat-investigation-soc-analysts.md
  - entities/tools/splunk.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/arxiv-2608-17361-trusted-workflow-relays.md
  - concepts/trusted-workflow-relay-email-abuse.md
maturity: validated
created: 2026-05-17
updated: 2026-05-17
---

## Relations

- @concepts/phishing.md
- @concepts/social-engineering.md
- @concepts/soc-operations.md
- @concepts/incident-response.md
- @concepts/threat-hunting.md
- @concepts/threat-intelligence.md
- @concepts/malware-analysis.md
- @entities/people/mostafa-yahia.md
- @sources/effective-threat-investigation-soc-analysts.md
- @entities/tools/splunk.md
- @sources/100-splunk-queries-soc-analyst.md

## Raw Concept

Created 2026-05-17 from deep-read of @sources/effective-threat-investigation-soc-analysts.md Ch 1-2 (Yahia, Packt 2023). The wiki has `@concepts/phishing.md` for the attacker-side technique catalog (spear/clone/vishing/smishing/MFA-bypass) but lacked a defender-side investigation workflow page. This page is the SOC analyst's playbook for triaging a suspicious email — distinct from the strategic phishing-prevention guidance on `@concepts/phishing.md`.

## Narrative

Phishing accounts for ~41% of initial-access attempts in IBM X-Force telemetry — making suspicious-email triage the single most common Tier-1 SOC ticket [Source: yahia ch 1 p. 4]. This page is the workflow for triaging one of those tickets: from the moment an alert fires (or a user reports a suspicious email) to the verdict (benign / phishing / malicious-attachment / compromised-mailbox) and the post-triage containment actions.

### Email threat taxonomy

| Threat type | Adversary goal | Mechanism |
|-------------|----------------|-----------|
| **Spearphishing — attachment** | Initial access OR credential harvest | Weaponized Office doc (VBA macro), PDF (embedded JS), ISO/HTML/ZIP that bypasses gateway AV |
| **Spearphishing — link** | Credential harvest OR malware download | URL to phishing page (login-page clone) or cloud-hosted malware download |
| **Business Email Compromise (BEC)** | Fraudulent wire transfer | Email thread hijacking OR exec / supplier domain spoofing; usually no attachment |
| **Blackmail / sextortion** | Bitcoin extortion | Spoof victim's own email (`From:` = victim's address); screenshots/passwords from infostealer + dark-web leaks as "proof" |

[Source: yahia ch 1 pp. 5-10]

### Attacker email-security evasion tradecraft

| Evasion technique | Defender control it defeats |
|-------------------|-----------------------------|
| Newly registered sender domains | Reputation-based domain blocklists (low signal until first malicious use) |
| Compromised legitimate SMTP server IPs | Reputation-based IP blocklists |
| Malware sleep up to ~3 min after detonation | Sandbox real-time-monitoring window |
| Encrypted attachment with password in email body | Sandbox automated detonation (can't pass password non-interactively) |
| VM / analysis-tool discovery in payload | Sandbox environment fingerprint |
| Payload only responds to victim-environment IPs | Generic sandbox detonation infra |
| Phishing hosted on appspot.com / web.app / vendor SaaS | Reputation-based URL blocklists + the user's "trusted-brand-domain" heuristic |
| SSL/TLS certificate on the phishing site | The "green padlock = safe" user mental model |

[Source: yahia ch 1 pp. 10-12]

### Common phishing-keyword catalog

**Subject-line keywords** [Source: yahia ch 1 p. 21]: `RE:`, `FW:`, `Invoice`, `Missing Inv`, `New Message from`, `New scanned`, `You have a New Message`, `Verification Required`, `Action Required`, `Urgent`, `Payment Confirmation`, `Outstanding Balance`.

**Attachment filename keywords**: `invoice`, `order`, `contract`, `payment`, `offer`, `planning`, `SWIFT`, `purchase`, `quote`, `receipt`, `statement`.

Bulk-hunt these keywords across the secure-email-gateway corpus (Splunk / Elastic / Sentinel) to surface low-volume long-tail campaigns.

### The 5-sub-investigation workflow

Yahia's framework — for any single suspicious email, walk all five before issuing a verdict [Source: yahia ch 1 pp. 12-22]:

1. **Sender domain + SMTP reputation** — check sender domain age + reputation (URLscan, VirusTotal, Cisco Talos Intelligence); resolve `Return-Path` domain via [MxToolbox](https://mxtoolbox.com/) against ~82 IP/domain blacklists. New domains + non-blacklisted-but-low-reputation IPs are amber flags.
2. **Spoofing validation** — compare `Return-Path:` vs `From:` (mismatch = spoofing tell). Resolve sender claimed-domain MX records; WHOIS the actual sending SMTP IP. SPF / DKIM / DMARC fails are confirming evidence. See the [Email-authentication reference](#email-authentication-reference) below.
3. **Sender behavior** — does this sender normally send to this recipient? First-contact + bulk-send + non-business-hours + unusual geolocation are all behavioral flags. Modern email gateways (Proofpoint, Mimecast, Microsoft Defender for O365) ship behavioral scoring built-in.
4. **Subject + filename keyword hunt** — match against the keyword catalog above. A "Verification Required" subject with an `invoice.iso` attachment from a 3-day-old sender domain is a near-certain verdict.
5. **Content analysis** — defang the URL(s) (`hxxp://`, `[.]`), submit to [URLscan](https://urlscan.io/) (private mode for sensitive engagements). Hash the attachment(s), pivot via [VirusTotal](https://www.virustotal.com/), detonate in [ANY.RUN](https://any.run/) (interactive cloud sandbox — beats automated sandboxes on the sleep/password-encryption/env-aware evasions above). Decode any base64 PowerShell args via [CyberChef](https://gchq.github.io/CyberChef/).

### Email-authentication reference

The email-flow hop chain: **MUA → MSA → MTA → MX (recipient domain) → MDA → recipient MUA**. Each hop adds a `Received:` header — read these **bottom-to-top** (oldest hop first) to reconstruct the path [Source: yahia ch 2 p. 27].

#### SPF (Sender Policy Framework)

DNS TXT record declaring which IPs are authorized to send for the domain.

Example: `v=spf1 ip4:192.168.1.0/24 -all`

| Qualifier | Behavior on SPF check fail |
|-----------|----------------------------|
| `-all` | Hard fail — reject |
| `~all` | Soft fail — mark as spam |
| `?all` | Neutral — no preference |
| `+all` | Pass any sender (insecure, never use) |

[Source: yahia ch 2 p. 40]

#### DKIM (DomainKeys Identified Mail)

Cryptographic signature over selected headers + body, public key published in DNS.

| Field | Meaning |
|-------|---------|
| `v` | DKIM version (always 1) |
| `a` | Algorithm (e.g., `rsa-sha256`) |
| `c` | Canonicalization (`relaxed/relaxed` or `simple/simple`) |
| `d` | Signing domain |
| `s` | Selector — DNS pubkey at `<s>._domainkey.<d>` |
| `t` | Epoch signing timestamp |
| `bh` | Base64 hash of canonicalized body |
| `h` | Colon-list of headers covered by signature |
| `b` | The encrypted signature itself |

[Source: yahia ch 2 pp. 41-43]

#### DMARC (Domain-based Message Authentication, Reporting & Conformance)

Policy on what to do when SPF + DKIM fail.

Example: `v=DMARC1; p=reject; pct=100; rua=mailto:postmaster@example.com`

| Field | Meaning |
|-------|---------|
| `v` | DMARC version |
| `p` | Policy on fail: `none` / `quarantine` / `reject` |
| `pct` | Percent of failing mail to which policy applies (1-100) |
| `rua` | mailto: for aggregate reports |

[Source: yahia ch 2 p. 43]

**Investigation rule of thumb:** missing DKIM signature + SPF fail + `Return-Path` mismatch = spoofed message. The Fedex-impersonation case in Yahia Ch 1 pp. 18-20 demonstrates this end-to-end: sender claimed `fedex.com`, sending SMTP IP `95.211.214.81` was not in the fedex MX record set, no DKIM signature, SPF fail — confirmed spoof.

### Tool stack

| Stage | Tool | What it does |
|-------|------|--------------|
| Sender / IP / domain reputation | [MxToolbox](https://mxtoolbox.com/) | ~82 IP+domain blacklist aggregate; also MX/SPF/DKIM/DMARC record lookup |
| Sender / IP / domain reputation | [Cisco Talos Intelligence](https://talosintelligence.com/) | IP+domain reputation scoring |
| URL detonation | [URLscan.io](https://urlscan.io/) | Sandbox a URL; capture screenshot, DOM, network requests; private mode for sensitive submissions |
| Attachment hash pivot | [VirusTotal](https://www.virustotal.com/) | 70+ AV-engine + sandbox + community-comment pivot — see also @concepts/threat-intelligence.md |
| Interactive sandbox | [ANY.RUN](https://any.run/) | Cloud sandbox with interactive UI — defeats sleep, password-encryption, env-aware evasions |
| Decoder / encoder | [CyberChef](https://gchq.github.io/CyberChef/) | Base64 / URL / hex decode chains, especially for encoded PowerShell args |
| IOC enrichment | [AbuseIPDB](https://www.abuseipdb.com/) | Inbound-IP reputation — see @concepts/threat-intelligence.md |

### Triage outcomes + handoffs

| Verdict | Containment action | IR handoff |
|---------|--------------------|------------|
| **Benign** | Release from quarantine; tune detection if false-positive | None |
| **Phishing — unclicked / unopened** | Purge from all O365 / Workspace mailboxes via tenant-wide search-and-delete; block sender + URL at gateway | None unless campaign-scale (>20 recipients) |
| **Phishing — credentials submitted** | Force password reset + MFA re-enroll + revoke active sessions for affected user(s); audit `signInLogs` / `auditLogs` for post-compromise activity | Tier-2 IR — assume mailbox compromise until proven otherwise |
| **Malicious attachment — executed** | EDR isolate affected host; pull memory + disk image if scope justifies; pivot via @entities/tools/sysmon.md events 1+3+11+12-14 for execution + persistence artifacts | Tier-2 / Tier-3 IR + reverse engineering (@concepts/malware-analysis.md) |
| **BEC — wire transfer initiated** | Immediate AR/AP freeze; bank recall request (golden window ~24 hrs); FBI IC3 + local LE notification if US-based; legal + insurance loop-in | Specialized BEC IR; almost always external counsel |

### Defender priorities

- **Email gateway tuning** — every blocked malicious email is a free signal. Pipe gateway block-reasons into the SIEM for trend analysis.
- **DMARC enforcement** — publish `p=reject` (or `p=quarantine` minimum) on every owned domain. Most enterprise mailboxes still ship `p=none` which gives spoofers a free pass.
- **User reporting button** — give end-users a "Report Phishing" button that pipes into a SOC queue rather than just-delete. User-reported phishing is the highest-precision signal in the SIEM (~10x base-rate vs gateway-fired alerts).
- **Sandbox both attachments + URLs** at the gateway, but assume sandbox-evasive tradecraft (above) will succeed against your specific automated sandbox config. Interactive sandbox (ANY.RUN) for post-delivery investigation closes part of that gap.
- **Threat-intel feedback** — every confirmed-phishing IOC (sender domain, sending IP, malicious URL, attachment hash) goes back to threat-intel (@concepts/threat-intelligence.md) — both your internal MISP/OpenCTI + your ISAC.

## Snippets

> As per the IBM Security X-Force report, 41% of the attackers prefer phishing techniques to gain initial access to the victim's environment. — Yahia Ch 1 p. 4 [Source: effective-threat-investigation-soc-analysts.pdf]

> There is a field called Return-Path that specifies the email address where bounce messages and errors are sent if the email can't be delivered. When an email is received, the sender's mailbox address is compared with the Return-Path header address; if they do not match, this could indicate a spoofed email. — Yahia Ch 2 p. 35

> An attacker can employ a technique of sending a malware file to the victim in the form of a compressed folder or document file, encrypted with a password, which is then shared with the victim via the email body for decryption. Since submitting an attachment file to a sandbox by an email gateway is not an interactive submission process, the password cannot be provided to the sandbox during file analysis to decrypt and analyze the file. — Yahia Ch 1 p. 11

## See also

- @concepts/phishing.md — attacker-side techniques (smishing, vishing, MFA bypass, infrastructure)
- @concepts/social-engineering.md — broader sociotechnical attack family
- @concepts/threat-intelligence.md — pivot stack (VirusTotal / X-Force / AbuseIPDB / Google)
- [Microsoft Defender for Office 365 — submission portal](https://security.microsoft.com/reportsubmission) (for tenant-wide phishing reporting)
- [APWG — Anti-Phishing Working Group](https://apwg.org/) (industry sharing + phishing IOC feeds)
