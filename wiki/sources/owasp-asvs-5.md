---
title: OWASP Application Security Verification Standard (ASVS) 5.0
type: source
tags: [owasp, asvs, application-security, verification, web, api]
keywords: [ASVS 5.0, ASVS 5.0.0, L1, L2, L3, OAuth, OIDC, WebRTC, frontend, OWASP]
related:
  - concepts/pre-release-product-pentest.md
  - concepts/web-pentest-methodology.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: unread-stub
---

## Relations

- @concepts/pre-release-product-pentest.md — pre-launch product test loop maps onto ASVS L1/L2/L3 assurance bars
- @concepts/web-pentest-methodology.md — web/API methodology; ASVS is the verification-requirements complement to WSTG

## Raw Concept

- **Title:** OWASP Application Security Verification Standard (ASVS) 5.0
- **Author / publisher:** OWASP Foundation
- **Type:** Official standard (project page + GitHub repo)
- **Location / URLs:**
  - Project: https://owasp.org/www-project-application-security-verification-standard/
  - GitHub: https://github.com/OWASP/ASVS
- **Retrieved:** 2026-08-02
- **Read status:** unread-stub

## Narrative

OWASP ASVS 5.0.0 was released 2025-05-30. It is a requirements catalog for verifying application and API security — roughly ~350 requirements across 17 chapters — not a step-by-step test guide (that role stays with OWASP WSTG). [TENTATIVE]

Scope covers traditional web apps and APIs. Version 5 expands coverage relative to 4.x with material for modern auth and client surfaces, including OAuth, OIDC, WebRTC, and frontend-oriented controls. [TENTATIVE]

Assurance levels (common product-security usage):

| Level | Role |
|-------|------|
| **L1** | Quick bar — minimum viable security checks; often used for early staging or low-risk surfaces |
| **L2** | Default ship bar — standard assurance for most commercial products before customer launch |
| **L3** | High-assurance — elevated requirements for high-risk data, regulated, or critical-trust systems |

[TENTATIVE] — level framing and counts above are from project-page / release messaging and have not been deep-read requirement-by-requirement in this wiki. Upgrade `read_status` and re-cite chapter numbers when a full ingest lands.

Primary use in this wiki: map pre-release product pentest scope and residual-risk reports to an explicit L1/L2/L3 bar (@concepts/pre-release-product-pentest.md), and pair with WSTG-driven testing under @concepts/web-pentest-methodology.md.
