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
phase_0_verdict: "GO 2026-05-16 — MIT verified (LICENSE file is the full MIT text, Copyright 2020 j3ssie), Go dependency surface permissive (no GPL/AGPL in go.mod direct deps), mature (6,314 stars, 8yr-old project, active multi-contributor commits through 2026-05-12). Cloud runaway-compute concern RESOLVED: --auto-destroy, `cloud destroy all --force`, and max_hourly_spend / max_total_spend cost limits are first-class documented features."
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

- `[CONFIRMED]` Cloud resource-cleanup logic — runaway-compute protection exists and is first-class. Resolved by the Phase-0 audit below: `--auto-destroy`, `osmedeus cloud destroy all --force`, and configurable `limits.max_hourly_spend` / `limits.max_total_spend` cost ceilings are documented features. [Source: github.com/j3ssie/osmedeus @ f82afde — docs/cloud/]

## Phase-0 Audit (2026-05-16)

Clone + metadata inspection only (no execution). Repo: `github.com/j3ssie/osmedeus` @ commit `f82afde` (2026-05-12).

**License — verified clean.** `LICENSE` file is the verbatim, complete MIT License text ("Copyright (c) 2020 j3ssie"). MIT matches the eval claim. No per-file SPDX headers observed (MIT projects routinely rely on the root LICENSE — not a blocker); repo-level license is unambiguous.

**Go dependency licenses — clean, no copyleft.** `go.mod` direct-dependency scan: the surface is dominated by permissive licences — Pulumi SDKs (Apache-2.0), AWS SDK v2 / DigitalOcean godo / Linode linodego / Hetzner hcloud-go (Apache-2.0 / MIT), gofiber/Fiber (MIT), Charmbracelet bubbletea/lipgloss (MIT), spf13/cobra (Apache-2.0), uptrace/bun (BSD-3), redis/rueidis (Apache-2.0), `golang.org/x/*` (BSD-3), `github.com/coder/acp-go-sdk` (the ACP subprocess-agent dep — Apache-2.0). **No GPL/AGPL or other strong-copyleft modules found** in direct deps; `go.sum` grep for `gpl/agpl` returned only a false-positive on `goldmark-emoji` (MIT). Clean for internal security use; if Osmedeus output were ever embedded in closed-source consulting deliverables the full transitive `go.sum` should get a proper license-scanner pass, but nothing here raises a Phase-0 flag.

**Maturity — observed vs claimed.** Claimed ~6,300 stars / last commit ~2026-04-04 / ~4 open issues. Observed (GitHub API 2026-05-16): **6,314 stars**, **4 open issues** (5 including PRs), MIT, not archived, created 2018-11-10 (~8-year-old project), **last push 2026-05-11** — more recent than the eval doc's 2026-04-04 (eval was slightly stale; project is actively moving). Commit log shows steady multi-contributor flow through May 2026 (lead `j3ssie`/Jessie Ho plus external contributors — Shai Rod, Georg Heindl, etc.). Established, industry-recognized recon orchestrator; maturity claim holds and is if anything understated on recency.

**Failure-mode probe (cloud resource-cleanup / runaway compute) — CONCERN RESOLVED.** This was the eval's flagged risk and the open `[NEEDS VERIFICATION]` item. The repo ships a dedicated `docs/cloud/` directory documenting teardown and cost control as first-class features:
- `--auto-destroy` flag tears down provisioned infra after a scan completes (documented across AWS / GCP / Hetzner / DigitalOcean / Linode provider docs).
- `osmedeus cloud destroy <infra-id>` and `osmedeus cloud destroy all --force` for manual / emergency cleanup; `osmedeus cloud list` to detect orphaned instances.
- Configurable cost ceilings: `osmedeus cloud config set limits.max_hourly_spend` and `limits.max_total_spend`.
- Provider docs explicitly advise "**Always use `--auto-destroy`** to prevent forgotten instances" and include per-instance cost references and spot-instance guidance.
Runaway-compute protection is present, documented, and recommended by the project itself. The eval's concern was warranted in principle but is addressed by the tool — the operator must opt into the safeguards.

**Verdict: GO.** MIT throughout, permissive Go dependency surface with no copyleft contamination, mature and actively maintained 8-year project, and the one substantive concern (cloud runaway compute) is mitigated by built-in, documented teardown + spend-limit controls. Clean for internal cybersec use. Operational caveat unchanged: distributed cloud scans must run only against authorized targets and should always use `--auto-destroy` plus a `max_total_spend` ceiling.

## Snippets

> "It simplifies intricate security pipelines into declarative, auditable YAML workflows, enabling conditional branching and precise host-level execution ... natively accommodating ACP subprocess agents like Claude Code and Codex." [Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — URL 9]

Repo: https://github.com/j3ssie/osmedeus
