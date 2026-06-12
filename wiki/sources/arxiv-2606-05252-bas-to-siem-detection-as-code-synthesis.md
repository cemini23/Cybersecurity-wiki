---
title: BAS finding → Sigma rule — deterministic detection-as-code synthesis (arXiv 2606.05252)
type: source
tags: [source, arxiv, bas, siem, sigma, detection-engineering, owasp]
keywords: [2606.05252, detection-as-code, breach attack simulation, sigma, locked probe corpus, lumytics]
related:
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/llm-defense-lattice.md
  - entities/tools/splunk.md
  - entities/tools/wazuh.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-08700-autosut-environment-semantics-gap.md
maturity: draft
read_status: read
created: 2026-06-06
updated: 2026-06-11
---

## Relations

- @concepts/siem.md — detection content pipeline from BAS gaps to SIEM rules
- @concepts/soc-operations.md — SOC workflow: simulate → detect gap → write rule
- @concepts/threat-hunting.md — starter rules as hunt hypotheses, not finished prod content
- @concepts/agent-runtime-guardrails.md — LLM-side locked corpus aligns with OWASP LLM probes
- @entities/tools/llm-defense-lattice.md — companion locked-corpus BAS (engine-side attribution)
- @entities/tools/splunk.md — Sigma converts to Splunk SPL backends
- @entities/tools/wazuh.md — FOSS SIEM path for ported Sigma rules
- @sources/arxiv-2606-02822-owasp-llm-defense-attribution.md — same author/corpus discipline; defense-side output

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Attack Simulation to SIEM Rule: Deterministic Detection-as-Code Synthesis with Probe-Level Traceability |
| Author | Alexandre Cristovão Maiorano (Lumytics) |
| arXiv | 2606.05252 |
| Location | `raw-sources/arxiv-2606.05252-from-attack-simulation-to-siem-rule-determin.pdf` |
| Retrieved | 2026-06-06 |
| Read status | **read** |

## Narrative

BAS tools surface **detection gaps** — what the simulator achieved that monitoring would miss — but SIEM operators still hand-author Sigma YAML today. This paper closes the loop **deterministically** when probes come from a **locked corpus** with stable `probe_id` values and OWASP LLM/Web Top 10 + MITRE ATT&CK tags [CONFIRMED].

### Synthesis pipeline

```
finding.metadata.probe_id → corpus entry → OWASP category → Sigma template → starter rule
```

- **Template library** N=23 skeletons (8 legacy MITRE T-code + 9 OWASP LLM Top 10 + 6 OWASP Web Top 10; 19 exercised by released corpora).
- **Traceability contract**: each emitted rule carries URIs to the originating finding and MITRE technique; combined with content-hashed run records → byte-stable audit path from fired alert back to probe.
- **Reproducibility envelope**: external reviewer can re-derive every rule from published corpus + template library + synthesis pseudocode alone — no proprietary engine required.

### Corpora + coverage

| Corpus | Probes | Bypassed findings → rules |
|--------|--------|---------------------------|
| LLM (OWASP LLM Top 10) | 17 | 17/17 emitted; all parse + convert to Splunk/Elasticsearch |
| Web (OWASP Web Top 10) | 23 | structurally validated (no held-out attack replay) |

### Live SIEM replay (OpenSearch + Lucene)

On held-out subsets after v2 template rubric (regex on semantic markers, not keyword-only v1 which scored 0/50):

| Benchmark | Fire rate | Notes |
|-----------|-----------|-------|
| AdvBench subset (50) | **30%** (15/50) | v2-integrated engine 60%; SIEM drop from backend shim |
| HarmBench subset (50) | **14%** (7/50) | |
| Benign LLM baseline | **7.7% FP** | |

**Deliberate non-claims**: starter-rule quality only — not production-ready; no controlled analyst time-on-task study (structural break-even ~4–8 findings/category vs 30–60 min manual estimate).

### Positioning vs peers

- **garak** — locked OWASP LLM probes + verdicts; does **not** emit detection content. This synthesis function is the proposed back-half.
- **SigmaHQ** — ~3k hand-authored rules; complementary depth, not competing coverage for corpus-probe→rule traceback.
- **CALDERA** — pre-attack ability metadata; this pipeline consumes **post-attack BAS findings**.
- **LLM-generative rule writers** — traded for exact reproducibility and probe-level traceback.

Companion to arXiv:2606.02822 / @entities/tools/llm-defense-lattice.md: that work measures **which defense closes which probe**; this work maps **bypassed probes to starter Sigma** with the same locked-corpus integrity chain.

## Snippets

> "Every bypassed-probe finding yields a starter rule, and all 17/17 emitted rules parse and convert to Splunk and Elasticsearch backends."
> — [Source: arxiv-2606.05252 abstract, retrieved 2026-06-06]

> "Determinism and probe-level traceability are what let auto-generated detection content be governed like code — version-controlled, diffed across corpus revisions, reviewed, and signed off."
> — [Source: arxiv-2606.05252 §1, retrieved 2026-06-06]

> "We do not claim that auto-generated rules are production-rule level."
> — [Source: arxiv-2606.05252 §6 Conclusion, retrieved 2026-06-06]

## Dead Ends

- **Treating starter rules as ship-ready** — paper explicitly scopes to analyst review + tuning before prod deployment.
- **Keyword-only template rubric (v1)** — 0/50 AdvBench fire rate; regex semantic markers required for any signal.
- **Splunk replay deferred** — OpenSearch-only live measurement; pysigma `\b` compatibility gap noted for follow-up.
