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
phase_0_verdict: "GO 2026-05-16 — Apache-2.0 verified (LICENSE file is the full Apache-2.0 text), all declared deps permissive (FastMCP Apache-2.0 / Javalin Apache-2.0 / httpx BSD-3 / SLF4J MIT; no GPL bundling, no .jar files in repo), actively maintained (last commit 2026-04-20, multi-contributor), Mseep.ai badge confirmed real in README."
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

- `[NEEDS VERIFICATION 2026-05-16]` Reliability of `get_smali_of_class` against heavily obfuscated or commercially packed APK structures. (Not resolvable by a Phase-0 metadata audit — requires hands-on testing.)

## Phase-0 Audit (2026-05-16)

Clone + metadata inspection only (no execution). Repo: `github.com/zinja-coder/jadx-mcp-server` @ commit `3d53597` (2026-04-20).

**License — verified clean.** `LICENSE` file is the verbatim, complete Apache-2.0 license text. README license badge and the closing `## 📄 License` section both state Apache-2.0 ("inherits the Apache 2.0 License from the original JADX repository"). No SPDX per-file headers on the Python sources (common for Apache projects relying on a root LICENSE — not a blocker), so the SPDX-header claim is partially soft: license is unambiguous at the repo level.

**Dependency licenses — clean, no copyleft.** Python deps (`pyproject.toml` / `requirements.txt`): `fastmcp` (Apache-2.0), `httpx` (BSD-3-Clause), `requests` (Apache-2.0). README's Dependencies section additionally credits the Java-plugin side: Javalin (Apache-2.0), SLF4J (MIT), org.w3c.dom (W3C license). **No GPL/AGPL in the dependency surface.** Confirmed **no bundled `.jar`/`.class` files** in the repo — JADX itself is not vendored here; this server talks over MCP/HTTP to a *separately distributed* modified `jadx-gui` plugin (`zinja-coder/jadx-ai-mcp`). So the "JADX is Apache-2.0, confirm no GPL bundling" probe passes trivially: nothing is bundled. (Note for completeness: upstream JADX is Apache-2.0.)

**Maturity — observed vs claimed.** Claimed ~472 stars / ~5 open issues. Observed (GitHub API 2026-05-16): **510 stars**, **5 open issues** (6 open including PRs), Apache-2.0, not archived, created 2025-04-08, last push 2026-04-20. Star count drifted upward from the eval doc (healthy). Commit cadence is active and recent; releases tagged (v6.3.0 in late March 2026); **multi-contributor** (lead `zinja-coder`/Jafar Pathan plus external PR contributors merged — Mostafa Nazari, bx33661, ChineseAStar), so not a single-author project.

**Failure-mode probe (MCP server on a security workstation).** (a) LICENSE = Apache-2.0 confirmed. (b) Dependency license check clean — all permissive, no GPL bundling, no vendored binaries. (c) Actively maintained — last commit ~4 weeks before audit, healthy multi-contributor PR flow. (d) **Mseep.ai audit badge claim CONFIRMED** — README has a dedicated `## Audited and Received Assessment Badge` section with the live MseeP.ai Security Assessment Badge image and link (`mseep.ai/app/zinja-coder-jadx-mcp-server`). Badge presence is verified; the *depth/rigour* of the third-party Mseep.ai assessment itself is not independently evaluated here.

**Verdict: GO.** Apache-2.0 throughout, permissive dependency surface, no copyleft contamination, actively maintained, not single-author. Clean for internal cybersec-workstation use. Standard MCP-server caution applies operationally (it can decompile and expose arbitrary APK contents to the LLM — run against authorized samples only), but nothing in the Phase-0 metadata audit blocks adoption.

## Snippets

> "By bridging Python's FastMCP with Java's Javalin web framework, it creates a robust, automated conduit allowing LLMs to interact dynamically with the JADX decompiler ... a Live Debugger Assistant, which grants the LLM real-time access to stack frames, threads, and memory variables during execution." [Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — URL 7]

Repo: https://github.com/zinja-coder/jadx-mcp-server
