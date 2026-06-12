---
title: Google discovery-document AI fuzzing at scale
type: concept
tags: [api-security, google-vrp, fuzzing, discovery-documents, k112]
keywords: [arvin-shivram, api-keys, bug-bounty, ai-assisted-fuzzing]
related:
  - sources/brief-k112-cybersec-google-ai-api-fuzzing-2026-06-12.md
  - sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md
  - entities/tools/ai-research-skills.md
  - "@osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @sources/brief-k112-cybersec-google-ai-api-fuzzing-2026-06-12.md — K112 brief ingest
- @entities/tools/ai-research-skills.md — model/MLOps surface (pairs with API-surface fuzzing)
- @osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md — Post 4 Arvin Shivram

## Raw Concept

K112 Arvin Shivram case study: scale API fuzzing using Google **discovery documents** (Swagger-like REST specs) + mass API key harvest + LLM-generated parameter mutations. Author claims 1,500 APIs / 3,600 keys / $500k bounties `[NEEDS VERIFICATION 2026-06-12]`.

## Narrative

### Attack chain

1. Harvest GCP API keys (APK grep, browser intercept, IPA analysis)
2. Filter to Google-owned projects via Cloud Marketplace `infoSharing` + project numbers from API errors
3. Enumerate live `*.googleapis.com` hosts (CT logs, keyword brute, extension captures)
4. Fetch `/$discovery/rest` per host (note July 2025 path removals; label-gated hidden endpoints e.g. `GOOGLE_INTERNAL`)
5. AI fuzz from schemas; human triage

### Defensive takeaways

| Control | Rationale |
|---------|-----------|
| Per-API key least privilege | Keys in client binaries are public |
| Discovery access monitoring | Spec = attacker roadmap |
| Rate limits beyond WAF | AI fuzz increases diversity |
| Label-gated endpoint audit | Hidden methods bypass default discovery |

### Scope

Described in authorized Google VRP / bugSWAT context — replicate only on in-scope programs.

## Sources

- @osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md (Post 4)
- Author prior discovery-doc article (URL in original X post — verify before deep-read source page)
