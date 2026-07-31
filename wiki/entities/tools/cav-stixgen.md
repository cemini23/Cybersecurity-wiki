---
title: CAV-STIXGen — CAV CVE→STIX benchmark (Reference)
type: entity
category: tool
tags: [entity, tool, stix, cti, dataset, reference, open-weight]
keywords: [CAV-STIXGen, figshare, STIX 2.1, autonomous vehicle CVE]
related:
  - sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md
  - concepts/llm-cve-to-stix-generation.md
  - concepts/threat-intelligence.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/autosut.md
maturity: draft
created: 2026-07-20
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-20 — figshare share-link only; license/size unverified; no local clone"
wire_status: deferred
wire_target: "figshare license check before any download"
---

## Relations

- @sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md — paper
- @concepts/llm-cve-to-stix-generation.md — methodology
- @concepts/threat-intelligence.md
- @entities/frameworks/mitre-attack.md
- @entities/tools/autosut.md — complementary STIX quality measurement

## Raw Concept

Academic benchmark + prompts/scripts for evaluating open-weight LLMs on automotive CVE→STIX 2.1 generation. Claimed release: figshare share `29f4ceff6bb1c6de5700`.

## Narrative

### Phase-0 (2026-07-20): REFERENCE

| Gate | Status |
|------|--------|
| Public GitHub | **Missing** |
| Figshare | Private share URL; HTML WAF challenge on curl; API search no public hit |
| License | **Unknown** until share opens |
| Size | **Unknown** — skip local adopt pending license + ≤500MB check |
| Failure mode | Unverified STIX gold; ATT&CK incomplete even on best models |
| Verdict | **REFERENCE** — use published metrics + prompting ladder; do not treat LLM STIX as TIP-ready |

### Use without clone

- Steal DFS prompting structure for any CVE→STIX lab
- Gate automation on SRO + ATT&CK Match@All
- Revisit adopt when figshare publishes a citable DOI + license
