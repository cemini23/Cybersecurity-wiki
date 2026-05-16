---
title: Osmedeus — Orchestration Engine for Security Scanning
type: entity
tags: [tool, orchestration, offensive, recon, bug-bounty, automation, go, mit]
keywords: [osmedeus, security orchestration, recon automation, yaml workflow, master-worker, redis, sarif, acp subprocess agent, bug bounty]
related:
  - concepts/red-team-operations.md
  - concepts/bug-bounty.md
  - concepts/web-pentest-methodology.md
  - entities/tools/nmap.md
  - "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
  - "@ccc-wiki/entities/tools/osmedeus-acp-orchestration.md"
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
---

# Osmedeus — Orchestration Engine for Security Scanning

## Relations

- @concepts/red-team-operations.md — Osmedeus orchestrates the recon + scanning phases of an engagement
- @concepts/bug-bounty.md — declarative YAML workflows automate the recon pipeline bug-bounty hunters rebuild per target
- @concepts/web-pentest-methodology.md — scales web-attack-surface enumeration across hosts
- @entities/tools/nmap.md — Osmedeus integrates nmap as one of its 80+ security utility functions
- @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — cross-wiki source: OSINT tool-eval doc that routed this page (Adopt tier, cybersec primary fit)
- @ccc-wiki/entities/tools/osmedeus-acp-orchestration.md — cross-wiki: Osmedeus's ACP subprocess-agent orchestration as a CCC conductor pattern

## Raw Concept

Cross-routed from the OSINT workspace tool-evaluation ingest (2026-05-16). The eval doc rated Osmedeus **Adopt** tier with cybersec as the primary-fit wiki. This page is the cybersec-wiki home; deeper synthesis accumulates on later ingests.

## Narrative

**Osmedeus** is a modern orchestration engine for security scanning — it turns sprawling recon/scan pipelines into declarative, auditable, repeatable workflows.

- **License**: MIT — clean, permissive.
- **Stack**: Go / Docker / Redis / YAML.
- **Maturity** (per eval doc, doc-level): ~6,300 stars, last commit 2026-04-04, 4 open issues — an established, industry-recognized tool.

### Architecture

A **Go-based master-worker pattern backed by Redis queues** lets Osmedeus scale scans across cloud providers (AWS, GCP, DigitalOcean). Pipelines are expressed as **declarative YAML workflows** with conditional branching and host-level execution control — auditable and version-controllable, unlike ad-hoc shell glue. It ships **80+ security utility functions**, including SARIF-output parsing and nmap integration, which removes a lot of the plumbing in red-team / bug-bounty automation.

### Agent / LLM integration

Osmedeus has added AI orchestration: tool-calling agent loops and sub-agent orchestration, with native support for **ACP subprocess agents** (Claude Code, Codex). This bridges traditional programmatic vulnerability discovery and LLM-driven autonomous recon — and is the reason a sibling stub exists in the CCC meta-wiki (`@ccc-wiki/entities/tools/osmedeus-acp-orchestration.md`) documenting the subagent-orchestration pattern.

### Use context

Intended for **authorized engagements** — pentests, bug-bounty programs, adversary emulation. The YAML-workflow model also serves blue teams building reproducible scan baselines (`@concepts/purple-team-operations.md`).

- `[NEEDS VERIFICATION 2026-05-16]` Cloud resource-cleanup logic — confirm runaway-compute protection before running distributed AWS/GCP scans.

## Snippets

> "It simplifies intricate security pipelines into declarative, auditable YAML workflows, enabling conditional branching and precise host-level execution ... natively accommodating ACP subprocess agents like Claude Code and Codex." [Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — URL 9]

Repo: https://github.com/j3ssie/osmedeus
