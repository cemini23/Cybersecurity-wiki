---
title: Toward Secure LLM Agents — threat surfaces survey (arXiv 2606.10749)
type: source
tags: [source, arxiv, survey, agent-security, lifecycle, evaluation]
keywords: [2606.10749, llm agent security, 247 papers, threat surfaces, delegated authority, persistent state]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/agentic-containment-principles.md
  - concepts/trajectory-context-control.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
maturity: draft
read_status: read
created: 2026-06-11
updated: 2026-06-15
---

## Relations

- @concepts/ai-for-cybersecurity.md — lifecycle security framing for LLM × cyber workflows
- @concepts/agent-runtime-guardrails.md — defense-layer taxonomy complement
- @sources/arxiv-2606-04990-agent-traces-evidence-provenance.md — narrower provenance/eval survey (33 pp vs 42 pp lifecycle)
- @entities/tools/llm-defense-lattice.md — OWASP BAS attribution slice of defense eval gap

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation |
| Authors | Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang (Nanjing U, TUM) |
| arXiv | 2606.10749 |
| Corpus | **247 papers** (hybrid retrieval + LLM-assisted screening) |
| Location | `raw-sources/arxiv-2606.10749-toward-secure-llm-agents-threat-surfaces-attacks.pdf` |
| Retrieved | 2026-06-11 |
| Read status | **read** (abstract + framework + conclusions; full 42 pp skimmed) |

## Narrative

Lifecycle-based **systems-oriented** survey: agent security = interaction of **information flow**, **delegated authority**, and **persistent state** — not prompt-level safety alone [CONFIRMED].

### Four organizing questions

1. How should LLM agent security be **modeled**?
2. Which **threat surfaces** and attack families dominate?
3. What **defenses** exist and what tradeoffs?
4. How are security claims **evaluated**?

### Findings [CONFIRMED]

| Theme | Survey conclusion |
|-------|-------------------|
| Dominant attacks | Prompt injection + **tool-mediated control-flow hijacking** |
| Emerging | **Persistent state corruption** + **multi-agent propagation** |
| Defenses | Useful building blocks but **weakly compositional** — layered stack needed |
| Benchmarks | Underrepresent **long-horizon**, **stateful**, deployment-sensitive risks |
| Prescription | Explicit trust boundaries, privilege control, **provenance-aware state**, realistic eval |

Maps cleanly onto this wiki's K95–K100 stack: skill/MCP injection, SPI, MSTI, provenance tracing (04990), CFD artifact gap (09084).

## Snippets

> "Secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings."
> — [Source: arxiv-2606.10749 abstract, retrieved 2026-06-11]

> "This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework."
> — [Source: arxiv-2606.10749 abstract, retrieved 2026-06-11]

## Dead Ends

- **Single-defense vendor claims** without compositional eval — survey flags weak cross-layer coverage.
- **Static prompt benchmarks** as sole agent-security gate — understate persistent/multi-agent failure modes per authors.
