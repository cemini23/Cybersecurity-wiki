---
title: Taxonomy-driven mapping of OSS AI risk mitigation tools
type: concept
tags: [concept, ai-governance, llm-security, tooling-landscape, lab]
keywords: [ShieldAI, MIT AI risk taxonomy, tool coverage gaps, layered mitigation, 2608.07446]
related:
  - sources/arxiv-2608-07446-shieldai-oss-ai-risk-tools.md
  - entities/tools/shieldai-risk-taxonomy-mapping.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/post-training-adaptation-taxonomy.md
  - entities/tools/fuzzyai.md
maturity: draft
created: 2026-08-10
updated: 2026-08-10
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2608-07446-shieldai-oss-ai-risk-tools.md
- @entities/tools/shieldai-risk-taxonomy-mapping.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md
- @concepts/post-training-adaptation-taxonomy.md
- @entities/tools/fuzzyai.md

## Raw Concept

Select and compose open-source LLM eval/guardrail/observability tools by **taxonomy coverage**, not stars alone; expect governance/legal gaps that require HITL/org process.

## Narrative

Useful when stocking the local abliterated lab or pre-release product pentest stack: map each candidate (Garak, Promptfoo, PyRIT, NeMo Guardrails, Langfuse, …) to explicit risk subcategories; treat LLM-assisted capability extraction as provisional until human adjudicated. Do not assume tooling covers board oversight, whistleblower, or market-risk controls. Layered architecture: pre-deploy eval → runtime guardrails → observability → human oversight. REFERENCE matrices live under `raw-sources/repos/ShieldAI`. [CONFIRMED]
