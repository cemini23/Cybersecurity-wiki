---
title: "Video-Index: a curated meta-benchmark for video understanding"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.00960, k388]
related:
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-10-02
updated: 2026-10-02
phase_0_verdict: "REFERENCE 2026-10-02 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K388)"
---

## Relations

## Relations

- @concepts/benchmark-shortcut-attack-pyramid-audit.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Video-Index: a curated meta-benchmark for video understanding |
| arXiv | 2610.00960 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.00960-video-index-a-curated-meta-benchmark-for-video-u.pdf |
| Retrieved | 2026-10-02 |
| Read status | read (deep-read via grok CLI) |

## Narrative

**K388** — a benchmark score should certify the capability it claims, but models can exploit answer options, question text, or partial visual evidence instead. The authors define an **attack pyramid**: five nested shortcut-attacker sets with growing access (options → text → other items → one frame or captions → shuffled/truncated video). **Exploitability** ε = max attacker accuracy − chance; a benchmark **breaks** at the first level where ε exceeds the reference model's margin. Auditing 115 video benchmarks: **35 break before seeing a single frame**; on 51 benchmarks with temporal probes, **shuffled frames keep a median 96%** of full-video accuracy; near-duplicate questions make up at least half the items in 63 benchmarks. Operator steal for **any** agent-security eval, not just video: **a score is a capability certificate only above the strongest tested shortcut** — report a **breaking level** beside the certificate, and gate your own benchmark with a red-team pass that drops items a weak attacker already solves. Repo not stated. **Audit-only — no precheck script.**

## Snippets

> See arXiv 2610.00960 abstract. [Source: arXiv 2610.00960 (retrieved 2026-10-02)]
