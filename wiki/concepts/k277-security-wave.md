---
title: "k277 security wave — code-domain safety lag + confirm-then-report scanning"
type: concept
tags: [concept, agent-security, k277, safety-alignment, code-domain]
keywords: [CodeMimicry, code-domain safety, PageBreak, Numbat, K277]
related:
  - concepts/inbound-security-wave-2026-10-07.md
  - concepts/k278-security-wave.md
  - sources/arxiv-2609.39902-codemimicry-2026-10-01.md
  - sources/newsletter-rss-tldrsec-2026-10-01-tldr-sec-348---googles-pagebreak-scanner-perplex.md
  - sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md
  - concepts/llm-codegen-prompt-security-redistribution.md
maturity: draft
created: 2026-10-02
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K277 wave)"
---

## Relations

- @concepts/inbound-security-wave-2026-10-07.md — inbound brief wave 2026-10-07
- @concepts/k278-security-wave.md — next wave
- @sources/arxiv-2609.39902-codemimicry-2026-10-01.md — CodeMimicry (unread stub; source not obtained locally)
- @sources/newsletter-rss-tldrsec-2026-10-01-tldr-sec-348---googles-pagebreak-scanner-perplex.md — TLDR Sec 348 (unread stub)
- @sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md — K391 KaliBench
- @concepts/llm-codegen-prompt-security-redistribution.md — K309 codegen prompt redistribution

## Raw Concept

Aggregation page for the **K277 cyber-lab** brief (`briefs/2026-10-01_k277-cyber-lab.md`), which the
daily routine wrote but never materialised as wiki pages. This page records the content that brief
already vetted.

## Narrative

Two findings, one threat-class and one tooling.

**Code-domain safety lag.** A harmful request wrapped in valid code dodges refusal — CodeMimicry
reports roughly **96% success across eight commercial models in about 1.5 attempts**. Natural-language
safety training does not carry into the code modality. The useful half is the mitigation table the
authors report, as **residual** success after each defence:

| Defence | Residual success |
|---------|------------------|
| Llama Guard + perplexity filtering | 76–100% |
| Representation Bending | 38% |
| Circuit Breaker | 8% |
| SelfDefend | 4–14% |

The method uses **comments and docstrings as a side channel**, so stripping them helps. The lesson to
carry: **prompt-level guards are not sufficient for inputs that carry code** — the code modality needs
its own control, not a text guard reused.

**Confirm, then report.** Google's **PageBreak** agent validates a suspected cross-site-scripting bug
against a running environment *before* reporting it, reporting near-zero false positives and 500+ bugs
since November 2025. Perplexity open-sourced **Numbat**, which hooks coding harnesses and blocks risky
agent actions with 52 built-in rules. Names only — do not install from this note.

**Why this is an audit pattern.** Both halves point the same way: a detector's *claim* is not evidence
until something checks it against ground truth. PageBreak confirms before reporting; the code-safety
table reports what survives each defence rather than asserting the defence works. That is the same
discipline as @concepts/ai-redteam-evidential-ceiling.md and the K388 breaking-level rule
(@concepts/benchmark-shortcut-attack-pyramid-audit.md).

**Operator note:** no exploit path, payload, or step list belongs on this page. The K277 brief is
correct to keep it to the defensive table and the names.

## Snippets

> Defensive half is the part to keep … prompt-level guards are not sufficient for inputs that carry
> code. [Source: `briefs/2026-10-01_k277-cyber-lab.md`]
