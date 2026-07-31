---
title: CAV-STIXGen — open-weight LLMs for CVE→STIX (autonomous vehicles) (arXiv 2607.16175)
type: source
tags: [source, arxiv, stix, cti, cav, open-weight, mitre-attack, cwe]
keywords: [2607.16175, CAV-STIXGen, STIX 2.1, SDO, SRO, autonomous vehicle, CVE-to-STIX]
related:
  - concepts/llm-cve-to-stix-generation.md
  - entities/tools/cav-stixgen.md
  - concepts/threat-intelligence.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/autosut.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-20 — figshare share-link dataset (https://figshare.com/s/29f4ceff6bb1c6de5700); no GitHub; WAF-gated download at ingest; steal prompting + metrics"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-20_k196-cav-stixgen-llm-cti-prod.md`

## Relations

- @concepts/llm-cve-to-stix-generation.md — synthesis
- @entities/tools/cav-stixgen.md — Phase-0 entity
- @concepts/threat-intelligence.md — STIX CTI pipeline
- @entities/frameworks/mitre-attack.md — ATT&CK mapping hardness
- @entities/tools/autosut.md — STIX semantics gap (complementary)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities |
| Authors | Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury, Md Rayhanur Rahman |
| arXiv | 2607.16175 |
| Dataset | [figshare share](https://figshare.com/s/29f4ceff6bb1c6de5700) — prompts + replication scripts claimed |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.16175-evaluating-open-weight-llms-for-generating-struc.pdf` |
| Retrieved | 2026-07-20 |
| Read status | **read** |

## Narrative

Builds **CAV-STIXGen**: 183 CAV-related CVEs (from 445 NVD candidates; κ=0.94) manually annotated to STIX 2.1 SDO/SRO + CWE + ATT&CK. Evaluates **11 open-weight** models (4B–120B) under contextless / STIX-guided / dynamic few-shot prompting at temps 0–1.0.

### Dataset stats [CONFIRMED]

| Metric | Value |
|--------|-------|
| CVEs retained | 183 (2012–2025) |
| SDO / SRO instances | 1,383 / 1,395 |
| Avg SDO / SRO per CVE | 7.56 / 7.62 |
| CWE / ATT&CK mappings | 211 / 294 |
| Top ATT&CK | T1499 (48); top pair T1203–T1499 (10) |
| Top CWE | CWE-787, CWE-20 |

### Headline LLM results [CONFIRMED]

| Task | Best-ish F1 / note |
|------|---------------------|
| SDO extraction | ~**0.94** (Phi-4 / Codestral / Qwen-Coder / LLaMA-70B under DFS) |
| SRO extraction | ~**0.63** peak (Qwen-Coder DFS) — hard |
| CWE mapping | ~**0.99** under DFS for several models |
| ATT&CK Match@1 | up to **0.68** (Gemma-4-31B); Match@All much lower |
| Multi-agent | Gemma-4-31B SDO F1 **0.91**; Codestral SRO F1 **0.43** |

Dynamic few-shot ≫ contextless. No single model wins all subtasks. Vulnerability SDO easy; infrastructure / threat-actor / rich SROs need examples.

### Steal for CTI automation

1. Prefer **STIX-guided + dynamic few-shot** over bare "make STIX" prompts
2. Gate production on **SRO + ATT&CK Match@All**, not SDO/CWE alone
3. Pair AutoSUT: generated STIX still has environment-semantics gaps
4. Automotive / OT CTI: reuse CAV keyword→NVD filter pattern for domain corpora

### Phase-0

| Gate | Status |
|------|--------|
| Artifact | Figshare private share; API search did not surface a public article ID |
| License | Unclear until share opens |
| Size | Unknown (download WAF-challenged 2026-07-20) |
| Verdict | **REFERENCE** — metrics + prompting patterns only until license/size verified |

## Snippets

> "Single-model configurations achieve F1 scores of 0.94 for SDO, 0.63 for SRO, and 0.99 for CWE mapping, while complete MITRE ATT&CK mapping remains challenging."
[Source: arxiv-2607.16175 abstract]
