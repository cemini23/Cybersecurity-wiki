---
title: "Buffer Overflow"
type: concept
tags: [exploit-development, buffer-overflow, memory-corruption, offensive-security]
keywords: [buffer overflow, stack overflow, heap overflow, shellcode, exploit development, memory corruption]
related:
  - concepts/exploit-development.md
  - concepts/privilege-escalation.md
  - entities/programming-languages/c.md
  - sources/hacking-the-art-of-exploitation-2nd-edition.md
  - sources/buffer-overflow-introduction.md
  - sources/buffer-overflow-guide-1.md
  - sources/buffer-overflow-for-beginners-joas.md
  - sources/introducao-ao-buffer-overflow-1.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

Memory corruption vulnerability class where a program writes beyond the bounds of a stack- or heap-allocated buffer. Foundation of classic binary exploitation: stack-based overflows overwrite return addresses to hijack control flow; heap-based overflows corrupt allocator metadata. Mitigations include ASLR, DEP/NX, stack canaries, and SafeSEH. Essential knowledge for OSCP, OSWE, and eCPTX certifications.

## Relations

- @concepts/exploit-development.md
- @concepts/privilege-escalation.md
- @entities/programming-languages/c.md
- @sources/hacking-the-art-of-exploitation-2nd-edition.md
- @sources/buffer-overflow-introduction.md
- @sources/buffer-overflow-guide-1.md
- @sources/buffer-overflow-for-beginners-joas.md
- @sources/introducao-ao-buffer-overflow-1.md
