---
title: CWEEP — early RTL CWE prevention via lexical static analysis
type: concept
tags: [concept, hardware-security, rtl, cwe, static-analysis]
keywords: [CWEEP, RTL, CWE early prevention, Verible, 2607.29604]
related:
  - sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md
  - entities/tools/cweep.md
  - concepts/ai-for-cybersecurity.md
  - concepts/cogate-confidence-gated-secure-code.md
  - concepts/chiplet-llm-hardware-security.md
  - sources/arxiv-2608-05063-chiplet-llm-hardware-security.md
  - concepts/rtl-codegen-poison-defense.md
maturity: draft
created: 2026-08-03
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md
- @entities/tools/cweep.md
- @concepts/ai-for-cybersecurity.md
- @concepts/cogate-confidence-gated-secure-code.md
- @concepts/chiplet-llm-hardware-security.md
- @sources/arxiv-2608-05063-chiplet-llm-hardware-security.md

## Raw Concept

Catch hardware CWEs in RTL with lexical static analysis before full security specs exist.

## Narrative

Hardware SDL often waits on heavyweight property writing. **CWEEP** shifts left: CWE-oriented Verible lint rules + localization + optional autofix. Useful when an engagement or product includes FPGA/ASIC RTL — otherwise REFERENCE. Pair software CWE decode-time gating (@concepts/cogate-confidence-gated-secure-code.md) with hardware early lint when both surfaces exist. [CONFIRMED — paper + clone README]
