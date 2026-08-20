---
title: "Trusted workflow relay — service-authentic unauthorized send"
type: concept
tags: [concept, email, phishing, cloud, initial-access, k296]
keywords: [trusted workflow relay, cross-tenant notification, send-authorization, SPF-DKIM-DMARC gap]
related:
  - sources/arxiv-2608-17361-trusted-workflow-relays.md
  - concepts/phishing.md
  - concepts/phishing-investigation.md
  - concepts/responsible-disclosure.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K296)"
---

## Relations

- @sources/arxiv-2608-17361-trusted-workflow-relays.md
- @concepts/phishing.md
- @concepts/phishing-investigation.md
- @concepts/responsible-disclosure.md

## Raw Concept

When is a "trusted" cloud notification actually an unauthorized relay?

## Narrative

A multi-tenant notification pipeline must bind four things before send: initiating principal, tenant, target object/recipient, and admitted content. Fail any one and a legitimate notification service becomes an **application-layer relay**. The message is not forged — infrastructure and domain authentication can be entirely legitimate. [Source: arXiv 2608.17361]

Authorization decomposition (paraphrase, not an exploit checklist): MayAct on the object · MayTarget the recipient across tenants · MayOriginate the privileged side-effect · SafeContent in the service template. A trusted workflow relay exists when delivery is authentic **and** that conjunction is false.

**SOC / product-pentest steal:** treat "SPF+DKIM+DMARC pass" as **sender-identity**, not **workflow authorization**. Hunt for notification origination that is missing tenant-binding, typed templates, object-level authz, or token-audience checks. Device-code (RFC 8628) phishing composes with a trusted send channel. **Authorized owned-lab / engagement / bounty program only.** Do not send unsolicited messages; the source paper used researcher-controlled mailboxes and benign proof text.

## Snippets

> Authentics(m) means the message genuinely originates from the provider service; it does not assert that the initiating application action was authorized. [Source: arXiv 2608.17361 §2.1]
