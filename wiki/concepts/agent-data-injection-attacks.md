---
title: Agent data injection attacks (ADI)
type: concept
tags: [concept, agent-security, ipi, trusted-untrusted, data-injection]
keywords: [adi, agent data injection, probabilistic delimiter, dt du isolation, 2607.05120]
related:
  - sources/arxiv-2607-05120-agent-data-injection-attacks.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/agent-execution-provenance.md
  - concepts/llm-code-review-agent-security.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - concepts/mcp-taint-style-vulnerabilities.md
  - sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
  - entities/tools/spellsmith.md
  - sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - "@ccc-wiki/concepts/agent-data-injection-attacks.md"
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - entities/tools/aha-auto-research-red-teaming.md
  - sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md
  - concepts/agent-reconnaissance-ipi-pentesting.md
  - sources/arxiv-2607-19837-know-your-agent-recon.md
maturity: draft
created: 2026-07-09
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
---

**Briefs:** `briefs/2026-07-09_adi-trusted-untrusted-data-handoff.md`, `briefs/2026-07-09_prod-mcp-trusted-untrusted-data-isolation-checklist.md`

## Relations

- @sources/arxiv-2607-19837-know-your-agent-recon.md
- @concepts/agent-reconnaissance-ipi-pentesting.md
- @sources/arxiv-2607-05120-agent-data-injection-attacks.md — ADI paper + benchmark (2607.05120)
- @concepts/mcp-execution-control-invariants.md — HCP I1/I4 principal binding complements DT/DU isolation

## Raw Concept

Ingest 2026-07-09: arXiv 2607.05120 — **agent data injection** bypasses instruction-injection defenses by forging **trusted** fields (sender, tool names, delimiters) inside agent data, not by injecting new instructions.

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/adi` (~5.1MB, shallow; `compsec-snu/adi`). Lab reproduction of trusted/untrusted isolation only.


### Trust model inside agent data

```
Agent context = Instruction I + Data D = (DT trusted, DU untrusted)
II attack:  DU misread as I
ADI attack: DU misread as DT (metadata / structure / security anchor)
```

Wiki layers:
- **Admission** (@concepts/mcp-security-posture.md) — which tools enter catalog
- **Execution control** (@concepts/mcp-execution-control-invariants.md) — what invocations may do
- **ADI gap** — **within** tool responses: no DT/DU boundary enforcement

### Probabilistic delimiter injection

Attackers embed near-valid delimiters in `DU` so the LLM parses fake objects/fields. Structural consistency matters: consistent JSON attacks **31–43%** ASR vs inconsistent **12–20%**.

### prod-mcp / lazy-tool steals [TENTATIVE]

| Control | Rationale |
|---------|-----------|
| Server-side DT assignment | Never let LLM infer sender/tool-name from untrusted body alone |
| Nonce field names (randomization) | Blocks delimiter collision on key-value formats |
| Strict data-flow labels | CaMeL-class taint on tool-response parsing |
| Sanitize with utility tradeoff | Strips legit URLs/paths — impractical alone |
| Red-team ADI suite | `compsec-snu/adi` + AgentDojo ADI extension (108 attacks) |

### vs tool-description poisoning

@concepts/cross-tool-description-poisoning.md poisons **tool metadata at registration**. ADI poisons **runtime agent data** after trusted tools return attacker-influenced content — orthogonal failure modes.

### Coding-agent relevance

Spoofed GitHub maintainer identity + fake tool results → RCE / merge-without-review on Claude Code, Codex, Gemini CLI. Pair merge-gate hardening (@concepts/llm-code-review-agent-security.md) with **identity provenance** on tool blocks.

## Snippets

> "Current agents do not isolate trusted data from untrusted data."
[Source: arxiv-2607.05120 abstract]
