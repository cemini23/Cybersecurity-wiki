---
title: Substrate constraints for scalable coding-agent oversight
type: concept
tags: [concept, coding-agents, oversight, steerability, substrate, verification]
keywords: [substrate constraints, docs cli, per-function review, invariant locality, scalable oversight, 2607.02389]
related:
  - sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md
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
  - "@ccc-wiki/concepts/substrate-constraints-coding-agent-oversight.md"
maturity: draft
created: 2026-07-07
updated: 2026-07-07
---

**Briefs:** `briefs/2026-07-07_steerability-substrate-coding-agent-oversight-handoff.md`, `briefs/2026-07-07_harness-substrate-constraints-checklist.md`

## Relations

- @sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md — paper + 2×2 experiment (2607.02389)
- @concepts/llm-code-review-agent-security.md — adversarial PR framing vs structural backdoor review

## Raw Concept

Ingest 2026-07-07: arXiv 2607.02389 — **steerability via constraints** replaces prompt-only oversight of coding agents with enforceable substrate + lightweight projection tools. Small trusted reviewer (Gemma 4B) reaches **90.9%** backdoor recall vs **54.5%** on unconstrained code.

## Narrative

### Prompt advisory vs substrate enforceable

```
Advisory layer     → system prompts, skills, planner instructions (may drift)
Substrate layer    → linters, types, runtime contracts, VM/network/inference proxies (refuse violations)
Projection layer   → docs CLI / AST views (bounded context for reviewers)
```

Complements @concepts/agent-runtime-guardrails.md (side-effect authority) and @concepts/local-agent-runtime-audit.md (runtime implementation STRIDE) by making **generated code** itself easier to audit.

### Substrate conventions (Python) [TENTATIVE]

| Control | Purpose |
|---------|---------|
| ruff security + bugbear + bandit | Block bare-except, obvious injection patterns |
| pyrefly + jaxtyping | Narrow types visible in headers |
| beartype + pydantic strict | Runtime contract enforcement |
| Frozen/slotted/kw-only dataclasses | Prevent smuggling via mutable extras |
| `tuple` / `Mapping` over `list` / `dict` | Reduce silent mutation |
| `Literal` discriminators | Hypervisible branch contracts |
| **Invariants in module docstrings** | Locality beats centralized ARCHITECTURE.md (L5 signal) |
| `core/` purity split | Per-function review bundles stay ≤4K tokens |

### Projection CLI pattern

~200 LoC AST tool with three commands:

- `docs module X` — public API + Invariants/Conventions blocks
- `docs symbol X.Y` — signature, fields, docstring
- `docs examples X` — tests-as-spec (planned; Hypothesis-friendly)

For **developer-owned local repos**, paper argues this beats MCP context dumps that saturate reviewer context (@concepts/mcp-security-posture.md). Does **not** replace prod-mcp admission for untrusted third-party servers.

### Multi-pass per-function review

8B reviewer fixates on first finding in single-pass (C4 single-pass **4/8** vs multi-pass **10/11**). Minimum scaffolding:

1. Self-consistency (name ↔ body ↔ docstring)
2. I/O contract (type width vs misuse)
3. Invariant check (module docstring vs body)

Pair with SEVRA framing red-team (@concepts/llm-code-review-agent-security.md) and cognitive-heuristic perturbations (@concepts/cognitive-heuristics-llm-vuln-detection.md).

### Machine-layer stack

| Layer | Control |
|-------|---------|
| VM | Hardware-isolated agent environment (@concepts/agent-vm-sandboxing.md) |
| Network proxy | Egress allowlist |
| Inference proxy | Per-message IPI probe + planned privacy rewriter |

### Eval template

Use 2×2 **substrate × projection tools** when benchmarking oversight agents — not just strong-writer / weak-reviewer capability gaps.

## Snippets

> "Substrate constraints, in contrast, are not advisory: linters, type checkers, runtime contract validators … refuse to run code that violates them."
[Source: arxiv-2607.02389 §3.1 — paraphrase anchor]
