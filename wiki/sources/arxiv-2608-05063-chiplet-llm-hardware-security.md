---
title: Hardware design and security in the era of chiplets and LLMs (arXiv 2608.05063)
type: source
tags: [source, arxiv, hardware-security, chiplet, llm, eda]
keywords: [2608.05063, chiplet, 2.5D, LLM-EDA, Root of Trust, split manufacturing]
related:
  - concepts/chiplet-llm-hardware-security.md
  - concepts/cweep-rtl-cwe-early-prevention.md
  - entities/tools/cweep.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: "REFERENCE 2026-08-06 — survey/position; no code"
wire_status: wont_wire
wire_target: "REFERENCE"
---

**Briefs:** `briefs/2026-08-06_k247-chiplet-llm-hw-prod.md`

## Relations

- @concepts/chiplet-llm-hardware-security.md
- @concepts/cweep-rtl-cwe-early-prevention.md
- @entities/tools/cweep.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Hardware Design and Security in the Era of Chiplets and LLMs |
| Authors | Knechtel, Sinanoglu, Gratz, Karri |
| arXiv | 2608.05063 |
| Code | none |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.05063-hardware-design-and-security-in-the-era-of-chipl.pdf` |
| Retrieved | 2026-08-06 |

## Narrative

Unified analysis of two expansions of the hardware attack surface: **heterogeneous 2.5D chiplet** systems (incl. LLM accelerators) and **LLM-driven EDA** pipelines. Defenses reviewed: 2.5D split manufacturing + active interposers for isolated RoT; native threats + SOTA defenses for LLM-EDA; how LLMs can also advance hardware security. [CONFIRMED abstract]

### Steal

1. Chiplet + LLM-EDA = expanded supply-chain / EDA trust surface — threat-model both
2. Pair CWEEP early RTL CWE lint with chiplet/EDA LLM risk awareness when RTL is in scope

## Snippets

> "they radically expand the hardware attack surface."
[Source: arXiv 2608.05063 abstract]
