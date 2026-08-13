---
title: Software license binding design
type: concept
tags: [concept, licensing, license-binding, product-pentest, hardware-id, activation]
keywords: [license binding, digital license, OA3, KMS, ADBA, FlexNet, floating license, node-locked, activation, hardware hash, TPM attestation]
related:
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/pre-release-product-pentest.md
  - concepts/anti-tamper-protection-classes.md
  - sources/microsoft-oa3-hardware-hash.md
  - sources/oofhours-autopilot-hardware-hash.md
  - sources/microsoft-autopilot-motherboard-replacement.md
  - sources/microsoft-volume-activation-clients.md
  - sources/flexera-flexnet-licensing.md
  - sources/collberg-thomborson-software-protection-tools.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — license-binding architecture for owned-product design; no keygens/emulators"
---

## Relations

- @concepts/hardware-bound-identity-anticheat-licensing.md — identifier map this page consumes; same field inventory (OA3/TMP/SMBIOS)
- @concepts/pre-release-product-pentest.md — license binding is part of the pre-launch ship bar for owned products
- @concepts/anti-tamper-protection-classes.md — binding is the *entitlement* half; anti-tamper is the *resistance* half
- @sources/microsoft-oa3-hardware-hash.md — the canonical hardware-bound license (one key ↔ one computer)
- @sources/oofhours-autopilot-hardware-hash.md — 4K HH field inventory (encoded, per-field matching)
- @sources/microsoft-autopilot-motherboard-replacement.md — the documented hardware-change repair path
- @sources/microsoft-volume-activation-clients.md — the online-lease side (KMS/ADBA 180-day model)
- @sources/flexera-flexnet-licensing.md — commercial floating/node-locked entitlement stack
- @sources/collberg-thomborson-software-protection-tools.md — tamper-proofing is what keeps the binding check intact

## Raw Concept

Operator asked (2026-08-12): how do first parties design a license that survives reinstall, resale, and hardware changes — and how does that map to **our** product's license? Lane 1 of the license-bind / anti-tamper ingest.

**In scope:** architecture, what is collected/verified, class names of attacks (patch / keygen / loader / emulator / unpack) as *catalog*, official repair/re-bind paths, how to design **your** license.

**Out of scope:** working keygens, serial algorithms, Denuvo/Steam/EAC bypass, VMProtect/Themida unpack scripts, license emulators, warez, "unban this title." Cite *Epic v. Araujo* (`@sources/epic-games-v-araujo-hwid-spoofer-judgment.md`) as legal ceiling.

## Narrative

### 1. The binding menu

A license is *bound* when its validity depends on something outside the app binary. First-party systems bind to **more than one** of:

| Binding | Example | What it collects / verifies | Fails if |
|---------|---------|------------------------------|----------|
| Account | Windows digital license linked to Microsoft account; FlexNet named-user | Account identity + device claim | Account sharing / different account claims the device |
| Device hash | OA3 4K HH (DiskSerialNumber, EkPubHash, MacAddress, SMBIOS UUID/serial…); FlexNet machine fingerprint | Multi-field encoded inventory, matched per-field | You check only one field (e.g. `MachineGuid`) |
| TPM / attestation | Riot TPM EK as identity; Windows `SystemIdentification` `Source=Tpm` | Factory-burned key, hardware-backed ID | Socketed dTPM swap is cheaper than the ban |
| Online lease | KMS / ADBA (180-day renewal), FlexNet floating seats | Periodic server contact, seat count, compliance telemetry | Offline cracks / clock wind-back (vendor-side detection exists) |

**What fails if you only check `MachineGuid`:** it is a registry GUID generated at OS install and dies on clean reinstall. [CONFIRMED 2026-08-12 — same identifier-map evidence as @concepts/hardware-bound-identity-anticheat-licensing.md §1]

Thesis of this lane: bind to **≥2 layers**, reject sentinel IDs, and document a hardware-change path the way Autopilot does. [TENTATIVE design guidance — synthesized, not a single first-party source]

### 2. First-party repair paths (the part crackers skip)

- **OA3 / Autopilot:** motherboard replaced → deregister → replace → recapture 4K HH → reregister. Official. [CONFIRMED Microsoft Learn autopilot-motherboard-replacement]
- **Digital license:** sign in with the linked Microsoft account, mark "I changed hardware on this device recently", reactivate. Repeated hardware changes hit an exception-path limit. [CONFIRMED Microsoft support/Q&A 2026-08-12]
- **KMS/ADBA:** no per-device bind at all — the lease is the binding (180 days, renew every 7 days, retry every 2h; 25-client / 5-server activation thresholds). [CONFIRMED Microsoft Learn volume activation]

Design rule: if your users cannot re-bind after hardware change through an **official** path, they will go looking for the unofficial one.

### 3. Design rules for your own license (product-pentest steal)

Same steal as @concepts/hardware-bound-identity-anticheat-licensing.md §4, extended for the license lane:

1. **Bind to ≥2 independent layers** — device hash + account + server lease; never a single client-side GUID.
2. **Read from more than one layer** — a license check that reads SMBIOS *and* disk serial *and* TPM EK rejects inconsistent tuples.
3. **Server authority** — the license server verifies and records; the client reports. Never let a client-side `bool licensed` be the authority (same rule as @concepts/mobile-app-attestation.md server-verifies).
4. **Repair path documented** — deregister → re-bind flow like Autopilot, with rate limits on reuse.
5. **Revocation** — leaked keys / mass duplication must be revocable server-side; FlexNet-class stacks report "red flag behavior" like cloning and clock wind-back. [CONFIRMED Revenera FlexNet page]
6. **Tamper resistance is separate** — binding decides *who is entitled*; @concepts/anti-tamper-protection-classes.md decides *how hard it is to fake the answer*. Do not budget one without the other.

### 4. Legal ceiling

*Epic v. Araujo*: HWID-spoofer sales pled as DMCA §1201 circumvention (default judgment). Forging an OEM hardware association is fraud, not research. [CONFIRMED docket 2025 — @sources/epic-games-v-araujo-hwid-spoofer-judgment.md]

## Snippets

> "Hardware Association — A unique association that joins a single Microsoft-issued Windows product key to a single computer. The OA 3.0 Tool generates this value by using the hardware hash and the product key value."
[Source: https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-activation-3 (retrieved 2026-08-12)]

> "KMS activations are valid for 180 days (the activation validity interval). To remain activated, KMS client computers must renew their activation by connecting to the KMS host at least once every 180 days."
[Source: https://learn.microsoft.com/en-us/windows/deployment/volume-activation/activate-windows-clients-vamt (retrieved 2026-08-12)]

> "FlexNet Publisher (formerly FlexLM) is the de facto standard in software licensing solutions." … "Report and act on 'red flag behavior', such as license cloning or clock wind-back."
[Source: https://www.revenera.com/software-monetization/products/software-licensing/flexnet-licensing (retrieved 2026-08-12)]

## Dead Ends

- **Keygen / serial-math ingests** — out of scope by floor; not a research gap, a legal line.
- **KMS emulator / fake license server write-ups** — existence-only NO-GO, same class as HWID-spoofer kits. Not ingested.
- **Single-registry-GUID bindings** — fail the reinstall test; rejected as a design pattern, not as a wiki gap.
