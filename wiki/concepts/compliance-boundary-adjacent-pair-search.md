---
title: "Compliance boundary testing by adjacent pairs (K398)"
type: concept
tags: [concept, agent-security, k398]
keywords: [2610.04693, K398]
related:
  - sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/responsible-disclosure.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K398)"
---

## Relations

- @sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md
- @concepts/threat-preserving-representation-sensitivity.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/responsible-disclosure.md

## Raw Concept

Question: **Compliance boundary testing by adjacent pairs** — operator steal from arXiv 2610.04693?

## Narrative

A regulatory obligation is decided by **what a response omits**, so it leaves no keyword to grep for. Test it by walking from a verified-compliant anchor under a growing edit budget and stopping at the **first verdict change** — that gives two adjacent responses straddling the boundary, differing by a few words. Minimality is then a property of the search, not a filter applied after it. Score coverage as **distinct (obligation × defeat mode) cells** holding a certified pair, not as a count of probes. Freeze the judging committee: if it adapts with the search, the boundary moves with it. Complements K396 — both replace a single judged score with a controlled comparison.

## Snippets

> See arXiv 2610.04693 abstract. [Source: arXiv 2610.04693 (retrieved 2026-10-06)]
