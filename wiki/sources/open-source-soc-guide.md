---
title: "Open-Source Security Operations Center (SOC).pdf"
type: source
tags: [soc, siem, blue-team, book, open-source]
keywords: [open-source soc, soc pillars, siem, log analysis, security analytics, basta, threat intelligence, zero trust]
related:
  - concepts/soc-operations.md
  - concepts/siem.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/threat-intelligence.md
  - concepts/zero-trust.md
  - entities/frameworks/cyber-kill-chain.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/sysmon.md
maturity: draft
read_status: skimmed
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: Open-Source Security Operations Center (SOC).pdf
- **Author**: Alfred Basta, Nadine Basta, Waqar Anwar, Mohammad Ilyas Essar (Wiley, 2025) [Source: open-source-soc-guide.pdf p.1]
- **Type**: PDF (textbook, ~15 chapters)
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs)
- **Retrieved**: 2026-05-16
- **Pages**: ~400+
- **Read-status**: skimmed (Ch 1-2 + partial Ch 3 extracted; **Ch 4-15 not yet readable** — see verification flag below)

## Narrative

Wiley 2025 academic-style textbook by Basta et al. on building an open-source SOC. The book is structured around five pillars (people, processes, technology, governance, **data**) and chapters covering: SOC pillars, threat intelligence, log analysis, network-traffic analysis, endpoint analysis, SIEM, security analytics + ML, insider-threat detection, IR, and emerging trends.

**[NEEDS VERIFICATION 2026-05-17]** — only Chapters 1-2 + partial Chapter 3 were extractable in the current ingest pass. Chapters 4-15 are present in the TOC but the body text was not surfaced in the file-read response. A re-extraction (or direct manual read of the PDF) is required before this source can be promoted to `read`. Material below is sourced strictly from Ch 1-2.

### What was extracted (Ch 1-2)

- **Modern SOC definition + drivers** — distributed workforces, cloud-native infrastructure, third-party / supply-chain risk, regulatory + privacy pressure (GDPR, CCPA, HIPAA), real-time-detection demand, and skills-shortage all push organizations toward formalized SOCs.
- **The five pillars** — extends the traditional people/process/technology model with **governance** + **data** as first-class pillars. Data pillar = the lifeblood: collection, normalization, retention, integrity, privacy. Without a data-quality discipline, every downstream control degrades.
- **3 SOC operating models** — in-house, co-managed, MSSP. Choice is driven by 7 criteria (budget, expertise, regulatory, infrastructure complexity, threat landscape, scalability, control + visibility).
- **Alert-volume reality** — see Snippets. 20k-endpoint org generates ~500k alerts/day; analyst can process ~1k/day, ~10 of which are genuine. This number alone justifies the SOAR + ML-prioritization push.
- **Cyber Kill Chain (Lockheed-Martin 7-stage)** — reconnaissance → weaponization → delivery → exploitation → installation → C2 → actions on objectives. Used by Basta et al. as the kill-chain reference framework alongside MITRE ATT&CK.
- **Threat intelligence (Ch 2)** — three-tier model: **strategic** (board / CISO level — risk landscape, geopolitical context, multi-year trends), **tactical** (TTP-level — IOC feeds, ATT&CK mapping, malware family profiles), **operational** (campaign-level — specific actor + infrastructure). Sources split into OSINT, commercial feeds, ISAC / industry sharing, government (CISA, NCSC, ENISA).
- **Zero-Trust adoption signal** — 76% of firms have begun executing a zero-trust approach (Nispel 2023). Treated as default network-design assumption in the book.

### Adoption decisions

- **`concepts/soc-operations.md`** — extended with 3 SOC-model framework, alert-volume scale numbers, Pillar-4 (Data) framing, Cyber Kill Chain 7-stage table.
- **`concepts/threat-intelligence.md`** — NEW page created from Ch 2 content (the wiki had no dedicated threat-intel page previously).
- **NOT YET CREATED** — `concepts/log-analysis.md`, `concepts/network-traffic-analysis.md`, `concepts/security-analytics-ml.md`, `concepts/insider-threat.md`. These chapters exist in the book's TOC but the body text was not extracted; deferring page creation until Ch 4-8 are readable.

## Snippets

> A company with 20,000 endpoints can generate up to 500,000 alerts per day. — Basta et al., Open-Source SOC, Ch 1 [Source: open-source-soc-guide.pdf]

> An analyst could get 1000 alerts per day, but only 10 of them may represent genuine hazards. — Basta et al., Open-Source SOC, Ch 1 [Source: open-source-soc-guide.pdf]

> 76% of firms have at least begun to execute a zero-trust approach. — Nispel (2023), cited in Basta et al. Ch 1 [Source: open-source-soc-guide.pdf]

> The five pillars of a SOC are people, processes, technology, governance, and **data**. — Basta et al., Ch 1 [Source: open-source-soc-guide.pdf]

> Threat intelligence operates across three tiers: strategic (long-horizon risk + board-level decisions), tactical (TTPs + IOCs + ATT&CK mapping), and operational (specific campaigns + actors + infrastructure). — Basta et al., Ch 2 (paraphrase) [Source: open-source-soc-guide.pdf]

> The Cyber Kill Chain decomposes an intrusion into seven sequential stages: reconnaissance, weaponization, delivery, exploitation, installation, command and control, and actions on objectives. — Lockheed-Martin, cited in Basta et al. Ch 1 [Source: open-source-soc-guide.pdf]

> A SOC choice (in-house, co-managed, MSSP) should be evaluated against budget, expertise, regulatory, infrastructure complexity, threat landscape, scalability, and control + visibility. — Basta et al., Ch 1 (paraphrase) [Source: open-source-soc-guide.pdf]

## Dead Ends

- **Direct `read_file_content` of the 6.2 MB PDF** returned a 150 KB extraction that exceeded the inline token limit; delegated to a subagent which surfaced Ch 1-2 + partial Ch 3 only. Ch 4-15 body text appears truncated in the extracted stream. Path forward: re-extract via a different tool (pdftotext / page-range read) before the source can move to `read`.

## Relations

- @concepts/soc-operations.md
- @concepts/siem.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/threat-intelligence.md
- @concepts/zero-trust.md
- @entities/frameworks/cyber-kill-chain.md
- @entities/frameworks/mitre-attack.md
- @entities/tools/sysmon.md
