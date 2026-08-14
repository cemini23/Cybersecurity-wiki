---
title: Endpoint encryption and deniable-storage classes
type: concept
tags: [concept, encryption, deniable-storage, fde, opsec, product-defense]
keywords: [full-disk encryption, FDE, BitLocker, FileVault, LUKS, plausible deniability, hidden volume, VeraCrypt, at-rest encryption, coerced password, TPM]
related:
  - concepts/system-hardening.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/commercial-spyware-stalkerware-defense.md
  - concepts/anonymity-networks.md
  - sources/veracrypt-hidden-volumes.md
  - sources/microsoft-bitlocker-overview.md
  - sources/apple-filevault.md
  - entities/tools/ente.md
  - concepts/e2ee-consumer-cloud-threat-model.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
wire_target: "REFERENCE — FDE + deniable-storage *classes* for operator OPSEC and product design; no hidden-volume how-to, no forensics-evasion"
---

## Relations

- @concepts/system-hardening.md — at-rest confidentiality as one layer of the desktop trust stack
- @concepts/hardware-id-masking-opsec.md — identifier layers and at-rest confidentiality are separate OPSEC planes; FDE ≠ anonymity
- @concepts/commercial-spyware-stalkerware-defense.md — deniable storage does **not** beat live endpoint compromise
- @concepts/anonymity-networks.md — FDE/deniability are at-rest properties; network-path unlinkability is a different plane
- @sources/veracrypt-hidden-volumes.md — the deniable-storage *class* (hidden-volume architecture, first-party)
- @sources/microsoft-bitlocker-overview.md — the FDE class on Windows (BitLocker / Device Encryption)
- @sources/apple-filevault.md — the FDE class on macOS (FileVault)

## Raw Concept

Operator-requested follow-up to the OPSEC/product-defense batch (2026-08-12). Files the **classes** of endpoint encryption and plausible deniability: what each protects, what it does *not* hide, and the dual-use/coercion threat model. Architecture + first-party documentation only.

**In scope:** the class distinction between full-disk encryption (FDE) and deniable-storage volumes; threat models each addresses; key / TPM / unlock mechanics as architecture; where these sit in the trust stack; operator + product steals.

**Out of scope:** hidden-volume *creation procedures*; header-wipe or forensics-evasion steps; "beat forensic imaging" how-tos. Existence and limits, not a setup guide.

## Narrative

### 1. FDE protects the *lost disk*, not the *running OS*

Full-disk encryption (BitLocker / FileVault / LUKS-class) encrypts the volume so that **a thief with the hardware but without the key cannot read the data at rest**. [CONFIRMED Microsoft Learn — @sources/microsoft-bitlocker-overview.md; Apple Support — @sources/apple-filevault.md] That is the threat model: lost, stolen, or inappropriately decommissioned device. It says nothing about confidentiality on a **running** device — once the OS has unlocked the volume and the user is logged in, any code running as the user (or root, or in the kernel) reads plaintext through the mounted filesystem.

Two architecture facts weaken the common "stolen laptop" story:

- **TPM-backed unlock.** BitLocker's default configuration lets the TPM release the key when the boot configuration looks unchanged — seamless unlock for the legitimate user, but no pre-boot secret. The attacker cannot read a cloned disk, but a device that boots itself unlocks itself. TPM + PIN restores a pre-boot secret at user-friction cost. [CONFIRMED Microsoft Learn]
- **FileVault unlocks at login.** Same class: protection against offline access to the disk, not against a logged-in attacker. [CONFIRMED Apple Support]

### 2. The deniable-storage class: hiding *that a second filesystem exists*

Plausible-deniability volumes (VeraCrypt hidden volume as the canonical class) are built for the **coerced-password** threat model: someone with the power to force you to reveal a password. The architecture: a VeraCrypt volume's free space is **always filled with random data at creation**, so a hidden volume placed in that free space is **indistinguishable from random data** — and a hidden header "cannot be identified." The passphrase selects which volume mounts: outer password → outer (decoy) volume; hidden password → hidden volume. [CONFIRMED veracrypt.io — @sources/veracrypt-hidden-volumes.md]

Deniability therefore rests on two things the *user* must get right, not the software: (a) the outer volume must be plausibly populated with "sensitive-looking files that you actually do NOT want to hide," and (b) the documented usage rules must be followed (substantially different passwords; no Quick Format / Dynamic; no in-place-encrypted filesystem). [CONFIRMED veracrypt.io]

### 3. The limits of the class

1. **It does not beat live malware.** Deniable storage protects against a coerced/passive examiner holding the disk. An implant running on the device after unlock reads whatever the user mounts — the same endpoint-compromise reality as @concepts/commercial-spyware-stalkerware-defense.md. [TENTATIVE synthesis]
2. **It does not hide that encryption exists.** FDE and deniable volumes both visibly use encryption; deniability is about *which* content, not *whether*. If mere possession of an encrypted volume is itself the signal, this class does not help.
3. **FDE with seamless TPM unlock is not deniable** — the device self-unlocks; there is no moment of coercion at which a decoy is presented.
4. **Deniability degrades with use.** The documented security precautions exist because mistakes (Quick Format / Dynamic, or a filesystem encrypted in place) break the free-space-randomness guarantee the hidden header depends on. [CONFIRMED veracrypt.io]

### 4. Dual-use framing

The coerced-password threat model is the legitimate reading: journalists, dissidents, and operators who carry data across borders or hostile checkpoints, where refusing a password has consequences. The same machinery is the hiding mechanism for crime. This wiki documents the **existence, architecture, and limits** of the class — the defense/OPSEC reading — and does **not** carry setup procedures or forensics-evasion steps. Framing follows the freedom-of-information posture of @concepts/commercial-spyware-stalkerware-defense.md.

### 5. Operator + product steals

- **Operator:** for high-threat travel, the deniable-storage *class* is worth knowing exists and knowing its limits; the practical control stack is still `@concepts/system-hardening.md` (a hardened, uninfected device) + `@concepts/hardware-id-masking-opsec.md` (identifier separation). Encryption does not replace either.
- **Product:** if **your** product stores secrets or user data on the endpoint, FDE alone is not a confidentiality control — it is a lost-device control. Design against the running-OS threat: keep long-term keys out of the session, bind release integrity (`@concepts/product-build-integrity-slsa-sigstore.md`), and treat "we encrypted the disk" as insufficient for "our secrets are safe."

## Snippets

> "Using a so-called hidden volume allows you to solve such situations without revealing the password to your volume."
[Source: https://veracrypt.io/en/Hidden%20Volume.html (retrieved 2026-08-12)]

> "free space on any VeraCrypt volume is always filled with random data when the volume is created" … "no part of the (unmounted) hidden volume can be distinguished from random data."
[Source: https://veracrypt.io/en/Hidden%20Volume.html (retrieved 2026-08-12)]

> "BitLocker is a Windows data protection feature that integrates with the operating system and helps address the threats of data theft or exposure from lost, stolen, or inappropriately decommissioned devices."
[Source: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/ (retrieved 2026-08-12)]

> "FileVault encrypts the data on the startup disk so that it can't be accessed without your login password or recovery key."
[Source: https://support.apple.com/guide/mac-help/mh11785/mac (retrieved 2026-08-12)]

## Dead Ends

- **Hidden-volume / header-wipe walkthroughs** — NO-GO existence-only; the class is documented, the procedure is not.
- **"How to beat forensic imaging"** — out of scope; that is the evasion side, not the operator-OPSEC reading this page carries.
