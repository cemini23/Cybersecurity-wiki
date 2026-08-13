---
title: Hardware-bound identity — anti-cheat HWID and licensing
type: concept
tags: [concept, anti-cheat, licensing, hwid, windows, kernel, opsec]
keywords: [HWID ban, BattlEye, Easy Anti-Cheat, Vanguard, FACEIT, OA3, hardware hash, SMBIOS, kernel anti-cheat]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/game-hacking.md
  - concepts/windows-pentest.md
  - concepts/av-edr-bypass.md
  - concepts/pre-release-product-pentest.md
  - concepts/owned-target-whitehat-lab.md
  - sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
  - sources/s4dbrd-kernel-anti-cheats.md
  - sources/secret-club-battleye-architecture-2019.md
  - sources/microsoft-oa3-hardware-hash.md
  - sources/microsoft-autopilot-motherboard-replacement.md
  - sources/microsoft-systemidentification-getsystemidforpublisher.md
  - sources/game-hacking-1-anti-cheat-bypass.md
  - sources/oofhours-autopilot-hardware-hash.md
  - sources/checkpoint-evasions-firmware-tables.md
  - sources/microsoft-getruntimeattestationreport.md
  - sources/riot-vanguard-on-demand-2026.md
  - sources/epic-games-v-araujo-hwid-spoofer-judgment.md
  - sources/faceit-enhanced-verification.md
  - entities/tools/battleye.md
  - entities/tools/easy-anti-cheat.md
  - entities/tools/riot-vanguard.md
  - concepts/software-license-binding.md
  - concepts/anti-tamper-protection-classes.md
  - concepts/mobile-app-attestation.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/microsoft-elam.md
  - sources/microsoft-kernel-dma-protection.md
  - sources/irdeto-denuvo-anti-cheat-anti-tamper.md
  - entities/tools/denuvo.md
  - concepts/secure-boot-vs-device-ownership.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — identifier map + AC/licensing architecture; no spoof-driver clones"
---

## Relations

- @concepts/hardware-id-masking-opsec.md — same identifier layers; this page is the AC/licensing consumer
- @concepts/game-hacking.md — RE practice home; HWID bans live here as a control, not a how-to
- @concepts/windows-pentest.md — kernel callbacks / firmware tables are Windows internals
- @concepts/av-edr-bypass.md — kernel AC uses the same callback surface as EDR
- @concepts/pre-release-product-pentest.md — hardware-bind your own product’s license the way OA3 does
- @concepts/owned-target-whitehat-lab.md — written scope before touching any third-party AC
- @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md
- @sources/s4dbrd-kernel-anti-cheats.md
- @sources/secret-club-battleye-architecture-2019.md
- @sources/microsoft-oa3-hardware-hash.md
- @sources/microsoft-autopilot-motherboard-replacement.md
- @sources/microsoft-systemidentification-getsystemidforpublisher.md
- @sources/game-hacking-1-anti-cheat-bypass.md — Joas corpus stub (unread)
- @sources/oofhours-autopilot-hardware-hash.md — 4K HH is an encoded field inventory
- @sources/checkpoint-evasions-firmware-tables.md — NtQuerySystemInformation class 76 / RSMB / FIRM
- @sources/microsoft-getruntimeattestationreport.md — signed driver-history report (HVCI)
- @sources/riot-vanguard-on-demand-2026.md — boot-start exception + TPM EK as HWID
- @sources/epic-games-v-araujo-hwid-spoofer-judgment.md — HWID spoof pled as DMCA circumvention
- @sources/faceit-enhanced-verification.md — hardware identifiers in multi-account checks
- @entities/tools/battleye.md
- @entities/tools/easy-anti-cheat.md
- @entities/tools/riot-vanguard.md
- @concepts/software-license-binding.md — license design consumes the same identifier map (2026-08-12 lanes 1–5)
- @concepts/anti-tamper-protection-classes.md — protection classes AC/DRM instantiate
- @concepts/mobile-app-attestation.md — mobile cousin: Secure Enclave / Play verdicts
- @sources/microsoft-hvci-memory-integrity.md — hypervisor-enforced kernel CI (trust stack)
- @sources/microsoft-elam.md — boot-start driver classification (trust stack)
- @sources/microsoft-kernel-dma-protection.md — IOMMU fencing of hot-plug PCIe (trust stack)
- @sources/irdeto-denuvo-anti-cheat-anti-tamper.md — vendor exemplar (kernel AC + anti-piracy)
- @entities/tools/denuvo.md — Denuvo vendor entity (REFERENCE)
- @concepts/secure-boot-vs-device-ownership.md — Vanguard Pre-Check consumes the same boot trust stack; ownership vs attestation tension

## Raw Concept

Operator asked (2026-08-12, written-scope lab/product) to ingest anti-cheat and license HWID so the wiki can work the identifier map. Same layers as @concepts/hardware-id-masking-opsec.md; different *consumers* (ban lists and license servers).

**In scope:** architecture, what is collected, why user-mode patches fail, how cheap spoofs are detected, first-party hardware-bound licensing (OA3 / Autopilot).

**Out of scope for this wiki:** spoof-driver source, IOCTL-hook recipes, license keygens, bypassing a publisher ban on a game you do not own as a product under test. Those stay crimeware / ToS-evasion even when the lab is otherwise authorized.

## Narrative

### 1. What “HWID” means to an anti-cheat

There is still no single field. Kernel anti-cheats hash a **bundle** and store it server-side against the account. Typical members (kernel-readable, survive OS reinstall unless noted): [CONFIRMED 2026-08-12 compilation — Microsoft OA3Tool critical fields via Oofhours + firmware-table API via Check Point + Riot TPM-EK language; not a vendor AC spec]

| Group | Examples | Typical access |
|-------|----------|----------------|
| Firmware | SMBIOS UUID, board/BIOS serial, system manufacturer/product | `NtQuerySystemInformation` info-class 76 (`SystemFirmwareTableInformation`), providers `'RSMB'` / `'FIRM'` |
| Storage | Disk firmware serial (not NTFS volume serial) | storage query IOCTL / OA3 `DiskSerialNumber` |
| NIC | Factory MAC | NDIS / adapter; OA3 `MacAddress` |
| CPU | CPUID vendor/brand string | `CPUID` |
| OS install | `MachineGuid` | Registry — **does not** survive clean install |
| TPM | EK / `SystemIdentification` when `Source=Tpm`; OA3 `EkPubHash` + `TpmVersion` | TPM / WinRT |

Microsoft’s OA3 “hardware hash” (4K HH) is an **encoded inventory**, matched **per-field**, not a digest: DiskSerialNumber, TpmVersion, EkPubHash, MacAddress, ProductKeyId, SMBIOS family/manufacturer/product/serial/UUID. [CONFIRMED Oofhours 2022 + Microsoft Learn]

A HWID **ban** follows the bundle, not the email. A **digital license** follows the OA3 association. Same defensive lesson as OPSEC: change one member and the rest still match.

### 2. Load order beats user-mode spoof

Usermode anti-cheat is blind to ring 0. Kernel AC moved into the kernel for that reason. [CONFIRMED s4dbrd]

Three-component model (BattlEye as the public example): kernel driver + SYSTEM service + in-game DLL. BattlEye names: `BEDaisy.sys`, `BEService.exe`, `BEClient_x64.dll`, plus `BEServer`. [CONFIRMED secret.club 2019 architecture]

**Demand-start (BattlEye, EAC):** driver loads with the game, unloads after. A boot-start cheat driver can already be resident.

**Boot-start (classic Vanguard `vgk.sys`):** `SERVICE_BOOT_START` — observes later driver loads; allowlist rather than blocklist. [CONFIRMED s4dbrd]

**On-demand exception (Vanguard, 2026):** if the box passes Pre-Check (Win11 25H2+, Secure Boot, TPM 2.0, VBS, HVCI, IOMMU), Riot will **not** load the driver at boot. Microsoft `GetRuntimeAttestationReport` gives a Secure-Kernel-signed list of drivers loaded while Vanguard was dormant. [CONFIRMED Riot first-party + Microsoft Learn]

ARES 2024 (arXiv 2408.00500): BattlEye and EAC showed only minor rootkit-like traits under their metrics; **FACEIT AC and Vanguard** classified as rootkit-like (boot/stealth/callback breadth). Capability ≠ malice — same Windows primitives as EDR. [CONFIRMED abstract]

**The trust stack underneath (2026-08-12):** On-Demand-class AC/DRM consume a Windows trust stack, not just a driver: **ELAM** gives the OS a boot-start classifier; **HVCI** (memory integrity) enforces kernel code integrity from the hypervisor; **WDAC/App Control** is the policy allow-list; **IOMMU/Kernel DMA Protection** fences hostile peripherals. Riot Pre-Check (Secure Boot, TPM 2.0, VBS, HVCI, IOMMU) is exactly this stack. [CONFIRMED Microsoft Learn HVCI/ELAM/DMA + Riot 2026] Two consequences: (a) AC/DRM that *require* HVCI + attestation change the loader threat model — observation moves from "what loaded" to "what the secure kernel signs as loaded" (@sources/microsoft-getruntimeattestationreport.md); (b) a lab that disables these features is modelling a different, older target class.

### 3. Spoofer *classes* (adversary catalog, not a kit)

Public RE describes three classes. This wiki records the class, not a procedure.

| Class | What it tries | Why kernel AC usually still sees the real ID |
|-------|----------------|-----------------------------------------------|
| Registry / WMI overlay | Patch what usermode apps read | Kernel reads firmware tables and storage IOCTLs directly |
| Kernel intercept | Hook identifier IOCTLs / return fake SMBIOS | Load-after-Vanguard is observed; sentinel values and cross-checks flag junk |
| Physical | Different NIC EEPROM, different disk, motherboard swap, **TPM/CPU swap** | Microsoft Autopilot: deregister → replace board → recapture 4K HH. Riot: TPM EK is factory-burned; they treat socketed **dTPM** swap as too cheap, so restricted accounts must use **fTPM**. [CONFIRMED Riot 2026] |

Cheap-spoof tells that ACs look for (public RE, not a how-to): all-`F` SMBIOS UUID; disk serial that does not match the claimed model’s format; firmware UUID ≠ registry UUID. [TENTATIVE s4dbrd §12]

**Product-pentest steal:** if you hardware-bind *your* license, read from more than one layer and reject sentinel/inconsistent tuples. Do not trust a single registry GUID.

### 4. Licensing vs anti-cheat

| | Anti-cheat HWID ban | OA3 / Autopilot hardware hash |
|--|---------------------|-------------------------------|
| Goal | Stop new accounts on the same PC | Bind a Windows key / MDM enrollment to one machine |
| Who stores the tuple | Game publisher backend | Microsoft |
| Official hardware change | Unpublished / support lottery | Microsoft documents motherboard-replacement steps |
| TPM | Vanguard Pre-Check requires TPM 2.0 (+ Secure Boot / VBS / HVCI / IOMMU for On-Demand). Riot: EK as hardware identity; restricted accounts = fTPM only. [CONFIRMED Riot 2026] | Hash includes TpmVersion + EkPubHash |

Do not treat a “license spoofer” as an OA3 tool. Forging an OEM hardware association is fraud. Epic pled **hardware-ID bans + HWID spoofers** as DMCA §1201 circumvention in *Epic v. Araujo* (C.D. Cal. 2:24-cv-10835; default judgment $175,521). [CONFIRMED docket 2025]

FACEIT Stage-1 multi-account checks explicitly review **hardware identifiers** plus network and match telemetry. [CONFIRMED FACEIT support]

For **your** product: hash the same fields OA3 does, document a repair path like Autopilot’s, and test that a clean Windows reinstall does **not** reset a TPM-backed ID (@sources/microsoft-systemidentification-getsystemidforpublisher.md).

### 5. Lab rules (this wiki)

1. Written scope: owned anti-cheat, owned license server, or engagement letter. Not “I want to play on a banned Valorant account.”
2. No clone of commercial HWID changers or mapper kits (`wont_wire`).
3. Joas *Game Hacking 1 – Anti Cheat BYPASS* upgraded 2026-08-12: PDF fetched, read (19 pages), archived to egress-fi. It is a link-index deck — only its AC-component taxonomy (p.12–13) is ingested; bypass-guide titles stay catalog-only.
4. Pair with @concepts/av-edr-bypass.md: kernel AC callbacks look like EDR because they **are** the same APIs.

## Dead Ends

- **Registry-only “HWID changer” vs Vanguard/EAC/BattlEye kernel readers** — fails the layer test. [TENTATIVE public RE 2026-08-12]
- **Clean OS reinstall as unban / new license** — firmware + disk serial + TPM EK remain. [CONFIRMED Microsoft SystemIdentification + OA3 fields + Riot EK language]
- **Socketed dTPM swap as cheap unban** — Riot first-party: restricted accounts require fTPM because discrete TPMs are often unsoldered. [CONFIRMED Riot On-Demand]
- **Ingesting secret.club bypass posts or commercial HWID-spoofer gitbooks as runbooks** — architecture yes; kit bodies stay out. DeepSeek citation hunt (2026-08-12) surfaced storefront gitbooks and public GitHub spoof repos — logged as **NO-GO clone**, not ingested.
- **Boot-start as the only Vanguard model** — stale after On-Demand (2026) on attested 25H2 boxes. [CONFIRMED Riot]
