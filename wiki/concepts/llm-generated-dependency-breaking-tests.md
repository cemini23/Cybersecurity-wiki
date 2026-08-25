---
title: "LLM-generated dependency breaking-change tests (K300)"
type: concept
tags: [concept, supply-chain, dependency-update, llm-tests, k300, defensive]
keywords: [breaking changes, LLM-generated tests, focal method, BUMP, dependency update, crash-type, candidate tests]
related:
  - sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md
  - concepts/llm-generated-compliance-artifacts.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/llm-code-review-agent-security.md
  - concepts/npm-supply-chain-defense.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K300 dependency tests are candidates)"
---

**Briefs:** `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md
- @concepts/coding-agent-supply-chain-install-gap.md — the install/update-time attack surface
- @concepts/llm-code-review-agent-security.md — LLM-driven review shares the candidate-not-gate discipline
- @concepts/npm-supply-chain-defense.md — dependency risk family
- @concepts/ai-for-cybersecurity.md — where AI-assisted update triage fits in the stack

## Raw Concept

Question this page answers: **can LLM-generated tests cheaply catch dependency breaking changes before an update breaks a client, and how should we trust them?**

## Narrative

**The problem:** libraries evolve and occasionally break the contract with clients. Client test suites miss breaking changes (BCs) because coverage only exercises the library subset the client uses. Meanwhile **deferred updates correlate with security vulnerabilities** — the fix/security-patch cadence stalls when updates feel risky.

**The BreakGuard pattern (K300, 2608.20167):**
1. Statically find every client method (focal method) that invokes a target library method (call site).
2. Generate a test per focal method with an LLM.
3. A BC is detected when the test **passes on the pre-breaking version and fails on the breaking version** — a differential predicate, not an absolute assertion.

**Measured behavior (89 BUMP BCs):** 30.3% detection (27/89) at best config, ~$0.90 mean per detected BC; full-class context best; **crash-type BCs detect reliably, behavioral BCs largely don't**. [TENTATIVE] single paper.

### Operator steal

- **LLM-generated dependency tests are *candidates*, not a SIEM/merge gate.** Use them in a PR workflow as triage: "this update may break the client here" — then **human review / CI re-run before treating as a gate** (pairs `llm-code-review-agent-security.md` — SEVRA lesson: never let the LLM be the only reviewer).
- **Crash-type first**: expect good signal on exceptions/API-signature breaks; expect silent misses on behavioral/return-semantics changes.
- **Cost discipline**: ~$0.90/detected-BC means you spend little to surface breakage early; the failure mode is *false confidence*, not cost.
- **Pairs the install-gap concept**: the same dependency-update surface is where supply-chain install-gap attacks and typosquat land — update risk is both security and availability.

**Dual-ID:** Cybersec **K300** (2608.20167) ≠ ProgrammerNomad/BreakGuard (Windows break-reminder) ≠ any other BreakGuard. No matching repo with SPDX at hunt → REFERENCE, no clone.

## Snippets

> LLM-generated tests are **candidates**, not a SIEM/merge gate. [Source: K300 wire 2026-08-21]

> Crash-type breaking changes are detected more reliably than behavioral BCs. [Source: arXiv 2608.20167 abstract, paraphrased]
