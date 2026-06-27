---
title: CLAWAUDIT — local LLM agent runtime source audit (arXiv 2606.21071)
type: source
tags: [source, arxiv, agent-security, openclaw, static-analysis, clawaudit]
keywords: [2606.21071, clawaudit, openclawbench, local agent runtime, semgrep, codeql, stride]
related:
  - concepts/local-agent-runtime-audit.md
  - entities/tools/clawaudit.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-23449-aohp-os-level-agent-harness.md
  - entities/tools/aohp.md

maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-27
phase_0_verdict: "CONDITIONAL-GO 2026-06-24 — github.com/SRestLabUB/ClawAudit artifact, 0★, gh api LICENSE null/404; Semgrep/CodeQL rules usable after manual triage + license check"
---

## Relations

- @concepts/local-agent-runtime-audit.md — runtime-layer audit methodology
- @entities/tools/clawaudit.md — CLAWAUDIT + OPENCLAWBENCH entity

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Local LLM Agents as Vulnerable Runtimes: A Source-Code Audit of the Agent Runtime Layer |
| Authors | Zhengsong Zhang, Zongze Li, Jiawei Guo, Haipeng Cai |
| Affiliation | University at Buffalo, SUNY |
| arXiv | 2606.21071v1 [cs.CR] |
| Code | [github.com/SRestLabUB/ClawAudit](https://github.com/SRestLabUB/ClawAudit) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.21071-pdf-local-llm-agents-as-vulnerable-runtimes-arxi.pdf` |
| Retrieved | 2026-06-24 |
| Read status | **read** (abstract, STRIDE taxonomy, OPENCLAWBENCH eval, recall tables) |

## Narrative

Frames local agents (OpenClaw, Nanobot) as **privileged software runtimes** — not model wrappers. The safety boundary is the implementation layer: prompt builder, parser, tool dispatcher, skill loader, memory writer, network client, permission gate.

**CLAWAUDIT** derives a five-category STRIDE taxonomy with agent-specific static rules (47 Semgrep YAML + 30 CodeQL queries). **OPENCLAWBENCH**: 446 OpenClaw advisories, temporal split 229 train / 217 test.

### Held-out test recall

| Backend | Baseline | CLAWAUDIT |
|---------|----------|-----------|
| Semgrep Pro | 21.7% | **66.8%** |
| CodeQL security-extended | 13.8% | **75.1%** |

Train/test gap ≤4 pp — rules generalize. **Caveat:** recall-oriented rules need substantial manual triage before production CI gates.

### Boundary categories (B1–B5)

Untrusted input → prompt builder (B1) → model → tool dispatcher (B2) → filesystem/sandbox (B3) / network (B4) / handler permission gate (B5).

Complements behavioral benchmarks (MalSkillBench, SeClaw) and marketplace scanners (ClawHub/SkillSpector) — those treat the agent as a black box; CLAWAUDIT audits **source structure**.

`[TENTATIVE]` — OpenClaw-focused benchmark; generalization to other local agent stacks unverified in this wiki.

## Snippets

> "A local LLM agent is not merely a model wrapper or a tool-use policy; it is a privileged software runtime."

> "CLAWAUDIT raises Semgrep recall from 21.7% (Pro baseline) to 66.8%, and CodeQL recall from 13.8% (security-extended) to 75.1%."

[Source: arxiv-2606.21071-pdf-local-llm-agents-as-vulnerable-runtimes-arxi.pdf]
