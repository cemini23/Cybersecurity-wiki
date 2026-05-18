---
title: Threat Intelligence
type: concept
tags: [threat-intel, blue-team, soc, osint, ttp]
keywords: [threat intelligence, cti, strategic intel, tactical intel, operational intel, ioc, ttp, isac, misp, opencti]
related:
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/osint-for-cybersecurity.md
  - concepts/adversary-emulation.md
  - concepts/ransomware.md
  - entities/frameworks/mitre-attack.md
  - entities/frameworks/cyber-kill-chain.md
  - entities/threat-actors/apt28.md
  - entities/threat-actors/apt29.md
  - entities/threat-actors/lazarus.md
  - entities/threat-actors/lockbit.md
  - sources/open-source-soc-guide.md
  - sources/effective-threat-investigation-soc-analysts.md
  - concepts/phishing-investigation.md
  - entities/people/mostafa-yahia.md
  - entities/tools/splunk.md
maturity: validated
created: 2026-05-17
updated: 2026-05-17
---

## Relations

- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/osint-for-cybersecurity.md
- @concepts/adversary-emulation.md
- @concepts/ransomware.md
- @entities/frameworks/mitre-attack.md
- @entities/frameworks/cyber-kill-chain.md
- @entities/threat-actors/apt28.md
- @entities/threat-actors/apt29.md
- @entities/threat-actors/lazarus.md
- @entities/threat-actors/lockbit.md
- @sources/open-source-soc-guide.md
- @sources/effective-threat-investigation-soc-analysts.md
- @concepts/phishing-investigation.md
- @entities/people/mostafa-yahia.md
- @entities/tools/splunk.md

## Raw Concept

The wiki had no dedicated threat-intelligence page despite >15 pages referencing CTI concepts. Created from @sources/open-source-soc-guide.md Ch 2 (Basta et al., Wiley 2025) which provides the three-tier strategic/tactical/operational typology and the OSINT-vs-commercial-vs-ISAC source taxonomy. Anchor page for any future ingest that touches CTI feeds, ISAC participation, MISP / OpenCTI, or adversary attribution.

## Narrative

**Threat intelligence (CTI)** is the discipline of collecting, processing, and disseminating information about adversaries, their tradecraft, and their infrastructure — and integrating it into security decisions. CTI sits between raw threat data (a feed of IOCs) and actionable defense (a tuned detection rule, a patched CVE, a board-level budget decision). [Source: open-source-soc-guide.pdf Ch 2]

### Three-tier typology

| Tier | Audience | Time horizon | Outputs | Example artifacts |
|------|----------|--------------|---------|-------------------|
| **Strategic** | Board, CISO, risk + audit | Months to years | Threat-landscape briefings, geopolitical risk, sector-specific attack trends | Annual industry reports (Verizon DBIR, Mandiant M-Trends, ENISA Threat Landscape) |
| **Tactical** | SOC analysts, detection engineers, threat hunters | Days to weeks | TTPs mapped to MITRE ATT&CK, malware family profiles, IOC bulk feeds | STIX/TAXII feeds, MISP events, vendor IOC bulletins |
| **Operational** | IR + hunt + red-team leads | Hours to days | Specific campaign + actor + infrastructure intel | Watering-hole-domain list during an active intrusion; IP-block pivot from a confirmed C2 |

[CONFIRMED — Basta et al. Ch 2; mirrored in industry standard Mandiant + CrowdStrike + Recorded Future tier definitions]

### Source taxonomy

- **OSINT** — public-source intel: VirusTotal, AbuseIPDB, URLhaus, AlienVault OTX, Shodan, Censys, vendor blogs (Mandiant / CrowdStrike / Microsoft / Cisco Talos), social platforms, leaked-data sites. Free but noisy + variable quality. See @concepts/osint-for-cybersecurity.md.

### Canonical SOC-analyst pivot stack

Per @sources/effective-threat-investigation-soc-analysts.md (Yahia Ch 14), the named-entity OSINT-TI pivots every Tier-1 SOC analyst should know cold:

| Pivot | Best for | URL |
|-------|----------|-----|
| **VirusTotal** | File hashes, domains, URLs, outbound IPs | https://www.virustotal.com/ |
| **IBM X-Force Exchange** | Domains, IPs, hashes — corporate-grade enrichment | https://exchange.xforce.ibmcloud.com/ |
| **AbuseIPDB** | Inbound IP reputation (Tier-1 first-stop) | https://www.abuseipdb.com/ |
| **Google** | Open-web context — copy the IOC into search; vendor blogs + threat-actor reports surface | https://google.com/ |

These four are the **first-touch pivots** before reaching for commercial feeds. They are also the universal-language IOCs — anything you'd hand off to another SOC, ISAC member, or external IR firm.

- **Commercial feeds** — Recorded Future, ZeroFox, Anomali, Flashpoint, Intel 471. Higher signal-to-noise + analyst-validated, but $$$ and license-bounded for sharing.
- **ISAC / industry sharing** — sector-specific Information Sharing & Analysis Centers (FS-ISAC for finance, H-ISAC for healthcare, MS-ISAC for state + local gov, E-ISAC for electricity). Member-only, high-trust, often the fastest source for sector-targeted campaigns.
- **Government** — CISA AIS + #StopRansomware advisories (US), NCSC NCC + Early Warning (UK), ENISA (EU), ACSC (Australia). Free, public, late-binding but authoritative.
- **Internal telemetry** — your own SIEM + EDR + DNS + proxy logs feed back into CTI. Often the highest-signal source for *your* environment but ignored by orgs without a mature intel lifecycle.

### The intel lifecycle (5-step)

The classical CTI lifecycle, traceable to the US-IC + commercialized by SANS + the major CTI vendors:

1. **Direction** — define intelligence requirements (IRs). What decisions does the org need to make? Without IRs, CTI becomes IOC-feed-vomit.
2. **Collection** — pull from the sources above against IRs.
3. **Processing** — normalize, deduplicate, enrich (whois, geo, passive DNS, reverse pivots).
4. **Analysis + production** — turn processed data into a report, a rule, a hunt query, or a board slide.
5. **Dissemination + feedback** — deliver to the consumer (SOC, IR, exec); capture feedback to refine the next loop.

### Frameworks that operationalize CTI

- **MITRE ATT&CK** — the dominant TTP taxonomy. Tactical CTI maps adversary behavior to T-numbers; threat-hunting builds detections per technique. See @entities/frameworks/mitre-attack.md.
- **Cyber Kill Chain** — Lockheed-Martin's 7-stage intrusion model. Strategic CTI uses it to frame "where on the kill chain do we have the weakest controls?" See @entities/frameworks/cyber-kill-chain.md.
- **Diamond Model** — intrusion analysis primitive: adversary / capability / infrastructure / victim. Operational CTI lives here — every confirmed intrusion is a diamond.
- **STIX 2.1 / TAXII 2.1** — OASIS standards for representing + exchanging CTI. STIX = the data model; TAXII = the transport. Most modern CTI platforms speak both.

### Tooling stack (open-source-leaning)

- **MISP** (Malware Information Sharing Platform) — the open-source CTI platform standard, used by ISACs + CERTs worldwide. STIX/TAXII-compatible, supports IOC enrichment + correlation.
- **OpenCTI** — newer Filigran-maintained platform; richer graph + ATT&CK integration than MISP.
- **TheHive + Cortex** — IR case management + observable enrichment (paired with MISP).
- **Yeti** — lightweight threat-knowledge repository, good for small teams.
- **TAXII server (Anomali / EclecticIQ / OpenCTI's built-in)** — to publish feeds to consumers.

### CTI in the SOC

Per @sources/open-source-soc-guide.md Ch 2, the CTI function should:

- **Feed detection engineering** — every new IOC / TTP becomes a candidate rule. Detection coverage is measured against ATT&CK technique counts.
- **Drive proactive hunting** — see @concepts/threat-hunting.md. Hunts are hypothesis-driven and the hypotheses come from CTI ("APT29 just published their post-compromise TTP; do we see WMI Event Subscription persistence in our env?").
- **Inform IR** — known-actor profile + likely next-step = guided IR. See @concepts/incident-response.md.
- **Support adversary emulation** — purple-team exercises emulate specific actors. CTI provides the playbook. See @concepts/adversary-emulation.md.

### Common pitfalls

- **IOC dumping with no IRs** — orgs subscribe to 10 feeds, ingest 1M IOCs/day, fire 50k alerts, and detect nothing they wouldn't have caught otherwise. CTI without direction is noise.
- **Strategic-only CTI** — the threat-intel function writes glossy reports but never ships a detection rule. CTI must close the loop into the SOC + IR + detection-eng workflows.
- **Static IOCs** — IPs + domains rot in days. Pivoting to TTPs + behaviors (Pyramid of Pain top) is the higher-leverage play. See @concepts/threat-hunting.md.
- **Attribution overreach** — naming an actor in an exec report demands evidence quality on par with the named-actor risk. Most intrusions cannot be confidently attributed; "consistent with X cluster" is usually the right frame.

## Snippets

> Threat intelligence operates across three tiers: strategic (long-horizon risk + board-level decisions), tactical (TTPs + IOCs + ATT&CK mapping), and operational (specific campaigns + actors + infrastructure). — Basta et al., Open-Source SOC, Ch 2 (paraphrase) [Source: open-source-soc-guide.pdf]

### MISP IOC export (STIX 2.1, abridged)

```json
{
  "type": "indicator",
  "spec_version": "2.1",
  "id": "indicator--abc...",
  "created": "2026-05-17T00:00:00Z",
  "pattern": "[file:hashes.'SHA-256' = 'e3b0c44...']",
  "pattern_type": "stix",
  "valid_from": "2026-05-17T00:00:00Z",
  "labels": ["malicious-activity"],
  "kill_chain_phases": [
    { "kill_chain_name": "mitre-attack", "phase_name": "execution" }
  ]
}
```

### Pyramid-of-Pain pivot rule of thumb

> A hash blocks one binary. A C2 domain blocks one campaign. A TTP blocks an actor. — Bianco's Pyramid of Pain (paraphrase) [Source: enterprise.verizon.com / detect-respond.blogspot.com]

## See also

- @concepts/threat-hunting.md — hypothesis-driven hunts powered by tactical CTI
- @concepts/osint-for-cybersecurity.md — OSINT collection techniques that feed CTI
- @entities/frameworks/mitre-attack.md — the TTP taxonomy that anchors tactical CTI
- [No More Ransom](https://www.nomoreransom.org/) — ransomware-family CTI directory
- [CISA #StopRansomware](https://www.cisa.gov/stopransomware) — government CTI bulletins
