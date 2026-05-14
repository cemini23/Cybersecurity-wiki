---
title: "AI-Infra-Guard (Tencent) — AI red-teaming platform fingerprinting vulns across 64 AI frameworks"
type: entity
category: tool
tags: [entity, tool, ai-red-team, vulnerability-fingerprinting, ai-infrastructure-security, enterprise-backed, k44, steal-from-doc-level-pending-phase-0]
keywords: [ai-infra-guard, tencent, vllm-vuln, ollama-vuln, comfyui-vuln, swagger-docs, trpc-go-config, apache-2-with-attribution]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @image-gen-wiki/entities/tools/ai-infra-guard.md — cross-route stub (ComfyUI vuln detection)

## Raw Concept

A Tencent-backed AI red-teaming and fingerprinting platform built in Go that identifies vulnerabilities across **64 AI frameworks** including vLLM, Ollama, ComfyUI. Continuous fingerprint updates (v4.1.8). Stack: Go, Docker Compose, Swagger. **Apache-2.0 (with restrictive attribution clauses), claimed 3,700 stars, last commit 2026-05-14**. K44 verdict: **Steal-from** (attribution clauses complicate white-labeled IP transfer; replicate detection schemas, don't embed the binary).

## Narrative

K44 primary fit: Cybersec-wiki (LLM vuln-discovery directive). Cross-route: Image-gen-wiki (ComfyUI vuln detection layer).

**Steal-from rationale**: Apache-2.0 base license is permissive, but the K44 eval flags **explicit and restrictive attribution clauses** on repackaged deployments. For IP-sale anonymity + clean white-label transfer, Cemini extracts the Swagger API definitions and detection schemas; the compiled Go backend (`trpc_go.yaml`) is not embedded.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/Tencent/AI-Infra-Guard`)
- G2: License audit — read LICENSE + NOTICE files for the exact attribution requirements
- G3: Detection-signatures audit — confirm 64-framework coverage, identify which framework-detection schemas are most relevant to Cemini's stack (vLLM, Ollama directly relevant)
- G4: Exposed-config-file detection (K44 NEEDS VERIFICATION) — these signatures fortify /opt/cemini's own config-file exposure surface

**Cross-route to image-gen**: ComfyUI is the dominant local image-gen runtime. AI-Infra-Guard's ComfyUI vuln signatures port directly into image-gen-wiki's defensive operations layer.

## Snippets

> "This comprehensive AI Red Teaming platform identifies and fingerprints vulnerabilities across 64 distinct AI frameworks, including critical infrastructure like vLLM, Ollama, and ComfyUI."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶217]
