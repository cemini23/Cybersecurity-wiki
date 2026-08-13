---
title: VeraCrypt hidden volumes (veracrypt.io official docs)
type: source
tags: [source, encryption, deniable-storage, veracrypt, vendor-doc]
keywords: [VeraCrypt, hidden volume, outer volume, plausible deniability, hidden header, coerced password, free space, random data]
related:
  - concepts/endpoint-encryption-deniable-storage.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party hidden-volume *architecture* doc; no procedures ingested"
wire_status: wont_wire
---

## Relations

- @concepts/endpoint-encryption-deniable-storage.md — the deniable-storage class page consuming this architecture

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Hidden Volume |
| Publisher | VeraCrypt (veracrypt.io) |
| URL | https://veracrypt.io/en/Hidden%20Volume.html |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party documentation of the hidden-volume architecture. A hidden volume is created **within another VeraCrypt volume** (in its free space); the outer volume is a decoy populated with "sensitive-looking files that you actually do NOT want to hide." Because "free space on any VeraCrypt volume is always filled with random data when the volume is created," a hidden header "cannot be identified, as they appear to consist entirely of random data." The passphrase selects which volume mounts: outer password → outer volume; hidden password → hidden volume. VeraCrypt first tries the standard header, then attempts hidden-header decryption at bytes 65536–131071. [CONFIRMED veracrypt.io]

Deniability is contingent on usage rules: the two passwords "must be substantially different"; free-space randomness assumes Quick Format / Dynamic are disabled and no in-place-encrypted filesystem; the wizard scans the outer-volume cluster bitmap to size the hidden volume safely. Ingested as **architecture + limits**, not a creation procedure (see the class page's floor).

## Snippets

> "Using a so-called hidden volume allows you to solve such situations without revealing the password to your volume."

> "It should be impossible to prove whether there is a hidden volume within it or not."
[Source: https://veracrypt.io/en/Hidden%20Volume.html (retrieved 2026-08-12)]
