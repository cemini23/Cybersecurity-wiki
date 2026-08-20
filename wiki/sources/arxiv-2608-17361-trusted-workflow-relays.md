---
title: "Trusted Workflow Relays — cross-tenant email abuse (arXiv 2608.17361)"
type: source
tags: [source, arxiv, email, m365, initial-access, k296]
keywords: [2608.17361, trusted workflow relay, cross-tenant, notification abuse, Nigam]
related:
  - concepts/trusted-workflow-relay-email-abuse.md
  - concepts/phishing.md
  - concepts/phishing-investigation.md
  - concepts/responsible-disclosure.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "REFERENCE 2026-08-20 — case study, no public exploit kit. Authorized email/lab / written-scope product pentest only. Do not clone. Do not write third-party phishing runbooks."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K296 Trusted Workflow Relays)"
---

**Briefs:** `briefs/2026-08-20_k296-trusted-workflow-relays.md`

## Relations

- @concepts/trusted-workflow-relay-email-abuse.md
- @concepts/phishing.md — attachment-free, service-authentic send
- @concepts/phishing-investigation.md — SPF/DKIM/DMARC can pass
- @concepts/responsible-disclosure.md — three workflows disclosed and remediated

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Trusted Workflow Relays: Cross-Tenant Email Abuse and Composable Red Team Initial-Access Primitives in Multi-Tenant Clouds |
| Authors | Priyank Nigam (Microsoft Security Engineering) |
| arXiv | 2608.17361 (cs.CR, v1 18 Aug 2026) CC BY-NC-ND |
| Code | none |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.17361-trusted-workflow-relays-cross-tenant-email-abuse.pdf` |
| Retrieved | 2026-08-20 |
| Read status | read (full 8 pp.) |

## Narrative

Cloud apps send notifications through **provider-operated mail identities**. That improves deliverability and splits the actor who supplies parameters from the service principal that originates the message. In three responsibly disclosed and remediated cross-tenant notification workflows, an authenticated low-priv actor could reach recipients across tenant boundaries and, to varying degrees, control content a trusted provider delivered. Definition: a **trusted workflow relay** is a delivered, service-authentic message for which the application-level send-authorization predicate is false. Analogous to a classical SMTP open relay, but the failure moved **up the stack**. SPF/DKIM/DMARC can authenticate the message and still not prove the send was authorized. Maps to MITRE ATT&CK attachment-free phishing; links to device-code phishing (RFC 8628). Controls: tenant binding, typed templates, object-level authorization, token audience validation, identity telemetry. [CONFIRMED] paper + disclosed/remediated; no live kit.

**Wiki rule:** awareness + product-pentest checklist. No third-party phishing kits, no live relay against tenants you do not own.

## Snippets

> SPF, DKIM, and DMARC can authenticate a message yet cannot establish that an application-level send was authorized. [Source: arXiv 2608.17361 abstract]
