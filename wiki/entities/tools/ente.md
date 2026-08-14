---
title: "ente — open-source E2EE cloud (photos / auth / locker)"
type: entity
tags: [tool, e2ee, cloud, encryption, privacy, reference, k281]
keywords: [ente, E2EE, end-to-end encryption, Ente Photos, Ente Auth, Ente Locker, zero-knowledge, recovery, share links, Cure53, self-host, AGPL]
related:
  - concepts/e2ee-consumer-cloud-threat-model.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/anonymity-networks.md
  - concepts/endpoint-encryption-deniable-storage.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "NO clone 2026-08-14 — github.com/ente-io/ente AGPL-3.0, ~704MB (>500MB cap). Atto steal-from (threat-model + UX); do not vendor AGPL into Atto. Cyber entity page + Atto brief K281."
wire_status: policy_wired
wire_target: "Atto brief is the wire — briefs/2026-08-14_ente-e2ee-cloud-steal.md (K281); cyber policy: E2EE cloud is steal-from not adopt"
---

**Briefs:** `~/Projects/atto/briefs/2026-08-14_ente-e2ee-cloud-steal.md` (primary) · `briefs/2026-08-14_k281-ente-e2ee-cloud.md`

## Relations

- @concepts/e2ee-consumer-cloud-threat-model.md — the E2EE cloud threat-model + Atto-fit synthesis
- @concepts/hardware-id-masking-opsec.md — device-recovery identity surface (recovery keys, hardware-bound factors)
- @concepts/anonymity-networks.md — zero-knowledge trust model is the anonymity-flavored alternative to provider trust
- @concepts/endpoint-encryption-deniable-storage.md — E2EE cloud ≠ deniable storage (same FDE lesson: server-side encryption ≠ client-side deniability)

## Raw Concept

ente is a fully open-source, **end-to-end encrypted cloud** platform. Three products on one monorepo: **Ente Photos** (Apple/Google Photos alternative — 3× replication, face detection, semantic search, private sharing, collaborative albums, family plans), **Ente Auth** (free 2FA authenticator, Authy alternative), **Ente Locker** (documents/credentials vault). AGPL-3.0 monorepo with client apps (iOS/Android/F-Droid/Web/Linux/macOS/Windows) + server. Cryptography externally audited by Cure53, Symbolic Software, Fallible. 10GB free; self-hostable.

## Narrative

**Why Atto cares (operator-flagged).** Atto is a family-genealogy vault with local vault (M2), redacted share (M11), audit (M13). ente is the closest *product-shaped* reference for an **E2EE family archive + share** that Atto is not: photos/files, collaborative albums, family plans, recovery keys, share links, zero-knowledge server. The steal is **product + threat-model fit**, not code:

- **AGPL-3.0 → do not vendor.** Copyleft contaminates Atto (a commercial product). Reference only.
- **No clone** — ~704MB exceeds the 500MB soft-cap.
- Atto's differentiators vs ente: genealogy-data model (truth.ged), redacted/audited share (SSN last-4 asserts), local-first vault — ente shows what the *consumer E2EE cloud* UX should feel like (recovery keys, family plans, share links, cross-platform), which informs Atto's M2/M11/M13 direction.

**Cyber awareness (not a pentest kit).** ente is a legitimate E2EE provider; documenting it is threat-model + product-fit, not an attack kit. Relevant cyber angle: how E2EE consumer clouds handle **recovery** (the identity/account-recovery surface), **share-link exposure**, and **zero-knowledge claims** — worth auditing in any owned-lab engagement involving E2EE products.

**Phase-0: NO clone** (AGPL, 704MB > cap). Atto brief is the K281 wire.

## Snippets

> Ente is a service that provides a fully open source, end-to-end encrypted platform for you to store your data in the cloud without needing to trust the service provider. [Source: github.com/ente-io/ente README]

> Our source code and cryptography have been externally audited by Cure53, Symbolic Software and Fallible. [Source: README]

> Ente Photos is a paid service, but we offer 10GB of free storage. You can also clone this repository and choose to self-host. [Source: README]
