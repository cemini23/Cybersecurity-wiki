---
title: "Association-based privacy attacks in wireless protocols — formal modeling and mitigation (arXiv 2608.11337)"
type: source
tags: [source, arxiv, wireless, bluetooth, wifi-p2p, privacy, unlinkability, formal-verification, tamarin]
keywords: [2608.11337, association inference, AInf, allowlist, PNL, BAT attack, Tamarin, distance bounding, condition-oblivious responses, replay resistance, Wi-Fi P2P, BLE reconnection]
related:
  - concepts/association-inference-attack-wireless.md
  - concepts/wireless-pentest.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/responsible-disclosure.md
maturity: draft
read_status: read
created: 2026-08-13
updated: 2026-08-13
phase_0_verdict: "REFERENCE 2026-08-13 — Tamarin models + C++ code behind anonymized review artifact (pcloud), no public GitHub/SPDX. Formal-model + mitigation steal-from for authorized wireless lab; vendor-acknowledged. K275 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K275)"
---

**Briefs:** `briefs/2026-08-13_k275-association-privacy-wireless.md`

## Relations

- @concepts/association-inference-attack-wireless.md
- @concepts/wireless-pentest.md — BLE / Wi-Fi Direct (P2P) are pentest surfaces; the privacy attack here is the *passive+active tracking* side
- @concepts/hardware-id-masking-opsec.md — MAC randomization ≠ unlinkability; allowlist side channels defeat it
- @concepts/responsible-disclosure.md — Wi-Fi Alliance + Bluetooth SIG acknowledged findings and plan stakeholder publication

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Association-based Privacy Attacks in Wireless Protocols: Formal Modeling and Mitigation |
| Authors | Mohit Kumar Jangid (IIT Jodhpur); Felix Engelmann, Zhiqiang Lin (Ohio State University) |
| arXiv | 2608.11337 (cs.CR, v1 11 Aug 2026) |
| Code | Tamarin models + C++ prototypes behind anonymized pcloud review artifact (no public GitHub/SPDX at retrieval 2026-08-13) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.11337-association-based-privacy-attacks-in-wireless-pr.pdf` |
| Retrieved | 2026-08-13 |
| Read status | read (14 pp, full text extracted) |

## Narrative

This paper formalizes **Association Inference (AInf)** attacks: an adversary uses replay/relay against wireless protocols that keep an **allowlist** (Preferred Network List in Bluetooth, persistent group config in Wi-Fi P2P) to infer whether a prospective device belongs to a target user's privacy-sensitive group — revealing household membership and, via location, tracking.

**Root cause** (formalized in a process calculus with `insert`/`lookup` on per-reader databases): allowlists + conditional checks over shared persistent data emit **distinguishable responses** (ok vs err, silent-discard, plaintext status, plaintext replay counter echoes). Four infrastructure requirements: local shared-data scope (privacy-sensitive), persistent data across sessions, protocol responses dependent on that data (privacy-critical conditions), and replay/relay reachability. The key formal result: a tag authenticating to two readers with different allowlists produces frames `{w1→ok, w3→err}` vs `{w1→ok, w3→ok}` that are **not statically equivalent** — an adversary distinguishing the two settings can link tag interactions.

**Case studies** (Tamarin 1.6.1, 1,137 LoC, ~20 lemmas, all proofs < 3 min):
- **Bluetooth reconnection** — RPA resolution via IRK allowlist. Vulnerabilities at advertisement (replay of RPA, WA+FO failure) plus **newly discovered** plaintext `START_ENC_REQ` at step 4 and silent-discard at step 6 (FO violations) that expose LTK-mismatch outcomes.
- **Wi-Fi P2P persistent group formation** — netID/PSK allowlist. Newly discovered FO violations via plaintext replay-counter `rc` echoes and nonce `n_A` equality across messages, plus silent-discard.

**Mitigation** (two-staged: prevention/trapping + detection): revised 3-way handshake that derives the session key from the first messages (so everything from round 2 on is ephemerally encrypted + integrity-protected), **condition-oblivious responses** (random same-size values on failure — no distinguishable context), **replay resistance** via fresh-session-key messages, and a **distance-bounding (DiB)** check immediately after the handshake to deterministically detect relay. Keeps fast reconnection (median 11–65 ms without DiB; 47.8–123.3 ms with 8–16 DiB rounds), no synchronization required.

**Disclosure:** both Wi-Fi Alliance and Bluetooth SIG acknowledged the findings and agreed with the proposed solutions; both plan to publish the reports to stakeholders. `[CONFIRMED]` — stated by the authors, not independently verified.

**Pentest/privacy relevance:** this is the tracking-privacy side of wireless tradecraft — the same BLE/Wi-Fi Direct surfaces a pentester enumerates are also tracking vectors. The formalization (allowlist side channels) and the mitigation pattern (oblivious responses + DiB) transfer to any protocol using shared-key allowlists for reconnection.

## Snippets

> The presence of allowlists in wireless protocols and conditional checks over this data are the root causes enabling an adversary to deduce user association in privacy-sensitive groups. [Source: arXiv:2608.11337 abstract]

> Since the outputs of cryptographic hash functions and nonces are indistinguishable... However, the different remaining reply messages break the static equivalence: `{w1→ok, w3→err} ≁ {w1→ok, w3→ok}`. An adversary can exploit this discrepancy to distinguish the setting they are in and use it to link tag interactions. [Source: arXiv:2608.11337 p.6]

> Encouragingly, both Wi-Fi Alliance and Bluetooth SIG have acknowledged our findings and agreed with our proposed solutions. Furthermore, both interest groups plan to publish our reports to stakeholders. [Source: arXiv:2608.11337 p.1]

## Dead Ends

- Authors explicitly exclude compromised devices, secret-key leakage, and timing side channels — the threat model is Dolev-Yao with replay/relay only; distance-bounding attack classes (Mafia Fraud, Terrorist Fraud, etc.) are out of scope.
- Condition-oblivious responses cost energy/performance (they replace efficient silent-discard); the paper suggests a privacy/performance toggle for high-privacy users. Formal modeling is not fully automated — significant manual Tamarin model building/debugging.
