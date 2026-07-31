---
title: Optimistic Verifiable Claims — confidential G-code bidding (arXiv:2607.25517)
type: source
tags: [paper, blockchain, smart-contracts, IP, manufacturing, G-code, optimistic-verification]
keywords: [OVC, Optimistic Verifiable Claim, Solidity, Arbitrum, opBNB, confidential bidding, Arrow paradox]
related: []
maturity: draft
created: 2026-07-29
updated: 2026-07-31
cross-wiki-source: @3d-printing-wiki/sources/2026-corn-optimistic-verifiable-claims.md
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

# Optimistic Verifiable Claims — confidential G-code bidding (arXiv:2607.25517)

## Relations

- @3d-printing-wiki/sources/2026-corn-optimistic-verifiable-claims.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from 3D-printing ingest pass 28 (2026-07-29). Blockchain / smart-contract lane: optimistic adjudication of claims about concealed manufacturing artifacts (G-code).

## Narrative

**OVC** (Corn, Rožman, Podržaj — Ljubljana ME) lets a Consumer publish a verifiable claim about concealed G-code (e.g. filament consumption) so Providers can bid without seeing the design. Challenge → deterministic on-chain predicates (Access / Identity / Conformance / Feature). Honest path keeps the artifact private.

**Security angle for this wiki:** optimistic confidentiality + L2 cost bounds for large-artifact on-chain verification; not a substitute for OT physical attestation (contrast Firewall3D on `@3d-printing-wiki`). Ethereum impractical at industrial G-code sizes; Arbitrum/opBNB workable. Phase-0: **REFERENCE**.

Primary write-up + Phase-0 live on `@3d-printing-wiki/sources/2026-corn-optimistic-verifiable-claims.md`. Code: https://github.com/fsprojekti/optimistic-verifiable-claims (MIT).

## Snippets

> "OVC makes confidential, claim-based bidding economically feasible on Arbitrum and opBNB, but not on Ethereum at industrial scale."
[Source: arXiv:2607.25517v1 abstract]
