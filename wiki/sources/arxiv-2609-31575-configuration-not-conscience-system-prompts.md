---
title: "Configuration, not conscience: a large-scale empirical study of LLM system prompts"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.31575, k377]
related:
  - concepts/nl-security-rules-vs-builtin-deny.md
  - concepts/genai-access-control-policy-enforcement.md
  - concepts/llm-system-prompt-corpus-audit.md
  - concepts/system-prompt-leakage.md
maturity: draft
read_status: read
created: 2026-09-28
updated: 2026-09-28
phase_0_verdict: "REFERENCE 2026-09-28 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K377)"
---

## Relations

- @concepts/llm-system-prompt-corpus-audit.md
- @concepts/system-prompt-leakage.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Configuration, not conscience: a large-scale empirical study of LLM system prompts |
| arXiv | 2609.31575 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.31575-configuration-not-conscience-a-large-scale-empir.pdf |
| Retrieved | 2026-09-28 |
| Read status | read (abstract + triage) |

## Narrative

**K377** — merged corpus of **407** leaked / reconstructed / official system prompts from **62** vendors (29 near-duplicate clusters / 66 files). Operational text dominates: ~**58%** classified words **tool/protocol**, ~**5%** **safety policy**; strictest rule-lines guard **tool use and file safety** over harmful-content by ~**11:1**. Treat leaked prompts as **operational configuration and supply-chain**, not vendor values. Prompt **rot** (version chains, stale refs, contradictions) is a maintenance debt. Authors publish **no new extraction** and report vendor aggregates. **Do not clone leak corpora. Do not paste leaked prompt bodies into wiki.** Audit-only (no precheck script). Pairs system-prompt leakage (LLM07).

## Snippets

> See arXiv 2609.31575 abstract. [Source: arXiv 2609.31575 (retrieved 2026-09-28)]
