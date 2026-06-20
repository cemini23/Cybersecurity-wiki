---
title: Skillgate — Mitiga Labs free agent config scanner (SaaS)
type: entity
tags: [tool, ai-security, skill-supply-chain, mcp, saas, mitiga]
keywords: [skillgate, mitiga, skill.md, claude.md, hooks, mcp poisoning, owasp agentic ai]
related:
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - entities/tools/ecc.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
phase_0_verdict: "Reference 2026-06-20 — free SaaS at skillgate.mitiga.ai; closed source; use for third-party skill triage, not prod allowlist automation without export audit"
---

## Relations

- @entities/tools/nvidia-skillspector.md — local FOSS alternative (Apache-2.0)
- @entities/tools/defenseclaw.md — enterprise runtime governance
- @concepts/agent-skill-injection.md — SKILL.md / hooks / MCP poisoning taxonomy
- @sources/arxiv-2606-01494-clawhub-security-signals.md — scanner disagreement context (ClawHub study)

## Raw Concept

Digest pass 2026-06-20 (R7). [Mitiga Labs Skillgate](https://skillgate.mitiga.ai) — free scanner for AI agent configuration files: skills, hooks, agent rules, MCP server configs, `CLAUDE.md`, `AGENTS.md`. Productized from Mitiga **"License to Skill"** research series (June 2026).

## Narrative

Skillgate reads (does not execute) configuration at a **pinned GitHub commit** or pasted file content. Pipeline: signature + AST analysis + LLM-as-judge → risk score /100 and verdict (Clean / Risky / Suspicious / Dangerous). Maps findings to **OWASP Agentic AI Top 10**, MITRE ATT&CK, and ATLAS.

### Detection scope (press release)

| Surface | Technique families (80+ rules) |
|---------|------------------------------|
| SKILL.md, hooks, CLAUDE.md, Cursor/Continue/Cline rules | Direct execution, prompt manipulation, obfuscation |
| MCP tool descriptions, settings | Tool/MCP poisoning, credential exposure, supply chain |

### Mitiga Labs empirical backdrop [TENTATIVE — vendor research]

- 50k+ instruction files across 7k+ public repos (Apr–Jun 2026)
- Documented cases: benign testing skill exfiltrating full codebase to attacker repo; session-start hook shipping credentials
- `ANTHROPIC_BASE_URL` override attacks rerouting Claude traffic; 1,230+ hardcoded API keys in agent/MCP configs

### Phase-0 audit (2026-06-20)

| Check | Result |
|-------|--------|
| License / code | **Closed-source SaaS** — no repo to audit |
| Cost | Free tier; account required to submit scans |
| Data handling | Repos scanned at pinned commit — **do not** submit prod credentials or private engagement repos without vendor ToS review |
| Overlap | Competes with SkillSpector + DefenseClaw pre-connect scan + ecc-agentshield — different rule packs; no published pairwise overlap study |
| Verdict | **Reference** — triage unknown public skills before install; not a substitute for local allowlist + runtime guards (AIRGuard, P2 deny-all) |

## Snippets

> Skillgate applies more than 80 detection rules across 6 technique families, including direct execution, prompt manipulation, tool and MCP poisoning, supply chain, obfuscation, and credential exposure.

[Source: mitiga.io press release 2026-06-16, retrieved 2026-06-20]
