---
title: "defenseclaw — enterprise AI security governance (Cisco AI Defense)"
type: entity
tags: [tool, ai-security, governance, defensive, agentic-ai, runtime, apache-2.0, adopt]
keywords: [defenseclaw, cisco ai defense, agentic ai security, capability scanning, runtime traffic inspection, mcp scanner, skill-scanner, sidecar, admission-control]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/responsible-disclosure.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - entities/tools/seclaw-eval.md
  - entities/tools/agentredguard.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - "@ccc-wiki/entities/tools/defenseclaw.md"
  - "@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md"
maturity: draft
created: 2026-05-21
updated: 2026-06-04
cross-wiki-source: @osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md
phase_0_verdict: "CONDITIONAL-GO 2026-06-04 — CLI skill/MCP scanners ADOPTED on laptop (CCC trial); full sidecar optional after DEFENSECLAW_LLM_KEY + port 18970 + hooks."
---

# defenseclaw — enterprise AI security governance

## Relations

- @concepts/ai-for-cybersecurity.md — secures agentic AI runtimes in enterprise deployments
- @concepts/llm-adversarial-fuzzing.md — complements FuzzyAI by providing the defensive-detection layer
- @concepts/llm-pentest-automation.md — governance for LLM-driven security tooling
- @concepts/responsible-disclosure.md — audit-trail requirements for authorized testing
- @concepts/agent-runtime-guardrails.md — guardrail taxonomy synthesizing enterprise + OSS patterns
- @concepts/seclaw-agent-security-evaluation.md — benchmark vs runtime gate (SeClaw)
- @entities/tools/nvidia-skillspector.md — skill/MCP supply-chain scanner complementing runtime governance
- @entities/tools/airguard.md — open-source runtime authority guard (MIT)
- @entities/tools/chaincaps.md — MCP composition IFC reference
- @entities/tools/seclaw-eval.md — trajectory benchmark (Reference until code ships)
- @entities/tools/llm-defense-lattice.md — OWASP LLM HTTP BAS lattice (Reference)
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — formal ePCA guardrail research complement
- @ccc-wiki/entities/tools/defenseclaw.md — CCC adoption trial + skill-vetting integration

## Raw Concept

Routed from K42 OSINT-wiki tool eval (2026-05-15). Deepened from `@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md` (2026-06-04). `cisco-ai-defense/defenseclaw` — Apache-2.0, ~712★ (2026-06-04).

## Narrative

Go gateway + Python CLI providing security governance for agentic AI workloads:

- **MCP scanner** — inspect MCP manifests for dangerous capability patterns before connection
- **Skill scanner** — audit SKILL.md for exfiltration, unsafe deserialization, prompt-injection surfaces
- **Admission control** — gate external MCP servers post-scan
- **CodeGuard** — static secrets / unsafe-pattern checks on tool code
- **Observability** — optional OTLP + Splunk Docker bundles

Primary cybersec fit: blue-team governance for pentest agents, SOC copilots, and threat-intel summarizers. Complements @entities/tools/fuzzyai.md (offense-only) and @entities/tools/nvidia-skillspector.md (skill supply-chain preflight).

### Laptop adoption posture (2026-06-04 CCC trial)

| Component | Status |
|-----------|--------|
| `make all` → `~/.local/bin/defenseclaw` | **ADOPTED** |
| `skill-scanner scan` / `mcp-scanner` | **ADOPTED** — Phase-0 skill/MCP pre-screen |
| `defenseclaw agent discover` | **ADOPTED** — inventory claudecode/cursor/codex/geminicli |
| Sidecar on `:18970` | **OPTIONAL** — down until LLM key + hook setup |
| Splunk/OTel Docker bundles | **OPTIONAL** — enterprise observability only |

### Sidecar install path (optional full stack)

1. Clone `cisco-ai-defense/defenseclaw`; `make all` (installs CLI to `~/.local/bin`).
2. Set **`DEFENSECLAW_LLM_KEY`** for LLM-assisted scanner paths (required for full sidecar; unset = doctor partial fail).
3. Start sidecar on **port 18970** (default in docs); wire agent runtime hooks (Codex / Claude Code hook points per `docs/INSTALL.md`).
4. Run **`defenseclaw doctor`** — expect 13 pass / 5 fail until sidecar + key configured (CCC trial baseline).

Import boundary: laptop analyst workflow only until prod MCP allowlist runbook validated. Not a CeminiSuite prod dependency without separate security review.

### MCP scanner runbook (authorized lab / prod allowlist)

1. Export inventory: `defenseclaw agent discover` → list connected agent runtimes.
2. For each MCP server in scope: `mcp-scanner scan <manifest-or-path>` before adding to allowlist.
3. Block or quarantine servers failing: over-broad tool permissions, shell/exec without auth, credential exfil patterns.
4. Re-scan on manifest/version change; pair with @entities/tools/nvidia-skillspector.md for skill files and @concepts/agent-runtime-guardrails.md for runtime authority controls.
5. For prod MCP stacks (conductor/lazy-tool): treat scanner output as **advisory** — human GO required before enabling write tools.

### Splunk / OTel bundles (optional)

Docker-compose observability bundles ship in repo for enterprise SIEM ingestion. Use when OTLP export to Splunk is in scope; skip on laptop-only pentest workflows. See repo `docs/` for bundle layout.

## Phase-0 audit (2026-06-04)

| Check | Result |
|-------|--------|
| License | **Apache-2.0** [CONFIRMED] |
| Maturity | ~712★; active (push 2026-06-03) |
| Failure mode | Sidecar complexity; Cisco Splunk assumptions |
| vs SeClaw | defenseclaw = **runtime gate**; SeClaw = **benchmark** when code ships |

## Snippets

```bash
# CCC trial baseline (2026-06-04)
make all
defenseclaw doctor          # partial until DEFENSECLAW_LLM_KEY + :18970 sidecar
defenseclaw agent discover
skill-scanner scan <path>   # pre-install skill vet
```

## Dead Ends

- **Sidecar without LLM key** — doctor fails; CLI scanners still usable standalone.
- **Replacing SeClaw benchmark** — scanners gate install; they do not score multi-step tool trajectories (see @concepts/seclaw-agent-security-evaluation.md).
