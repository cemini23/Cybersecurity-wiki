---
title: Anti-tamper protection classes
type: concept
tags: [concept, anti-tamper, software-protection, obfuscation, drm, product-pentest]
keywords: [anti-tamper, integrity check, packing, code virtualization, online heartbeat, Denuvo, VMProtect, Themida, obfuscation, tamper-proofing, watermarking]
related:
  - concepts/software-license-binding.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/game-hacking.md
  - concepts/av-edr-bypass.md
  - sources/game-hacking-1-anti-cheat-bypass.md
  - entities/tools/denuvo.md
  - sources/irdeto-denuvo-anti-cheat-anti-tamper.md
  - sources/collberg-thomborson-software-protection-tools.md
  - concepts/pre-release-product-pentest.md
  - concepts/product-build-integrity-slsa-sigstore.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — protection *classes* for owned-product design and lab RE; no unpack scripts"
---

## Relations

- @concepts/software-license-binding.md — binding is the entitlement half; this page is the resistance half
- @concepts/hardware-bound-identity-anticheat-licensing.md — kernel AC is the anti-tamper consumer of the OS trust stack
- @concepts/game-hacking.md — AC component inventory (Joas deck) lives on the source page
- @concepts/av-edr-bypass.md — same detection surface (hooks, debuggers, integrity checks) from the *protector's* side
- @sources/game-hacking-1-anti-cheat-bypass.md — Joas deck p.12–13: AC component taxonomy (link-index deck)
- @entities/tools/denuvo.md — vendor exemplar of the anti-tamper class (REFERENCE, no clone)
- @sources/irdeto-denuvo-anti-cheat-anti-tamper.md — first-party anti-piracy + kernel AC product pages
- @sources/collberg-thomborson-software-protection-tools.md — 2002 taxonomy anchor (obfuscation / tamper-proofing / watermarking)
- @concepts/pre-release-product-pentest.md — "strip the protection" rehearsal belongs in the pre-launch loop
- @concepts/product-build-integrity-slsa-sigstore.md — client tamper-resistance is downstream of shipping the binary you built

## Raw Concept

Operator asked (2026-08-12): what are the *classes* of anti-tamper protection — so we can reason about them as a defender/designer (and name vendor exemplars without filing unpack how-tos). Lane 2 of the license-bind / anti-tamper ingest.

**In scope:** architecture, what is collected/verified, class names of attacks (patch / keygen / loader / emulator / unpack) as *catalog*, official repair/re-bind paths, how to design **your** license.

**Out of scope:** working keygens, serial algorithms, Denuvo/Steam/EAC bypass, VMProtect/Themida unpack scripts, license emulators, warez, "unban this title." Cite *Epic v. Araujo* (`@sources/epic-games-v-araujo-hwid-spoofer-judgment.md`) as legal ceiling.

## Narrative

### 1. Crackers attack classes, not products

Every protection product is an instance of a small set of **classes**. Crack scenes optimize against the class, so defenses must be evaluated by class, not by brand. [TENTATIVE synthesis]

Collberg & Thomborson (IEEE TSE 2002) fixed the academic vocabulary: three protection goals — **obfuscation** (resist analysis), **tamper-proofing** (detect/respond to modification), **watermarking** (prove authorship) — under a malicious-host threat model. [CONFIRMED title/venue; taxonomy details TENTATIVE — full text not pulled this run, see source page]

### 2. The class map

| Class | What it does | Exemplars (class, not how-to) | What crackers do (catalog only) |
|-------|--------------|-------------------------------|---------------------------------|
| Integrity checks | Hash/CRC the binary or memory regions at runtime | Denuvo anti-tamper; AC file-integrity checks | patch the check (nop the branch) |
| Packing / wrapping | Compress or encrypt the payload, unpack at load | UPX (legit packer); commercial protectors | generic unpack / dump-after-OEP |
| Code virtualization | Translate hot code into VM bytecode | VMProtect / Themida *class* | devirtualization research (slow, per-VM) |
| Online heartbeat / server authority | Server re-verifies entitlements and state | Denuvo Anti-Piracy activation; FlexNet license server; @concepts/mobile-app-attestation.md verdicts | emulator / fake server (existence-only) |
| OS trust stack | OS enforces load/execution policy below the app | HVCI / ELAM / WDAC; kernel AC (Denuvo kernel AC) | attacks shift to the trust boundary (firmware, DMA, driver bugs) |

Integrity checks and packing buy *time*; virtualization buys *difficulty*; server authority buys *control*; the OS trust stack buys *load-order*. Mature products layer several classes. [TENTATIVE synthesis]

### 3. Anti-cheat as an anti-tamper consumer

Joas *Game Hacking 1 – Anti Cheat BYPASS* (link-index deck) lists the AC component inventory — the same classes, aimed at cheats instead of pirates: file integrity checks, string detection, classic anti-debug, obfuscation, signature detection, hook detection, memory integrity checks, virtualization, kernel drivers (blocking process-access-token creation), virtualization detection. And the author's thesis: "To bypass anticheat you must understand how it works. Anticheat work very similarly to Antivirus." [CONFIRMED deck p.12–13 — @sources/game-hacking-1-anti-cheat-bypass.md]

### 4. Product-pentest steal

1. **Pick classes by attacker economics**, not brand: a license that only hashes its own file is one `nop` from free.
2. **Server authority is the highest-value class** — move entitlement decisions server-side (@concepts/software-license-binding.md §3.3).
3. **Defender-side:** the same classes protect *your* product that EDR vendors use to protect endpoints — read @concepts/av-edr-bypass.md for the evasion catalog to know what your protection must survive.
4. **Test on an owned lab build:** the pre-release loop (@concepts/pre-release-product-pentest.md) should include a "strip the protection" rehearsal to measure how long it takes, not whether it is impossible. [TENTATIVE design guidance]

### 5. Legal ceiling + scope

Removing or defeating a protection on a title you do not own as a product under test is DMCA §1201 territory (see *Epic v. Araujo* via @sources/epic-games-v-araujo-hwid-spoofer-judgment.md). Class-level architecture is catalogued; unpack procedures are not.

## Snippets

> "Prevent piracy at launch by securing executables with robust anti-piracy technology." … "reinforcing platform DRM systems to ensure only legitimate users can play"
[Source: https://irdeto.com/video-games/denuvo-anti-piracy/ (retrieved 2026-08-12)]

> "To bypass anticheat you must understand how it works. Anticheat work very similarly to Antivirus."
[Source: Game Hacking 1 – Anti Cheat BYPASS.pdf p.13 (egress-fi cybersec/joas-game-hacking-1.pdf)]

> Paper: C. Collberg, C. Thomborson, "Watermarking, Tamper-Proofing, and Obfuscation — Tools for Software Protection," IEEE Transactions on Software Engineering 28(6), 2002. DOI 10.1109/TSE.2002.1027797.
[Source: https://doi.org/10.1109/TSE.2002.1027797 (retrieved 2026-08-12; abstract not pulled — verify taxonomy details on deep-read)]

## Dead Ends

- **"Unpack VMProtect 3" / tuts4you / UnknownCheats unpack blogs** — existence-only NO-GO as runbook ingests. Class names are catalogued above; step-by-step unpack procedures stay out.
- **Denuvo reverse-engineering write-ups** — same NO-GO; the vendor page is the ingested source, not scene RE.
- **Devirtualization research** — exists in academic literature; catalogued as the counter to the virtualization class, not ingested as a toolkit.
