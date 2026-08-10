---
title: ShieldAI taxonomy-driven OSS AI risk tools (arXiv 2608.07446)
type: source
tags: [source, arxiv, ai-governance, llm-security, tooling-landscape]
keywords: [2608.07446, ShieldAI, MIT AI risk taxonomy, Promptfoo, Garak, PyRIT, NeMo Guardrails]
related:
  - concepts/taxonomy-driven-oss-ai-risk-mitigation.md
  - entities/tools/shieldai-risk-taxonomy-mapping.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-10
updated: 2026-08-10
phase_0_verdict: "GO 2026-08-10 — Apache-2.0 mapping repo ~896KB (prompts + matrices + notebooks). REFERENCE adopt; no runtime MCP."
wire_status: wont_wire
wire_target: "REFERENCE clone; concept policy_wired"
---

**Briefs:** `briefs/2026-08-10_k266-shieldai-prod.md` · local-lab

## Relations

- @concepts/taxonomy-driven-oss-ai-risk-mitigation.md
- @entities/tools/shieldai-risk-taxonomy-mapping.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools |
| Authors | Alam, Popchanovska, Gjorgjevikj, Rizinski, Chitkushev, Vodenska, Trajanov |
| arXiv | 2608.07446 |
| Code | https://github.com/afreen99/ShieldAI-A-Taxonomy-Driven-Analysis-of-Open-Source-AI-Risk-Mitigation-Tools @ `400bcbc` · Apache-2.0 · local `raw-sources/repos/ShieldAI` (~896KB) |
| Dashboard | https://afreen99.github.io/ShieldAI-A-Taxonomy-Driven-Analysis-of-Open-Source-AI-Risk-Mitigation-Tools/ |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.07446-taxonomy-driven-analysis-of-open-source-ai-risk.pdf` |
| Retrieved | 2026-08-10 |

## Narrative

Maps **21** OSS LLM eval/security/observability tools (Promptfoo, DeepEval, Garak, PyRIT, NeMo Guardrails, Langfuse, Arize Phoenix, …) onto **32** subcategories of an extended MIT AI Risk Mitigation taxonomy via LLM+RAG extraction + 3-rater validation (Fleiss κ≈0.509; majority-vote F1≈75.5%). Landscape is skewed toward technical/operational controls; governance, legal/regulatory, and financial/market controls stay largely unaddressed by code-level tools → layered architecture with human/org processes required. [CONFIRMED]

## Snippets

> Tools clustered around technical and operational controls … while governance oversight, legal and regulatory remedies, and financial and market controls remain largely unaddressed by code-level mechanisms. [Source: arxiv.org/abs/2608.07446 abstract]
