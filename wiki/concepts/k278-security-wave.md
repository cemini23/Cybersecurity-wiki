---
title: "k278 security wave — KaliBench NL-to-CLI"
type: concept
tags: [concept, agent-security, k278, tool-use, benchmark]
keywords: [KaliBench, NL-to-CLI, Kali Linux, runtime-free verification, K278]
related:
  - sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md
  - concepts/kalibench-nl-to-cli-tool-use-eval.md
  - concepts/k277-security-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K391)"
---

## Relations

- @sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md — KaliBench source (K391 deep-read)
- @concepts/kalibench-nl-to-cli-tool-use-eval.md — the reusable steal
- @concepts/k277-security-wave.md — previous wave

## Raw Concept

Aggregation page for the **K278 cyber-lab** brief (`briefs/2026-10-02_k278-cyber-lab.md`). The paper
it names is **KaliBench**, which landed in the same week's inbox and is ingested as **K391** — so this
page points at that ingest rather than duplicating it.

## Narrative

KaliBench measures whether a model can turn a plain-language request into an **exact, executable**
command for a real security tool: 8,504 query–command pairs, 1,642 tools, 23 capability dimensions,
five phases. Scoring is **runtime-free** — canonicalisation plus alias-aware matching, nothing is run.

| Setting | Result |
|---------|--------|
| Best open-weight, unrestricted | 41.3% exact |
| Best proprietary, unrestricted | 61.68% exact |
| Tool selection, unrestricted → restricted | 72.0% → 95.2% |
| Exact-correct, unrestricted → hinted | 22.3% → 73.1% |

**Tool choice is not the bottleneck; the arguments are.** Narrow the candidate set and tool selection
nearly resolves; exactness does not move until the arguments are pinned down.

Two things transfer:

1. **The runtime-free verifiable reward.** Canonicalisation plus alias-aware matching gives a
   deterministic score without executing anything — the same rule the K276 and K277 findings reached
   from other directions: score against a **fixed reference**, not against a model's own account.
2. **The argument-vs-selection split** is a good diagnostic shape for any tool-invocation gate.

**Licence caution — now verified.** The K278 brief said the dataset licence "is claimed as CC BY-NC 4.0
— a claim, not a verified fact. Verify with `gh api` before any use." That verification was run on
2026-10-02: `RISys-Lab/KaliBench` returns **null SPDX**, has **no LICENSE file** (all variants 404), and
its README carries **no licence text**. The paper states CC BY-NC 4.0; the repository does not back it.
**No clone, no dataset download.** Full record: @concepts/kalibench-nl-to-cli-tool-use-eval.md.

**Operator note:** no exploit path, payload, or step list on this page.

## Snippets

> Tool choice is not the bottleneck; the arguments are. [Source: `briefs/2026-10-02_k278-cyber-lab.md`]
