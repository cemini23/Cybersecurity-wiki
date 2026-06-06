---
title: chekusu/mails — AI email parsing, dual-use phishing-domain enumeration
type: concept
tags: [concept, phishing, threat-intel, email-parsing, dual-use, brand-abuse-monitoring]
keywords: [chekusu, mails, ai email parsing, phishing-domain enumeration, sender-domain inventory, cloudflare workers, threat-intel]
related:
  - concepts/phishing.md
  - concepts/osint-for-cybersecurity.md
  - "@osint-wiki/sources/eval-github-repos-2026-05-13.md"
maturity: draft
created: 2026-05-15
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-github-repos-2026-05-13.md"
---

# chekusu/mails — AI email parsing, dual-use phishing-domain enumeration

## Relations

- @concepts/phishing.md — defensive use case: parsing inbound mail to inventory phishing sender-domains, headers, embedded URLs
- @concepts/osint-for-cybersecurity.md — sender-domain / header extraction as a threat-intel OSINT collection technique
- @osint-wiki/sources/eval-github-repos-2026-05-13.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

`chekusu/mails` is an **MIT-licensed** AI email-parsing service running on Cloudflare Workers/D1. Surfaced in the 2026-05-13 14-repo GitHub eval (`@osint-wiki/sources/eval-github-repos-2026-05-13.md`) as **ADOPT**.

It is **dual-use**. The OSINT primary use is financial / regulatory mailroom intake. The **cybersecurity use is phishing-domain enumeration** — parsing inbound mail to extract and inventory sender domains, headers, and embedded URLs for threat-intel and brand-abuse monitoring. The MIT license is clean for adoption.

This stub records the cybersec-side use-case independently of the OSINT-side primary entity page, so analysts can pick it up without the financial-intake framing.
