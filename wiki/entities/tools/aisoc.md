---
title: "AiSOC — self-hosted AI Security Operations Center"
type: entity
tags: [tool, langgraph, soc-orchestrator, investigation-ledger, neo4j, mit, defensive-security]
keywords: [aisoc, beenuar, langgraph soc, investigation ledger, neo4j, 14 log sources, ci-gated eval]
related:
  - "@osint-wiki/entities/tools/aisoc.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - "@osint-wiki/concepts/conductor-orchestrator.md"
  - concepts/defense-in-depth.md
maturity: draft
created: 2026-05-12
updated: 2026-05-16
osint_eval_origin: doc2-url-26 (cross-routed; cybersec defensive-ops primary)
---

## Relations

- `@osint-wiki/entities/tools/aisoc.md` — OSINT cross-route (Cemini orchestrator angle)
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin eval (URL 26)
- `@osint-wiki/concepts/conductor-orchestrator.md` — Cemini orchestrator pattern
- @concepts/defense-in-depth.md — AI SOC orchestration as a defensive automation layer
## Raw Concept

- **Repo**: `github.com/beenuar/AiSOC`
- **License**: MIT
- **Tier**: Steal-from / Adopt-candidate (full deployment) / Reference (architecture)

## Narrative

Self-hosted AI Security Operations Center: ~600-line LangGraph orchestrator with Investigation Ledger in Neo4j, 14 log sources, public CI-gated eval harness, OpenAPI specs + Terraform/Helm packaging. Production-grade DevSecOps reference implementation for blue-team automation.

### Phase-0 audit pending

Resource footprint (16GB? More?), supported SIEM integrations, eval-harness coverage, license compat for any wiki-side reuse. Worth a full deep-eval.
