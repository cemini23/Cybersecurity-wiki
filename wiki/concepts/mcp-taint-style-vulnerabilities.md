---
title: MCP taint-style vulnerabilities
type: concept
tags: [concept, mcp, taint-style, server-security, injection]
keywords: [taint-style, mcp server, command injection, ssrf, path traversal, spellsmith, 2607.07461]
related:
  - sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
  - entities/tools/spellsmith.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/agent-data-injection-attacks.md
  - sources/arxiv-2607-05120-agent-data-injection-attacks.md
  - concepts/ai-for-cybersecurity.md
  - concepts/mcp-security-evidence-grounded-detection.md
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
maturity: draft
created: 2026-07-09
updated: 2026-07-18
---

**Briefs:** `briefs/2026-07-09_spellsmith-mcp-taint-mitigation-handoff.md`

## Relations

- @sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md — NVD study + SpellSmith (2607.07461)
- @entities/tools/spellsmith.md — description-augmentation defense reference

## Raw Concept

Ingest 2026-07-09: arXiv 2607.07461 — **81.13%** of catalogued MCP server CVEs are taint-style (user input → sensitive sink). Exploitation is **LLM-mediated**: malicious prompts steer tool argument filling, not direct server access.

## Narrative

### MCP workflow attack point

```
Tool registration (metadata only) → LLM plans → tools/call (user-controlled args) → server sink
```

**75.47%** of vulns trigger at **invocation** — aligns with prod-mcp needing pre-invoke policy, not just admission scans.

### Taint taxonomy (53-case study)

| Type | Share |
|------|-------|
| Command injection | 50.94% |
| Path traversal | 16.98% |
| Unauthorized access | 11.32% |
| SSRF | 5.66% |
| SQL / code injection | 3.77% each |

Metadata gap: only **7%** of tool descriptions include security-aware (T3) guidance.

### Mitigation lanes

| Lane | Mechanism | Cost |
|------|-----------|------|
| Code patch | Avg **203 LOC** / 37.3d cycle | High; often incomplete |
| Input/output guards | MCP Guardian-class | Reactive; misses planner misalignment |
| **SpellSmith** | Augment `description` + reflection | Low touch; **0.13%** case ASR in paper |
| HCP execution invariants | Post-admission invoke control | Complements description layer |

### prod-mcp checklist steal

1. Classify each allowlisted tool by sink (network, filesystem, shell, DB)
2. Require T3 security clauses in proxied tool descriptions
3. Add reflection turn before high-risk `tools/call`
4. Do not assume code-level server patches keep pace (92.3d exposure on unfixed)

## Snippets

> "Taint-style vulnerabilities constitute a substantial fraction (81.13%) of the total MCP server vulnerabilities."
[Source: arxiv-2607.07461 §1 — paraphrase anchor]
