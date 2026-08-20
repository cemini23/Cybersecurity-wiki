---
title: "Knowledge-driven detection-rule grounding (CTI → Sigma)"
type: concept
tags: [concept, detection-engineering, sigma, cti, k297]
keywords: [AUTOSIGMA, template-based rule grounding, LLM-as-a-Judge, Sigma validity]
related:
  - sources/arxiv-2608-19011-ti-to-detection-rule-grounding.md
  - concepts/threat-intelligence.md
  - concepts/threat-hunting.md
  - concepts/soc-operations.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K297); optional lab note"
---

## Relations

- @sources/arxiv-2608-19011-ti-to-detection-rule-grounding.md
- @concepts/threat-intelligence.md
- @concepts/threat-hunting.md
- @concepts/soc-operations.md

## Raw Concept

How to turn narrative CTI into detection content without hallucinated Sigma.

## Narrative

Manual Sigma authoring does not scale with APT reporting cadence. Raw LLM generation produces syntactically pretty rules that miss IoCs, invent fields, or ignore ATT&CK coverage. AUTOSIGMA's three-part answer:

1. **Enrich** sparse CTI against an external cyber knowledge base (fill missing steps / aliases).
2. **Ground** generation in retrieved, already-validated Sigma templates (syntax + industry shape).
3. **Judge** with a dual-LLM loop that scores validity / relevancy separately from coverage.

[Source: arXiv 2608.19011]

**SOC implication:** generated rules are *candidates*. Deploy only after human review against your telemetry schema. Measure IoC coverage, MITRE technique coverage, semantic relevancy, and syntactic validity as **four** numbers — not one "the LLM wrote a rule" boolean. Pair with Pyramid-of-Pain hygiene: IoC-only rules rot; template-grounded behavioral detections last longer (related GraphRAG CTI work is a different paper).

**Phase-0:** REFERENCE; no public code; no auto-deploy to Wazuh/Splunk.

## Snippets

> Crafting Sigma rules manually is labor-intensive and error-prone. Automating this pipeline from raw CTI text to relevant Sigma rules remains an open challenge. [Source: arXiv 2608.19011 §I]
