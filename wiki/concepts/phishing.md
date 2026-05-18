---
title: "Phishing"
type: concept
tags: [phishing, social-engineering, red-team, offensive-security, defensive-security]
keywords: [phishing, spear phishing, whaling, email attacks, social engineering, pretexting, MFA bypass]
related:
  - concepts/social-engineering.md
  - concepts/red-team-operations.md
  - sources/phishing-dark-waters.md
  - sources/hacking-multifactor-authentication.md
  - concepts/2026-05-13_chekusu-mails-dual-use.md
  - concepts/phishing-investigation.md
  - sources/effective-threat-investigation-soc-analysts.md
maturity: draft
created: 2026-05-15
updated: 2026-05-17
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

Social engineering technique using deceptive emails, messages, or websites to steal credentials, deliver malware, or manipulate targets. Red-team perspective: infrastructure setup (domain typosquatting, email spoofing, SMTP relays), pretext development, payload delivery (macro docs, HTML smuggling, QR codes), and MFA bypass (evilginx2, Modlishka proxy-based). Defensive perspective: SPF/DKIM/DMARC, email filtering, user awareness training, phishing simulation programs.

## Relations

- @concepts/social-engineering.md
- @concepts/red-team-operations.md
- @sources/phishing-dark-waters.md
- @sources/hacking-multifactor-authentication.md
- @concepts/2026-05-13_chekusu-mails-dual-use.md — AI email-parsing tool; dual-use for phishing-domain enumeration and brand-abuse monitoring
- @concepts/phishing-investigation.md — defensive SOC-analyst triage workflow (Yahia 5-step + SPF/DKIM/DMARC)
- @sources/effective-threat-investigation-soc-analysts.md — Yahia Packt 2023, defensive-investigation perspective
