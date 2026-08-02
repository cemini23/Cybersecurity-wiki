---
title: "Buffer Overflow"
type: concept
tags: [exploit-development, buffer-overflow, memory-corruption, offensive-security]
keywords: [buffer overflow, stack overflow, heap overflow, shellcode, EIP, ESP, ASLR, DEP, SEH, Vulnserver]
related:
  - concepts/exploit-development.md
  - concepts/privilege-escalation.md
  - entities/programming-languages/c.md
  - sources/hacking-the-art-of-exploitation-2nd-edition.md
  - sources/buffer-overflow-introduction.md
  - sources/buffer-overflow-guide-1.md
  - sources/buffer-overflow-for-beginners-joas.md
  - sources/introducao-ao-buffer-overflow-1.md
  - sources/elearnsecurity-ecppt-notes-exam.md
  - entities/certifications/ecppt.md
  - entities/tools/deepzero.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-15
updated: 2026-08-02
---

## Relations

- @concepts/exploit-development.md — broader exploit-dev curriculum
- @concepts/privilege-escalation.md — BOF often used for local/remote code exec → priv
- @entities/programming-languages/c.md — unsafe C APIs as root cause class
- @sources/hacking-the-art-of-exploitation-2nd-edition.md — classic deep text
- @sources/buffer-overflow-introduction.md — Joas 66p intro (deep-read 2026-08-02)
- @sources/buffer-overflow-guide-1.md — Joas 32p guide (deep-read 2026-08-02)
- @sources/buffer-overflow-for-beginners-joas.md — 1p cheatsheet + lab links (deep-read 2026-08-02)
- @sources/introducao-ao-buffer-overflow-1.md — Portuguese sibling stub
- @sources/elearnsecurity-ecppt-notes-exam.md — eCPPT notes include BOF lab block
- @entities/certifications/ecppt.md — cert that still drills classic stack BOF
- @entities/tools/deepzero.md — modern Windows kernel pipeline (related memory-corruption research)

## Raw Concept

Memory-corruption vulnerability class and foundational binary-exploitation technique. Expanded 2026-08-02 from Joas deep-read batch (three BOF sources + eCPPT notes BOF section) plus existing stub.

## Narrative

### Definition

A **buffer overflow** occurs when a program writes more data into a fixed-size buffer than it can hold, past the allocated bounds, corrupting adjacent memory. In the classic **stack-based** case, that corruption can overwrite a saved frame pointer and the **return address (EIP/RIP)**, hijacking control flow to attacker-controlled code (**shellcode**) or a ROP chain. Heap overflows corrupt allocator metadata or adjacent objects instead of the return address. [CONFIRMED — Joas intro + guide]

### Why it still matters

Modern OS/compiler mitigations (ASLR, DEP/NX, stack canaries, SafeSEH/SEHOP, CFG, etc.) made naive remote stack BOFs rarer on hardened targets, but:

- Certification labs (eCPPT, OSCP-style, Vulnserver/SLMail-class apps) still teach the classic path
- Embedded/legacy Windows services and poorly hardened internal tools remain in scope on many engagements
- The mental model (registers, stack frames, badchars, egghunters) transfers to modern exploit-dev

### Mental model (x86)

| Piece | Role |
|-------|------|
| Buffer | Fixed stack (or heap) allocation |
| ESP/RSP | Stack pointer |
| EBP/RBP | Frame base |
| EIP/RIP | Next instruction — **overwrite target** in classic stack BOF |
| Shellcode | Position-independent machine code payload (often “get shell”) |
| Badchars | Bytes filtered by the vulnerable path (null, newline, etc.) |

Process layout (simplified): **text** (code) | **data** | **heap** (malloc) | **stack** (LIFO locals + returns). [CONFIRMED — buffer-overflow-introduction.pdf]

### Exploit development steps (operator checklist)

From Joas Guide 1:

1. Identify and analyze the bug (fuzz / crash / source)
2. Control memory (offset to EIP, pattern create/offset)
3. Redirect execution (JMP ESP gadget, SEH chain, etc.)
4. Inject shellcode (watch badchars / nulls)
5. Harden C2 channel as needed (encrypt socket) for post-exploit realism

[CONFIRMED — buffer-overflow-guide-1.pdf p.11]

### Defenses (pair every exploit page)

- **Developer:** avoid unbounded `gets`/`strcpy`/`scanf`; use bounded APIs; safer languages; fuzz + ASAN
- **OS/compiler:** ASLR, DEP/NX, canaries, CFG/CET on modern Windows/Linux
- **Ops:** least privilege service accounts; network isolation of legacy apps; patch/replace EOL network services

### Lab shortlist (authorized only)

VulnHub “Stack Overflows for Beginners”, Vulnserver, SLMail 5.5, PCMan FTP 2.0.7, CyberSecurityUP Buffer-Overflow-Labs — all **owned lab / exam lab** only. [CONFIRMED — beginners cheatsheet]

### Cert mapping

eCPPT and related eLearnSecurity tracks still expect practical stack BOF competence alongside network/AD content (@entities/certifications/ecppt.md, @sources/elearnsecurity-ecppt-notes-exam.md).

## Snippets

```text
Unsafe C APIs to treat as red flags: gets, scanf("%s"), strcpy without bounds
Mitigations to check on target: ASLR, DEP/NX, canaries, SEH protections
```

[Sources: buffer-overflow-introduction.pdf p.11, buffer-overflow-guide-1.pdf p.4–5]
