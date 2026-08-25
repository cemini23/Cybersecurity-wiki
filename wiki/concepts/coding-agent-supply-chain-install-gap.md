---
title: Coding-agent supply-chain install gap
type: concept
tags: [concept, supply-chain, coding-agent, llm, install-gap]
keywords: [2607.15143, pre-install gate, typosquat, separator confusion, registry redirect, harness]
related:
  - concepts/llm-generated-dependency-breaking-tests.md
  - concepts/nl-security-rules-vs-builtin-deny.md
  - sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
  - concepts/npm-supply-chain-defense.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - "@ccc-wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md"
maturity: draft
created: 2026-07-17
updated: 2026-07-18
---

## Relations

- @sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md — primary paper
- @ccc-wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md — CCC K179 ADOPT checklist
- @concepts/npm-supply-chain-defense.md — release-age cooldown for Node; orthogonal to agent auto-install
- @concepts/cage-1-enterprise-agent-governance-eval.md — package install = Prebind-class bind

## Raw Concept

What fails when coding agents set up projects by reading docs and running package managers without verifying name, source, or version?

## Narrative

### Attack surface

Documentation (README, requirements, Makefile) becomes a **code-execution vector**: edit docs → agent installs attacker registry / vulnerable pin / separator-confused name.

### Defender stack (steal)

1. Treat `pip`/`npm`/`cargo`/`uv` as **Prebind** actions (K151)
2. Deterministic gate: allowlisted names, pinned versions, allowlisted registry hosts — before any install script runs
3. Never `--yolo` / auto-approve package managers on untrusted repos
4. Measure security on **harness×model** pairs (Cursor auto-exec ≠ Claude Code approval)
5. Keep classical npm cooldown (@concepts/npm-supply-chain-defense.md) for human/CI installs — agents still need the gate

### Vs skill injection

Skill/MCP admission (@concepts/skillsec-lifecycle-agent-skill-security.md) is a sibling: both are supply-chain admission problems. Install-gap is **package-manager bind**; SkillSec is **skill artifact lifecycle**.

## Snippets

See source page.
