---
title: "KaliBench: a fine-grained benchmark for cybersecurity tool use on Kali Linux with runtime-free verifiable rewards"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.02206, k391]
related:
  - concepts/k278-security-wave.md
  - concepts/k277-security-wave.md
  - concepts/kalibench-nl-to-cli-tool-use-eval.md
  - concepts/secure-ai-powered-pentest-agents.md
  - concepts/privescalate-llm-linux-privilege-escalation.md
  - concepts/security-agent-authority-auditability-slr.md
maturity: draft
read_status: read
created: 2026-10-02
updated: 2026-10-02
phase_0_verdict: "REFERENCE 2026-10-02 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K391)"
---

## Relations

- @concepts/k278-security-wave.md — K278 wave aggregation page
- @concepts/k277-security-wave.md — K277 wave aggregation page
## Relations

- @concepts/kalibench-nl-to-cli-tool-use-eval.md
- @concepts/secure-ai-powered-pentest-agents.md
- @concepts/privescalate-llm-linux-privilege-escalation.md
- @concepts/security-agent-authority-auditability-slr.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | KaliBench: a fine-grained benchmark for cybersecurity tool use on Kali Linux with runtime-free verifiable rewards |
| arXiv | 2610.02206 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.02206-kalibench-a-fine-grained-benchmark-for-cybersecu.pdf |
| Retrieved | 2026-10-02 |
| Read status | read (deep-read via grok CLI) |

## Narrative

**K391** — measures whether a model can turn a plain-language request into an **exact, executable** Kali Linux command: 8,504 query–command pairs, 1,642 tools, 23 capability dimensions, five security phases. Scoring is **runtime-free** — deterministic canonicalisation plus alias-aware matching, no execution. Headline: **no open-weight model exceeds 42% exact-command accuracy** unrestricted (best 41.3%); proprietary best is 61.68%. The diagnostic that transfers: **tool choice is not the bottleneck, the arguments are** — tool accuracy rises **72.0% → 95.2%** when candidates are narrowed, and exact-correct rises **22.3% → 73.1%** only when documentation is supplied. SFT+GRPO on the benchmark lifts an 8B model by **7.5 points** mean Total Score, near a 685B MoE. Operator steal: score tool invocation against a **fixed reference**, and **split tool-selection from argument-construction** in any tool-gate diagnostic. **Licence discrepancy:** the paper states **CC BY-NC 4.0**, but the repo has **no LICENSE file and no README licence text** (verified via `gh api` 2026-10-02) — treat the claim as unverified, **no clone**. Repo `github.com/RISys-Lab/KaliBench`. **No attack payloads in wiki.**

## Snippets

> See arXiv 2610.02206 abstract. [Source: arXiv 2610.02206 (retrieved 2026-10-02)]
