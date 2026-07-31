---
title: SWE-Pruner Pro — prune tool outputs from coder-LLM internals (arXiv 2607.18213)
type: source
tags: [source, arxiv, coding-agent, context-pruning, efficiency]
keywords: [2607.18213, SWE-Pruner Pro, context pruning, SWE-Bench, token savings]
related:
  - entities/tools/swe-pruner-pro.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-07-21 — github.com/Ayanami1314/swe-pruner-pro Apache-2.0 in pyproject (~8.7MB shallow); no LICENSE file — lab only"
wire_status: deferred
wire_target: "LICENSE file watch"
---

**Briefs:** `briefs/2026-07-21_k200-swe-pruner-pro-prod.md`

## Relations

- @entities/tools/swe-pruner-pro.md
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SWE-Pruner Pro: The Coder LLM Already Knows What to Prune |
| Authors | Yuhang Wang et al. (SJTU LLM4SE; Douyin) |
| arXiv | 2607.18213 |
| Code | [github.com/Ayanami1314/swe-pruner-pro](https://github.com/Ayanami1314/swe-pruner-pro) |
| Local clone | `raw-sources/repos/swe-pruner-pro` (~8.7MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.18213-swe-pruner-pro-the-coder-llm-already-knows-what.pdf` |
| Retrieved | 2026-07-21 |

## Narrative

Instead of a separate classifier (SWE-Pruner), attach a small head to the **agent's own internals** to keep/prune each tool-output line (length-aware). Up to **39%** prompt+completion token savings with quality preserved; on MiMo-V2-Flash also **+3.8%** SWE-Bench Verified resolve and **+2.2** Oolong long-context points.

### Steal

1. Prefer internal-representation pruning over external classifiers for coding agents
2. Bound prune-head inference overhead; measure resolve rate not just tokens
3. CCC harness: candidate for long-trajectory tool-output bloat

### Phase-0

| Gate | Status |
|------|--------|
| License | **PASS** — `pyproject.toml` Apache-2.0 (no LICENSE file — watch) |
| Size | **PASS** — ~8.7MB |
| Stars | 1 — WATCH |
| Verdict | **CONDITIONAL-GO** lab |

## Snippets

> "saves up to 39% of prompt and completion tokens while preserving task quality"
[Source: arxiv-2607.18213 abstract]
