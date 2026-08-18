---
title: "CHIVE — counterfactual hypothesis investigation (GO REFERENCE)"
type: entity
tags: [tool, interpretability, eval, reference, k290]
keywords: [CHIVE, adamkarvonen/chive, MIT, counterfactual simulatability]
related:
  - sources/arxiv-2608-16747-chive-counterfactual-explanations.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/llm-code-review-agent-security.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "GO REFERENCE 2026-08-18 — github.com/adamkarvonen/chive MIT; shallow clone `.local/adopts/chive` ~11MB <500. Runtime wont_wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K290); runtime wont_wire"
---

## Relations

- @sources/arxiv-2608-16747-chive-counterfactual-explanations.md
- @concepts/counterfactual-simulatability-llm-explanations.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/llm-code-review-agent-security.md

## Raw Concept

Anthropic Fellows pipeline + datasets for in-the-wild counterfactual explanation eval. Interpretability-eval steal, not a pentest harness.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | GO REFERENCE clone |
| Path | `.local/adopts/chive` (gitignored) |
| LICENSE | MIT (file verified) |
| Size | ~11 MB (`du -sm`) |
| Wire | K290 explanation-as-evidence policy; **runtime wont_wire** |
