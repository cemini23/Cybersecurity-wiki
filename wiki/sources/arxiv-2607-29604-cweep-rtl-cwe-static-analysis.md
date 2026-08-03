---
title: CWEEP RTL CWE static analysis (arXiv 2607.29604)
type: source
tags: [source, arxiv, hardware-security, rtl, cwe, static-analysis]
keywords: [2607.29604, CWEEP, RTL, CWE, Verible, hardware security]
related:
  - concepts/cweep-rtl-cwe-early-prevention.md
  - entities/tools/cweep.md
  - concepts/ai-for-cybersecurity.md
  - concepts/cogate-confidence-gated-secure-code.md
maturity: draft
read_status: read
created: 2026-08-03
updated: 2026-08-03
phase_0_verdict: "CONDITIONAL-GO 2026-08-03 — Apache-2.0 Verible fork; ~15MB; hardware RTL lab only"
wire_status: deferred
wire_target: "lab RTL lint only — no Cursor alwaysApply"
---

**Briefs:** `briefs/2026-08-03_k233-cweep-prod.md`

## Relations

- @concepts/cweep-rtl-cwe-early-prevention.md
- @entities/tools/cweep.md
- @concepts/ai-for-cybersecurity.md
- @concepts/cogate-confidence-gated-secure-code.md — software CWE co-decoding sibling theme

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention |
| Authors | Bryan Kwan, Benjamin Tan (U Calgary) |
| arXiv | 2607.29604 |
| Code | https://github.com/bryan-kwan/cweep (Apache-2.0 Verible fork) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.29604-cweep-a-lexical-static-analysis-framework-for-cw.pdf` |
| Retrieved | 2026-08-03 |

## Narrative

Lexical/static **RTL** checkers for hardware CWEs without needing a full security specification — usable early while properties are still under construction. Localizes the offending RTL site and can suggest autofix patches. Eval: up to **60.8%** correct warnings vs **17.5%** for a prior tool on the same dataset; also tested on HACK@DAC SoCs and an LLM-generated 3874-module buggy set. [CONFIRMED abstract + Phase-0 README]

### Steal

1. Run CWE-class lint **before** full SDL property packs exist
2. Prefer tools that **localize** the RTL line, not only emit design-level alerts
3. Autofix is assistive — re-verify (subset auto-fixes fail when pattern ⊆ larger weakness)

### Phase-0

**CONDITIONAL-GO** — clone for owned RTL lab only; not a Cursor/agent runtime wire.

## Snippets

> "CWEEP does not require a detailed security specification, so it can be used in the early stages of RTL development while properties are still under construction."
[Source: arXiv 2607.29604 abstract]
