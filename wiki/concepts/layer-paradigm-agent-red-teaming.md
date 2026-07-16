---
title: Layer-paradigm agent red teaming
type: concept
tags: [concept, agent-security, ai-red-team, mcp, layer-model]
keywords: [layer-paradigm, infra-scan, mcp-scan, agent-scan, jailbreak-harness, ai-infra-guard]
related:
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - entities/tools/ai-infra-guard.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/local-agent-runtime-audit.md
  - concepts/llm-pentest-automation.md
  - concepts/agentic-containment-principles.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - entities/tools/clawaudit.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - entities/tools/aha-auto-research-red-teaming.md
  - sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - sources/arxiv-2607-11151-amt-x-phase-structured-multi-turn-red-teaming.md
  - sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md
maturity: draft
created: 2026-07-01
updated: 2026-07-16
---

## Relations

- @sources/arxiv-2606-31227-ai-infra-guard-technical-report.md — AI-Infra-Guard technical report (2606.31227)
- @entities/tools/ai-infra-guard.md — reference implementation + Phase-0

**Briefs:** `briefs/2026-07-01_ai-infra-guard-layer-paradigm-red-team-handoff.md`, `briefs/2026-07-01_ai-infra-guard-external-scanner-lab-checklist.md`

## Raw Concept

Ingest 2026-07-01: arXiv 2606.31227 argues **one-size-fits-all** security tooling fails on AI agents because attack surfaces are **heterogeneous across layers** — each layer needs a matched **detection paradigm**, not a single scanner type.

## Narrative

### Layer stack

```
Model          ← statistical jailbreak / alignment robustness (many adversarial trials)
Agent behavior ← black-box runtime probing; skill package supply chain
Protocol/tool  ← MCP servers, tool metadata, agentic static+LLM audit
Infrastructure ← deterministic CVE/misconfig rules on AI component images
```

### Paradigm matching (AI-Infra-Guard M1–M4)

| Layer | Why heterogeneous | Fitting paradigm | Example module |
|-------|-------------------|------------------|----------------|
| Infrastructure | Versioned CVEs, known misconfigs | Rule DB + fingerprinting | Infra-Scan (75+ components, 1,400+ rules) |
| Protocol/tool | Schema/description semantics | LLM-assisted agentic audit | MCP-Scan |
| Agent behavior | Runtime-only exposure; skill install paths | Multi-turn black-box red team | Agent-Scan (+ skill packages) |
| Model | Alignment is statistical | Operator suite × datasets | Jailbreak harness (26+ operators, 16 datasets) |

### Wiki integration

- **Do not collapse layers** — @concepts/mcp-security-posture.md admission/DCI gates protocol layer; @concepts/local-agent-runtime-audit.md covers **host runtime** implementation; @concepts/agent-skill-injection.md covers **persistent skill SPI** — none substitutes for infra CVE scanning or model jailbreak eval.
- **Lab ordering** — infra fingerprint → MCP/skill static audit → runtime agent probe → model robustness; failures at lower layers invalidate higher-layer tests.
- **Cemini constraint** — run breadth scanners (AI-Infra-Guard, DefenseClaw, SkillSpector) as **external Docker** only; vendoring triggers Tencent NOTICE §4(d) on @entities/tools/ai-infra-guard.md.

### Gaps / limits [TENTATIVE]

- Layer model is **descriptive** — no formal proof that four layers are complete; federated multi-agent deployments may need an additional **inter-agent trust** layer.
- Black-box agent scans may miss @concepts/context-fractured-decomposition-attacks.md style multi-turn fractures.
- Rule freshness for Infra-Scan still decays like any vuln scanner — pair with EPSS/KEV triage for prioritization.

## Snippets

> "The attack surface of an AI agent is stratified across layers (infrastructure, protocol/tool, agent behavior, and model), and no single detection paradigm fits all of them."
[Source: arxiv-2606.31227-ai-infra-guard-technical-report.pdf abstract — paraphrase anchor]
