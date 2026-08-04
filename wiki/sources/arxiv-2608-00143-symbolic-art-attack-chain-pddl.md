---
title: Symbolic ART attack-chain PDDL granularity (arXiv 2608.00143)
type: source
tags: [source, arxiv, adversary-emulation, atomic-red-team, pddl, planning]
keywords: [2608.00143, Atomic Red Team, PDDL, AALM, AURORA, Fast Downward]
related:
  - concepts/symbolic-art-attack-chain-granularity.md
  - concepts/adversary-emulation.md
  - concepts/red-team-operations.md
  - entities/tools/caldera.md
  - entities/frameworks/mitre-attack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-04
updated: 2026-08-04
phase_0_verdict: "REFERENCE 2026-08-04 — no public code located"
wire_status: wont_wire
wire_target: "REFERENCE — methodology only"
---

**Briefs:** `briefs/2026-08-04_k236-symbolic-art-attack-chain-prod.md`

## Relations

- @concepts/symbolic-art-attack-chain-granularity.md
- @concepts/adversary-emulation.md
- @concepts/red-team-operations.md
- @entities/tools/caldera.md
- @entities/frameworks/mitre-attack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Symbolic Attack Chain Generation from Atomic Red Team Techniques: An Empirical Study of Predicate Representation Granularity |
| Authors | Ramya Varunsegar (Newcastle) |
| arXiv | 2608.00143 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.00143-symbolic-attack-chain-generation-from-atomic-red.pdf` |
| Retrieved | 2026-08-04 |

## Narrative

LLM translates Atomic Red Team techniques → PDDL predicates; Fast Downward plans attack chains. Compares AURORA-style **9-category AALM** vs empirically reduced **5-category** scheme from ART execution evidence. On a 16-technique corpus, plan validity/cost largely insensitive to granularity (**81.3%** identical outcomes); finer predicates mainly improve internal justification structure, not chain viability. [CONFIRMED abstract]

### Steal

1. Prefer executable ART/Caldera evidence when choosing predicate schemas — do not assume 9-way AALM is required
2. Eval planner quality on validity/cost **and** fidelity of justification, separately
3. LLM translation + deterministic planner remains the safe hybrid (hallucination contained to encoding)

## Snippets

> "plan validity and cost are largely insensitive to granularity, with 81.3% identical outcomes across both schemes."
[Source: arXiv 2608.00143 abstract]
