---
title: "Constrained-action AI remediation for SIEM/XDR via a guardrails proxy"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.09906, k410]
related:
  - concepts/constrained-action-soc-remediation.md
  - concepts/step-level-agent-guardrails.md
  - concepts/non-decaying-loop-safety-state.md
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K410)"
---

## Relations

## Relations

- @concepts/constrained-action-soc-remediation.md
- @concepts/step-level-agent-guardrails.md
- @concepts/non-decaying-loop-safety-state.md
- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Constrained-action AI remediation for SIEM/XDR via a guardrails proxy |
| arXiv | 2610.09906 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610-09906-constrained-action-ai-remediation-for-siem-xdr-v.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K410** — SOCs are drowning in correlated alerts with too few analysts, and LLM remediation is the obvious lever. This wires an LLM into SIEM/XDR **through a NeMo-Guardrails proxy** so the model proposes remediation but a rail constrains what it can emit. Injection defence over 200 adversarial variants (AdvBench, JailbreakBench, HarmBench, homoglyph, Base64, fake `[SYSTEM]` framing, zero-width): **proxy recall 94.5% at 0.1% FPR** against a raw LLM's **25.0% at 0.0%** — +69.5 pp — with the proxy catching **189/200** at the input rail.

The cost is latency: proxy P50 **14.14 s** against **0.31 s** for the bare call (~46×), and the latency curve goes bimodal. The fix is the interesting part: a **deterministic Tier-0 gate** in front — **58% recall at 0.00% FPR, 0.18 s (78× faster)**, and alone it recovers all 50 augmented records **with zero LLM calls**. Live active-response testing (T1110, T1059, T1078): **54 injected alerts produced 41 action records, every one requiring manual approval, none dispatched**, and an argument validator rejected a target failing its schema. Operator steal: **cheap deterministic gate first, LLM rail second, and human approval on every action** — the schema validator is doing real work, not decoration. Pairs K307/K312 (gate before the irreversible step).

## Snippets

> See arXiv 2610.09906 abstract. [Source: arXiv 2610.09906 (retrieved 2026-10-09)]
