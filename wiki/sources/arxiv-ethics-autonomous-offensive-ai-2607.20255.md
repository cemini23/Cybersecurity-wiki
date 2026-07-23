---
title: Ethics of autonomous offensive AI agents — arXiv 2607.20255
type: source
tags: [source, arxiv, ethics, offensive-security, agentic-ai]
keywords: [2607.20255, Happe, Cito, Wachter, indeterminacy, moral attribution]
related:
  - concepts/ethics-autonomous-offensive-ai-agents.md
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/responsible-disclosure.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-23
phase_0_verdict: "REFERENCE 2026-07-23 — ethics analysis; no code"
---

**Briefs:** `briefs/2026-07-23_k211-ethics-autonomous-offensive-agents-prod.md`

## Relations

- @concepts/ethics-autonomous-offensive-ai-agents.md
- @concepts/agentic-offensive-security-kill-chain.md
- @concepts/responsible-disclosure.md
- @concepts/llm-pentest-automation.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Ethics of Autonomous AI Agents for Offensive Security |
| Authors | Andreas Happe, Jürgen Cito (TU Wien); Jasmin Wachter (Klagenfurt) |
| arXiv | 2607.20255 |
| Code | none |
| CCC | K208 light steal → `@ccc-wiki/concepts/offensive-agent-ethics-oversight-posture.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20255-the-ethics-of-autonomous-ai-agents-for-offensive.pdf` |
| Retrieved | 2026-07-23 |

## Narrative

Agentic offensive tools differ from Nessus/Metasploit-class deterministic tooling along **three indeterminacies**:

1. **Action** — non-deterministic policy; hard to explain ex-ante/ex-post → attribution + safety review friction
2. **Impact** — open-ended via model agency + opaque LLM supply chains
3. **User population** — skill floor dropped; indeterminate who can industrialize offense

Combined with offense/defense cost asymmetry → short-term favors attackers. Moral attribution diffuse across users, tool-makers, third parties. Stratified recommendations + **methodological humility**.

### Steal

1. Keep **human moral agency** explicit in autonomous offensive agent runbooks
2. Pre-deploy review cannot assume deterministic tool semantics
3. Dual-use frameworks need update for indeterminate user × impact

## Snippets

> "agentic security tools exhibit indeterminacy along three independent dimensions… Combined with the structural cost asymmetry between offense and defense, they enable the industrialization of offensive capability."
[Source: arxiv-2607.20255 abstract]
