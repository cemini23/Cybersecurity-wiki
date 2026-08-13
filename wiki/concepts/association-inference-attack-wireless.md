---
title: "Association inference attacks in wireless — allowlist side channels and formal mitigation"
type: concept
tags: [methodology, wireless, privacy, unlinkability, bluetooth, wifi-p2p, formal-verification, tamarin, tracking]
keywords: [association inference, AInf, allowlist, PNL, preferred network list, unlinkability, BAT attack, replay, relay, distance bounding, condition-oblivious response, Tamarin, BLE, Wi-Fi Direct]
related:
  - sources/arxiv-2608-11337-association-privacy-wireless-formal.md
  - concepts/wireless-pentest.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/responsible-disclosure.md
  - sources/vanhoef-asiaccs2016-mac-randomization-not-enough.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K275)"
---

# Association inference attacks in wireless — allowlist side channels and formal mitigation

## Relations

- @sources/arxiv-2608-11337-association-privacy-wireless-formal.md — the source paper
- @concepts/wireless-pentest.md — BLE and Wi-Fi Direct (P2P) are pentest surfaces; AInf is the tracking-privacy read of the same protocol steps
- @concepts/hardware-id-masking-opsec.md — MAC randomization is necessary but not sufficient; allowlist response behavior leaks association even when addresses rotate
- @concepts/responsible-disclosure.md — vendor-acknowledged (Wi-Fi Alliance + Bluetooth SIG) before public release
- @sources/vanhoef-asiaccs2016-mac-randomization-not-enough.md — prior evidence that MAC-layer randomization alone fails unlinkability; AInf generalizes the mechanism to allowlists

## Raw Concept

The question this page answers: why do wireless reconnection protocols that use shared-key **allowlists** (PNL in Bluetooth, persistent group config in Wi-Fi P2P) leak whether two devices belong to the same user, and how do you fix it formally and in practice? Answer pattern: allowlist condition checks emit distinguishable responses; replay/relay lets an adversary probe those responses; the fix is condition-oblivious responses + replay resistance + distance bounding, verified symbolically with Tamarin.

## Narrative

### The attack primitive

An adversary with a static location for a target's device records wireless communication (replay) or establishes a relay link between a target device and an arbitrary prospective device. When the protocol reaches a **privacy-critical condition** (IRK resolution, MIC verification, PSK group join), the *response* — ok vs err, plaintext status, silent-discard, plaintext replay-counter echo — reveals whether the prospective device shares the target's allowlist. A positive result confirms the prospective device belongs to the target user's household/group; the adversary learns the target user is present at the prospective device's location.

Four necessary conditions for the attack: (1) **local shared-data scope** — the allowlist group is privacy-sensitive (household/IoT pair), so association reduces to an individual; (2) **persistent shared data** across sessions (that's the point of a PNL); (3) **privacy-critical conditions** — protocol responses depend on allowlist membership; (4) **replay/relay reachability** — the medium is wireless, so probing needs no physical access.

### Why randomization is not enough

Bluetooth's RPA (randomized hashed IRK addresses) and Wi-Fi MAC randomization both fail against this attack class because the *allowlist response* is the side channel, not the address. The paper builds on the BAT Attack (allowlist-based Bluetooth tracking) and shows the mechanism generalizes: the formal model finds new checkpoints deep in the reconnection sequence (plaintext `START_ENC_REQ`, plaintext replay-counter echoes, silent-discard) that previous work missed.

### The formalization

The paper extends the Hirschi/Baelde unlinkability building blocks — **Well-Authentication (WA), Frame Opacity (FO), No-Desynchronization (ND)** — with a process-algebra `insert_r/lookup_r` extension for per-reader allowlists. The core result is that two readers with different allowlists produce frames that are not statically equivalent (`ok,err` vs `ok,ok`), which is exactly the distinguishability an adversary exploits. Tamarin models confirm the proposed design satisfies WA, FO, ND, plus Replay-Resistance (RR) and Distance-Bounding (DiB).

### The mitigation pattern (transferable)

1. **Condition-oblivious responses** — on condition failure, respond with random values of the same size/count as success responses. No distinguishable context during the handshake.
2. **Replay resistance without counters** — derive a fresh session key early (from the first messages of a revised 3-way handshake), so from round 2 onward all messages are ephemerally encrypted + integrity-protected; any replay is deterministically detected. Avoids counter-based ND violations.
3. **Distance bounding after the handshake** — timed challenge-response (Hancke–Kuhn style) detects relay; performed immediately after key establishment so setup is shared and fast reconnection is preserved.

This combination is what both Wi-Fi Alliance and Bluetooth SIG acknowledged and plan to take to stakeholders. `[CONFIRMED]` (author-stated; not independently verified).

### Authorized-use framing

AInf is a **tracking attack** on real people's devices. Documented here for: (a) understanding why MAC randomization / PNL defenses fail (defensive privacy engineering), (b) authorized wireless lab evaluation of owned devices, and (c) product pentest where BLE/Wi-Fi Direct reconnection surfaces are in scope. Do not use against third-party devices; no LIVE tracking outside authorized lab/engagement scope (K275).

## Snippets

> An adversary with the ability to relay or replay packets between a distant device associated with a targeted user's privacy-sensitive group, whether it be a household or paired phone, can disclose the user's association and even pinpoint their location. [Source: arXiv:2608.11337 p.1]

> We employ a combination of condition oblivious responses, replay-resistant techniques, and distance bounding checks to propose design changes mitigating AInf attacks. [Source: arXiv:2608.11337 abstract]

## Dead Ends

- The proposed design's overhead is DiB-bound; 8–16 challenge rounds add ~30–80 ms reconnection latency. On hardware without timing precision (commodity Wi-Fi/BT adapters), DiB can only be simulated — real deployment needs UWB-class or dedicated radio timing.
- The formal proof of the *absence* of AInf under the new design is explicitly left as future work; the paper proves the properties hold on the proposed models, not that the class is closed.
