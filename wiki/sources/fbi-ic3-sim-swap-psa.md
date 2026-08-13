---
title: FBI IC3 PSA — Criminals Increasing SIM Swap Schemes
type: source
tags: [source, fbi, ic3, sim-swap, account-takeover, gov-publication]
keywords: [SIM swap, port-out, IC3, I-020822-PSA, SMS 2FA, account recovery, social engineering, insider threat]
related:
  - concepts/account-recovery-deanonymization.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party US government PSA"
wire_status: wont_wire
---

## Relations

- @concepts/account-recovery-deanonymization.md — SIM swap as the canonical recovery-takeover vector

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Criminals Increasing SIM Swap Schemes to Steal Millions of Dollars from US Public |
| Publisher | FBI Internet Crime Complaint Center (IC3) |
| Alert | I-020822-PSA, 2022-02-08 |
| URL | https://www.ic3.gov/PSA/2022/PSA220208 |
| Retrieved | 2026-08-12 |
| Location | gov HTML (no PDF archive; PDF mirror 404'd on fetch) |

## Narrative

First-party FBI PSA documenting SIM-swap scale, mechanics, and guidance. Scale: IC3 received **320 complaints / ~$12M** adjusted losses Jan 2018–Dec 2020, then **1,611 complaints / >$68M** in 2021. [CONFIRMED, retrieved 2026-08-12]

Mechanics: criminals target mobile carriers via **social engineering** (impersonating the victim), **insider threat** (paying off a carrier employee), or **phishing** (deceiving employees into downloading malware against carrier systems). After the swap, "the victim's calls, texts, and other data are diverted to the criminal's device," enabling "Forgot Password" / "Account Recovery" requests and interception of SMS-based two-factor codes. [CONFIRMED, retrieved 2026-08-12]

Individual guidance (class-level, not how-to): don't advertise financial/crypto holdings; don't hand over passwords/PINs to unsolicited callers; verify by dialing the carrier's official number; avoid posting phone/address/PII; use unique passwords; be alert to changes in SMS connectivity; use strong MFA (biometrics, physical tokens, authenticator apps); don't store passwords in mobile apps for one-tap login. Carrier guidance: educate staff on SIM swap; inspect emails for lookalike sender addresses; verify customer credentials before moving a number; authenticate third-party-retailer calls. Victim steps: contact the carrier immediately to regain the number, change passwords, alert financial institutions, report to local LE/FBI and IC3. [CONFIRMED, retrieved 2026-08-12]

## Snippets

> "Once the SIM is swapped, the victim's calls, texts, and other data are diverted to the criminal's device. This access allows criminals to send 'Forgot Password' or 'Account Recovery' requests to the victim's email and other online accounts associated with the victim's mobile telephone number."

> "Use strong multi-factor authentication methods such as biometrics, physical security tokens, or standalone authentication applications to access online accounts."
[Source: https://www.ic3.gov/PSA/2022/PSA220208 (retrieved 2026-08-12)]
