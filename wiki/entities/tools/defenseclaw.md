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
  - entities/tools/clawaudit.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - concepts/local-agent-runtime-audit.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - entities/tools/seclaw-eval.md
  - entities/tools/sevra-bench.md
  - entities/tools/agentredguard.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - "@ccc-wiki/entities/tools/defenseclaw.md"
  - concepts/mcp-security-posture.md
  - "@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md"
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - entities/tools/malskillbench.md
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - entities/tools/ecc.md
  - entities/tools/skillgate.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - concepts/safeclawbench-staged-agent-security.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/self-evolving-agent-security.md
maturity: draft
created: 2026-05-21
updated: 2026-06-24
cross-wiki-source: "@osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md"
phase_0_verdict: "CONDITIONAL-GO 2026-05-31 — CLI scanners + Codex sidecar (observe) ADOPTED on laptop; LLM judge optional via DEFENSECLAW_LLM_KEY; action mode + Splunk optional."
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

### Laptop adoption posture (2026-05-31 sidecar trial)

| Component | Status |
|-----------|--------|
| `make all` → `~/.local/bin/defenseclaw` | **ADOPTED** |
| `skill-scanner scan` / `mcp-scanner` | **ADOPTED** — Phase-0 skill/MCP pre-screen |
| `defenseclaw agent discover` | **ADOPTED** — inventory claudecode/cursor/codex/geminicli |
| Sidecar on `:18970` + Codex hooks | **ADOPTED (observe, on-demand)** — start when using Codex + defenseclaw telemetry; not required for CLI-only scans or Cursor workflow |
| `DEFENSECLAW_LLM_KEY` + LLM judge | **OPTIONAL** — doctor still fails until set; local YARA scanners work without |
| `OPENCLAW_GATEWAY_TOKEN` | **N/A (Codex standalone)** — only for OpenClaw fleet upstream |
| Splunk/OTel Docker bundles | **OPTIONAL** — enterprise observability only |

### Sidecar trial runbook — Codex on macOS (laptop)

Prerequisites: `defenseclaw` + `defenseclaw-gateway` on PATH (`make all` or curl installer with `--connector codex`). Python 3.11+ for MCP scanner.

**1. Gateway + sidecar**

```bash
defenseclaw setup gateway --host 127.0.0.1 --api-port 18970 --non-interactive --no-verify
defenseclaw-gateway start
curl -sf http://127.0.0.1:18970/health | jq .
```

Expect `api.state=running`, `connector.name=codex`, `gateway.state=disabled` (standalone — no OpenClaw fleet).

**2. Wire Codex connector (observe mode — default)**

```bash
defenseclaw setup codex --yes --restart
```

Writes `~/.defenseclaw/hooks/codex-hook.sh`, patches `~/.codex/config.toml` (hash-checked backup). Telemetry: hooks → `/api/v1/codex/hook`; no proxy inserted in LLM path.

**3. Verify**

```bash
defenseclaw doctor          # 2026-05-31 trial: 18 pass / 3 fail / 10 skip
defenseclaw-gateway status  # API + watcher + guardrail RUNNING; Agent Codex RUNNING
defenseclaw skill scan <path-to-skill-dir>
```

Expected doctor failures until optional keys wired:

| Check | Fix |
|-------|-----|
| `DEFENSECLAW_LLM_KEY` | `defenseclaw setup llm --non-interactive` or `defenseclaw keys set DEFENSECLAW_LLM_KEY` — only needed for LLM analyzer / judge |
| `OPENCLAW_GATEWAY_TOKEN` | Ignore on Codex-only laptop; set only when pointing at remote OpenClaw fleet |

**4. Optional — LLM judge + action mode**

```bash
defenseclaw setup llm                    # prompts for provider/model/key → ~/.defenseclaw/.env (0600)
defenseclaw setup codex --mode action --yes --restart   # PreToolUse deny on policy hits
```

Start in **observe**; flip to **action** only after reviewing hook backups and scope.

**5. Optional — Splunk / OTel**

```bash
defenseclaw setup local-observability up    # bundled Prom/Loki/Tempo/Grafana on loopback
defenseclaw setup splunk --logs --accept-splunk-license --non-interactive   # Docker Splunk Free
```

**6. Teardown / stop**

```bash
defenseclaw setup guardrail --disable      # restore direct Codex LLM access; removes hook entries
defenseclaw-gateway stop
```

Sidecar logs: `~/.defenseclaw/gateway.log`. Live tail: `tail -f ~/.defenseclaw/gateway.jsonl | jq`.

### One-shot alternative

```bash
defenseclaw quickstart --connector codex --scanner local --no-judge --yes
```

Equivalent to init → guardrail → gateway start with local pattern scanners (zero API keys). Lists missing keys at end.

### MCP scanner runbook (authorized lab / prod allowlist)

1. Export inventory: `defenseclaw agent discover` → list connected agent runtimes.
2. For each MCP server in scope: `mcp-scanner scan <manifest-or-path>` before adding to allowlist.
3. Block or quarantine servers failing: over-broad tool permissions, shell/exec without auth, credential exfil patterns.
4. Re-scan on manifest/version change; pair with @entities/tools/nvidia-skillspector.md for skill files and @concepts/agent-runtime-guardrails.md for runtime authority controls.
5. For prod MCP stacks (conductor/lazy-tool): treat scanner output as **advisory** — human GO required before enabling write tools.

### Splunk / OTel bundles (optional)

Docker-compose observability bundles ship in repo for enterprise SIEM ingestion. Use when OTLP export to Splunk is in scope; skip on laptop-only pentest workflows. See repo `docs/` for bundle layout.

## Phase-0 audit (2026-05-31)

| Check | Result |
|-------|--------|
| License | **Apache-2.0** [CONFIRMED] |
| Maturity | ~712★; active (push 2026-06-03) |
| Sidecar trial | **PASS** — `:18970` health OK; Codex hooks wired; observe mode |
| Failure mode | Action mode can block tools — test in lab first; OpenShell N/A on macOS |
| vs SeClaw | defenseclaw = **runtime gate**; SeClaw = **benchmark** when code ships |

Import boundary: laptop analyst workflow only until prod MCP allowlist runbook validated. Not a CeminiSuite prod dependency without separate security review.

## Snippets

```bash
# Sidecar trial baseline (2026-05-31 — Codex observe)
defenseclaw setup gateway --host 127.0.0.1 --api-port 18970 --non-interactive --no-verify
defenseclaw-gateway start
defenseclaw setup codex --yes --restart
defenseclaw doctor          # 18 pass / 3 fail (LLM key + OpenClaw token) until optional keys set
curl -sf http://127.0.0.1:18970/health

# CLI-only (no sidecar)
skill-scanner scan <path>
defenseclaw agent discover
defenseclaw-gateway stop
```

## Dead Ends

- **Sidecar without LLM key** — doctor fails on `DEFENSECLAW_LLM_KEY`; local YARA scanners + hook telemetry still work. LLM judge requires `defenseclaw setup llm`.
- **Replacing SeClaw benchmark** — scanners gate install; they do not score multi-step tool trajectories (see @concepts/seclaw-agent-security-evaluation.md).
