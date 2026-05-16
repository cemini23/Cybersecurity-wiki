---
title: "AI-Infra-Guard (Tencent) — AI red-team scanner with mandatory NOTICE attribution (vendor-poison)"
type: entity
category: tool
tags: [entity, tool, ai-red-team, vulnerability-fingerprinting, ai-infrastructure-security, tencent-zhuque-lab, k44, conditional-go-phase-0-2026-05-14, vendor-poison-mandatory-attribution, external-docker-only]
keywords: [ai-infra-guard, tencent, vllm-vuln, ollama-vuln, comfyui-vuln, swagger-docs, mandatory-attribution-section-4d, telemetry-opt-out-default-on, NEVER-vendor-source, external-container-scanner-only]
related:
  - concepts/llm-pentest-automation.md
maturity: validated
created: 2026-05-14
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @image-gen-wiki/entities/custom-nodes/ai-infra-guard.md — cross-route stub (ComfyUI vuln detection)
- @concepts/llm-pentest-automation.md — AI-infra vuln scanning is an applied LLM/AI-pentest-automation tool
## Raw Concept

A Tencent Zhuque Lab AI red-team scanner in Go + Python that fingerprints vulnerabilities across 64 AI components (v4.1.8). Stack: Go core + Python (AIG-PromptSecurity, mcp-scan, agent-scan), Docker Compose. **Apache-2.0 verbatim BUT with Mandatory Attribution NOTICE (§4(d)) that contaminates derivatives — 3,690 stars verified, 44 contributors, 1,458 commits, pushed 2026-05-14 (today)**. K44 verdict needs refinement: SAFE as external Docker scanner; POISON-PILL if vendored.

## Narrative

### Phase-0 audit verdict (2026-05-14): CONDITIONAL-GO (external Docker only)

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | License verbatim Apache-2.0 | **PASS** | Apache-2.0 unmodified text |
| G1 | NOTICE file generic | **FAIL — VENDOR-POISON** | NOTICE adds **Mandatory Attribution Requirement (§4(d))** forcing derivatives to state "Based on Tencent Zhuque Lab AI-Infra-Guard" in product docs / About page / release notes + link the original repo. Apache-2.0 §4(d) makes this legally enforceable on derivative works |
| G2 | Maturity | **PASS** | 3,690★ (vs claimed 3,700, near-exact), 44 contributors, pushed today |
| G3 | Rule freshness | **PASS** | Rule files dated 2026-05; LiteLLM supply-chain CVE shipped 2026-03; active maintenance |
| G4 | Functionality matches K44 claim | **PASS** | AI red-team scanner covering Agent/MCP/Skills/AI-infra/jailbreak |
| G5 | Telemetry phone-home | **PASS — NEUTERED** | `DEEPTEAM_TELEMETRY_OPT_OUT` default `"YES"`; Sentry DSN empty, PostHog host `localhost:0`, New Relic key `dummy_key` — all stubbed |
| G6 | Tencent-server auto-pull | **PASS** | No auto-update mechanism; rules ship in-repo |
| G7 | Docs language | **PASS** | 9 README locales (EN/ZH/JA/ES/DE/FR/KR/PT/RU); internal mcp-scan/agent-scan READMEs Chinese-only |
| G8 | CLA / inbound license | **PASS** | No CLA; Apache-2.0 §5 inbound=outbound |
| G9 | Cemini-stack coverage overlap | **PARTIAL** | Covers ComfyUI (8 subpkgs), LiteLLM, vLLM, Dify, AnythingLLM, Flowise, MCP servers, AI-agent configs. Does NOT cover PostgreSQL / LangGraph / FastAPI / kb-server MCP specifically |

### License verdict: RESTRICTIVE-ATTRIBUTION (vendor-poison)

The NOTICE file enumerates "Mandatory Attribution Requirement (per Apache License 2.0, Section 4(d))" requiring any derivative — open-source or commercial — to:
1. State "Based on Tencent Zhuque Lab AI-Infra-Guard" in product documentation, About page, or release notes
2. Link to the original repo

README §License re-asserts this and prohibits "repackaging this project as an original product without disclosing its origin." Per-file headers in `AIG-PromptSecurity/deepteam/telemetry.py` restate the requirement, escalating contamination risk if even a single file is vendored.

### Cemini IP-sale impact: POISON-PILL if vendored, SAFE as external scanner

**DO NOT VENDOR.** Embedding any AI-Infra-Guard module into the Cemini codebase contaminates the IP package — an acquirer would inherit the "Tencent Zhuque Lab" attribution obligation in their About / docs / UI forever. This is the exact failure mode K44 flagged.

**SAFE as external Docker scanner.** Running AIG via `docker-compose.images.yml` as a black-box CI / security tool whose findings flow into Cemini reports does NOT create a derivative work and incurs no attribution debt on Cemini IP.

### Final verdicts

- **Cybersec-wiki**: **CONDITIONAL-GO** — document as AI red-team landscape entity; recommend external Docker invocation only.
- **Image-gen-wiki**: **CONDITIONAL-GO** (best fit) — 8 ComfyUI rule packs + AI-agent-config detection is genuinely useful for image-gen defensive ops. Same external-container constraint.
- **Cemini IP package**: **DO NOT VENDOR.** External scanner only if used at all.

### Critical caveats

1. **Mandatory attribution = vendor-poison** — any source file copied into Cemini triggers the NOTICE inheritance under Apache-2.0 §4(d). Use only as external Docker container.
2. **No Cemini-stack coverage** — vLLM/Ollama coverage exists but Cemini doesn't use them; PostgreSQL/LangGraph/FastAPI/kb-server are not in AIG's scope.
3. **Cross-route primary fit** — image-gen-wiki is the better primary home (real ComfyUI scanning value); cybersec-wiki keeps a cross-route stub.

## Snippets

> "This comprehensive AI Red Teaming platform identifies and fingerprints vulnerabilities across 64 distinct AI frameworks, including critical infrastructure like vLLM, Ollama, and ComfyUI."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶217 — Phase-0 audit confirms 64-component coverage but flags Mandatory Attribution NOTICE as vendor-poison for the Cemini IP package. External Docker invocation only.]
