---
title: "Minecraft Bedrock add-on distribution integrity"
type: concept
tags: [concept, supply-chain, code-integrity, bedrock, minecraft]
keywords: [bedrock, behavior pack, resource pack, script module, manifest, mcpedl, curseforge, addon supply chain]
related:
  - concepts/product-build-integrity-slsa-sigstore.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/mobile-app-attestation.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (Basgiath add-on)"
---

## Relations

- @concepts/product-build-integrity-slsa-sigstore.md — release-artifact integrity: what signing buys
- @concepts/coding-agent-supply-chain-install-gap.md — install-time trust for third-party code
- @concepts/mobile-app-attestation.md — platform attestation vs a user-installed artifact

## Raw Concept

Question: **what runs on a player's device when they install a third-party Minecraft Bedrock add-on, and what should a publisher or an installer check?**

Raised by the **Basgiath** project (`OSINT WORKSPACE/agents/dragon-rider-map/`), a free fan-made
Bedrock map and add-on distributed through MCPEDL and CurseForge.

## Narrative

A Bedrock add-on is a zip of packs. A **behavior pack** may include a `script` module: JavaScript that
runs on the player's device, not on a server. Installing a third-party add-on is therefore an
**install-time trust decision over someone else's executable code**, the same class as installing an npm
package or a browser extension — with the difference that the distribution channel is a community file
host, not a package registry with provenance tooling.

### What to read in a manifest

The relevant fields live in the behavior pack's `manifest.json`. Read them before installing anything
third-party, and keep them minimal when publishing:

| Field | Why it matters |
|-------|----------------|
| `modules[].type` | `script` means code executes on the player's device. `data` and `resource` are inert content. |
| `modules[].entry` | The script path. Read the file. A pack whose script is not readable is not reviewable. |
| `dependencies[]` | Pins the `@minecraft/server` version. An unpinned or mismatched API version changes behaviour across engine updates. |
| `capabilities` | Bedrock allows a pack to declare elevated capabilities. Treat any request beyond what the pack needs as a red flag. `[NEEDS VERIFICATION 2026-10-06]` — confirm the exact accepted values against current Bedrock docs before relying on this. |
| `uuid` / `header.version` | Fixed UUIDs colliding with another installed pack cause undefined behaviour. Version is the pack's own, not a signature. |

### The distribution gap

Free community hosting gives **no signature and no provenance**. A repost — the normal way files spread
on MCPEDL and CurseForge — is byte-indistinguishable from the original to the end user. The download
page is the only trust anchor. This is exactly the gap @concepts/product-build-integrity-slsa-sigstore.md
describes for software releases, minus the tooling: Bedrock has no SLSA-equivalent attestation for
third-party add-ons. `[NEEDS VERIFICATION 2026-10-06]` — re-check whether the Marketplace's curated
channel carries any verification that free channels do not.

### Install review (defender)

Before installing a third-party Bedrock add-on:

1. Read `manifest.json`. Is there a `script` module? If not, the supply-chain risk is content-only.
2. If there is, read the entry script. Note every import and every outbound call.
3. Check the script API version against the engine you run.
4. Prefer a pack whose publisher ships a source repo you can compare the zip against.
5. Install on a throwaway world first. A script module runs with the game's privileges on your device.

### Publish checklist (the Basgiath case)

For a free fan add-on publishing through MCPEDL / CurseForge:

- Ship the **minimum** module set. A `data`-only pack avoids the trust problem entirely; add `script`
  only where the feature needs it.
- **Pin** the `@minecraft/server` version and say which engine version you tested.
- **No network calls, no dynamic evaluation, no obfuscated code** in a fan add-on. Each is hard to
  justify and each is what makes a review impossible.
- Publish the **source** next to the `.mcaddon` so a user can diff it.
- Keep the "not official / not affiliated" notice — that is an **IP** control, not a security one, but
  it is the control that keeps the project alive (see the project's own `docs/IP-RULES.md`).

The Basgiath `behavior_pack/manifest.json` as of 2026-10-06 declares a `data` module and a `script`
module (entry `scripts/main.js`) against `@minecraft/server` and `@minecraft/server-ui` **2.0.0**, and
declares **no** `capabilities`. The script is a plain import of those two modules with no network or
evaluation calls — a benign shape. Re-check on each release.

## Snippets

> A `script` module means someone else's JavaScript runs on your device when you load the world.

