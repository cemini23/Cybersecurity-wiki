---
title: "Tripwire — training-free safety-neuron clamp (arXiv 2608.14392)"
type: source
tags: [source, arxiv, llm-security, refusal, watch, k240]
keywords: [2608.14392, Tripwire, safety neuron, Welch, BH-FDR, abliterated, HITL]
related:
  - concepts/tripwire-safety-neuron-clamp.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/concept2scenario-refusal-suppression.md
  - concepts/llm-pentest-automation.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "WATCH 2026-08-18 — no clone, no PoC, no weight download. Inbound brief K240 (≠ OSINT/GW Talon K240, ≠ CCC robotics K240)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K240 Tripwire)"
---

**Briefs:** `briefs/2026-08-17_k240-tripwire-abliterated-watch.md`

## Relations

- @concepts/tripwire-safety-neuron-clamp.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/concept2scenario-refusal-suppression.md
- @concepts/llm-pentest-automation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Tripwire (training-free safety-neuron clamp) |
| arXiv | 2608.14392 |
| Code | none for this wiki — **no PoC** |
| Retrieved | 2026-08-17 (inbound brief); filed 2026-08-18 |
| Read status | read (brief + paper claims as cited) |

## Narrative

Tripwire identifies safety neurons (Welch + BH-FDR + utility filter) and clamps them at the harmful-conditional mean, in two equivalent modes (detector-gated inference vs bias-patch). Reported ASR at most **2%** with utility drop **0.5–5.3%**. [TENTATIVE] single source.

**Lab policy.** Do **not** apply the clamp to deliberately abliterated / low-refusal lab models without HITL — the paper's clamp restores aligned refusal. Qwen 27B ABLITERATED GGUF and Uncensored FP8 stay **Watch**; no Hugging Face weight download this batch. HTB cheatsheets (null SPDX) and Dshell/DShield stay Context. No jailbreak / Tripwire PoC in this wiki.

**Dual-ID:** inbound brief **Cybersec K240** ≠ OSINT/GW K240 Talon ≠ CCC K240 Julia MCP solver.

## Snippets

> Identify safety neurons (Welch + BH-FDR + utility filter), clamp at harmful-conditional mean. [Source: briefs/2026-08-17_k240-tripwire-abliterated-watch.md]
