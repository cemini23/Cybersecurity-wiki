---
title: ECC — cross-harness agent operator system + AgentShield (MIT)
type: entity
tags: [tool, ai-security, claude-code, cursor, codex, cross-harness, skill-supply-chain, mcp]
keywords: [ecc, affaan-m, ecc-agentshield, cross-harness, hermes, skill.md, agent configuration audit]
related:
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/tools/skillgate.md
  - "@ccc-wiki/entities/tools/claude-code-ultimate-guide.md"
  - concepts/local-agent-runtime-audit.md

maturity: draft
created: 2026-06-20
updated: 2026-07-18
phase_0_verdict: "CONDITIONAL-GO 2026-06-20 — MIT verified (repo + ecc-agentshield npm); install ecc-agentshield only from official npm/github; full ECC bundle Steal-from patterns; typosquat risk at 218k★ scale"
---

## Relations

- @entities/tools/nvidia-skillspector.md — parallel skill/MCP config scanner (Apache-2.0, local)
- @entities/tools/defenseclaw.md — enterprise MCP/skill governance complement
- @concepts/agent-skill-injection.md — SKILL.md / hooks / MCP as attack surface
- @concepts/mcp-security-posture.md — K100 admission + scan stack
- @ccc-wiki/entities/tools/claude-code-ultimate-guide.md — CCC harness ops cross-route

## Raw Concept

Digest pass 2026-06-20 (R8/R9). [github.com/affaan-m/ecc](https://github.com/affaan-m/ecc) — **Everything Claude Code** v2.0.0 cross-harness operator system (Claude Code, Cursor, Codex, OpenCode, Gemini). Security-relevant sub-package: **`ecc-agentshield`** (npm, MIT) — scans agent configs for vulns, misconfigs, injection risks.

## Narrative

**Local adoption (2026-07-18):** `npm i -g ecc-agentshield@1.4.0` → `~/.local/bin/agentshield` (v1.5.0 runtime); source `raw-sources/repos/agentshield` (~5.2MB). Full ECC bundle still Steal-from / skill_audit required.


ECC is a **harness-native workflow layer**: shared `SKILL.md`, rules, hooks, MCP configs, install manifests — adapted per harness at the edge. v2.0.0 (2026-06) adds Hermes operator story + cross-harness architecture docs. [TENTATIVE] — viral repo (~218k★); project warns install only from verified channels (official GitHub, `ecc-universal` / `ecc-agentshield` npm, GitHub App `ecc-tools`, ecc.tools).

### Cybersecurity relevance

| Component | Role | Wiki fit |
|-----------|------|----------|
| **ecc-agentshield** | Pre-flight audit of Claude Code / agent configs (injection, misconfig) | **CONDITIONAL-GO** — laptop pre-install gate alongside SkillSpector |
| **Shared SKILL.md / hooks / MCP** | Same supply-chain surface as K95/K114 skill injection | Steal portability patterns; **do not** blind-import third-party skills |
| **Cross-harness rules** | AGENTS.md, CLAUDE.md, Cursor rules — SPI persistence channels | Pairs with @concepts/agent-skill-injection.md write-path audit |

### Phase-0 audit (2026-06-20)

| Check | Result |
|-------|--------|
| License | **MIT** — LICENSE file + `gh api` SPDX on repo; `ecc-agentshield` npm MIT |
| Maturity | 218k★, 230+ contributors, active (pushed 2026-06-19) |
| Supply-chain | **High typosquat risk** — README explicitly warns unofficial mirrors may contain malware |
| Failure mode | Over-broad skill/hook/MCP bundles → same blast-radius as vibe-coded over-permissive backends (see 2606.20023 OPUR) |
| Verdict | **CONDITIONAL-GO** for `ecc-agentshield` npm audit on laptop; **Steal-from** cross-harness skill packaging; **NO-GO** full ECC plugin install without skill_audit on every bundled skill |

### vs existing stack

- **SkillSpector** — local, Apache-2.0, semantic agentic-risk + OSV; ECC AgentShield overlaps on config audit — run both on high-risk skill imports [NEEDS VERIFICATION 2026-06-20]
- **DefenseClaw** — enterprise policy + MCP scanner sidecar; ECC is operator/harness distribution, not SIEM-grade governance
- **Skillgate** — SaaS, closed source; ECC AgentShield is local/npm

## Snippets

```bash
# Phase-0 probe only — verify package before install
npm view ecc-agentshield license description
```

[Source: github.com/affaan-m/ecc README — verified install channels warning, retrieved 2026-06-20]
