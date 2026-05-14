---
title: "czkawka — Rust-based filesystem dedup/empty-dir/visual-similarity scanner (dual MIT/GPL)"
type: entity
category: tool
tags: [entity, tool, filesystem-analysis, deduplication, visual-similarity-hash, dual-license, k44, steal-from-doc-level-pending-phase-0]
keywords: [czkawka, qarmin, czkawka-core, krokiet-gui, cedinia-gui, slint-frontend, dual-license-isolation, mit-core-gpl-gui]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @image-gen-wiki/entities/tools/czkawka.md — cross-route stub (LoRA training dataset dedup)

## Raw Concept

A Rust filesystem-analysis tool that locates duplicate binaries, empty directories, and visually-similar images at high speed using memory-safe Rust. **DUAL LICENSE**: `czkawka_core` (the algorithmic library) is MIT; the Slint-based GUI frontends (Krokiet, Cedinia) are GPL-3.0. **31,000 stars** per K44 doc-level eval. K44 verdict: **Steal-from** (with strict GUI/core build isolation).

## Narrative

K44 primary fit: Cybersec-wiki (filesystem analysis for malware persistence detection, rapid hashing for anomaly detection). Cross-route: Image-gen-wiki (LoRA training dataset deduplication).

**Critical license-isolation discipline**: only `czkawka_core` may be linked into Cemini-suite or sister-wiki tooling. The GPL-3.0 GUI frontends (Krokiet/Cedinia) must remain physically un-built and uncoupled in any extraction path. **Build pipelines must explicitly target `czkawka_core` crate dependencies only** — verify via `cargo tree` that no Slint-GUI crates appear in the dependency graph.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/qarmin/czkawka`) — 31k stars is plausible (well-established project), spot-check is sufficient
- G2: Dual-license confirmation — read LICENSE + LICENSE.GPL + per-crate Cargo.toml license fields
- G3: Cargo build with `--no-default-features` + manual feature flagging to confirm `czkawka_core` builds standalone without pulling Slint
- G4: Visual-similarity hash algorithm audit — confirm perceptual-hash function used (pHash, dHash, etc.) for cross-validation against alternatives

**Use case in Cybersec**: filesystem hashing for malware persistence detection — duplicate files in unexpected locations are a sub-pattern.

**Use case in Image-gen**: LoRA training corpus dedup — preventing duplicate or visually-identical training samples that bias the resulting LoRA.

## Snippets

> "The repository functions under a precarious dual-license model. The core mathematical algorithms (czkawka_core) are MIT-licensed and safe, but the Slint-based GUI frontends (Krokiet, Cedinia) enforce the GPL-3.0 license. Extreme prejudice and rigid build isolation must be utilized to decouple the core library from the GUI to prevent IP-sale poisoning."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶338]
