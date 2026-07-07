---
title: Neuro-symbolic auditable reasoning for security findings
type: concept
tags: [concept, neuro-symbolic, audit, k100, datalog, smt, vuln-discovery]
keywords: [2606.00669, neurolog, datalog, souffle, z3, auditable-reasoning]
related:
  - sources/arxiv-neurolog-auditable-vuln-discovery-2606.00669-2026-06-05.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/responsible-disclosure.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/defending-code-reference-harness.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md
  - concepts/agent-probabilistic-datalog-verification.md
  - sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md
  - concepts/substrate-constraints-coding-agent-oversight.md
maturity: validated
created: 2026-06-05
updated: 2026-07-07
---

## Relations

- @sources/arxiv-neurolog-auditable-vuln-discovery-2606.00669-2026-06-05.md — NeuroLog paper (deep-read)
- @concepts/llm-vulnerability-discovery.md — two-stage Detect→Attack pipelines; NeuroLog as compile-free variant
- @concepts/responsible-disclosure.md — libarchive upstream disclosure pattern from evaluation
- @concepts/ai-for-cybersecurity.md — LLM role boundaries in security workflows
- @entities/tools/defending-code-reference-harness.md — execute-to-crash ASAN complement (NeuroLog = compile-free audit)

## Raw Concept

K100 OSINT handoff → cybersec canonical page for **auditable** vuln reasoning (Datalog derivation trees + SMT witnesses), distinct from opaque LLM-only triage.

## Narrative

Security findings need **reproducible evidence chains** — especially for disclosure and retest. Pure LLM vuln hunting produces plausible narratives without derivations; pure static analysis needs builds. **Neuro-symbolic auditable reasoning** assigns each engine a narrow job [CONFIRMED]:

| Phase | Engine | Output artifact |
|-------|--------|-----------------|
| Extract | LLM (schema-bound) + tree-sitter | Typed facts per function |
| Compose | Datalog (Soufflé) | Finding + **derivation tree** |
| Filter | Z3 (+ optional likely-invariants) | SAT model or infeasible |
| Validate | LLM + ASan harness | Crash input PoC |

Analyst-facing report should cite: fact tuples → rule application → SMT witness → harness result — mirroring wiki `[CONFIRMED]` / citation-tag discipline.

**Runtime policy Datalog (2606.20510):** same Soufflé toolchain, different job — probabilistic taint verification on agent trajectories (PII/redaction classifiers) vs NeuroLog's static vuln derivation trees. See @concepts/agent-probabilistic-datalog-verification.md.

### When to use

- **Opportunistic source audit** (single-header libs, vendored C) without standing up CodeQL build graph.
- **Engagement appendix** where client asks *how you knew* a bug was reachable.
- **Not** a replacement for org-standard SAST/DAST on built products with existing CI gates.

### Steal-from for briefs

Template section: `## Reasoning chain` with Datalog-style steps + Z3 witness summary + ASan one-liner — export from NeuroLog-style tooling when available [NEEDS VERIFICATION 2026-05-31 on public NeuroLog release].

## Snippets

> "The LLM is constrained to the schema: it does not invent relations, only fill tuples."
> — [Source: arxiv-2606.00669 §1, retrieved 2026-05-31]

## Dead Ends

- **Trusting LLM-extracted facts without re-run** — mistakes become missing recall, not fake findings, but still require Soufflé replay on frozen fact DB for audit.
- **Routing to OSINT wiki** — financial quant NeuroLog use cases stay OSINT; this page is security vuln discovery only.
