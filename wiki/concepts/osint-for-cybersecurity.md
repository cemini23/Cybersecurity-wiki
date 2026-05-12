---
title: OSINT for Cybersecurity
type: concept
tags: [osint, recon, reconnaissance, intelligence]
keywords: [osint, open source intelligence, recon, investigation, shodan, maltego]
related:
  - entities/tools/maltego.md
  - concepts/red-team-operations.md
  - concepts/social-engineering.md
  - concepts/threat-hunting.md
  - sources/osint-overview-pt-1.md
  - sources/apostila-a-arte-do-osint-para-pentesters.md
  - sources/fundamentos-de-osint.md
  - sources/investigation-using-osint-with-a-focus-on-intelligence-operations-and-dark-web-o.md
  - sources/using-osint-techniques-to-investigate-human-trafficking-and-missing-persons-pt-1.md
  - sources/using-osint-to-investigate-human-trafficking-and-missing-persons.md
  - sources/using-osint-to-investigate-school-shooters.md
  - sources/ransomware-investigation-osint-and-hunting-overview-pt1.md
  - entities/people/joas-a-santos.md
  - concepts/anonymity-networks.md
  - entities/programming-languages/python.md
maturity: validated
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @entities/tools/maltego.md
- @concepts/red-team-operations.md
- @concepts/social-engineering.md
- @concepts/threat-hunting.md
- @sources/osint-overview-pt-1.md
- @sources/apostila-a-arte-do-osint-para-pentesters.md
- @sources/fundamentos-de-osint.md
- @sources/investigation-using-osint-with-a-focus-on-intelligence-operations-and-dark-web-o.md
- @sources/using-osint-techniques-to-investigate-human-trafficking-and-missing-persons-pt-1.md
- @sources/using-osint-to-investigate-human-trafficking-and-missing-persons.md
- @sources/using-osint-to-investigate-school-shooters.md
- @sources/ransomware-investigation-osint-and-hunting-overview-pt1.md
- @entities/people/joas-a-santos.md
- @osint-wiki/concepts/typed-relation-dependencies.md
- @concepts/anonymity-networks.md
- @entities/programming-languages/python.md

## Raw Concept

7+ corpus PDFs explicitly scope to OSINT — pentest-side (APOSTILA A ARTE DO OSINT PARA PENTESTERS, OSINT Overview, FUNDAMENTOS DE OSINT) + investigative-side (human trafficking, missing persons, school shooters, ransomware investigation).

## Narrative

OSINT (Open-Source Intelligence) is the discipline of collecting + analyzing publicly available information to support an investigation or operation. In cybersecurity it appears in three distinct roles: [CONFIRMED]

**1. Pentest / Red Team recon.** Pre-engagement OSINT establishes the target's external footprint without sending a single packet to their infrastructure: subdomain enumeration via crt.sh, dnsdumpster, Censys; corporate identity mapping via LinkedIn / GitHub / Twitter; leaked credentials via HaveIBeenPwned / Dehashed / IntelX; technology fingerprinting via Wappalyzer / BuiltWith; certificate-transparency mining for shadow domains. The corpus's *APOSTILA A ARTE DO OSINT PARA PENTESTERS.pdf* anchors the pentest-side methodology.

**2. Defensive / threat intelligence.** Threat-intel teams use OSINT to track threat actors — OPSEC mistakes in social media, infrastructure reuse across campaigns, public TTP write-ups, leaked builder kits on criminal forums. The corpus's *Ransomware Investigation (osint and hunting).pdf* anchors this use case.

**3. Investigation (human-impact context).** Law enforcement + nonprofits use OSINT for human trafficking investigations, missing-persons searches, child-safety case work, threat assessments for school violence. Four corpus PDFs cover this niche specifically: human-trafficking (EN + PT-BR), missing persons, and school shooters. **This use case requires extra ethical care** — victim privacy + chain-of-custody for evidence + jurisdictional rules around what's admissible.

### Tool families

- **Domain + IP**: whois / dig / crt.sh / SecurityTrails / Shodan / Censys / DNSDumpster / DNS history sites
- **People + accounts**: Sherlock, WhatsMyName, Maigret (cross-platform username lookups); Holehe, Epieos (email enumeration); LinkedIn / Twitter / Facebook / Instagram with proper OPSEC
- **Leaked credentials**: HaveIBeenPwned, Dehashed, IntelX, ScyllaDB credential dumps
- **Graph + linkage**: @entities/tools/maltego.md (commercial + community), SpiderFoot, Recon-ng (frameworks that orchestrate the smaller tools)
- **Code search**: GitHub Dorking (`extension:env DB_PASSWORD`), GitLeaks, TruffleHog for repo secret discovery
- **Image + geolocation**: reverse image search (TinEye, Yandex), EXIF tools, GeoSpy AI for image-derived geolocation
- **Dark web** (caveat: needs Tor + OPSEC): Ahmia, OnionLand, Dread, exposed-credentials dumps on criminal forums. Use VMs + read-only browsing; never paste anything identifying.

### Cross-wiki anchor

The sibling **OSINT wiki** (@osint-wiki/) covers OSINT primarily through the financial-research lens (ticker due-diligence, congressional-trade tracking, prediction-market sentiment), with deeper coverage of source-evaluation methodology + exploration-graph dead-ends. When this wiki needs a methodology reference, prefer linking there rather than duplicating. Example: see @osint-wiki/concepts/typed-relation-dependencies.md for that methodology.
