---
title: Tails — MAC address anonymization (project docs)
type: source
tags: [source, tails, opsec, anonymity, mac-randomization]
keywords: [Tails, MAC anonymization, OUI, IMSI, IMEI, local network]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Tails docs; Tails itself is an OS, not a wiki clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md
- @concepts/anonymity-networks.md — Tails is the Tor+amnesic live OS counterpart

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MAC address anonymization (user + design docs) |
| Publisher | Tails Project |
| URLs | https://tails.net/doc/first_steps/welcome_screen/mac_spoofing/index.en.html · https://tails.net/contribute/design/MAC_address/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Tails enables MAC anonymization **by default** for the session. User doc: MAC identifies the device on the **local network**, not on the Internet; IP identifies location on the Internet. Disable when allowlists / public kiosk machines / driver failure would break connectivity. Cellular still reveals IMSI + IMEI. Captive portals may send MAC to auth servers. [CONFIRMED user doc]

Design doc: keep OUI (first 3 bytes), randomize last 3; delay bringing NICs up until Welcome Screen decision; fail-closed (disable NIC) if spoof fails. Threat model includes “looking like a spoofed MAC is itself suspicious.” [CONFIRMED design doc]

OPSEC steal: this is the **right shape** of a control (default-on, fail-closed, documented when to disable) — still only one layer.

## Snippets

> "While your IP address identifies where you are on the Internet, your MAC address identifies which device you are using on the local network. MAC addresses are only useful on the local network and are not sent over the Internet."
[Source: https://tails.net/doc/first_steps/welcome_screen/mac_spoofing/index.en.html (retrieved 2026-08-12)]

> "When using mobile phone connectivity, such as 3G or GSM, the identifier of your SIM card (IMSI) and the serial number of your phone (IMEI) are always revealed to the mobile phone operator."
[Source: same]
