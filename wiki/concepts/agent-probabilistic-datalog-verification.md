---
title: Agent probabilistic Datalog verification
type: concept
tags: [agent-security, guardrail, formal-methods, datalog, probabilistic-verification, dro, reference-monitor]
keywords: [2606.20510, probabilistic datalog, distributionally robust optimization, praline, souffle, noisy classifiers, pii detector, taint tracking]
related:
  - sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - entities/tools/chaincaps.md
  - entities/tools/airguard.md
maturity: draft
created: 2026-06-21
updated: 2026-07-31
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md — primary source (2606.20510)
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — deterministic ePCA layer (SMT)
- @concepts/neuro-symbolic-auditable-reasoning.md — shared Datalog/Soufflé toolchain for auditable reasoning (vuln discovery vs runtime policy)

## Raw Concept

Ingest 2026-06-21: arXiv:2606.20510 — when agent runtime monitors use **noisy classifiers** (PII detectors, redactors, secret scanners), deterministic Boolean policy evaluation is wrong. This page positions **distributionally robust probabilistic Datalog** as the formal layer between crisp ePCA/SMT guards and empirical LLM-as-Judge filters.

## Narrative

### Three enforcement layers (2026 stack)

```
Layer 3 — Semantic alignment / LLM-as-Judge     (probabilistic, no lower bound)
Layer 2 — Probabilistic Datalog + DRO           (sound upper bound on violation P)  ← 2606.20510
Layer 1 — Deterministic ePCA / SMT              (UNSAT deadlocks on crisp predicates) ← 2605.29251
Layer 0 — AIRGuard / ChainCaps / allowlists     (authority + composition + admission)
```

Layer 2 matters when Layer 1 predicates are fed by **imperfect upstream models** — the common case in enterprise copilots and MCP stacks with content scanners.

### When to use vs ePCA

| Signal | Prefer deterministic ePCA | Add probabilistic Datalog |
|--------|---------------------------|---------------------------|
| Policy expressible as crisp logic | ✓ | optional |
| Upstream PII/secret/redaction classifiers | brittle without Layer 2 | ✓ |
| Correlated predicate failures (same dir, batch API) | independence breaks | ✓ DRO bound |
| Latency budget <1 ms per step | ePCA ~0.44 ms (paper) | SDP relaxation higher latency `[TENTATIVE]` |

### Correlation classes (Praline model)

| Class | Meaning | Monitor impact |
|-------|---------|----------------|
| POS | Positively correlated failures | Independence **underestimates** risk |
| NEG | Negatively correlated | Independence may overestimate |
| IND | Independent | Standard product-of-marginals |

Operators can supply hints (e.g., "files in `/contracts/` correlate") — two-phase inference in Praline discovers POS/NEG/IND from data + static propagation.

### Production checklist

1. **Identify probabilistic predicates** in your intercept path — anything with per-call error rate (regex secret scan, VT label, embedding classifier).
2. **Do not threshold alone** — fixed τ on P(violation) loses utility or misses correlated tail risk.
3. **Compile policy to Datalog** taint rules (propagate/merge/declassify) over tool-call trajectory — same Soufflé ecosystem as NeuroLog-style audits.
4. **Pair with Layer 0** — probabilistic verification does not replace least-privilege tool admission (TOOLPRIVBENCH OPUR) or MCP SPI/DCI controls.
5. **Eval on correlated batches** — red-team sibling-file leaks and multi-response MCP reads, not only isolated false negatives.

### Phase-0 adoption

| Artifact | Verdict |
|----------|---------|
| 2606.20510 framework | **Reference** — Google ©, no public code in paper |
| Praline (Wang OOPSLA2 2025) | **Reference** — prior art engine; artifact not Phase-0'd in this ingest |
| Soufflé Datalog engine | **GO** — existing FOSS toolchain (NeuroLog pattern) |

See `briefs/2026-06-21_probabilistic-agent-guardrail-dro-handoff.md` for prod-mcp / lazy-tool integration notes.
