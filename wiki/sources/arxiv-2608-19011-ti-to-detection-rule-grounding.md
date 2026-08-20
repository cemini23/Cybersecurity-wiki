---
title: "AUTOSIGMA — CTI to Sigma via knowledge enrichment + template grounding (arXiv 2608.19011)"
type: source
tags: [source, arxiv, detection-engineering, sigma, cti, k297]
keywords: [2608.19011, AUTOSIGMA, Sigma, CTI, LLM-as-a-Judge, Concordia, Ericsson]
related:
  - concepts/knowledge-driven-detection-rule-grounding.md
  - concepts/threat-intelligence.md
  - concepts/threat-hunting.md
  - concepts/soc-operations.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "REFERENCE 2026-08-20 — no public SPDX repo (YouTube demo only). Do not clone. Pattern steal: enrich + template-ground + judge loop, not raw LLM-to-Sigma."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K297 TI→detection) + lab-redteam note"
---

**Briefs:** `briefs/2026-08-20_k297-autosigma-ti-detection.md`

## Relations

- @concepts/knowledge-driven-detection-rule-grounding.md
- @concepts/threat-intelligence.md
- @concepts/threat-hunting.md
- @concepts/soc-operations.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation |
| Authors | Sepehr Ghaffarzadegan, Boubakr Nour, Makan Pourzandi, Mourad Debbabi, Chadi Assi (Concordia + Ericsson Research) |
| arXiv | 2608.19011 (cs.CR, v1 19 Aug 2026) CC BY 4.0 |
| Code | none public at retrieval; demo https://youtu.be/iSr6IurQ6BM |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.19011-from-threat-intelligence-to-detection-knowledge.pdf` |
| Retrieved | 2026-08-20 |
| Read status | read (abstract + pipeline + headline eval) |

## Narrative

AUTOSIGMA turns unstructured CTI into Sigma rules without treating an LLM as a from-scratch rule author. Pipeline: structured knowledge-base enrichment of partial inputs → match against an existing Sigma repository (template grounding) → dual-LLM-as-a-Judge iterative validation. Evaluated on public blogs plus APT41 / APT28 / APT29 reports. Headline (cloud LLMs, averaged): IoC coverage ~90% vs ~20% ChatGPT-off-the-shelf; MITRE coverage ~91%; validity 100% on the cloud variants. Local Lily-Cybersecurity-7B is weaker (validity ~72% averaged). [TENTATIVE] single paper; generated rules still need human SIEM review before deploy.

**Steal:** do not prompt an LLM to emit a Sigma rule from a PDF and ship it. Ground in known templates; judge validity separately from relevancy and ATT&CK coverage; expect input-quality sensitivity.

**Phase-0:** no clone. Do not pull Lily-Cybersecurity weights for this.

## Snippets

> Rather than relying solely on language models, AUTOSIGMA leverages a structured knowledge base to enrich partial inputs, matches the enriched content against a repository of existing Sigma rules, and then employs an LLM-as-a-Judge mechanism to iteratively validate the rules. [Source: arXiv 2608.19011 abstract]
