---
title: Signal — Sealed Sender (Sender Privacy)
type: source
tags: [source, signal, sealed-sender, metadata, e2ee, privacy]
keywords: [sealed sender, sender certificates, delivery tokens, metadata, Signal server, profile key, X25519]
related:
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Signal protocol post"
wire_status: wont_wire
---

## Relations

- @concepts/metadata-traffic-analysis-anonymity.md — sender-hidden-from-service design; destination + timing remain
- @concepts/anonymity-networks.md — metadata-minimization pattern complementary to Tor

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sealed Sender (Signal Protocol Blog) |
| Publisher | Signal Messenger |
| URL | https://signal.org/blog/sealed-sender/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Signal's first-party write-up of sealed sender, a protocol change that removes the sender's identity from the outside of the message envelope so the service no longer learns "who is messaging whom." Two mechanisms replace authenticated send: **sender certificates** ("clients periodically retrieve a short-lived sender certificate from the service attesting to their identity") placed inside the encrypted envelope so the recipient can validate the sender without the service seeing it; and **delivery tokens** — "clients derive a 96-bit delivery token from their profile key and register it with the service," so only contacts/approved users can send sealed messages (an opt-in widens this at greater abuse risk). The envelope is Signal-encrypted, then additionally encrypted with an ephemeral X25519 key + the recipient's identity key, and handed to the service "without authenticating." [CONFIRMED, retrieved 2026-08-12]

What remains visible: the destination — "the service always needs to know where a message should be delivered." And the post explicitly flags that resistance to correlation "via timing attacks and IP addresses are areas of ongoing development," i.e. traffic-confirmation-style metadata is out of scope for sealed sender. [CONFIRMED, retrieved 2026-08-12]

For the wiki: this is the canonical **metadata-minimization** design — the server should not need to know the sender to deliver a message — and the honest enumeration of what a delivery service *must* still know.

## Snippets

> "Clients periodically retrieve a short-lived sender certificate from the service attesting to their identity."

> "Clients derive a 96-bit delivery token from their profile key and register it with the service."

> "The service always needs to know where a message should be delivered."
[Source: https://signal.org/blog/sealed-sender/ (retrieved 2026-08-12)]
