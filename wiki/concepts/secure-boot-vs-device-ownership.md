---
title: Secure Boot / attestation vs device ownership
type: concept
tags: [concept, boot-security, secure-boot, attestation, device-ownership, uefi, product-policy]
keywords: [Secure Boot, UEFI, measured boot, PK, KEK, db, dbx, Play Integrity STRONG, MEETS_STRONG_INTEGRITY, Vanguard Pre-Check, device ownership, custom kernel, dual-boot, GrapheneOS, rooted, attestation policy]
related:
  - concepts/mobile-app-attestation.md
  - concepts/system-hardening.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/anonymity-networks.md
  - concepts/software-license-binding.md
  - sources/microsoft-secure-boot.md
  - sources/microsoft-elam.md
  - sources/microsoft-hvci-memory-integrity.md
  - sources/riot-vanguard-on-demand-2026.md
  - sources/google-play-integrity-api.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — trust-stack vs ownership tension for product policy + operator boxes; no Secure Boot/DSE bypass"
---

## Relations

- @concepts/mobile-app-attestation.md — STRONG-tier attestation is the mobile face of the same trust stack
- @concepts/system-hardening.md — the trust stack as a hardening layer; Secure Boot is the pre-OS gate
- @concepts/hardware-bound-identity-anticheat-licensing.md — AC Pre-Check (Vanguard) consumes the same stack; TPM EK identity rides on it
- @concepts/anonymity-networks.md — custom-kernel / USB-boot anonymity setups (Tails) collide with Secure Boot policy
- @concepts/software-license-binding.md — TPM/attestation-backed binding relies on the trust stack; owners who disable it may fail binding
- @sources/microsoft-secure-boot.md — UEFI Secure Boot signature chain (PK/KEK/db/dbx)
- @sources/microsoft-elam.md — boot-order classification gate (who may load)
- @sources/microsoft-hvci-memory-integrity.md — code-integrity gate (may loaded code execute)
- @sources/riot-vanguard-on-demand-2026.md — Vanguard Pre-Check (25H2+, Secure Boot, TPM 2.0, VBS, HVCI, IOMMU)
- @sources/google-play-integrity-api.md — MEETS_STRONG_INTEGRITY hardware-backed tier

## Raw Concept

Operator-requested follow-up (2026-08-12): the tension between platform boot integrity / attestation and **user control of the device**. The same stack that stops evil-maid / bootkits also denies custom kernels, dual-boot, and some anonymity setups. First-party docs: Microsoft Learn (Secure Boot, ELAM, HVCI), Riot (Pre-Check), Google (Play Integrity).

**In scope:** what the trust stack asserts and when; the class of users it excludes; product-policy options (allow custom at lower trust vs lock STRONG); operator posture (Secure Boot on for the daily driver; written-scope lab exceptions).

**Out of scope:** Secure Boot / DSE / Magisk / Play-Integrity-Fix **bypass steps**; "load unsigned drivers" kits; custom-bootloader flashing how-tos. Policy + architecture, not evasion.

## Narrative

### 1. What the trust stack asserts

Boot integrity is a signature chain: UEFI firmware checks each piece of boot software (Option ROMs, EFI applications, the OS) against the **signature database (db)** / revoked list (**dbx**, which takes precedence on conflict), gated by the Key Enrollment Key (**KEK**) and platform key (**PK**). If the signatures are valid, the machine boots and control passes to the OS. [CONFIRMED Microsoft Learn — @sources/microsoft-secure-boot.md] Above it, Windows layers measured boot, ELAM (who may load — boot-order gate), and HVCI (may loaded code execute). [CONFIRMED Microsoft Learn — @sources/microsoft-elam.md, @sources/microsoft-hvci-memory-integrity.md]

The same idea extends past the desktop: Android's Play Integrity **MEETS_STRONG_INTEGRITY** is hardware-backed (Android 13+), and Vanguard **Pre-Check** demands Windows 11 25H2+, Secure Boot, TPM 2.0, VBS, HVCI, IOMMU before dropping the always-on driver. [CONFIRMED — @sources/riot-vanguard-on-demand-2026.md]

What the stack buys: the machine you boot is the machine the OEM/vendor vouches for — evil-maid (firmware tampering), bootkits, and unsigned/foreign loaders are excluded at the boundary. [CONFIRMED Microsoft Learn]

### 2. The ownership cost

The same gates exclude the owner:

- **Custom kernels / dual-boot** — booting a non-vendored OS image requires either a signed loader or disabling Secure Boot.
- **Custom-ROM Android (GrapheneOS-class)** — a bootloader-unlocked, custom-OS device fails `MEETS_STRONG_INTEGRITY`; STRONG is designed around a locked, certified, unmodified device.
- **Some anonymity setups** — Tails / USB-boot anonymity depends on booting an unsigned removable OS; on locked-down devices that path is closed by policy, not by user choice. (`@concepts/anonymity-networks.md` — the anonymity plane collides with the boot-trust plane.)
- **License/attestation binding** — product bindings that lean on TPM attestation (e.g. `@concepts/software-license-binding.md`) may simply fail for owners who disabled the stack, forcing a customer-service re-bind path or a lower-trust fallback.

The invariant: **attestation proves "this is a stock, vendor-vouched device" — it cannot also prove "this is my device to modify."** A product gets one or the other as the *default*, and decides which is worth more. [TENTATIVE synthesis]

### 3. Product policy — pick a lane and document the cost

| Policy | Who it serves | Who it excludes | Design consequence |
|--------|--------------|-----------------|--------------------|
| Lock STRONG | Anti-fraud / anti-cheat, high-assurance | Rooted / custom-ROM / power users | Treat non-STRONG as lower trust (limits / CAPTCHA), not necessarily deny; document the exclusion |
| Allow custom at lower trust | Wide reach, BYOD | — | Accept weaker integrity signals; pair with server-side risk signals |
| Hybrid tiered | Broad + sensitive tiers | Only the strict tier excludes | Play Integrity's own guidance: tiered enforcement beats binary allow/deny |

Play Integrity's first-party guidance supports tiering ("works best when used alongside other signals… not as your sole anti-abuse mechanism"). [CONFIRMED — @sources/google-play-integrity-api.md]

### 4. Operator posture

Daily driver: Secure Boot + TPM on — the same stack you'd demand of a high-assurance client. Lab boxes / RE targets (`@concepts/owned-target-whitehat-lab.md`, `@concepts/game-hacking.md`): may disable Secure Boot with **written scope**, because kernel RE and unsigned-driver lab work is precisely what the stack blocks. The written-scope discipline keeps the "owner disables it" fact inside the lab.

### 5. Out of scope — the evasion side

How to *disable* Secure Boot to load unsigned drivers, DSE bypass, Magisk / Play-Integrity-Fix to restore STRONG on a modified device — those are the attacker side of this exact control, and this page is the defender/product side. Catalogued as Dead Ends, not procedures.

## Snippets

> "Secure boot is a security standard developed by members of the PC industry to help make sure that a device boots using only software that is trusted by the Original Equipment Manufacturer (OEM)."
[Source: https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot (retrieved 2026-08-12)]

> "If an image hash is in both databases, the revoked signatures database (dbx) takes precedent."
[Source: https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot (retrieved 2026-08-12)]

> Vanguard Pre-Check requires "Windows 11 25H2+, Secure Boot, TPM 2.0, VBS, HVCI, IOMMU" before the always-on driver is dropped.
[Source: https://www.riotgames.com/en/news/vanguard-on-demand (retrieved 2026-08-12)]

> "The Play Integrity API works best when used alongside other signals as part of your overall anti-abuse strategy and not as your sole anti-abuse mechanism."
[Source: https://developer.android.com/google/play/integrity/overview (retrieved 2026-08-12)]

## Dead Ends

- **Secure Boot / DSE bypass walkthroughs** — NO-GO existence-only; the evasion side is catalogued, not documented.
- **Magisk / Play Integrity Fix-class write-ups** — existence-only (already on @concepts/mobile-app-attestation.md Dead Ends).
- **"Secure Boot off to load unsigned drivers" as a kit** — belongs to written-scope lab work only; not a how-to.
