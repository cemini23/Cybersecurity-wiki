---
title: AutoSUT — structured CTI environment-semantics measurement (Reference)
type: entity
tags: [tool, reference, threat-intel, stix, mitre-attack, adversary-emulation]
keywords: [autosut, sidneibarbieri, environment semantics gap, stix measurement, sut profiling]
related:
  - sources/arxiv-2606-08700-autosut-environment-semantics-gap.md
  - concepts/adversary-emulation.md
  - concepts/threat-intelligence.md
  - entities/frameworks/mitre-attack.md
  - sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md
  - concepts/llm-cve-to-stix-generation.md
  - entities/tools/cav-stixgen.md
  - sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md
maturity: draft
created: 2026-06-11
updated: 2026-07-20
phase_0_verdict: "Reference 2026-06-11 — reproducibility artifact on GitHub; measurement-only pipeline, no runtime deploy."
---

## Relations

- @sources/arxiv-2606-08700-autosut-environment-semantics-gap.md — paper + RQ definitions
- @concepts/adversary-emulation.md — declare corpus-supported vs analyst-authored SUT commitments
- @entities/frameworks/mitre-attack.md — STIX bundle inputs (Enterprise v18.1 primary)
- @concepts/llm-cve-to-stix-generation.md — complementary LLM STIX generation limits
- @entities/tools/cav-stixgen.md
- @sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md

## Raw Concept

Daily digest ingest (2026-06-11). GitHub: [sidneibarbieri/autosut-reproducibility-artifact](https://github.com/sidneibarbieri/autosut-reproducibility-artifact) — arXiv:2606.08700.

## Narrative

**Reference** measurement pipeline quantifying the **environment semantics gap** in public ATT&CK-style STIX: how far structured CTI narrows System-Under-Test (SUT) claims before analysts must supply versions, CVE state, and deployment detail.

**Use cases (purple/red planning):**
- Justify external enrichment steps in emulation plans (why STIX → lab is not automatic)
- Document lower-bound backend-family claims backed by corpus vs hand-waved environment assumptions
- Pair with detection-eval / cyber-range design when representativeness depends on SUT fidelity

**Not** an exploit generator or red-team execution platform — locates CTI boundary only.

## Snippets

Outputs: platform coverage, software CPE/version sparsity (97.6% lack both in Enterprise), profile confusion metrics, non-uniqueness witness (CVE-2021-41773).

## Dead Ends

- **AutoSUT output as sole SUT spec** — analyst-authored region remains mandatory for replay-ready labs.
