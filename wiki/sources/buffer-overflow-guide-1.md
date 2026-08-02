---
title: "Buffer Overflow Guide 1"
type: source
tags: [cybersecurity, joas-corpus, buffer-overflow, deep-read]
keywords: [buffer overflow, shellcode, stack overflow, heap, SEH, ASLR, DEP, Joas]
related:
  - concepts/exploit-development.md
  - entities/people/joas-a-santos.md
  - concepts/buffer-overflow.md
maturity: draft
created: 2026-05-12
updated: 2026-08-02
read_status: deep-read
---

## Relations

- @concepts/exploit-development.md
- @entities/people/joas-a-santos.md
- @concepts/buffer-overflow.md

## Raw Concept

- **Title:** Buffer Overflow Guide 1
- **Author:** Joas Antonio (Joas A Santos)
- **Type:** 32-page PDF slide/guide deck
- **Location:** Google Drive file ID `1h9U8cx8ms39_5LF9shbh1heRcIpNU08L` · local: `research to be indexed/buffer-overflow-guide-1.pdf` (660 KB, 32 pages)
- **Retrieved:** 2026-05-12; deep-read 2026-08-02
- **Read status:** deep-read

## Narrative

Structured intro from exploit vocabulary → mitigations → shellcode → RE links → curated walkthroughs.

| Section (approx.) | Content |
|-------------------|---------|
| p.2–3 | What is an exploit; what is shellcode (opcodes, goal = shell) |
| p.4 | Prereqs: C, Python, x86/x64 asm, memory/registers, DEP/NX/ASLR, reverse eng, fuzzing |
| p.5–6 | Stack-based BOF: overflow to overwrite EIP; classic remote code-exec path; notes modern mitigations reduced prevalence |
| p.7 | Heap corruption (dynamic allocator, insufficient space) |
| p.8 | Integer overflow as path to control-data overwrite |
| p.9 | Race conditions (file TOCTOU; non-reentrant signal handlers) |
| p.10 | Socket client/server programming as exploit plumbing |
| p.11 | Exploit steps: identify bug → control memory → redirect flow → inject shellcode → encrypt C2 socket |
| p.13–15 | Shellcode types (bind, reuse, execve, setuid, chroot, Windows); problems: addressing, null bytes, syscalls |
| p.17+ | Reverse-engineering link packs |
| p.21+ | Buffer Overflow 2–5 + SEH + shellcode encoder resource lists (Corelan, FuzzySecurity, Sec4US, SLAE) |

Educational link-heavy deck; not a full Corelan-class walkthrough itself. Good map of the curriculum surface for eCPPT/OSCP-style stack BOF labs. [CONFIRMED — full 32-page deep-read]

## Snippets

```text
Basic step-by-step development of an exploit (p.11):
1. Identify and analyze application bugs
2. Write code to manipulate and control the target's memory
3. Redirect the execution flow
4. Inject the Shellcode
5. Encrypt your socket communication
```

[Source: buffer-overflow-guide-1.pdf p.11]

```text
Prereqs (p.4): C, Python, Assembly x86/x64, memory addressing, BOF, reverse engineering,
registers, DEP/NX/ASLR, fuzzing concepts
```

[Source: buffer-overflow-guide-1.pdf p.4]
