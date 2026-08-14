---
title: "E2EE consumer cloud — threat model, recovery, share exposure (ente pattern)"
type: concept
tags: [concept, e2ee, cloud, threat-model, privacy, recovery, share, k281]
keywords: [E2EE, end-to-end encryption, zero-knowledge, recovery key, share link, Ente, family plan, account recovery, server-side vs client-side, Atto]
related:
  - entities/tools/ente.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/anonymity-networks.md
  - concepts/endpoint-encryption-deniable-storage.md
  - concepts/account-recovery-deanonymization.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
wire_status: policy_wired
wire_target: "Atto brief is the wire — ~/Projects/atto/briefs/2026-08-14_ente-e2ee-cloud-steal.md (K281)"
---

## Relations

- @entities/tools/ente.md — the reference product (AGPL, no clone)
- @concepts/hardware-id-masking-opsec.md — recovery-key / device-bound identity surface
- @concepts/anonymity-networks.md — zero-knowledge trust vs provider trust
- @concepts/endpoint-encryption-deniable-storage.md — E2EE cloud ≠ deniable storage
- @concepts/account-recovery-deanonymization.md — recovery flows are the classic deanonymization/account-takeover surface

## Raw Concept

E2EE consumer clouds (ente Photos/Auth/Locker, Proton, Tresorit) let users store data without trusting the provider: encryption keys never leave the client, so the server holds ciphertext only. The threat-model question for any builder (or auditor) is where the **trust boundaries and failure surfaces** actually sit — recovery, share links, metadata, and key management — because "zero-knowledge" describes the server, not the whole system.

## Narrative

### What E2EE actually guarantees (and doesn't)

- **Does guarantee:** server + its operators cannot read plaintext content; a server breach leaks ciphertext + metadata, not content. This is the core claim.
- **Does not guarantee:** client-side compromise (malware, physical device theft with unlocked keys), weak passphrase, recovery-key handling, share-link recipients, and metadata (file sizes, timing, graph) are still surfaces. **Zero-knowledge is about the server, not the system.**
- **Not deniable storage** — E2EE ≠ plausible deniability; see `endpoint-encryption-deniable-storage`. Server holds ciphertext that is provably yours.

### The five surfaces to audit (any E2EE product)

1. **Recovery** — how does a user get back in after losing the device/passphrase? Recovery keys, trusted-device flows, or KBA are the account-recovery + deanonymization surface (`account-recovery-deanonymization`). A recovery key is a bearer secret — how it's stored/protected determines whether "zero-knowledge" holds under coercion/theft.
2. **Share links** — shared albums/folders typically lower the trust bar for recipients. Are links bearer tokens? TTLs? Can they be revoked? Share exposure is the most common real-world leak path.
3. **Metadata** — encryption hides content, not existence. File count, sizes, access times, sharing graph are server-visible (or inferable).
4. **Key management** — client-generated keys, whether the server can swap in a malicious client (server-supplied app binary), and whether forward secrecy across devices exists.
5. **Audit + self-host** — an audited, self-hostable server (ente: Cure53/Symbolic/Fallible audits; AGPL self-host) is materially stronger than a closed provider for the "don't trust the service provider" claim.

### Atto fit (the K281 wire)

Atto (family-genealogy vault, local-first, redacted share M11, audit M13) is *not* building a photos cloud — but ente's product surfaces map onto Atto's vault/share milestones:

| Atto surface | ente reference pattern |
|---|---|
| M2 local vault / secrets | ente Locker (docs/credentials vault); recovery-key UX |
| M11 redacted family share | ente share links + access control (invite → login → publish ordering) |
| M13 vault + audit | ente's Cure53/Symbolic audits + self-host option as trust story |

The **recovery-key design** (bearer secret, offline storage, multi-device re-registration) and **share-gating** (email-allowlist invite, fail-closed publish) are the two most stealable UX/threat-model patterns. **AGPL → do not vendor ente code.** Steal threat-model + product fit only.

## Snippets

> [E2EE] store your data in the cloud without needing to trust the service provider. [Source: github.com/ente-io/ente README]

> Face detection. Semantic search. Private sharing. Collaborative albums. Family plans. … all while being fully end-to-end encrypted. [Source: README — Ente Photos]
