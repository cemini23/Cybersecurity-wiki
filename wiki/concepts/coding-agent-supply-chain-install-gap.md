---
title: Coding-agent supply-chain install gap
type: concept
tags: [concept, supply-chain, coding-agent, llm, install-gap]
keywords: [2607.15143, pre-install gate, typosquat, separator confusion, registry redirect, harness]
related:
  - entities/tools/background-agents.md
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - concepts/inbound-security-wave-2026-10-07.md
  - sources/wublock-2026-10-06-memtensor-agent-memory-supply-chain.md
  - sources/arxiv-2610-02861-kubernetes-agent-containment.md
  - concepts/agent-memory-supply-chain-compromise.md
  - concepts/bedrock-addon-distribution-integrity.md
  - concepts/llm-generated-dependency-breaking-tests.md
  - concepts/nl-security-rules-vs-builtin-deny.md
  - concepts/llm-codegen-prompt-security-redistribution.md
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
  - concepts/cashews-llm-malicious-package-detection.md
maturity: draft
created: 2026-07-17
updated: 2026-10-09
---

## Relations

- @entities/tools/background-agents.md — K408-K417 ingest / 2026-10-09
- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md — K408-K417 ingest / 2026-10-09
- @concepts/inbound-security-wave-2026-10-07.md — inbound brief wave 2026-10-07
- @sources/wublock-2026-10-06-memtensor-agent-memory-supply-chain.md — inbound brief wave 2026-10-07
- @sources/arxiv-2610-02861-kubernetes-agent-containment.md — inbound brief wave 2026-10-07
- @concepts/agent-memory-supply-chain-compromise.md — K283-b the memory layer is a supply-chain target
- @concepts/bedrock-addon-distribution-integrity.md — Basgiath: Bedrock add-on install-time trust over third-party code
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
