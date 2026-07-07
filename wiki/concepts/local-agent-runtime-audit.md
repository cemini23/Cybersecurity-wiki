---
title: Local agent runtime audit
type: concept
tags: [concept, agent-security, static-analysis, openclaw, runtime, stride]
keywords: [clawaudit, openclawbench, runtime layer, semgrep, codeql, b1-b5, 2606.21071]
related:
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - entities/tools/clawaudit.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/ecc.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/ai-infra-guard.md
  - sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md
  - concepts/substrate-constraints-coding-agent-oversight.md

maturity: draft
created: 2026-06-24
updated: 2026-07-07
---

## Relations

- @sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md — CLAWAUDIT paper (2606.21071)
- @entities/tools/clawaudit.md — artifact + OPENCLAWBENCH

## Raw Concept

Ingest 2026-06-24: local LLM agents (OpenClaw-class) are **privileged runtimes** — the implementation mediating untrusted input → model → host actions is an unexamined safety boundary.

## Narrative

### Runtime data-flow (audit boundaries)

```
Untrusted input (user, RAG, memory, tool output)
  → B1 prompt builder
  → model
  → B2 tool dispatcher
  → B3 filesystem/sandbox | B4 network | B5 handler permission gate
```

Marketplace scanners (SkillSpector, DefenseClaw) and behavioral benches (SeClaw, MalSkillBench) treat agents as black boxes. **CLAWAUDIT** targets **source-level** weaknesses with STRIDE-derived Semgrep/CodeQL rules.

### Eval signal (OPENCLAWBENCH held-out)

| Backend | Baseline recall | CLAWAUDIT |
|---------|-----------------|-----------|
| Semgrep Pro | 21.7% | 66.8% |
| CodeQL security-extended | 13.8% | 75.1% |

**Operational caveat:** high recall rules → heavy manual triage before CI gate. Layer with behavioral red-team, not replace.

### Assessment ladder for local agent stacks

1. Pre-install skill/MCP scan (SkillSpector + DefenseClaw)
2. **Runtime source audit** (CLAWAUDIT-class on agent fork)
3. **Layer-paradigm breadth scan** — AI-Infra-Guard M1–M4 external Docker pass (infra rules → MCP-Scan → Agent-Scan → jailbreak harness) per @concepts/layer-paradigm-agent-red-teaming.md
4. Behavioral trajectory eval (SeClaw)
5. Runtime authority guard (AIRGuard) on dispatched actions

See `briefs/2026-06-24_clawaudit-openclaw-runtime-audit-checklist.md` and `briefs/2026-07-01_ai-infra-guard-external-scanner-lab-checklist.md`.

`[TENTATIVE]` — OpenClaw advisories only; Nanobot/other stacks not measured.

## Snippets

> "No prior work has systematically examined the agent's own source tree to audit these components for implementation-level security weaknesses."

[Source: arxiv-2606.21071]
