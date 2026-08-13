---
title: Secure boot (Microsoft Learn, UEFI)
type: source
tags: [source, boot-security, secure-boot, uefi, windows, vendor-doc]
keywords: [Secure Boot, UEFI, PK, KEK, signature database, db, dbx, boot chain, OEM]
related:
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Secure Boot OEM doc"
wire_status: wont_wire
---

## Relations

- @concepts/secure-boot-vs-device-ownership.md — the trust-stack vs ownership concept page

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Secure boot (OEM guidance) |
| Publisher | Microsoft Learn |
| URL | https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Secure Boot is "a security standard developed by members of the PC industry to help make sure that a device boots using only software that is trusted by the Original Equipment Manufacturer (OEM)." On start, firmware verifies the signature of each piece of boot software (Option ROMs, EFI applications, the OS); if valid, control passes to the OS. Key material: signature database (**db**), revoked-signatures database (**dbx**, takes precedence on conflict), Key Enrollment Key (**KEK**, updates db/dbx), and platform key (**PK**, can sign KEK updates or turn off Secure Boot). OEM stores these databases in firmware NV-RAM at manufacturing. Requirements include UEFI 2.3.1, firmware signed RSA-2048/SHA-256, and rollback protection. [CONFIRMED Microsoft Learn]

Note (2026): Microsoft is updating the 2011-era Secure Boot certificates, which begin expiring June 2026 — relevant to long-lived devices.

## Snippets

> "Secure boot is a security standard developed by members of the PC industry to help make sure that a device boots using only software that is trusted by the Original Equipment Manufacturer (OEM)."

> "If an image hash is in both databases, the revoked signatures database (dbx) takes precedent."
[Source: https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot (retrieved 2026-08-12)]
