---
title: Google — Advanced Protection Program
type: source
tags: [source, google, advanced-protection, security-key, account-security, high-risk-users]
keywords: [Advanced Protection, passkey, security key, phishing-resistant, Safe Browsing, restricted app access]
related:
  - concepts/account-recovery-deanonymization.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Google program page"
wire_status: wont_wire
---

## Relations

- @concepts/account-recovery-deanonymization.md — phishing-resistant sign-in as the login door; recovery remains the alternate door

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Google Advanced Protection Program |
| Publisher | Google |
| URL | https://landing.google.com/advancedprotection/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Google's Advanced Protection Program is its "strongest security" layer for Google Accounts, aimed at high-risk users who "may be specifically targeted" — activists, journalists, political candidates and campaign staff (with testimonials from organizations like Defending Digital Campaigns). [CONFIRMED, retrieved 2026-08-12]

Protections: **phishing-resistant sign-in** — "requires you to use a passkey or a security key to verify your identity"; a stolen password is insufficient ("unauthorized users won't be able to sign in without them, even if they know your username and password"). **Stricter download checks** beyond Safe Browsing, and app installs restricted to verified stores (Google Play). **Restricted third-party app access** — only Google apps and verified third-party apps can reach account data (contacts, Drive, location), and only with user permission. [CONFIRMED, retrieved 2026-08-12]

The landing page does not describe the account-recovery procedure; that is the relevant gap for @concepts/account-recovery-deanonymization.md — Advanced Protection hardens *login* but the recovery path (phone, backup identity, physical custody of keys) remains the alternate entry that a determined attacker targets.

## Snippets

> "Advanced Protection requires you to use a passkey or a security key to verify your identity. … unauthorized users won't be able to sign in without them, even if they know your username and password."

> "Google's Advanced Protection practically eliminates credential theft." — campaign CISO testimonial
[Source: https://landing.google.com/advancedprotection/ (retrieved 2026-08-12)]
