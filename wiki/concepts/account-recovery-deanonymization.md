---
title: Account Recovery as Deanonymization
type: concept
tags: [account-recovery, sim-swap, deanonymization, identity, opsec, mfa]
keywords: [SIM swap, port-out, account recovery, forgot password, SSO, security keys, advanced protection, passkeys, backup codes, recovery contact]
related:
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/operator-lab-playbook.md
  - concepts/osint-for-cybersecurity.md
  - concepts/pre-release-product-pentest.md
  - sources/fbi-ic3-sim-swap-psa.md
  - sources/google-advanced-protection.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
---

## Relations

- @concepts/metadata-traffic-analysis-anonymity.md — anonymity dies when the *identity account* behind it is recovered by someone else
- @concepts/hardware-id-masking-opsec.md — hardware keys and TPM-backed identity are a recovery-identity plane
- @concepts/operator-lab-playbook.md — dedicated numbers/emails are identity, not convenience
- @concepts/osint-for-cybersecurity.md — recovery surfaces (phone, email, SSO) are what OSINT enumerates about a persona
- @concepts/pre-release-product-pentest.md — recovery flows are an authz-bypass class for your own product
- @sources/fbi-ic3-sim-swap-psa.md — SIM swap is the canonical recovery-takeover vector
- @sources/google-advanced-protection.md — phishing-resistant sign-in still routes through recovery

## Raw Concept

**In scope:** how threats work at the *class* level; first-party privacy/security controls; what an operator inventories; how to design a product so it does not become the deanonymizer or the spyware implant.

**Out of scope:** installing Pegasus/stalkerware; hidden-volume step-by-steps for hiding evidence; GFW/Tor-bridge recipes as a runbook; SIM-swap *how to steal a number*; exploits/PoCs; HWID spoofers; keygens; Magisk/Play Integrity Fix.

Freedom-of-information / anonymity framing: journalists, dissidents, operators, product users in hostile networks. **Not** "evade a lawful US warrant." Compelled-disclosure is a *threat model to document*, not a crime guide.

The attack class documented here is the *identity-recovery takeover* (SIM swap, account recovery abuse). It is a threat model to defend against and to design products against; it is not instructions for porting a number or stealing a recovery code.

## Narrative

### 1. Anonymity dies at recovery

A pseudonymous persona is only as strong as the least-survivable link back to a durable identity. Every provider that offers "forgot password" must, by design, be able to *give the account back to someone* — and that someone is whoever can satisfy the recovery checks. That makes recovery the highest-value, lowest-friction bypass in the system:

- **Recovery identity is broader than the password.** Phone number (SMS), recovery email, SSO identity provider, iCloud/Google account, passkeys synced to an identity cloud, backup codes stored in a screenshot — each is an alternate key that can re-enter the account.
- **The recovery oracle is a permanent human bypass.** Strong sign-in (hardware keys) raises the bar for *login*; the recovery flow is the designed exception that exists precisely so locked-out owners can get back in.

### 2. SIM swap: the canonical recovery-takeover vector

The FBI/IC3 documents the mechanism precisely: an attacker convinces the carrier to move the victim's number to a SIM in the attacker's possession (via **social engineering**, a paid carrier **insider**, or **phishing** that compromises carrier systems). "Once the SIM is swapped, the victim's calls, texts, and other data are diverted to the criminal's device. This access allows criminals to send 'Forgot Password' or 'Account Recovery' requests… Using SMS-based two-factor authentication, mobile application providers send a link or one-time passcode via text to the victim's number, now owned by the criminal." [CONFIRMED IC3 PSA I-020822-PSA, retrieved 2026-08-12]

Scale (FBI figures): 320 IC3 complaints / ~$12M adjusted losses Jan 2018–Dec 2020; **1,611 complaints / >$68M in 2021 alone**. [CONFIRMED IC3]

The defensive answer is structural, not user-education: the **FCC's December 2023 rules** require US carriers to authenticate customers with a secure method before a number is moved/ported and to notify the customer immediately on any SIM change or port-out request. [CONFIRMED FCC DOC-397990A1, retrieved 2026-08-12]

### 3. Provider recovery design (first-party, as a class)

- **Apple account recovery** — if you can't reset the password, recovery may take "several days or longer"; Apple support cannot shorten the wait; you get a confirmation email within ~72 hours and are told the expected access time; a **recovery contact** (up to five, each able to generate a six-digit code, Apple not knowing who they are) is the human fallback. [CONFIRMED Apple support 118574/102641, retrieved 2026-08-12]
- **Google Advanced Protection** — requires a passkey or security key to sign in ("unauthorized users won't be able to sign in without them, even if they know your username and password"), adds stricter download checks and restricted third-party app access; aimed at high-visibility targets (activists, journalists, campaigns). [CONFIRMED Google, retrieved 2026-08-12] The design tension: APP locks the *sign-in* door but the recovery door must still exist — so a person targeting the account targets the recovery identity (phone, backup email, enrolled keys' physical custody), not the password.

### 4. Operator steals (authorized work / personal OPSEC)

1. **Dedicated numbers and emails are identity, not convenience.** A burner phone number still anchors recovery for every account it's attached to. Treat phone + recovery email as high-value credentials: unique per persona, not reused, not posted publicly (the IC3 guidance: don't post your number/address/PII where OSINT can collect it).
2. **No SMS 2FA on high-value accounts.** SMS is the SIM-swap-interceptable channel. Use an authenticator app, a hardware security key, or passkey for anything that gates money, credentials, or a persona.
3. **Do not leak backup codes into screenshots/cloud.** A backup code in a photo library or synced note is the recovery key sitting in plaintext.
4. **Audit recovery surfaces when you inherit a persona or build a new one:** recovery email, recovery phone, enrolled devices, SSO providers, passkeys/security keys, backup codes. Each is a potential re-entry; each should be owned and controlled.
5. **Passkeys synced to an identity cloud** are only as anonymous as the cloud account they sync to — a passkey is a durable identity anchor, not an anonymity tool. Pair with @concepts/hardware-id-masking-opsec.md when the threat model includes device-based re-identification.

### 5. Product steal

**Recovery flows are an authz-bypass class in your own product.** Test them like any authentication boundary in @concepts/pre-release-product-pentest.md:

- Rate-limit and lock recovery; never let a single SMS code be the *only* re-entry path for a high-value account.
- Bind recovery to a durable, verifiable identity (e.g., a hardware key or a pre-registered recovery contact) rather than an SMS-forwardable number.
- Notify the account owner on *any* recovery action (the FCC-mandated pattern), with a cooling-off window before a number change takes full effect.
- Inventory every "alternate way in": recovery email, phone, SSO, backup codes, passkeys, device tokens. Each is a login you didn't build a UI for.

## Snippets

> "Once the SIM is swapped, the victim's calls, texts, and other data are diverted to the criminal's device. This access allows criminals to send 'Forgot Password' or 'Account Recovery' requests to the victim's email and other online accounts associated with the victim's mobile telephone number."
[Source: https://www.ic3.gov/PSA/2022/PSA220208 (retrieved 2026-08-12)]

> "Advanced Protection requires you to use a passkey or a security key to verify your identity. … unauthorized users won't be able to sign in without them, even if they know your username and password."
[Source: https://landing.google.com/advancedprotection/ (retrieved 2026-08-12)]
