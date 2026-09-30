---
title: "Auditable long-term memory: a deterministic retrieval chain measured at 479/475 of 500 on LongMemEval-S"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.38021, k385]
related:
  - concepts/auditable-long-term-memory-retrieval-chain.md
  - concepts/trajectory-context-control.md
  - concepts/kamr-knowledge-aligned-multihop-retrieval.md
maturity: draft
read_status: read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: "REFERENCE 2026-09-30 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K385)"
---

## Relations

## Relations

- @concepts/auditable-long-term-memory-retrieval-chain.md
- @concepts/trajectory-context-control.md
- @concepts/kamr-knowledge-aligned-multihop-retrieval.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Auditable long-term memory: a deterministic retrieval chain measured at 479/475 of 500 on LongMemEval-S |
| arXiv | 2609.38021 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609-38021-auditable-long-term-memory-a-deterministic-retri.pdf |
| Retrieved | 2026-09-30 |
| Read status | read (abstract + triage) |

## Narrative

**K385** — a long-term-memory answer can fail as a **quiet retrieval miss**: the system never retrieves the session that states the fact, then answers fluently and wrongly. Archivist's auditable chain keeps **stages 1–4 deterministic code** (hybrid candidate retrieval, cross-encoder rerank, coverage-first packet compilation, deterministic scaffolds) and uses the LLM only as a **replaceable final reader**. On LongMemEval-S it places all gold sessions in the candidate pool for **468/470** answerable questions and builds gold-complete packets for **462/470**; the headline reader scores **479/500** and **475/500** across two passes, bracketing Chronos High's **478/500** — the authors state the pair shows **neither superiority nor equivalence**. Operator steal: report **retrieval** metrics separately from the **reader** score; the reader choice moves the score by up to **386** points; measure **judge variance** (second judge 98.6% agreement, 472/500) and **verdict flips** on byte-identical answers; freeze a two-pass promotion rule; run **negative controls** (one verifier repaired 3 wrong drafts but broke **11** correct ones). Measurement-integrity surface: some reader lanes had tools enabled plus ~**59k–62k** characters of extra operator context per call — **not a closed-book measurement**. Repo `github.com/cjchanh/longmemeval-evidence` is **MIT evidence-only** (retrieval and scaffold sources held) — REFERENCE. **Audit only — no precheck script.** Pairs GT-MCP trajectory-context-control and K228 KAMR.

## Snippets

> See arXiv 2609.38021 abstract. [Source: arXiv 2609.38021 (retrieved 2026-09-30)]
