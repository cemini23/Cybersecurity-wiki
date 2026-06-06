---
title: "ironsh/iron-proxy — egress firewall for untrusted workloads"
type: entity
tags: [tool, egress, firewall, zero-trust, container, go, apache-2.0, adopt-eligible]
keywords: [iron-proxy, ironsh, egress firewall, untrusted workloads, policy, sandbox]
related:
  - concepts/zero-trust.md
  - concepts/network-security.md
  - concepts/defense-in-depth.md
  - concepts/container-security.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/super-spr.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - entities/tools/defending-code-reference-harness.md
maturity: draft
created: 2026-05-26
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md"
phase_0_verdict: "Adopt-eligible 2026-05-26 — Apache-2.0 verified; Phase-0 queue if egress-policy hardening is prioritized."
---

# ironsh/iron-proxy — egress firewall for untrusted workloads

## Relations

- @concepts/zero-trust.md — default-deny egress as identity/workload-boundary control
- @concepts/network-security.md — programmatic egress policy enforcement
- @concepts/defense-in-depth.md — contain compromised or untrusted processes at the network layer
- @concepts/container-security.md — sandbox / container egress restriction pattern
- @concepts/agent-vm-sandboxing.md — pairs with agent-VM isolation (Tier 2 pentest agents, LLM tool runners)
- @entities/tools/super-spr.md — sibling zero-trust networking implementation (different layer: VLAN/DNS vs egress firewall)
- @concepts/ai-for-cybersecurity.md — LLM agent workload egress containment
- @concepts/agent-runtime-guardrails.md — network-layer complement to runtime authority guards

## Raw Concept

Routed from K68 OSINT-wiki brief (`briefs/2026-05-26_k68-cybersec-tool-eval-from-osint.md`, 2026-05-26). Go egress firewall for untrusted workloads. Apache-2.0, ~421 stars. **Adopt-eligible** — Phase-0 if egress-policy hardening becomes a wiki priority.

## Narrative

`ironsh/iron-proxy` is an **egress firewall** designed to constrain what untrusted workloads (containers, agent sandboxes, CI jobs, pentest tooling) can reach on the network. Complements in-process scope gates (see @concepts/llm-pentest-automation.md Tier 2 model) with **network-layer default-deny**.

**Cybersec fit**: blue-team hardening for LLM agent runtimes, malware detonation labs, and purple-team exercise infrastructure where blast-radius containment matters as much as detection.

**Adoption gate**: Apache-2.0 clears license. Full Phase-0 still requires lab validation of policy syntax, performance under high-connection workloads, and integration with existing VPN/Zero Trust stacks (@entities/tools/super-spr.md, @entities/tools/vpn-self-hosted.md).

## Dead Ends

- **Replacing engagement scope declarations with firewall rules alone** — egress policy does not substitute for written authorization or in-agent scope YAML; stack both layers.
- **Deploying without egress allowlist review** — default-deny misconfiguration can break legitimate tool chains (DNS, package mirrors, API endpoints pentest agents require).
