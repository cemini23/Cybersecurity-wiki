---
title: AISPA user-centric system prompt auditing (arXiv 2607.28617)
type: source
tags: [source, arxiv, system-prompts, auditing, transparency]
keywords: [2607.28617, AISPA, SystemPromptIndex, protective vs problematic, 8 dimensions]
related:
  - concepts/aispa-system-prompt-assurance-audit.md
  - entities/tools/system-prompt-index.md
  - concepts/system-prompt-leakage.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-07-31
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-31 — SystemPromptIndex public dataset NO LICENSE; wait before clone"
---

**Briefs:** `briefs/2026-07-31_k232-aispa-prod.md`

## Relations

- @concepts/aispa-system-prompt-assurance-audit.md
- @entities/tools/system-prompt-index.md
- @concepts/system-prompt-leakage.md
- @concepts/ai-for-cybersecurity.md
- @concepts/agent-runtime-guardrails.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AISPA: User-Centric System Prompt Auditing for Large Language Model Applications |
| Authors | Lin, Zhu, Yang, Zhang, et al. (Stanford / CMU / UT Austin / multi-inst) |
| arXiv | 2607.28617 |
| Data/Site | https://SystemPromptIndex.com/ · github.com/XiangningLin/SystemPromptIndex (~11MB, **NO LICENSE**) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.28617-aispa-user-centric-system-prompt-auditing-for-la.pdf` |
| Retrieved | 2026-07-31 |

## Narrative

System prompts govern commercial AI apps but are rarely disclosed — trust/accountability gap. **AISPA**: eight-dimension user-centric taxonomy + human-in-the-loop audit workflow. Audit of **3,249 instructions / 88 products** (corpus also published as 1,017 prompts / span-level audits). Labels protective vs problematic. Variance huge (some orgs >60 protective instructions/product, others <5). Protective density rising over time; problematic instructions persist.

### Steal

1. Audit every production system prompt against AISPA-style dimensions before ship
2. Score protective vs problematic spans — not whole-prompt vibe checks
3. Watch LICENSE on SystemPromptIndex before any local clone / redistribution

## Snippets

> "system prompts … are rarely disclosed to the public or regulators, creating a serious trust and accountability gap"
[Source: arxiv-2607.28617 abstract]
