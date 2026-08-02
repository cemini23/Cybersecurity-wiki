---
title: "Buffer Overflow Introduction"
type: source
tags: [cybersecurity, joas-corpus, buffer-overflow, deep-read]
keywords: [buffer overflow, EIP, ESP, EBP, stack, heap, registers, Nico FTP, Joas]
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

- **Title:** Introduction to Overflow Buffer 1 (English translation of Portuguese original)
- **Author:** Joas Antonio (Joas A Santos)
- **Type:** 66-page PDF intro book/slides
- **Location:** Google Drive file ID `1COIloK_wynny5Jv_zDMY5m-i2ppO3CyV` · local: `research to be indexed/buffer-overflow-introduction.pdf` (1.9 MB, 66 pages)
- **Retrieved:** 2026-05-12; deep-read 2026-08-02 (full PDF obtained; text extract focus pp.1–40 + lab/ref tail)
- **Read status:** deep-read

## Narrative

Longer pedagogical arc than Guide 1:

1. **Definition** — buffer as fixed-capacity temp storage; write past bounds → corruption / control-flow risk
2. **Causes** — unbounded C library functions (`gets`, `scanf`, `strcpy`); unsafe patterns
3. **Defenses (developer)** — avoid unchecked copy APIs; secure-dev testing; language-level bounds; runtime limit checks
4. **Types** — stack vs heap and related classes (deck continues into practice)
5. **CPU registers (x86)** — EAX/EBX/ECX/EDX roles; ESP stack pointer; EBP frame; ESI/EDI; **EIP** next instruction
6. **Process memory map** — text (code), data (init/uninit), **heap** (malloc/free), **stack** (LIFO locals/returns)
7. **Assembly toolchain** — editor, assembler (nasm/masm/tasm), linker, debugger
8. **32 vs 64-bit** — word size; x86-64 compatibility layer notes
9. **Lab pointers** — e.g. Nico FTP SEH BOF with ASLR bypass PoCs (Exploit-DB 45442/45531) near end
10. **References** — OffSec Metasploit Unleashed payloads, Brazilian RE courses, YouTube

Primary value: register + memory-layout grounding before EIP overwrite labs. Pair with Guide 1 for shellcode/SEH link packs and Beginners cheatsheet for Vulnserver shortlist. [CONFIRMED — PDF obtained + deep-read of structure and key pages]

## Snippets

```text
Avoid buffer overflow (developer solutions, p.11):
- Avoid standard library functions that are not bound-checked (gets, scanf, strcpy)
- Regular testing; language-level protection; runtime limit checks on writes
```

[Source: buffer-overflow-introduction.pdf p.11]

```text
x86 general registers (p.16):
EAX accumulator / returns | EBX base data | ECX counter | EDX data extension
ESP stack pointer | EBP base pointer | ESI source | EDI dest | EIP instruction pointer
```

[Source: buffer-overflow-introduction.pdf p.16]

```text
Memory layout (p.21): text | data | heap (malloc) | stack (LIFO locals + return addresses)
```

[Source: buffer-overflow-introduction.pdf p.21]
