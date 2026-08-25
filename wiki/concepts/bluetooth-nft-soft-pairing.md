---
title: "Bluetooth NFT soft pairing — pairing ≠ authorization (K305)"
type: concept
tags: [concept, bluetooth, wireless, access-control, k305, lab-only]
keywords: [NFT soft pairing, NFBT, NFDT, Bluetooth pairing, decouple pairing from authorization, on-chain authorization, challenge-response, ERC1155]
related:
  - sources/arxiv-2608-22754-bluetooth-nft-soft-pairing.md
  - concepts/wireless-pentest.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K305)"
---

## Relations

- @sources/arxiv-2608-22754-bluetooth-nft-soft-pairing.md
- @concepts/wireless-pentest.md — BT service-auth surface inside wireless pentest scope

## Raw Concept

Question this page answers: **is a paired Bluetooth device an authorized device, and how do designs that separate pairing from authorization change how you test that boundary?**

## Narrative

Conventional Bluetooth conflates two things: **pairing** (establishing a long-term Link Key / trust relationship) and **service authorization** (whether the peer may use a service). Once paired, a peer is usually treated as authorized until manually unpaired — and the pairing ceremony itself is attackable (downgrade-to-Just Works, method confusion, pairing confusion, Stealtooth). **NFT soft pairing** (K305, 2608.22754) is an application-layer design that separates them: Bluetooth layer = connectivity, blockchain layer = trusted state, application layer = authorization logic. **NFBT** (user credential) ↔ **NFDT** (device identity) form a bidirectional on-chain binding; access requires a challenge-response signature proving NFBT ownership plus on-chain state verification. The result is *revocable, verifiable, fine-grained* authorization independent of pairing status — with ERC1155 keeping mint gas flat (~93.4% cheaper than ERC721-style per-credential minting in batch).

**What this changes for authorized wireless pentests (the steal):**
1. **Pairing status is not authorization.** When scoping a BT engagement (authorized lab / owned devices only), enumerate the *service-authorization decision point*, not just pairing state: is there a second credential, a verifier, an on-chain/remote check, or a local ACL? That decision point is the interesting attack surface.
2. **Link-key persistence is a stale-trust risk**: devices that stay "authorized" after the pairing relationship should have ended are a classic finding — NFT-style revocation is one fix family, but any revocable auth layer needs its revocation path tested (is revocation actually enforced at the service layer?).
3. **Verifiable-auth schemes move trust off-device**: challenge-response + verifier state means the device's *local* trust store is no longer the whole story — test the verifier and the binding, not just the radio (pairs `wireless-pentest`, blockchain-side surfaces excluded unless in scope).
4. **No LIVE pairing manipulation / unauthorized RF** — authorized-lab and owned-device testing only; the paper's prototype is REFERENCE (no code repo at hunt 2026-08-25).

## Snippets

> Access is no longer implicitly granted by pairing status but explicitly governed by on-chain NFT soft pairing state and cryptographic verification. [Source: arXiv 2608.22754, conclusion]
