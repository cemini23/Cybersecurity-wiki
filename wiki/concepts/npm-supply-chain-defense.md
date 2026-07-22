---
title: NPM supply-chain defense — release-age cooldown + version pinning
type: concept
tags: [concept, defensive-ops, supply-chain, npm, bun, package-manager, package-pinning]
keywords: [npm, supply-chain attack, min-release-age, minimum-release-age, bunfig, tanstack, save-exact, version pinning, lockfile, release-age cooldown]
related:
  - concepts/defense-in-depth.md
  - concepts/system-hardening.md
  - "@osint-wiki/concepts/npm-supply-chain-defense.md"
  - "@osint-wiki/sources/npm-supply-chain-defense-prompt-2026-05.md"
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - concepts/llm-code-review-agent-security.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
  - concepts/authority-framing-agentic-cicd.md
  - sources/arxiv-2607-19267-authority-framing-laundered-cicd.md
maturity: draft
created: 2026-05-12
updated: 2026-07-22
---

## Relations

- @sources/arxiv-2607-19267-authority-framing-laundered-cicd.md
- @concepts/authority-framing-agentic-cicd.md
- @concepts/defense-in-depth.md — package-manager hardening as one layer of a layered defensive strategy
- @concepts/system-hardening.md — release-age cooldown + version pinning as attack-surface reduction
- `@osint-wiki/concepts/npm-supply-chain-defense.md` — full concept page (origin, distilled)
- `@osint-wiki/sources/npm-supply-chain-defense-prompt-2026-05.md` — original prompt source
- @entities/tools/nvidia-skillspector.md — agent/MCP skill supply-chain scanning (extends npm-style defense to skills)
- @concepts/coding-agent-supply-chain-install-gap.md — agent auto-install needs pre-install gate beyond cooldown
- @sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md — install-gap empirics (2607.15143)

## Raw Concept

What prompted this page: TanStack package compromise late May 2026 triggered a widely-circulated defensive prompt; cross-routed from OSINT wiki because the pattern is a defensive-ops technique (package-manager hardening) that fits the cybersec wiki's defensive cluster.

## Narrative

A four-step Node.js supply-chain defense pattern:

1. **`~/.npmrc`** — `min-release-age=7`, `minimum-release-age=10080`, `save-exact=true`
2. **`~/.bunfig.toml`** — `[install]` `minimumReleaseAge = 604800`
3. **Pin exact versions** in `package.json` (strip `^` and `~` from all dep blocks)
4. **Commit the lockfile to git** (`bun.lock`, `package-lock.json`, `pnpm-lock.yaml`)

**Why it works** — a 7-day release-age cooldown means newly-published malicious versions don't get installed during their "fresh from compromise" window. Most npm-side compromises get caught and yanked within a few days; the cooldown amortizes that detection lag onto the registry rather than each user's CI.

**Coverage limits** — this defends against immediate-publish exploit chains, not against long-dormant compromise (typosquats prepped months in advance, maintainer-account takeovers where the malicious commit lives in the legitimate repo for weeks before release). See origin concept page for full caveats.

This is a stub. The full distillation, coverage analysis, and Cemini-prod deployment notes live on the OSINT-wiki origin page.
