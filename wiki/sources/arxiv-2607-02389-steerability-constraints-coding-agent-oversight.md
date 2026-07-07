---
title: Steerability via constraints — coding-agent oversight substrate (arXiv 2607.02389)
type: source
tags: [source, arxiv, coding-agents, oversight, substrate, steerability, dl4code]
keywords: [2607.02389, substrate constraints, scalable oversight, docs cli, backdoor detection, gemma reviewer]
related:
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-code-review-agent-security.md
  - concepts/local-agent-runtime-audit.md
  - concepts/agent-vm-sandboxing.md
  - concepts/mcp-security-posture.md
  - concepts/agent-execution-provenance.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - concepts/ai-for-cybersecurity.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/defending-code-reference-harness.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
maturity: draft
read_status: read
created: 2026-07-07
updated: 2026-07-07
phase_0_verdict: "Reference 2026-07-07 — ICML DL4Code workshop; no canonical public repo at ingest (BACKDOORS.md promised with code); adopt substrate + docs-CLI methodology"
---

**Briefs:** `briefs/2026-07-07_steerability-substrate-coding-agent-oversight-handoff.md`, `briefs/2026-07-07_harness-substrate-constraints-checklist.md`

## Relations

- @concepts/substrate-constraints-coding-agent-oversight.md — synthesis page
- @concepts/llm-code-review-agent-security.md — merge-gate / reviewer threat model complement

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Steerability via constraints: a substrate for scalable oversight of coding agents |
| Author | Thomas Winninger (Télécom SudParis; ENS Paris-Saclay) |
| Venue | Deep Learning for Code Workshop, ICML 2026, Seoul |
| arXiv | 2607.02389 |
| Code | Promised with experiment artifacts (`BACKDOORS.md`); **no public repo URL at ingest** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.02389-steerability-constraints-coding-agent-oversight.pdf` |
| Retrieved | 2026-07-07 |
| Read status | **read** (stance, system sketch, 2×2 backdoor experiment, appendix decomposition) |

## Narrative

Coding agents can generate thousands of LoC; the bottleneck shifts to **verification before execution**. Paper argues pre-LLM engineering controls — access control, network policy, linter-enforced conventions — transfer to agents and are **cheaper in tokens** than heavy MCP/agentic scaffolding.

### Three pillars

| Pillar | Mechanism | vs prompt-only |
|--------|-----------|----------------|
| **Substrate constraints** | ruff (security/bugbear/bandit), pyrefly, beartype, pydantic `extra="forbid"`, jaxtyping, frozen dataclasses | **Refuse** violating code — not advisory |
| **Machine isolation** | Hardware VM + egress allowlist + LiteLLM-style inference proxy (IPI probe, planned privacy rewriter) | No prompt can grant/revoke |
| **Projection CLI** | ~200 LoC `docs` CLI (module / symbol / examples) via AST — not raw MCP dumps | Lazy-load; human-auditable output |

### Backdoor experiment (11 stratified, ~500 LoC Python LM-eval toy)

Reviewer: **Gemma 4 e4b** (8B-class), per-function multi-pass review (self-consistency, I/O contract, invariant check).

| Setup | Caught | Recall |
|-------|--------|--------|
| C1 — unconstrained, no tools | 6/11 | **54.5%** |
| C2 — unconstrained + docs CLI | 9/11 | 81.8% |
| C3 — constrained substrate, no tools | 9/11 | 81.8% |
| C4 — constrained + docs CLI | 10/11 | **90.9%** |

**Decomposition [CONFIRMED]:** substrate alone +3 (L5 global invariants); tools alone +3; marginal +1 each when combined (L3b tools-only; L5c substrate-only).

**Key design signal:** L5 backdoors caught when invariants live in **module docstrings**; missed when same text sits in root `ARCHITECTURE.md` (context locality).

### vs wiki stack

| Concern | Existing wiki | This paper |
|---------|---------------|------------|
| Runtime implementation bugs | @concepts/local-agent-runtime-audit.md CLAWAUDIT | Substrate makes violations textually visible to weak reviewers |
| PR merge social engineering | @concepts/llm-code-review-agent-security.md SEVRA | Per-function invariant review on structured substrate |
| MCP context saturation | @concepts/mcp-security-posture.md | Prefers small composable CLI over protocol-bound tool dumps for local code |
| VM isolation | @concepts/agent-vm-sandboxing.md | VM + network proxy + inference proxy as machine-layer constraints |
| Trajectory eval | @concepts/seclaw-agent-security-evaluation.md | 2×2 substrate×tools as oversight eval template |

### Phase-0 (2026-07-07)

| Gate | Status |
|------|--------|
| License / repo | **N/A** — no public artifact at ingest |
| Domain fit | Coding-agent oversight methodology — high relevance to CCC harness + merge gates |
| Verdict | **Reference** — steal substrate checklist + docs-CLI pattern; re-audit when code releases |

## Snippets

> "Recall rises from 54.5% (unconstrained, no tools) to 90.9% (constrained substrate plus a ~200-LoC docs CLI), with substrate and tools contributing independently."
[Source: arxiv-2607.02389 abstract]

> "MCP mediated retrieval can work against this discipline by saturating the agent's context with raw payloads."
[Source: arxiv-2607.02389 §1 — paraphrase anchor]
