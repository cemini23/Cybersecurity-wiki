---
title: Docker agent sandbox with allowlist egress proxy
type: concept
tags: [concept, sandbox, docker, gvisor, agent-security, egress-control, vuln-discovery]
keywords: [vp-internal, allowlist proxy, gvisor, agent sandbox, untrusted code execution, defending-code]
related:
  - entities/tools/defending-code-reference-harness.md
  - entities/tools/iron-proxy.md
  - entities/tools/cua.md
  - concepts/agent-vm-sandboxing.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/agent-runtime-guardrails.md
  - concepts/exploit-development.md
  - concepts/agent-skill-injection.md
maturity: draft
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @entities/tools/defending-code-reference-harness.md — reference implementation (Anthropic, Apache-2.0)
- @entities/tools/iron-proxy.md — host-level egress firewall for non-Docker agent workloads
- @entities/tools/cua.md — VM-substrate alternative (Apple Virtualization.Framework + tracing)
- @concepts/agent-vm-sandboxing.md — disposable substrate + tracing methodology (VM variant)
- @concepts/llm-vulnerability-discovery.md — pipeline stage that needs crash-verified execution
- @concepts/agent-runtime-guardrails.md — runtime authority complements network isolation
- @concepts/exploit-development.md — ASAN crash triage inside sandbox
- @concepts/agent-skill-injection.md — poisoned skills can steer agent to disable sandbox overrides

## Raw Concept

K102 brief (2026-06-06): distill the **vp-internal + allowlist proxy** pattern from Anthropic's defending-code reference harness as a reusable control for any agent that executes untrusted or model-generated code.

## Narrative

When an LLM agent runs exploit PoCs, fuzz harnesses, or `/patch` validation commands, **substrate isolation alone is insufficient** if the sandbox has unrestricted egress. The defending-code pattern combines:

```
Agent orchestrator (host)
    → gVisor/Docker sandbox (target build + ASAN)
        → vp-internal network (no direct internet)
            → allowlist proxy (domain/port constrained egress only)
```

### Control properties

| Property | Why it matters |
|----------|----------------|
| **Internal-only network** | Target malware / RCE PoC cannot reach operator LAN or cloud metadata |
| **Allowlist egress** | Agent can fetch pinned deps or report URLs, not arbitrary C2 |
| **Human gate on interactive skills** | Read/write-only Claude Code skills stay outside sandbox; execution skills require `vp-sandboxed` |
| **Explicit override refusal** | Pipeline refuses unsandboxed autonomous run unless operator overrides (documented foot-gun) |

### When to use vs @concepts/agent-vm-sandboxing.md

- **Docker + gVisor** — CI-friendly, Linux/macOS via Docker Desktop; best for compile-and-crash C/C++ pipelines (@entities/tools/defending-code-reference-harness.md).
- **VM + tracing (cua/Lume)** — GUI/automation agents, macOS-native, full desktop replay traces.

Both address the same policy: **never let agent-selected code run on the host with host credentials.**

### Pentest / lab checklist [TENTATIVE]

1. Separate sandbox network from prod VLAN (no route to cemini-prod).
2. Default-deny egress; allowlist only build mirrors + artifact upload endpoints.
3. Vett agent skills/MCP that can invoke `bin/vp-sandboxed` or disable gVisor checks (@concepts/agent-skill-injection.md).
4. Pair with @entities/tools/iron-proxy.md if any orchestrator step runs outside Docker.

## Snippets

Pattern name from Anthropic reference: **`vp-internal`** network + **strict allowlist proxy** — [Source: defending-code-reference-harness README, retrieved 2026-06-06]

## Dead Ends

- **Allowlist proxy without skill vetting** — agent can still exfil via allowed domains if policy is too broad.
- **gVisor on Apple Silicon** — setup path is Docker Desktop–dependent; verify before engagement lab build [NEEDS VERIFICATION 2026-06-06].
