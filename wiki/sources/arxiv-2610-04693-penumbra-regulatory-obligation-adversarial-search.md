---
title: "Penumbra: sample-efficient adversarial search for regulatory obligations"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.04693, k398]
related:
  - concepts/compliance-boundary-adjacent-pair-search.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/responsible-disclosure.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K398)"
---

## Relations

## Relations

- @concepts/compliance-boundary-adjacent-pair-search.md
- @concepts/threat-preserving-representation-sensitivity.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/responsible-disclosure.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Penumbra: sample-efficient adversarial search for regulatory obligations |
| arXiv | 2610.04693 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.04693-penumbra-sample-efficient-adversarial-search-for.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K398** — agents now sit under **binding professional obligations** (portfolio analysis, clinical triage) that a violation leaves **no lexical signature** for: whether an omission is material depends on what the response *left out*. Probing that boundary is expensive — every probe costs a generation plus two adjudications — so the binding constraint is **sample efficiency, not volume**. PENUMBRA walks from a **verified anchor** under an **expanding edit budget**, scoring each edit with a **three-level committee** (clear / guarded / borderline); it keeps widening while the verdict class is unchanged, so **minimality is enforced rather than filtered for** — the first class change *is* the boundary. It then emits the **adjacent pair** straddling that change: one compliant and one violating response differing by a handful of words. Coverage is the **defeat surface** — distinct (obligation × defeat mode) cells carrying a certified pair. Numbers: adaptive allocation reaches uniform allocation's **full-budget coverage on 59% of candidates**; at equal records it covers **1.43×** the defeat modes of naive enumeration; on a financial-advisory constitution it returns **144 pairs over 60 obligations** and a clinical-triage constitution **49 pairs over 18**. The committee is **frozen** (adapting either side does not repair drift). Operator steal: an obligation boundary is best tested with **adjacent pairs**, not a single judged response — and it is the pair that shows where the obligation's own terms stop deciding. Pairs K396 (representation sensitivity) and K321 (construct validity). **No policy text or probe payloads in wiki.**

## Snippets

> See arXiv 2610.04693 abstract. [Source: arXiv 2610.04693 (retrieved 2026-10-06)]
