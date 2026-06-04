---
title: "Which Defense Closes Which Threat? — OWASP LLM Top 10 defense attribution (arXiv:2606.02822)"
type: source
tags: [arxiv, llm-security, owasp, bas, evaluation, defense-in-depth, research-paper]
keywords: [owasp llm top 10, defense lattice, breach attack simulation, llm01, llm06, llm07, paraphrase brittleness, refusal filter]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/llm-defense-lattice.md
  - entities/tools/defenseclaw.md
  - entities/tools/cryptex-oss.md
  - entities/tools/seclaw-eval.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
maturity: draft
read_status: read
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @concepts/agent-runtime-guardrails.md — per-defense-family attribution vs aggregate “LLM secured” claims
- @concepts/llm-adversarial-fuzzing.md — paraphrase brittleness on refusal-phrase filters
- @concepts/llm-pentest-automation.md — BAS-style pre-release probing for LLM endpoints
- @concepts/ai-for-cybersecurity.md — OWASP LLM Top 10 operational measurement
- @entities/tools/llm-defense-lattice.md — open benchmark artifacts (Docker lattice + 17-probe corpus)
- @entities/tools/defenseclaw.md — enterprise runtime governance (complementary to stub-lattice BAS)
- @entities/tools/cryptex-oss.md — attack-side paraphrase/mutation for brittleness testing
- @entities/tools/seclaw-eval.md — trajectory-aware agent benchmark (orthogonal eval axis)
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface ASR vs per-defense attribution
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — stateful agent trajectory eval

## Raw Concept

- **Title**: Which Defense Closes Which Threat? Attributing OWASP-LLM-Top-10 Coverage and Its Brittleness Under Paraphrasing
- **Author**: Alexandre Cristovão Maiorano (Lumytics)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2606.02822-which-defense-closes-which-threat-attributing-ow.pdf`
- **URL**: https://arxiv.org/abs/2606.02822
- **Artifacts**: https://github.com/alemaiorano/llm-defense-lattice
- **Retrieved**: 2026-06-04
- **Read-status**: read

## Narrative

BAS-style measurement for **OWASP LLM Top 10 (2025)** on synthetic Node.js Docker targets. Four-level **defense lattice** (single-axis ablations, not a cumulative chain):

| Target | Defenses | Categories closed (verbatim corpus) |
|--------|----------|-------------------------------------|
| **L₀** | None | All five probed categories fire |
| **L₁** | Refusal-phrase whitelist (Lakera-Guard-style regex) | LLM01 jailbreak, LLM07 system-prompt leakage |
| **L₂** | Budget-only (max_tokens, model allowlist, rate limit) | LLM02 sensitive-info disclosure, LLM10 unbounded consumption |
| **L₃** | L₁ ∪ L₂ + tool-registry auth + credential scrub | LLM06 excessive agency (requires full stack) |

**Key ops finding**: aggregate BAS coverage scores **hide** which mitigation family closes which OWASP category — teams can “pass” with refusal-only while budget/agency gaps remain.

**Brittleness**: 300 Gemini paraphrases (K=5 × 60 templates) drop L₁ block rate **15 pp** on LLM01 and **25 pp** on LLM07; L₂ budget controls show **0 pp** drop after rate-limit floor. Refusal whitelists defeated by LLM paraphraser without intent change; budget controls resist same mutation `[TENTATIVE]` — stub targets only.

Covers 5/10 OWASP LLM categories (LLM01/02/06/07/10); LLM03–05/08/09 need different target layers (SBOM, training pipeline, parsers, RAG index, semantic judge).

Engine: 25 agents (21 baseline + 4 OWASP-LLM-aware), 17-probe locked JSON corpus. Reported finding-level F₁ 0.86 on verbatim run (precision 1.00, recall 0.75).

## Snippets

> "A refusal whitelist that clears a static benchmark can be defeated by an LLM-driven paraphraser without changing attack intent; a budget control resists the same mutation."

> "Existing BAS benchmarks … answer with a single aggregate coverage number; none say which defense family closes which category."

[Source: arXiv:2606.02822 abstract + §1, retrieved 2026-06-04]
