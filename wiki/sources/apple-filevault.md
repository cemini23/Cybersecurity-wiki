---
title: FileVault (Apple Support)
type: source
tags: [source, encryption, filevault, macos, vendor-doc]
keywords: [FileVault, macOS, full-disk encryption, APFS, recovery key, iCloud recovery, at-rest encryption]
related:
  - concepts/endpoint-encryption-deniable-storage.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party FileVault doc"
wire_status: wont_wire
---

## Relations

- @concepts/endpoint-encryption-deniable-storage.md — the FDE class on macOS

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Protect data on your Mac with FileVault |
| Publisher | Apple Support |
| URL | https://support.apple.com/guide/mac-help/mh11785/mac |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

FileVault is macOS full-disk encryption: it "encrypts the data on the startup disk so that it can't be accessed without your login password or recovery key." It protects the OS from brute-force attacks directly against removed storage media, protects macOS Recovery from non-admin access, and enables a swift secure wipe by discarding cryptographic material. Without login credentials or the recovery key, encrypted APFS volumes remain inaccessible even on another computer. Recovery options: iCloud/Apple Account escrow or a ~24-character recovery key. [CONFIRMED Apple Support]

FileVault is an at-rest (login-gated) control: once the user is logged in, the data is readable by the running session — the FDE class boundary.

## Snippets

> "FileVault encrypts the data on the startup disk so that it can't be accessed without your login password or recovery key."

> "Don't forget your recovery key. If you turn on FileVault and then forget your login password and can't reset it, and you also forget your recovery key, you won't be able to log in, and your files and settings will be lost forever."
[Source: https://support.apple.com/guide/mac-help/mh11785/mac (retrieved 2026-08-12)]
