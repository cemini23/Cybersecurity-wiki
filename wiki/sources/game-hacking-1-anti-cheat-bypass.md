---
title: "Game Hacking 1 – Anti Cheat BYPASS"
type: source
tags: [cybersecurity, joas-corpus, anti-cheat, reverse-engineering]
keywords: [game hacking, anti-cheat components, file integrity, hook detection, memory integrity, Joas, link index]
related:
  - concepts/game-hacking.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/anti-tamper-protection-classes.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-08-12
read_status: read
phase_0_verdict: "REFERENCE 2026-08-12 — read; architecture (AC component taxonomy) only; bypass-guide titles catalog-only, never a runbook"
wire_status: wont_wire
---

## Relations

- @concepts/game-hacking.md — RE practice home
- @concepts/hardware-bound-identity-anticheat-licensing.md — AC component inventory supports the identifier/load-order map
- @concepts/anti-tamper-protection-classes.md — p.12–13 component list is the AC instance of the protection classes
- @entities/people/joas-a-santos.md


## Raw Concept

- **Title:** Game Hacking 1 – Anti Cheat BYPASS
- **Author:** Joas A Santos (see @entities/people/joas-a-santos.md)
- **Type:** PDF slide deck, 19 pages — curated **link-index** (reference lists), not a prose how-to
- **Location:** canonical `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/joas-game-hacking-1.pdf` (archived 2026-08-12); source Google Drive — `ebooks Joas` folder, file ID `1SbpXx6D6VSVFhtMxXEAyT2VGW01x0_Pq`
- **Retrieved:** 2026-08-12 (downloaded + full text extracted; catalogued as stub 2026-05-12)
- **Read status:** read (19/19 pages; text extraction, no page images)

## Narrative

**What the deck is:** a curated index of links/tutorial titles across: programming prerequisites (Assembly, C, C++, C#, Python — pages 2–7), reverse engineering (hooking, unpack guides, trainer tools, injectors, ReClass, CrackMes — pages 8–10), anti-cheat architecture (pages 11–13), bypass-guide titles (page 14), and UnknownCheats anti-cheat thread titles (pages 17–18), plus study materials (page 19: BlackHat Asia 2015 "Next Level Cheating", Immunity "Unveiling The Underground World Of Anti-Cheats" EU-19).

**Architecture ingested (p.12–13).** Anti-cheat components: file integrity checks, string detection for cheat tools, classic anti-debug, obfuscation, signature-based detection, hook detection, memory integrity checks, virtualization, kernel drivers which block process-access-token creation, virtualization detection. Anti-cheat work (ordered simple → advanced): file integrity checks → detecting debuggers → stops debugger attaching → detect Cheat Engine/memory editors → signature detection → detect DLL injection → detect hooks → block Read/WriteProcessMemory → memory integrity checks → statistical anomaly detection → heuristics. Author's framing: "To bypass anticheat you must understand how it works. Anticheat work very similarly to Antivirus."

**Deliberately NOT ingested as runbook:** page 14 bypass-guide titles (EAC, BattlEye, VAC, XignCode, Hackshield, FairFight, GamersClub, MTA:SA, CSGO Overwatch) and pages 17–18 UnknownCheats thread titles (drvmap, PCIe DMA cheat, HWID spoofing source, PatchGuard, VAC2 bypass) are recorded as *existence catalog* only — no steps, no thread URLs reproduced, no kits. They corroborate the attack-class catalog on @concepts/anti-tamper-protection-classes.md; the wiki does not carry their contents.

## Snippets

> "ANTI-CHEAT COMPONENTS — Features Anticheat Uses: File Integrity Checks · String Detection for cheat tools · Classic AntiDebug · Obfuscation · Signature Based Detection · Hook Detection · Memory Integrity Checks · Virtualization · Kernel Drivers which block process access token creation & more · Virtualization Detection"
[Source: Game Hacking 1 – Anti Cheat BYPASS.pdf p.12 (egress-fi cybersec/joas-game-hacking-1.pdf)]

> "To bypass anticheat you must understand how it works. Anticheat work very similarly to Antivirus. These are the basic things it does to stop you from cheating, kinda going from simple to more advanced"
[Source: Game Hacking 1 – Anti Cheat BYPASS.pdf p.13 (egress-fi cybersec/joas-game-hacking-1.pdf)]

## Dead Ends

- **Deck sections that are title-only** (p.11 "ANTI-CHEAT SOLUTIONS", p.15 "ANTI-CHEAT BYPASS TECHNIQUES", p.16 "DLL INJECTION / HIJACKING") — headers over link lists; there is no prose body to deep-read further.
- **UnknownCheats / guidedhacking links inside the deck** — existence-only; not reproduced, not followed up as runbook ingests.
