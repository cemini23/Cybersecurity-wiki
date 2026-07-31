---
title: "m4xx101/cryptex-oss — LLM red-teaming technique toolkit"
type: entity
tags: [tool, llm-security, red-team, adversarial, typescript, mit, adopt-eligible]
keywords: [cryptex-oss, llm red team, prompt transforms, mutators, jailbreak, fuzzing]
related:
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/red-team-operations.md
  - concepts/responsible-disclosure.md
  - entities/tools/fuzzyai.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - entities/tools/leakbench-area.md
maturity: draft
created: 2026-05-26
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md"
phase_0_verdict: "Adopt-eligible 2026-05-26 — MIT verified; queue Phase-0 alongside FuzzyAI for transform/mutator catalog comparison."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

# m4xx101/cryptex-oss — LLM red-teaming technique toolkit

## Relations

- @concepts/llm-adversarial-fuzzing.md — methodology umbrella for LLM-target offensive testing
- @concepts/ai-for-cybersecurity.md — LLM security discipline context
- @concepts/red-team-operations.md — authorized LLM robustness engagements
- @concepts/responsible-disclosure.md — ethics floor for adversarial prompt research
- @entities/tools/fuzzyai.md — primary incumbent LLM fuzzer; compare attack-method coverage vs cryptex transform catalog

## Raw Concept

Routed from K68 OSINT-wiki brief (`briefs/2026-05-26_k68-cybersec-tool-eval-from-osint.md`, 2026-05-26). TypeScript LLM red-teaming toolkit: **162 transforms**, **36 mutators**, **25 tool surfaces**. MIT, ~66 stars. **Adopt-eligible** — Phase-0 queue.

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/cryptex-oss` (~11MB, shallow). Compare transform catalog vs FuzzyAI in lab.


`m4xx101/cryptex-oss` catalogs **prompt transforms and mutators** for LLM red-teaming — a composable technique library rather than a single end-to-end fuzz loop. Overlaps @entities/tools/fuzzyai.md (18 named attack methods + PAIR/Crescendo) but emphasizes breadth of encoding/obfuscation/surface variants.

**Comparison axis for Phase-0**:

| Tool | Strength | Gap |
|---|---|---|
| FuzzyAI | PAIR/Crescendo research anchors, CyberArk maintenance | Narrower transform catalog |
| cryptex-oss | 162 transforms + 36 mutators | Smaller community; Phase-0 lab validation pending |

**Adoption gate**: MIT license clean. Run side-by-side jailbreak campaigns on an authorized test LLM before choosing primary framework or documenting when to use each.

## Dead Ends

- **Treating transform count as quality proxy** — 162 transforms ≠ 162 effective attacks; benchmark catch-rate on your target model class before standardizing.
- **Using on production LLM APIs without rate-limit + scope controls** — mutator chains can trigger provider abuse flags; isolate to authorized test endpoints.
