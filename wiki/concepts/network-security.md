---
title: Network Security + Firewall + Wireless + IoT/OT
type: concept
tags: [network, firewall, wireless, iot, ot]
keywords: [firewall, network security, wireless, wifi, iot, ot, ics]
related:
  - concepts/red-team-operations.md
  - entities/tools/nmap.md
  - sources/fundamentos-de-firewall.md
  - sources/introducao-a-network-security-1-0.md
  - sources/introducao-a-network-security-e-firewall.md
  - sources/offensive-security-wireless-fundamentals.md
  - sources/offensive-security-wireless.md
  - sources/hardware-hacking-introduction-overview.md
  - sources/pentest-iot-and-ot-overview.md
  - entities/people/joas-a-santos.md
  - concepts/zero-trust.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/red-team-operations.md
- @entities/tools/nmap.md
- @sources/fundamentos-de-firewall.md
- @sources/introducao-a-network-security-1-0.md
- @sources/introducao-a-network-security-e-firewall.md
- @sources/offensive-security-wireless-fundamentals.md
- @sources/offensive-security-wireless.md
- @sources/hardware-hacking-introduction-overview.md
- @sources/pentest-iot-and-ot-overview.md
- @entities/people/joas-a-santos.md
- @concepts/zero-trust.md

## Raw Concept

Eight corpus PDFs anchor.

## Narrative

Network security = traditional network-layer + perimeter topics (firewalls, IDS/IPS, segmentation, VLANs, NAC) plus the wireless + IoT + OT extensions. Wireless: WPA2 attacks (PMKID, handshake capture + offline crack with hashcat), WPA3 (Dragonblood), Evil Twin / captive-portal phishing. IoT: firmware extraction (binwalk), hardware interfaces (UART, JTAG, SPI dumps via Bus Pirate / Saleae), default credential mining. OT/ICS: Modbus, PROFINET, DNP3 protocol attacks — context-specific because of real-world safety implications. See @concepts/red-team-operations.md.
