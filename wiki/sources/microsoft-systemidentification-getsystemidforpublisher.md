---
title: Windows SystemIdentification.GetSystemIdForPublisher (Microsoft Learn)
type: source
tags: [source, windows, hardware-id, tpm, privacy, vendor-doc]
keywords: [SystemIdentification, GetSystemIdForPublisher, TPM, UEFI, Autopilot hardware hash]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/windows-pentest.md
  - concepts/system-hardening.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party API docs"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md — TPM/UEFI-backed IDs persist across clean install
- @concepts/windows-pentest.md — Windows identifier surface
- @concepts/system-hardening.md — know what the OS still discloses after reimage

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SystemIdentification.GetSystemIdForPublisher Method |
| Publisher | Microsoft Learn (UWP / WinRT) |
| URL | https://learn.microsoft.com/en-us/uwp/api/windows.system.profile.systemidentification.getsystemidforpublisher |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party Windows API for a **publisher-scoped** system ID. Documented properties: unique per system; same publisher → same ID for all users/apps; persists across restarts, reinstalls, **clean installs**, and most hardware changes — **when** backed by TPM or UEFI. Fallback is registry: then a clean install yields a new ID. Callers must read `SystemIdentificationInfo.Source`. [CONFIRMED Learn, retrieved 2026-08-12]

Related but distinct: Windows Autopilot **hardware hash** is an enterprise device-registration blob (serial + hardware hash CSV), not this API. [CONFIRMED Learn Autopilot docs]

OPSEC steal: “I reinstalled Windows” is not unlinkability if TPM/UEFI identification is on. Inventory `Source` on owned boxes. This page does not document how to forge TPM/UEFI identities.

## Snippets

> "The method will first attempt to use the Trusted Platform Module (TPM), if present, to get an ID. If a TPM is not present, the method will try to get an ID from the Unified Extensible Firmware Interface (UEFI). If neither of these sources is available, this method will return an ID that is backed by the Windows registry."
[Source: https://learn.microsoft.com/en-us/uwp/api/windows.system.profile.systemidentification.getsystemidforpublisher (retrieved 2026-08-12)]
