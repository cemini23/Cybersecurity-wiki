---
title: LLM research competency model (eight competencies)
type: concept
tags: [llm-literacy, research-methods, education, oversight]
keywords: [domain expertise, metacognition, AI literacy, reproducibility, prompt engineering]
related:
  - sources/arxiv-2607-16083-llm-research-competencies.md
  - concepts/ai-for-cybersecurity.md
  - concepts/cybersecurity-careers.md
  - concepts/llm-cve-to-stix-generation.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/arxiv-2607-16083-llm-research-competencies.md — rapid review + Zenodo pack
- @concepts/ai-for-cybersecurity.md — analyst oversight of LLM security outputs
- @concepts/cybersecurity-careers.md — training ladder
- @concepts/llm-cve-to-stix-generation.md — CTI generation needs domain oversight

## Raw Concept

Using LLMs for research (including security research and CTI drafting) is not primarily a prompt-engineering problem. Evidence from a 40-paper rapid review centers **human accountability**: domain expertise + skepticism first; AI literacy without domain mastery is an explicit risk.

## Narrative

### Eight competencies (priority for training)

1. **Domain expertise + oversight of AI outputs** — verify, don't trust
2. **Metacognition** — decide when AI helps vs when it contaminates method
3. **Ethics / integrity** — plagiarism, sensitive data, disclosure
4. **Prompt engineering for research** — constraints, datasets, workflows
5. **Reproducibility** — log model, params, prompts
6. **Study design** — plan AI use into methodology up front
7. **AI literacy / technical knowledge** — necessary but insufficient alone
8. **Analytical support** — code/stats assist with human final say

### Local artifact

Zenodo replication pack (CC-BY-4.0) at `raw-sources/repos/llm-research-competencies-zenodo` (~396KB) — coding CSVs + protocol for rubric reuse.
