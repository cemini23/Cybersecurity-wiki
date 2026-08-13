---
title: Sigstore overview (docs.sigstore.dev)
type: source
tags: [source, supply-chain, sigstore, keyless-signing, vendor-doc]
keywords: [Sigstore, Cosign, Fulcio, Rekor, OIDC, keyless signing, transparency log, ephemeral keys, SBOM, software provenance]
related:
  - concepts/product-build-integrity-slsa-sigstore.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Sigstore docs; no clone (public-good service)"
wire_status: wont_wire
---

## Relations

- @concepts/product-build-integrity-slsa-sigstore.md — the build-integrity concept page

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sigstore overview |
| Publisher | Sigstore (docs.sigstore.dev) |
| URL | https://docs.sigstore.dev/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Sigstore is an OpenSSF / Linux Foundation framework for signing and verifying software artifacts (release files, container images, binaries, SBOMs). Its model is **identity-based keyless signing**: Cosign generates an ephemeral keypair and sends a CSR to Fulcio with an OIDC identity token; Fulcio verifies the token and issues a short-lived certificate binding identity + public key; the private key is discarded after a single signing. Rekor is the tamper-resistant append-only transparency log where artifact digest, signature, and certificate are persisted. Verification: check the signature with the cert's public key → confirm the identity matches an expected identity → verify the cert chain to Sigstore's root of trust → prove Rekor inclusion. [CONFIRMED docs.sigstore.dev]

The shift: signing by identity (who built/signed it) instead of a manually-managed long-lived key.

## Snippets

> "Signatures are generated with ephemeral signing keys so there's no need to manage keys."

> "Signing events are recorded in a tamper-resistant public log so software developers can audit signing events."

> "You don't have to manage signing keys, and Sigstore services never obtain your private key."
[Source: https://docs.sigstore.dev/ (retrieved 2026-08-12)]
