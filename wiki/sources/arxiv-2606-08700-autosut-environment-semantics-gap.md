---
title: AutoSUT — environment semantics gap in structured CTI (arXiv 2606.08700)
type: source
tags: [source, arxiv, threat-intel, stix, mitre-attack, adversary-emulation, cyber-range]
keywords: [2606.08700, autosut, environment semantics gap, sut, stix, cpe, cve, replay-ready]
related:
  - entities/tools/autosut.md
  - concepts/adversary-emulation.md
  - concepts/threat-intelligence.md
  - concepts/threat-hunting.md
  - entities/frameworks/mitre-attack.md
  - sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
maturity: draft
read_status: read
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @entities/tools/autosut.md — measurement pipeline + GitHub reproducibility artifact
- @concepts/adversary-emulation.md — replay-ready SUT commitments vs analyst-authored region
- @concepts/threat-intelligence.md — structured CTI limits for environment narrowing
- @entities/frameworks/mitre-attack.md — Enterprise/Mobile/ICS STIX bundle analysis anchor
- @sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md — complementary AI-emulation fidelity axis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AutoSUT: The Environment Semantics Gap in Structured CTI for Adversary Emulation |
| Authors | Sidnei Barbieri, Ágney Lopes Roth Ferraz, Lourenço Alves Pereira Júnior (ITA) |
| arXiv | 2606.08700 |
| Code | https://github.com/sidneibarbieri/autosut-reproducibility-artifact |
| Location | `raw-sources/arxiv-2606.08700-autosut-the-environment-semantics-gap-in-structu.pdf` |
| Retrieved | 2026-06-11 |
| Read status | **read** |

## Narrative

Defines the **environment semantics gap**: SUT information required for a replay-ready adversary-emulation environment that **cannot be derived from public ATT&CK-style STIX alone**. AutoSUT measures where corpus-supported narrowing ends and analyst specification begins [CONFIRMED].

### Key measurements (ATT&CK Enterprise v18.1 primary)

| Metric | Finding |
|--------|---------|
| Platform tags | Common but coarse — 100% of 691 active techniques have `x_mitre_platforms`; structured `platform` field 0% |
| Software specificity | **97.6%** of software objects lack both version and CPE |
| CVE evidence | Sparse, fragmented between structured fields and free text |
| Profile confusion | **1.3%** at one linked software item → **0%** at two |
| Non-uniqueness | Section 7 witness: same campaign-compatible CTI supports multiple distinct SUTs including executable **CVE-2021-41773** replay |

Contrast datasets: CAPEC, FiGHT (5G) — same pattern: platform evidence moderate, CVE-linked coverage low.

### Operational implication

Structured CTI **narrows** backend-family and lower-bound environment claims but does **not uniquely determine** replay-ready SUTs. Emulation plans must declare which environment commitments the corpus supports vs analyst-authored (versions, vuln state, exposure surface).

Pairs with @sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md — even correct TTP procedure fails reproducibility when SUT is wrong; AI emulation adds persona convergence on top of CTI environment gap.

## Snippets

> "Structured CTI, therefore, constrains but does not uniquely determine the environment."
> — [Source: arxiv-2606.08700 abstract, retrieved 2026-06-11]

> "In Enterprise, 97.6% of software objects lack both [version and CPE]."
> — [Source: arxiv-2606.08700 abstract, retrieved 2026-06-11]

## Dead Ends

- **Assuming STIX bundle → lab topology** without external enrichment — gap is quantified, not hypothetical.
- **Single software link for attribution/emulation profile** — confusion remains until ≥2 anchored software/CVE items.
