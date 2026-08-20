---
title: "Rule blindness in compliance detectors (arXiv 2608.16852)"
type: source
tags: [source, arxiv, guard-models, compliance, watch]
keywords: [2608.16852, rule blindness, ICS, Llama Guard 3, Qwen3Guard, Lexsi Labs]
related:
  - concepts/compliance-detector-rule-blindness.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/ai-redteam-evidential-ceiling.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "Watch 2026-08-20 — 0 MB. No author repo. Do not clone FujitsuResearch/LLM-policy-violation-detection (related work only)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (rule-blindness crossed-rule audit)"
---

**Briefs:** `briefs/2026-08-18_k160-rule-blindness-compliance-detectors-from-seo.md`

## Relations

- @concepts/compliance-detector-rule-blindness.md
- @concepts/prompt-injection-detector-calibration.md — detector verdict ≠ stated rule
- @concepts/ai-redteam-evidential-ceiling.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models |
| Authors | Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu, Pratinav Seth (Lexsi Labs) |
| arXiv | 2608.16852 (cs.AI, v1 17 Aug 2026) CC BY 4.0 |
| Code | none located; FujitsuResearch related-work repo is **not** this artifact |
| Retrieved | 2026-08-20 via SEO overflow brief (no new PDF in cyber inbox) |
| Read status | read (abstract + inbound brief) |

## Narrative

Compliance detectors (guard models + activation probes checking outputs against written rules — GDPR, healthcare, finance, platform policy) exhibit **rule blindness**: deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged across every guard/probe tested (Llama Guard 3, Qwen3Guard, LPG, ICS). A policy-conditioned guard can cite the governing clause 91–95% of the time and barely change its verdict when that clause is swapped for its permissive counterpart. A crossed-rule benchmark (two rules × two scenarios) confirms it; step-by-step reasoning escapes it, not any fast detector. ICS is a cheap training-free activation readout (10 labelled pairs, one projection) — useful as an audit scalpel, does **not** beat bag-of-words on pooled generalization; an adaptive white-box attack removes ranking gain. [Source: arXiv 2608.16852]

SEO overflow: SEO keeps a stub; cyber owns the audit protocol. No jailbreak PoC.

## Snippets

> Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test. [Source: arXiv 2608.16852 abstract]
