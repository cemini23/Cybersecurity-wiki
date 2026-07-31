---
title: CoGate confidence-gated co-decoding for secure code (arXiv 2607.28529)
type: source
tags: [source, arxiv, secure-coding, llm, decoding-time]
keywords: [2607.28529, CoGate, co-decoding, CWEval, SafeCoder, OOD]
related:
  - concepts/cogate-confidence-gated-secure-code.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
read_status: read
created: 2026-07-31
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-31 — no public CoGate repo located"
---

**Briefs:** `briefs/2026-07-31_k231-cogate-prod.md`

## Relations

- @concepts/cogate-confidence-gated-secure-code.md
- @concepts/llm-code-review-agent-security.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CoGate: Confidence-Gated Co-Decoding for Secure Code Generation |
| Authors | Hu, Luo (GMU); Roush, Howard (Thoughtworks) |
| arXiv | 2607.28529 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.28529-cogate-confidence-gated-co-decoding-for-secure-c.pdf` |
| Retrieved | 2026-07-31 |

## Narrative

Co-decoding steers code LLMs with a security expert at each token — but prior acceptance rules ignore expert **confidence**. Under OOD/unseen patterns, unconfident expert guidance misleads. **CoGate** gates acceptance on expert confidence (entropy-normalized). Reports +2.9% Pass@10 / +5.4% Security Ratio vs CoSec+; +12.6% Func-Sec@10 on CWEval (unseen CWEs).

### Steal

1. Never apply security-expert steering when the expert is low-confidence
2. Decoding-time secure-code gates need an explicit confidence threshold
3. Eval on unseen CWE suites (CWEval-class), not only train-distribution CWEs

## Snippets

> "existing methods conflate whether a security expert prefers a token with whether the expert is trustworthy enough to guide generation."
[Source: arxiv-2607.28529 conclusion]
