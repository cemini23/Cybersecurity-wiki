---
title: Burp Suite
type: entity
tags: [web-pentest, proxy, portswigger, commercial-plus-free]
keywords: [burp, portswigger, intercepting proxy, repeater, intruder, scanner, extender]
related:
  - concepts/web-pentest-methodology.md
  - concepts/bug-bounty.md
  - sources/burp-suite-plugin-development.md
  - entities/people/joas-a-santos.md
  - entities/tools/kali-linux.md
  - concepts/pre-release-product-pentest.md
maturity: draft
created: 2026-05-12
updated: 2026-08-02
---

## Relations

- @concepts/web-pentest-methodology.md
- @concepts/bug-bounty.md
- @concepts/pre-release-product-pentest.md — primary web/API intercept tool for owned pre-launch product tests
- @sources/burp-suite-plugin-development.md
- @entities/people/joas-a-santos.md

- @entities/tools/kali-linux.md
## Raw Concept

Standard tool for web-app testing across the corpus. Anchored by Burp Suite Plugin Development.pdf.

## Narrative

PortSwigger's intercepting web proxy + integrated web-app testing toolkit. The de-facto standard across both pentest and bug-bounty workflows. [CONFIRMED]

**Editions:** Community (free, limited Scanner), Professional ($449/yr, full Scanner + Intruder rate-unlimited), Enterprise (CI/CD-integrated DAST).

**Key panes:** Proxy (intercept + history), Repeater (manual single-request iteration), Intruder (automated payload fuzzing — 4 attack types: sniper, battering ram, pitchfork, cluster bomb), Scanner (Pro-only DAST), Decoder, Comparer, Sequencer (session-token entropy analysis), Extender (BApp store + custom extensions in Java/Python/Ruby).

**Notable extensions** (BApp store): Logger++, Autorize, JWT Editor, Param Miner, Turbo Intruder, AuthMatrix, Hackvertor, Bypass WAF, ActiveScan++. The corpus's *Burp Suite Plugin Development.pdf* covers building your own. See @concepts/web-pentest-methodology.md for the full web-pentest workflow this tool slots into.
