---
title: Network Security + Firewall + Wireless + IoT/OT
type: concept
tags: [network, firewall, wireless, iot, ot]
keywords: [firewall, network security, wireless, wifi, iot, ot, ics]
related:
  - concepts/red-team-operations.md
  - concepts/zero-trust.md
  - entities/people/joas-a-santos.md
  - entities/tools/nmap.md
  - sources/crto-notes-to-exam-preparation.md
  - sources/elearnsecurity-ecppt-notes-exam.md
  - sources/elearnsecurity-ecptxv2-notes.md
  - sources/elearnsecurity-ewpt-notes.md
  - sources/elearnsecurity-ewptx-notes-basic-by-joas.md
  - sources/elearnsecurity-exploit-development-student-notes-by-joas.md
  - sources/fundamentos-de-firewall.md
  - sources/hardware-hacking-introduction-overview.md
  - sources/internet-safety-sexual-predators-and-stalkers-how-to-protect-yourself.md
  - sources/introducao-a-network-security-1-0.md
  - sources/introducao-a-network-security-e-firewall.md
  - sources/offensive-security-mac-control-bypass-notes-pt-1.md
  - sources/offensive-security-wireless-fundamentals.md
  - sources/offensive-security-wireless.md
  - sources/pentest-iot-and-ot-overview.md
  - sources/python-for-hackers-bootcamp.md
  - sources/using-osint-to-investigate-school-shooters.md
  - entities/tools/pydns-scanner.md
  - concepts/dns-server-discovery-vs-subdomain-enumeration.md
  - sources/hacking-computer-hacking-security-testing.md
  - sources/network-attacks-and-exploitation.md
  - concepts/defense-in-depth.md
  - concepts/linux-security.md
  - concepts/pivoting.md
  - concepts/system-hardening.md
  - concepts/wireless-pentest.md
  - entities/pydns-scanner-xullexer.md
  - entities/tpotce.md
  - sources/basic-network-sniffer.md
  - sources/ccna-questions-answers.md
  - sources/cisco-sdwan-nat-part-1.md
  - sources/cisco-sdwan-lab-documentation.md
  - sources/top-50-cybersecurity-interview-questions.md
  - sources/encryption-and-hashing.md
  - sources/networking-essentials-for-cybersecurity.md
  - entities/tools/gopacket.md
  - entities/tools/openvpn-install.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
---

## Relations

- @concepts/red-team-operations.md
- @concepts/zero-trust.md
- @entities/people/joas-a-santos.md
- @entities/tools/nmap.md
- @sources/crto-notes-to-exam-preparation.md
- @sources/elearnsecurity-ecppt-notes-exam.md
- @sources/elearnsecurity-ecptxv2-notes.md
- @sources/elearnsecurity-ewpt-notes.md
- @sources/elearnsecurity-ewptx-notes-basic-by-joas.md
- @sources/elearnsecurity-exploit-development-student-notes-by-joas.md
- @sources/fundamentos-de-firewall.md
- @sources/hardware-hacking-introduction-overview.md
- @sources/internet-safety-sexual-predators-and-stalkers-how-to-protect-yourself.md
- @sources/introducao-a-network-security-1-0.md
- @sources/introducao-a-network-security-e-firewall.md
- @sources/offensive-security-mac-control-bypass-notes-pt-1.md
- @sources/offensive-security-wireless-fundamentals.md
- @sources/offensive-security-wireless.md
- @sources/pentest-iot-and-ot-overview.md
- @sources/python-for-hackers-bootcamp.md
- @sources/using-osint-to-investigate-school-shooters.md
- @entities/tools/pydns-scanner.md
- @concepts/dns-server-discovery-vs-subdomain-enumeration.md


- @sources/hacking-computer-hacking-security-testing.md
- @sources/network-attacks-and-exploitation.md
- @concepts/defense-in-depth.md
- @concepts/linux-security.md
- @concepts/pivoting.md
- @concepts/system-hardening.md
- @concepts/wireless-pentest.md
- @entities/pydns-scanner-xullexer.md — async DNS-recon variant of the xullexer project; attack-surface mapping
- @entities/tpotce.md — T-Pot multi-honeypot deception framework (20+ honeypots, Suricata NMS, Elastic)
- @sources/basic-network-sniffer.md
- @sources/ccna-questions-answers.md
- @sources/cisco-sdwan-nat-part-1.md
- @sources/cisco-sdwan-lab-documentation.md
- @sources/top-50-cybersecurity-interview-questions.md
- @sources/encryption-and-hashing.md
- @sources/networking-essentials-for-cybersecurity.md
- @entities/tools/gopacket.md — Go packet-decoding library for network-layer analysis (Mandiant, Apache-2.0)
- @entities/tools/openvpn-install.md — Bash OpenVPN deployment automation; refined NAT detection + IPv6-routing handling

## Raw Concept

Eight corpus PDFs anchor.

## Narrative

Network security = traditional network-layer + perimeter topics (firewalls, IDS/IPS, segmentation, VLANs, NAC) plus the wireless + IoT + OT extensions. Wireless: WPA2 attacks (PMKID, handshake capture + offline crack with hashcat), WPA3 (Dragonblood), Evil Twin / captive-portal phishing. IoT: firmware extraction (binwalk), hardware interfaces (UART, JTAG, SPI dumps via Bus Pirate / Saleae), default credential mining. OT/ICS: Modbus, PROFINET, DNP3 protocol attacks — context-specific because of real-world safety implications. See @concepts/red-team-operations.md.
