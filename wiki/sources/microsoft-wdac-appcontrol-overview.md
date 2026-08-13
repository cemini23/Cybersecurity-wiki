---
title: App Control for Business and AppLocker overview (Microsoft Learn)
type: source
tags: [source, windows, hardening, application-control, vendor-doc]
keywords: [WDAC, App Control for Business, AppLocker, code integrity policy, managed installer, Intelligent Security Graph, Device Guard]
related:
  - concepts/system-hardening.md
  - concepts/windows-pentest.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/microsoft-elam.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party app-control doc; Learn ms.date 2026-03-29"
wire_status: wont_wire
---

## Relations

- @concepts/system-hardening.md — application control is the allow-list core of client hardening
- @concepts/windows-pentest.md — CI policies constrain kernel/user-mode tradecraft on hardened targets
- @sources/microsoft-hvci-memory-integrity.md — App Control policy can turn HVCI on (even in audit mode)
- @sources/microsoft-elam.md — adjacent trust-stack layer (boot-order gate)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | App Control and AppLocker Overview |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

**App Control for Business** (formerly WDAC / "configurable code integrity", originally Device Guard) controls which drivers and applications may run, under the MSRC security-servicing criteria. Rules key off signing-certificate attributes, binary metadata (original filename/version/hash), Intelligent Security Graph reputation, managed-installer identity, file path (1903+), or the launching process. Deployed via MDM/Intune, ConfigMgr, PowerShell, or GPO (GPO limited to single-policy format). **AppLocker** (Windows 7+) is the older, user/group-scoped sibling — "doesn't meet the servicing criteria for being a security feature."

Trust-stack position: WDAC is the *policy* gate — the allow-list that decides what is permitted to run at all, enforced below (and independently of) user-mode decisions. It composes with ELAM (boot order) and HVCI (execution integrity) into the Windows CI stack.

## Snippets

> "App Control was introduced with Windows 10 and allows organizations to control which drivers and applications are allowed to run on their Windows clients. It was designed as a security feature under the servicing criteria, defined by the Microsoft Security Response Center (MSRC)."

> "AppLocker helps to prevent end-users from running unapproved software on their computers but doesn't meet the servicing criteria for being a security feature."

[Source: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview (retrieved 2026-08-12)]
