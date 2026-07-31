---
title: "czkawka — Rust filesystem dedup + perceptual-hash scanner (clean MIT source + LGPL/MPL transitive contamination)"
type: entity
category: tool
tags: [entity, tool, filesystem-analysis, deduplication, perceptual-hash-bk-tree, k44, steal-from-conditional-phase-0-2026-05-14, k44-license-split-wrong, lgpl-mpl-transitive-contamination, python-fallback-imagehash-pybktree]
keywords: [czkawka, qarmin, czkawka-core, krokiet-gpl, cedinia-gpl, similar-values-threshold-table, blake3-xxh3-crc32, rawler-lgpl-symphonia-mpl, python-port-imagehash-pybktree-xxhash]
related:
  - concepts/malware-analysis.md
maturity: validated
created: 2026-05-14
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
wire_status: wont_wire
wire_target: "STEAL-FROM-CONDITIONAL — Python port recommended"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @image-gen-wiki/entities/training-tools/czkawka.md — cross-route stub (LoRA training dataset dedup)
- @concepts/malware-analysis.md — filesystem dedup + broken-file scanning supports malware-sample triage
## Raw Concept

A Rust filesystem-analysis tool for duplicate detection, perceptual-hash similar-image detection (BK-tree), audio fingerprinting, and broken-file scanning. **31,006 stars, 1,044 forks, 5y old, last push 2026-05-11**. K44 doc-level license-split framing was **materially wrong** — see verdict.

## Narrative

### Phase-0 audit verdict (2026-05-14): STEAL-FROM-CONDITIONAL (Python port recommended)

**Two critical K44 corrections (G4 + G9): the K44 license-split framing is wrong.**

1. **K44 said `czkawka_gui` is GPL-3.0 — it's actually MIT.** The real GPL-3.0 crates are `krokiet` (Slint UI) and `cedinia` (Android app), NOT `czkawka_gui` (GTK4 frontend, MIT).
2. **K44 missed transitive-license contamination**: `czkawka_core` declares MIT, but pulls `rawler` (LGPL-2.1, weak copyleft — dynamic-link / file-replacement obligations) and `symphonia` (MPL-2.0, file-level copyleft) as direct deps. The "clean MIT core" framing only holds at the source-text level; at the linked-binary level, czkawka_core pulls LGPL+MPL.

| Crate | Cargo.toml license | Actual content |
|-------|-------------------|----------------|
| `czkawka_core/` | MIT | MIT LICENSE_MIT verbatim, (c) 2020-2026 Rafał Mikrut |
| `czkawka_cli/` | MIT | MIT |
| **`czkawka_gui/`** | **MIT** | **NOT GPL — K44 wrong** (GTK4 frontend) |
| `krokiet/` | GPL-3.0-only | Slint UI frontend |
| `cedinia/` | GPL-3.0-only | Android app |

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo clones | **PASS** | `qarmin/czkawka` clean |
| G1 | License file matches Cargo.toml (core) | **PASS** | MIT verbatim |
| G2 | Cargo license accurate per crate | **PASS** | All 5 crates correctly declared |
| G3 | Reverse-imports absent | **PASS — CLEAN** | Zero `use krokiet::` / `use cedinia::` / `use czkawka_gui::` in czkawka_core/ |
| G4 | **Transitive deps permissive** | **FAIL — LGPL+MPL CONTAMINATION** | `rawler = "0.7.0"` is LGPL-2.1; `symphonia = "0.5" features = ["all"]` is MPL-2.0; `nom-exif` non-standard registry flag |
| G5 | Maturity | **PASS** | 31,006★, 5y old, commits today |
| G6 | Single-author risk | **WARN** | Rafał Mikrut ~83% of commits; bus factor 1 (90 occasional contributors) |
| G7 | Functionality matches claim | **PASS** | dup / similar-image / similar-video / audio / empty / temp / broken — all in `tools/` |
| G8 | Novel IP worth extracting | **PARTIAL** | Hand-tuned `SIMILAR_VALUES[4][6]` perceptual-hash threshold table is the real IP |
| G9 | K44 license claim accuracy | **FAIL** | K44 said GUI is GPL; it's MIT. K44 missed LGPL+MPL transitives entirely |

### Recommended path: clean-room Python port (avoid Rust vendor entirely)

**DO NOT vendor czkawka_core as a Rust dependency** — `rawler` (LGPL) + `symphonia` (MPL) will follow into the link graph. Instead, transcribe the algorithmic patterns + threshold table into a Python implementation using BSD/MIT building blocks.

### High-leverage extractable IP (MIT-attributed)

1. **`SIMILAR_VALUES[4][6]` threshold table** + `SimilarityPreset` enum (`czkawka_core/src/tools/similar_images/mod.rs:26-32` and `tools/duplicate/core.rs:6-13`) — hand-tuned `(hash_size ∈ {8,16,32,64}) × (preset ∈ Minimal..VeryHigh)` Hamming-distance cutoffs. **The actual novel IP**. Transcribe with attribution `[Source: czkawka_core/src/tools/similar_images/mod.rs (MIT)]`. **Sub-1h** in Python.
2. **Multi-stage dedup pipeline** (`czkawka_core/src/tools/duplicate/core.rs`) — name → size → prehash → full hash. Pattern, not code. **1–2h** in Python with `xxhash` (BSD) + `blake3` (CC0).
3. **pHash + BK-tree similar-images** (`czkawka_core/src/tools/similar_images/`) — image perceptual hashing + BK-tree fast Hamming lookup. **3–5h** in Python using `imagehash` (BSD) + `pybktree` (MIT).
4. **Parallel rayon walker with hardlink-grouping** (`czkawka_core/src/common/dir_traversal.rs:take_1_per_inode`) — generic concept; ~1h via `concurrent.futures` + `os.stat().st_ino` grouping.

### DO NOT TOUCH

- `krokiet/**` (GPL-3.0-only Slint UI)
- `cedinia/**` (GPL-3.0-only Android)
- `czkawka_core/src/common/image.rs` if it uses `rawler` (LGPL — confirm scope before transcribing)
- Any modified `symphonia` source (MPL file-level reciprocity)

### Recommended Python building blocks (all BSD/MIT/CC0)

- `imagehash` (BSD) — pHash, dHash, wHash
- `pybktree` (MIT) — BK-tree for Hamming-distance nearest-neighbor
- `xxhash` (BSD) — fast non-cryptographic hash
- `blake3` (CC0) — cryptographic hash, fastest of its class

Combine these with the transcribed `SIMILAR_VALUES` threshold table → **complete Python equivalent in 5–8 hours total**, with zero LGPL/MPL/GPL contamination.

### Final verdicts

- **Cybersec-wiki**: **STEAL-FROM-CONDITIONAL** — pattern-level extraction safe under MIT. Cybersec use case: forensic deduplication of case-file evidence + exhibit-image dedup.
- **Image-gen-wiki**: **STEAL-FROM-CONDITIONAL** (cross-route) — LoRA model deduplication, ComfyUI output dedup, training-dataset cleanup. Same Python-port path applies.

## Snippets

> "The repository functions under a precarious dual-license model. The core mathematical algorithms (czkawka_core) are MIT-licensed and safe, but the Slint-based GUI frontends (Krokiet, Cedinia) enforce the GPL-3.0 license. Extreme prejudice and rigid build isolation must be utilized to decouple the core library from the GUI to prevent IP-sale poisoning."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶338 — Phase-0 audit confirms the *concept* of dual-license isolation but corrects two K44 errors: (1) `czkawka_gui` is MIT not GPL (only `krokiet`/`cedinia` are GPL); (2) K44 missed transitive `rawler` (LGPL-2.1) + `symphonia` (MPL-2.0) contamination inside czkawka_core. Recommended path: Python port using imagehash + pybktree + xxhash, skip the Rust dep entirely.]
