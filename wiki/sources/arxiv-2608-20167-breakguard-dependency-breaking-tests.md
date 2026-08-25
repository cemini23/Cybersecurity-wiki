---
title: "BreakGuard — Detecting Dependency Breaking Changes with LLM-Generated Tests (arXiv 2608.20167)"
type: source
tags: [source, arxiv, supply-chain, dependency-update, llm-tests, k300]
keywords: [2608.20167, BreakGuard, breaking changes, BUMP dataset, LLM-generated tests, dependency update, crash-type, Concordia]
related:
  - concepts/llm-generated-dependency-breaking-tests.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/npm-supply-chain-defense.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "REFERENCE 2026-08-21 — paper claims a GitHub prototype but hunt found NO matching public repo with SPDX (only name collisions: ProgrammerNomad/BreakGuard Windows break-reminder, Tahiram32/breakguard unrelated MIT product). Re-hunt 2026-08-25: still no matching SPDX repo. No clone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K300 dependency tests are candidates)"
---

**Briefs:** `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @concepts/llm-generated-dependency-breaking-tests.md — primary synthesis (candidate tests, not a gate)
- @concepts/coding-agent-supply-chain-install-gap.md — the update-triggered breakage surface this detects
- @concepts/npm-supply-chain-defense.md — dependency risk family context

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BreakGuard: Towards Detecting Dependency Breaking Changes with LLM-Generated Tests |
| Authors | Rachna Raj (Concordia), Benoit Baudry (U Montréal), Diego Elias Costa (Concordia) |
| arXiv | 2608.20167 (15 pp) |
| Code | claimed "publicly available prototype on GitHub"; hunt (2026-08-21) found no matching repo with SPDX — name collisions only |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.20167-breakguard-towards-detecting-dependency-breaking.pdf` |
| Retrieved | 2026-08-21 |
| Read status | read (abstract + intro + RQs + results) |

## Narrative

BreakGuard detects **dependency breaking changes (BCs)** before they break client apps. Client test suites miss BCs because they only cover the subset of the library API the client actually uses. BreakGuard:

1. **Statically extracts focal methods** — every client method that invokes the target library method (call site).
2. **Generates tests per focal method** with an LLM — evaluated with 3 LLMs (GPT-4o, Qwen3-Coder-480B, GPT-OSS-120B) across 3 context levels (minimal, method, class).
3. **Detects a BC** when a generated test passes on the pre-breaking version and fails on the breaking version.

Results on **89 real-world breaking changes from the BUMP dataset**: best configuration detects **30.3% (27/89)** at a **mean cost of ~$0.90 USD per detected breaking change** (median ~$0.09 per breaking-update instance); richer context (full class) gives the best effectiveness/cost trade-off. **Crash-type BCs are detected more reliably than behavioral BCs** (behavioral changes remain largely undetected). Detected BCs span JSON, logging, parsing, application-framework, and utility libraries.

**Why it matters to the lab:** deferred dependency updates correlate with increased security vulnerabilities — an automated pre-update BC check (in a PR workflow, as the paper proposes) is a cheap triage layer. But the handoff wire is explicit: **LLM-generated tests are *candidates*, not a SIEM/merge gate** — human review before treating them as an update gate.

**Name collision:** `ProgrammerNomad/BreakGuard` (Windows screen-lock break-reminder app) is unrelated. No matching repo found at hunt → **REFERENCE, no clone**.

**Phase-0:** REFERENCE. Dual-ID: **Cybersec K300** (this paper) ≠ any other BreakGuard.

## Snippets

> Using the best-performing configuration, BreakGuard detects 30.3% of breaking changes (27 of 89) at a mean cost of roughly $0.90 USD per detected breaking change. [Source: arXiv 2608.20167 abstract]

> We find LLM-generated tests to be more reliable for detecting crash-type breaking changes as opposed to behavioural BCs. [Source: arXiv 2608.20167 abstract]
