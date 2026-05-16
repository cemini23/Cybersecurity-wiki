---
title: jadx-mcp-server — Android Reverse Engineering + Live Debugging via MCP
type: entity
tags: [tool, mcp, android, reverse-engineering, jadx, malware-analysis, claude-code, apache-2]
keywords: [jadx-mcp-server, jadx, android reverse engineering, decompiler, fastmcp, javalin, live debugger, smali, xref, mcp server]
related:
  - concepts/mobile-pentest.md
  - concepts/malware-analysis.md
  - entities/apktool-mcp-server.md
  - "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
---

# jadx-mcp-server — Android Reverse Engineering + Live Debugging via MCP

## Relations

- @concepts/mobile-pentest.md — APK decompilation + manifest parsing is core mobile-app pentest tradecraft
- @concepts/malware-analysis.md — automated decompilation + xref mapping for Android malware reverse engineering
- @entities/apktool-mcp-server.md — sibling Android-RE MCP server; apktool-mcp-server wraps Apktool (smali/resources), jadx-mcp-server wraps the JADX decompiler (Java source recovery + live debug)
- @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — cross-wiki source: the OSINT tool-eval doc that routed this page (Adopt tier, cybersec primary fit)

## Raw Concept

Cross-routed from the OSINT workspace tool-evaluation ingest (2026-05-16). The eval doc rated jadx-mcp-server **Adopt** tier with cybersec as the primary-fit wiki. This page is the cybersec-wiki home; deeper synthesis accumulates on later ingests.

## Narrative

**jadx-mcp-server** is a Model Context Protocol server that exposes the **JADX** Android decompiler to LLM agents (Claude Code, etc.), bridging Python's FastMCP with Java's Javalin web framework. It moves Android reverse engineering from a human-driven, click-through workflow toward an automated, agent-queryable one.

- **License**: Apache-2.0 — permissive, clean for enterprise/security-workstation use.
- **Stack**: Python / Java / FastMCP / Javalin.
- **Maturity** (per eval doc, doc-level): ~472 stars, 5 open issues; security posture noted as carrying an Mseep.ai audit badge.

### Capabilities

Static analysis exposed as MCP tools: `get_class_source` (extract decompiled Java), parse `AndroidManifest.xml`, cross-reference (`Xref`) mapping across obfuscated APKs, `get_method_by_name`, `get_smali_of_class`. Beyond static analysis it adds a **Live Debugger Assistant** — the agent gets real-time access to stack frames, threads, and memory variables during execution.

### Defensive / blue-team relevance

The intended use is **defensive automation**: rapidly surfacing insecure network API calls, hardcoded secrets, and weak crypto inside an APK during a mobile-app security review, and accelerating Android malware triage. It pairs with `@concepts/malware-analysis.md` (automated decompilation for sample triage) and `@concepts/mobile-pentest.md` (manifest/permission/component review). The FastMCP↔Javalin pattern is also a reusable template for exposing other stateful desktop RE tools to an LLM.

- `[NEEDS VERIFICATION 2026-05-16]` Reliability of `get_smali_of_class` against heavily obfuscated or commercially packed APK structures.

## Snippets

> "By bridging Python's FastMCP with Java's Javalin web framework, it creates a robust, automated conduit allowing LLMs to interact dynamically with the JADX decompiler ... a Live Debugger Assistant, which grants the LLM real-time access to stack frames, threads, and memory variables during execution." [Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — URL 7]

Repo: https://github.com/zinja-coder/jadx-mcp-server
