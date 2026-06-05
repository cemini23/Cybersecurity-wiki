---
title: NeuroLog — auditable neuro-symbolic vulnerability discovery (arXiv 2606.00669)
type: source
tags: [source, arxiv, neuro-symbolic, vuln-discovery, osint-handoff, compile-free]
keywords: [2606.00669, neurolog, datalog, souffle, z3, llm-fact-extractor, asan]
related:
  - concepts/neuro-symbolic-auditable-reasoning.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/responsible-disclosure.md
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-05-31
---

## Relations

- @concepts/neuro-symbolic-auditable-reasoning.md — canonical methodology synthesis
- @concepts/llm-vulnerability-discovery.md — compile-free alternative to CodeQL-first pipelines
- @concepts/responsible-disclosure.md — libarchive upstream filing pattern

## Raw Concept

| Field | Value |
|-------|-------|
| Title | NeuroLog: Reasoning You Can Audit — Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT |
| Author | Sanjay Rawat (Independent Researcher) |
| arXiv | 2606.00669 |
| Location | `raw-sources/arxiv-2606.00669-neurolog.pdf` |
| Retrieved | 2026-05-31 |
| Read status | **read** |

OSINT K100 handoff — cybersec owns vuln-discovery methodology; OSINT may keep financial-quant routing only.

## Narrative

**Problem:** CodeQL/CPG tools need a **working build**; free-form LLMs read source but **confabulate** and lose cross-function dataflow on large codebases [CONFIRMED].

**NeuroLog split:**

| Layer | Engine | Role |
|-------|--------|------|
| Fact extraction | LLM + tree-sitter | Per-function typed Datalog facts (Def, Use, ArithOp, Cast, Guard, Call…) — schema-constrained, no invented relations |
| Composition | Soufflé (~30 rules, 5 passes) | Cross-function taint / memory-safety findings with **derivation trees** |
| Feasibility | Z3 | Path SAT per finding; optional likely-invariants from few seed runs |
| PoC | LLM + ASan harness | Reads SAT model → Python crash generator; multi-shot with ASan feedback |

**No compile step** — tree-sitter parses; analyst can opportunistically audit libraries (stb, cJSON) without host-project build wrapper.

### Evaluation highlights [CONFIRMED]

| Target | Outcome |
|--------|---------|
| stb_vorbis CVE-2023-45676 | Re-found; 102-byte crash in **2** LLM iterations; ~37s extract, ~$0.005 LLM cost on stb |
| curl CVE-2023-38545 (CVSS 9.8) | Re-detected (SOCKS5 heap overflow) |
| libarchive HEAD | **5** new memory-safety bugs (4 unreported); upstream fixes merging |
| FFmpeg demuxer slice | Likely-invariant filter from 3 Matroska seeds drops 13.2% feasible set incl. static FP |

**8 published CVE-class** re-discoveries end-to-end with ASan confirmation across stb, cJSON, libxml2-scale run, FFmpeg slice, curl 8.3.0.

Contrast: Saturn/Pinpoint/Formulog stop at feasible/infeasible — NeuroLog uses **SAT witness as artifact** for crash synthesis.

**Steal-from:** report chains with auditable derivation trees + citation tags for engagement / CTF write-ups; not a prod scanner until license + reproducibility Phase-0 on released code [NEEDS VERIFICATION 2026-05-31].

## Snippets

> "We use an LLM only where it has a strong inductive bias — reading one C function and writing its dataflow as typed Datalog facts."
> — [Source: arxiv-2606.00669 §1, retrieved 2026-05-31]

> "Every step in the derivation is mechanically auditable and reproducible by re-running Soufflé on the same fact base."
> — [Source: arxiv-2606.00669 §3, retrieved 2026-05-31]

```
Def(start_decoder, len, 0, 3652)
Call(start_decoder, get32_packet, 3652)
ArithOp(start_decoder, 3653, _t, +, len, 1, "u32")
Call(start_decoder, setup_malloc, 3653)
→ TaintedNarrowArith → integer-overflow alloc sink (stb_vorbis)
```

## Dead Ends

- **Replacing CodeQL on built monorepos** — NeuroLog wins on compile-free opportunistic audits; mature CodeQL may still dominate when build infra exists.
- **ML single-function detectors** — paper cites over-claimed recall when caller context matters; NeuroLog explicitly delegates inter-procedural work to Datalog.
