---
title: AV / EDR Bypass
type: concept
tags: [evasion, offensive, windows, tradecraft]
keywords: [av bypass, edr bypass, evasion, ntdll unhooking, syscall, shellcode]
related:
  - concepts/red-team-operations.md
  - concepts/exploit-development.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/cobalt-strike.md
  - entities/programming-languages/c.md
  - entities/programming-languages/powershell.md
  - sources/av-and-edr-bypass-techniques-for-new-hackers-update-2022.md
  - sources/av-edr-bypass-red-team-village-pt-br.md
  - sources/offensive-security-evasion-techniques-pt-1.md
  - sources/bypassing-defenses-in-layers.md
  - sources/dll-hijacking-overview.md
  - entities/people/joas-a-santos.md
  - concepts/windows-pentest.md
  - entities/tools/metasploit.md
  - entities/certifications/ecptx.md
  - entities/tools/cua.md
  - concepts/agent-vm-sandboxing.md
  - concepts/endpoint-detection-response.md
  - entities/tools/nidhogg.md
maturity: validated
created: 2026-05-12
updated: 2026-05-24
---

## Relations

- @concepts/red-team-operations.md
- @concepts/exploit-development.md
- @entities/frameworks/mitre-attack.md
- @entities/tools/cobalt-strike.md
- @entities/programming-languages/c.md
- @entities/programming-languages/powershell.md
- @sources/av-and-edr-bypass-techniques-for-new-hackers-update-2022.md
- @sources/av-edr-bypass-red-team-village-pt-br.md
- @sources/offensive-security-evasion-techniques-pt-1.md
- @sources/bypassing-defenses-in-layers.md
- @sources/dll-hijacking-overview.md
- @entities/people/joas-a-santos.md
- @concepts/windows-pentest.md
- @entities/tools/metasploit.md
- @entities/certifications/ecptx.md
- @entities/tools/cua.md
- @concepts/agent-vm-sandboxing.md
- @concepts/endpoint-detection-response.md
- @entities/tools/nidhogg.md — kernel rootkit DKOM reference (GPL-3.0; defensive mapping only)

## Raw Concept

Anchored by *AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf* (full deck deep-read). Additional anchors: AV/EDR Bypass Red Team Village, Offensive Security Evasion Techniques, Bypassing defenses in layers, DLL Hijacking Overview.

## Narrative

**AV (Antivirus)** is a single program for scanning + detecting + removing viruses, originally signature-based. **EDR (Endpoint Detection and Response)** is a superset — antivirus *plus* firewall, whitelisting, monitoring, behavioral detection — operating on a client-server model centralized for an enterprise. EDR is detective + responsive where AV is preventive. [Source: AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf]

Bypassing AV/EDR requires understanding (1) how the solution works, (2) the OS it runs on, (3) how the OS + solution behave together, (4) bypass technique categories, and (5) programming (Python/Go/Ruby/C# at high-level; C/C++ + assembly at low-level) + Windows API + Sysinternals.

### Technique categories [CONFIRMED]

**1. Obfuscation** — distort malware while preserving its function. Simple but surprisingly effective against signature-based detection. Examples: PowerShell case randomization, Invoke-Obfuscation, renaming all strings in Mimikatz to Mimidogz to dodge string signatures.

**2. Encryption (crypters)** — encrypt the payload and ship a decryption stub. Two variants:
- *Scantime crypters* — decrypt, drop to disk, execute. Naive — disk drop is detected.
- *Runtime crypters* — decrypt + execute in memory, never touching disk. Standard for modern implants.

**3. NTDLL Unhooking** — most EDRs hook ntdll.dll (the Windows API gateway) at process start. Unhooking replaces the in-memory hooked ntdll.dll with a fresh copy from disk → the EDR is blind. Re-hooking at end of op covers tracks. [Source: AV and EDR Bypass Techniques.pdf]

**4. Direct + Indirect Syscalls** — high-level Windows APIs (kernel32, user32) call low-level APIs (ntdll), which finally invoke syscalls. EDR-hooked ntdll can be bypassed by:
- *Direct syscall* — emit the `syscall` instruction directly, skipping ntdll entirely. Detection: "Mark of the Syscall" — syscalls from outside known modules look suspicious.
- *Indirect syscall* — emit a `jmp` to a `syscall` instruction inside ntdll, so the syscall *originates* from a known module while still skipping the hook.
- *Vectored syscall* — use Windows VEH (Vectored Exception Handler) to modify RIP, redirecting execution into ntdll's syscall instruction. Bypasses RIP-based instrumentation-callback detection.

**5. Patching the patch** — EDRs that hook by patching specific function prologues (jmp to EDR inspection code) can be defeated by patching over the EDR's jmp with a no-op or by restoring the original prologue. Vendor-specific (see SpecialHoang + MDsec 2019 Cylance post). The disadvantage: every EDR vendor's hooks differ, so this approach needs per-vendor tuning.

**6. Unmanaged code invocation (DInvoke)** — call native Windows API functions dynamically via .NET P/Invoke without exposing them in the binary's Import Address Table. Bypasses static IAT analysis.

**7. UUID-encoded shellcode** — encode shellcode as UUIDs and reassemble at runtime via UuidFromStringA. Static analysis sees benign-looking UUID strings; no `syscall` instruction or recognizable shellcode in the binary opcode.

**8. LSA / LSASS protection bypass** — to read LSASS for credential dumping when LSA Protection (RunAsPPL) is enabled, options are: remove RunAsPPL registry key (worst — reboots lose credentials), disable PPL flags via kernel memory patching (via a signed-but-vulnerable driver like RTCore64.sys; see [PPLKiller](https://github.com/RedCursorSecurityConsulting/PPLKiller)), or read LSASS process memory directly with kernel-level access. [Source: AV and EDR Bypass.pdf]

### Mitigation (defender side)

Effective EDR catches behavioral patterns regardless of the bypass technique used: process tree anomalies, unusual API call sequences, syscall origin tracking, in-memory hash matching of decrypted payloads, ETW (Event Tracing for Windows) for tamper detection. Bypasses age quickly — every technique above has a corresponding defender response. The wiki tracks techniques with `[NEEDS VERIFICATION YYYY-MM-DD]` so we know to retest annually.

## Snippets

**Tooling lists from the corpus** [Source: AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf]

Obfuscators + bypassers:
- [AVIator](https://github.com/Ch0pin/AVIator) — AV bypass framework
- [PyFuscation](https://github.com/CBHue/PyFuscation) — PowerShell obfuscation by variables, functions, parameters
- [Veil-Evasion](https://github.com/Veil-Framework/Veil-Evasion) — payload obfuscation framework
- [Shellter Project](https://www.shellterproject.com/) — PE injector with dynamic encoding
- [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) — PowerShell obfuscation (Daniel Bohannon, 2016)
- [Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)
- [UnmanagedPowerShell](https://github.com/leechristensen/UnmanagedPowerShell)
- [FilelessRemotePE](https://github.com/D1rkMtr/FilelessRemotePE)
- [uuid-loader](https://github.com/pwn1sher/uuid-loader)
- [IORI_Loader](https://github.com/D1rkMtr/IORI_Loader)
- [VEH-PoC (Vectored Syscall)](https://github.com/RedTeamOperations/VEH-PoC/)
- [Awesome Red-Teaming Defense Evasion list](https://github.com/yeyintminthuhtut/Awesome-Red-Teaming#-defense-evasion)

Reading:
- [ired.team / Defense Evasion](https://www.ired.team/offensive-security/defense-evasion/)
- [MITRE ATT&CK Defense Evasion tactic (TA0005)](https://attack.mitre.org/tactics/TA0005/)
- [F-Secure: AV bypass techniques through an EDR lens](https://blog.f-secure.com/av-bypass-techniques-through-an-edr-lens/)
- [itm4n: Bypassing LSA Protection in userland](https://itm4n.github.io/bypassing-lsa-protection-userland/)
- [NCC Group: RIFT - Lazarus shellcode execution method](https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/)
- [DInvoke_rs by NVISO](https://github.com/NVISOsecurity/brown-bags/tree/main/DInvoke%20to%20defeat%20EDRs)
- [Remote Process Write Primitive via APC Routines](https://medium.com/@s12deff/remote-process-write-primitive-via-apc-routines-82c2598c6419) — mid-2026 write-up of an APC-routine-based remote write primitive; a recent data point for ETW/telemetry tamper-detection engineering. Catalogued via the OSINT v3 tool-eval (Reference-only tier).
