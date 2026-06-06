---
title: defending-code-reference-harness — Anthropic Docker vuln-discovery pipeline (Reference)
type: entity
tags: [tool, llm-security, docker, sandbox, asan, exploit-dev, reference, k102]
keywords: [anthropics, defending-code, gvisor, vp-internal, allowlist proxy, c-cpp, vulnerability harness]
related:
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - concepts/agent-vm-sandboxing.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/exploit-development.md
  - concepts/agent-skill-injection.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - entities/tools/cua.md
  - entities/tools/iron-proxy.md
  - "@osint-wiki/entities/tools/defending-code-reference-harness.md"
maturity: draft
created: 2026-06-06
updated: 2026-06-06
phase_0_verdict: "CONDITIONAL-GO 2026-06-06 — laptop Docker/gVisor only; Apache-2.0 LICENSE file; not for cemini-prod trading path."
---

## Relations

- @concepts/docker-agent-sandbox-allowlist-proxy.md — isolation + egress allowlist pattern this repo implements
- @concepts/agent-vm-sandboxing.md — sibling isolation methodology (VM vs Docker agent sandbox)
- @concepts/llm-vulnerability-discovery.md — recon → find → verify → report → patch pipeline
- @concepts/exploit-development.md — ASAN-backed C/C++ memory vuln verification stage
- @concepts/agent-skill-injection.md — untrusted agent skills driving harness need vetting before `/patch` or autonomous pipeline
- @concepts/neuro-symbolic-auditable-reasoning.md — NeuroLog audit trail (compile-free) vs this harness (execute-to-crash)
- @entities/tools/cua.md — VM-tracing sandbox for agent actions (different substrate, same untrusted-code problem)
- @entities/tools/iron-proxy.md — egress allowlist complement for non-Docker workloads
- @osint-wiki/entities/tools/defending-code-reference-harness.md — K102 Phase-0 source audit

## Raw Concept

K102 brief (`briefs/2026-06-06_k102-cybersec-defending-code-harness-from-osint.md`, 2026-06-06). GitHub: [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) — Apache-2.0 LICENSE file (~3.9k★ at Phase-0). Reference only — repo **not maintained**, not accepting contributions.

## Narrative

Anthropic open reference for **autonomous vulnerability discovery + remediation** with Claude: recon → find → ASAN verify → report → patch on C/C++ targets. Ships Claude Code skills (`/quickstart`, `/vuln-scan`, `/triage`, `/patch`) plus `harness/` autonomous pipeline and **`bin/vp-sandboxed`** gVisor wrapper.

**Security architecture [CONFIRMED]** — gold standard for running agent-generated exploit code off the host:

- Target builds run on **`vp-internal`** Docker network
- **Strict allowlist proxy** controls egress from sandbox
- Interactive skills (read/write files only) safe unsandboxed with human approval
- Autonomous pipeline **executes target code** — refuses outside gVisor unless explicitly overridden

**Phase-0 verdict: CONDITIONAL-GO** — steal `harness/prompts/` + network isolation pattern for authorized lab pipelines; requires Docker Desktop (Mac/Linux). **Do not** deploy on `@cemini-prod` trading stack or wire to prod-mcp write tools without operator GO.

**Complements** @concepts/neuro-symbolic-auditable-reasoning.md (NeuroLog): NeuroLog = symbolic audit without execution; this harness = crash-verified memory bugs via ASAN. Different surfaces, stackable in a research lab.

**Managed alternative:** Anthropic [Claude Security](https://claude.com/product/claude-security) hosted product — this repo is the DIY reference.

## Snippets

```bash
# One-time sandbox setup (gVisor)
scripts/setup_sandbox.sh
bin/vp-sandboxed  # invoke autonomous pipeline
```

> "Target image isolated on vp-internal network bound by strict allowlist proxy"
> — [Source: anthropics/defending-code-reference-harness README, retrieved 2026-06-06]

## Dead Ends

- **Prod trading / MCP write path** — frontier-model cost + arbitrary code execution; Cemini boundary = research laptop only.
- **GitHub API license NOASSERTION** — LICENSE file is Apache-2.0; verify file before code import [CONFIRMED 2026-06-06].
- **Works on every codebase OOTB** — README: run `/customize` to port language/detector; reference not product.
