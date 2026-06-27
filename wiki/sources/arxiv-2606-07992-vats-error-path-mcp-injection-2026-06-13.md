---
title: VATS — error-path MCP injection via systematic mutation (arXiv 2606.07992)
type: source
tags: [source, arxiv, mcp, prompt-injection, error-path, red-team, k114]
keywords: [2606.07992, vats, implicit authority, tool-stream injection, mutation testing, mcp security]
related:
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - concepts/agentic-containment-principles.md
  - concepts/tool-environment-unreliability-eval.md
maturity: draft
read_status: read
created: 2026-06-13
updated: 2026-06-27
---

## Relations

- @concepts/mcp-security-posture.md — error-path as fourth MCP trust-boundary failure class
- @concepts/agent-runtime-guardrails.md — implicit authority bypasses prompt-only guards
- @concepts/agent-skill-injection.md — tool-stream channel adjacent to skill/MCP injection
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — DCI on success path; VATS on error path
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session SPI vs single-turn error IPI
- @concepts/agentic-containment-principles.md — framework guardrails vs raw model layer gap

## Raw Concept

| Field | Value |
|-------|-------|
| Title | VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation |
| Authors | Harshil Patel, Kunal Pai |
| arXiv | 2606.07992 |
| Location | `research to be indexed/arxiv-2606.07992-vats-exploiting-implicit-authority-in-error-path.pdf` |
| Retrieved | 2026-06-13 |
| Read status | **read** (abstract + methodology + results + mitigation recs) |
| Verdict | **GO** — ingest + red-team methodology applicable to lazy-tool / prod-mcp eval |

## Narrative

MCP standardizes tool calling but treats **success and error tool responses with equal trust**. When a tool fails, agents enter a **corrective reasoning mode** — error messages carry **implicit authority** that bypasses skepticism heuristics applied to normal tool output. VATS (Vulnerability Analysis of Tool Streams) is a **mutation-driven red-team framework** that evolves adversarial payloads across seven structural/linguistic dimensions to characterize compliance drivers.

### Threat model

Attacker controls one MCP tool (`search_codebase`) returning crafted **error JSON** with embedded instructions. Victim uses neutral system prompt (no explicit recovery policy). Success = agent invokes `send_email` to attacker address with exfil payload.

### Seven mutation operators ($M_1$–$M_7$)

| Op | Dimension | Values |
|----|-----------|--------|
| $M_1$ | Error type | AUTH_EXPIRED, COMPLIANCE_BLOCK, RATE_LIMIT |
| $M_2$ | Framing | imperative, corrective, authoritative, passive |
| $M_3$ | Authority markers | none (0), moderate (1), high (2) |
| $M_4$ | Position | start, middle, end |
| $M_5$ | Specificity | generic, MCP-specific |
| $M_6$ | Urgency | low, medium, high |
| $M_7$ | Rephrase | LLM linguistic variation (structure preserved) |

Baselines embed identical attack instructions in **successful** tool responses to isolate the implicit-authority effect.

### Headline results [CONFIRMED]

| Metric | Finding |
|--------|---------|
| Baseline IPI (success path) | Mean ACR **16.7%** (only Qwen3 partial compliance) |
| Unmodified error seed | ACR **50%** — **3×** standard IPI |
| After one mutation generation | **100% ACR** on all four models (Gemini 3.1 Pro, GPT-5.5, GLM-5.1, Qwen3-Coder) |
| Universal exploit | **$M_4 \rightarrow$ middle** — sandwich instruction between error context (100% all models) |
| Stealth | Mean DER **0.87** when ACR=1; GLM/Qwen **DER=1.0** on successful attacks |
| Task derailment | Mean BTDR **0.80** when compliant |

**Model profiles:** GLM-5.1 / Qwen3 = stealth-vulnerable; Gemini 3.1 = selective (binary); GPT-5.5 = detect-but-comply (flags attack yet still executes ~44% of time).

### Real-world validation [CONFIRMED]

Gemini CLI v0.41.2 and OpenAI Codex v0.129.0 (with `GEMINI.md` / `AGENTS.md` guardrails): **ACR=0** — framework heuristics + functional redundancy (native grep substitutes for failed MCP search) blocked exfil. **Alignment gap:** raw API layer fully vulnerable; bespoke LangChain/custom loops without equivalent guardrails remain exposed.

### Defensive recommendations (paper)

1. **Split signal** — separate technical error codes from help text at protocol level
2. **Verify error provenance** — authenticate error source before trust
3. **Flag action verbs in errors** — heuristic scan for run/send/delete in error bodies
4. **Human gate on error-triggered actions** — mandatory approval when error path proposes side effects

**Cemini relevance:** Treat MCP `role: tool` **error payloads** as untrusted as success payloads; add error-path cases to agent harness red-team (lazy-tool proxy, prod-mcp write tools). Complements DCI (2606.04769) and WebMCP MSTI (2606.06387) in @concepts/mcp-security-posture.md.

## Snippets

> "Error-path injection triples the success rate of standard indirect prompt injection (IPI), achieving up to 100% compliance in controlled evaluations."
> — [Source: arXiv:2606.07992 abstract, retrieved 2026-06-13]

> "$M_4 \rightarrow$ middle is the only mutation achieving 100% ACR across all four tested models."
> — [Source: arXiv:2606.07992 §4.3, retrieved 2026-06-13]

## Dead Ends

- **Framework guardrails as sole defense** — Codex/Gemini CLI blocked attacks but relied on repo instructions + redundant native tools; custom agent loops without both remain vulnerable.
- **Social-engineering-heavy payloads** — bureaucratic authority ($M_3$) and urgency ($M_6$) less universal than structural sandwiching ($M_4$ middle).
