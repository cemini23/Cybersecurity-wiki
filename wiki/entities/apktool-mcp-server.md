---
title: apktool-mcp-server — Android Reverse Engineering via MCP
type: entity
tags: [tool, mcp, android, reverse-engineering, apktool, claude-code, apache-2]
keywords: [apktool-mcp-server, android reverse engineering, decode apk, smali, mcp server, apktool]
related:
  - concepts/mobile-pentest.md
  - concepts/malware-analysis.md
  - entities/tools/jadx-mcp-server.md
  - "@osint-wiki/entities/tools/apktool-mcp-server.md"
maturity: draft
created: 2026-05-14
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/entities/tools/apktool-mcp-server.md"
---

# apktool-mcp-server — Android Reverse Engineering via MCP

## Relations

- @concepts/mobile-pentest.md — Android APK decode / smali inspection is core to mobile-app pentesting
- @concepts/malware-analysis.md — APK decompilation for Android malware reverse engineering
- @entities/tools/jadx-mcp-server.md — sibling Android-RE MCP server; apktool-mcp-server wraps Apktool (smali/resources), jadx-mcp-server wraps the JADX decompiler (Java source recovery + live debug)
- @osint-wiki/entities/tools/apktool-mcp-server.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/apktool-mcp-server.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Wraps Apktool functionality (decode_apk, get_smali_file, modify_smali_file, build_apk) inside an MCP server for Claude Code-native Android reverse engineering. Apache-2.0 license, v3.0.1, independently audited by MseeP.ai. Adopt tier per K45 v3 multi-wiki tool eval.
