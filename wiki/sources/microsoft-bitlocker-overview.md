---
title: BitLocker Drive Encryption overview (Microsoft Learn)
type: source
tags: [source, encryption, bitlocker, windows, vendor-doc]
keywords: [BitLocker, full-disk encryption, Device Encryption, TPM, recovery key, AES, BitLocker To Go, self-encrypting drive]
related:
  - concepts/endpoint-encryption-deniable-storage.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party BitLocker overview"
wire_status: wont_wire
---

## Relations

- @concepts/endpoint-encryption-deniable-storage.md — the FDE class on Windows

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BitLocker Drive Encryption overview |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

BitLocker is Windows full-volume encryption addressing "data theft or exposure from lost, stolen, or inappropriately decommissioned devices" — the lost-disk threat model, not the running-OS one. AES (XTS/CBC, 128/256-bit). Best with a TPM, which "works with BitLocker to ensure the device hasn't been tampered with while the system is offline"; TPM + PIN/startup key gives pre-boot multifactor. On devices without a TPM, a startup key is mandatory (password is "discouraged and disabled by default, as it's subject to brute-force attacks"). The recovery password is saved to the Microsoft account (OOBE), OneDrive, Azure, or exported. Device Encryption is the simplified always-on variant on Windows 10/11. [CONFIRMED Microsoft Learn]

Key architecture point for the class page: default TPM-only unlock is seamless (the device self-unlocks at boot when the boot configuration is unchanged) — a "stolen laptop" protection, not a pre-boot identity gate.

## Snippets

> "BitLocker is a Windows data protection feature that integrates with the operating system and helps address the threats of data theft or exposure from lost, stolen, or inappropriately decommissioned devices."
[Source: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/ (retrieved 2026-08-12)]

> "The TPM works with BitLocker to ensure the device hasn't been tampered with while the system is offline."
[Source: same]
