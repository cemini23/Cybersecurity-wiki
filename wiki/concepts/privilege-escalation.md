---
title: Privilege Escalation
type: concept
tags: [post-exploitation, linux, windows]
keywords: [privilege escalation, linpeas, winpeas, kernel exploit, sudo abuse]
related:
  - concepts/windows-pentest.md
  - concepts/exploit-development.md
  - sources/linux-privilege-escalation-overview.md
  - sources/windows-privilege-escalation-overview.md
  - sources/conceitos-basicos-de-pos-exploracao-1.md
  - sources/introducao-a-pos-exploracao.md
  - entities/people/joas-a-santos.md
  - entities/certifications/oscp.md
maturity: validated
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/windows-pentest.md
- @concepts/exploit-development.md
- @sources/linux-privilege-escalation-overview.md
- @sources/windows-privilege-escalation-overview.md
- @sources/conceitos-basicos-de-pos-exploracao-1.md
- @sources/introducao-a-pos-exploracao.md
- @entities/people/joas-a-santos.md
- @entities/certifications/oscp.md

## Raw Concept

Anchored by Linux + Windows privesc PDFs + two post-exploitation overviews.

## Narrative

Privilege Escalation = elevating from an initial low-privilege foothold to higher privileges (typically root / SYSTEM / Domain Admin). Two flavors: [Source: Linux Privilege Escalation – Overview.pdf]

- **Horizontal** — same privilege level, different user. Cross-account access on the same machine, or one user's data via session hijacking on a web app. Less commonly fatal but expands attacker reach.
- **Vertical** — *(privilege elevation)* gaining the rights of a more privileged account. Root on Linux, SYSTEM or Domain Admin on Windows. Once vertical succeeds, the attacker can credential-dump, drop ransomware, erase logs, plant persistence.

### Linux PrivEsc — technique categories [CONFIRMED]

[Source: Linux Privilege Escalation – Overview.pdf]

1. **Kernel exploits** — vulnerabilities in the running kernel version. Lowest yield in modern hardened distros (KASLR, SMEP, SMAP) but always check version against [exploit-db Linux Kernel](https://www.exploit-db.com/) and curated kernel-exploit repos ([lucyoa](https://github.com/lucyoa/kernel-exploits), [xairy](https://github.com/xairy/linux-kernel-exploitation), [bcoles](https://github.com/bcoles/kernel-exploits)).
2. **Programs running as root** — any process listening / executing as root that handles attacker-controlled input becomes a vertical path.
3. **Installed software** — vulnerable packages, especially with setuid bits. `dpkg -l` / `rpm -qa` to enumerate.
4. **Weak / reused / plaintext passwords** — in `.bash_history`, config files, `.mysql_history`, environment variables, backup files.
5. **Inside services** — services bound only to localhost (Postgres, Redis, internal admin) often run with weaker auth — exploitable after initial foothold.
6. **SUID misconfiguration** — binaries with the setuid bit that drop to a shell or read/write arbitrary files. [GTFOBins](https://gtfobins.github.io/) is the canonical lookup for which standard Unix binaries are exploitable when SUID.
7. **Sudo-rights abuse** — `sudo -l` to enumerate. Any command that can drop a shell (`vim`, `nmap`, `less`, `awk`, `find`) → instant root. `SUDO_KILLER` automates discovery.
8. **World-writable scripts invoked by root** — cron jobs / systemd timers that run a writable script as root. Edit the script → wait for cron.
9. **Bad PATH configuration** — root's PATH containing writable directories before `/usr/bin/` lets an attacker drop a fake `ls` binary that root will execute.
10. **Cron jobs** — `/etc/crontab`, `/etc/cron.d/`, user crontabs. Look for relative paths, world-writable scripts, weak file permissions.
11. **Unmounted filesystems** — `/etc/fstab` may hint at offline volumes that contain credentials or sensitive data.

### Linux PrivEsc — enumeration scripts

Run one or two immediately after initial foothold: [Source: Linux Privilege Escalation – Overview.pdf]

- **[LinPEAS](https://github.com/carlospolop/PEASS-ng)** — de-facto standard, most comprehensive
- **[LinEnum](https://github.com/rebootuser/LinEnum)** — older but widely cited in training material
- **[linux-smart-enumeration (lse)](https://github.com/diego-treitos/linux-smart-enumeration)** — tunable verbosity
- **[linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)** — kernel-exploit recommender
- **[unix-privesc-check](https://pentestmonkey.net/tools/audit/unix-privesc-check)** — pentestmonkey classic
- **[SUDO_KILLER](https://github.com/TH3xACE/SUDO_KILLER)** — focused on sudo abuse
- **[BeRoot](https://github.com/AlessandroZ/BeRoot)** — covers Windows too
- **[Bashark](https://github.com/redcode-labs/Bashark)** — bash-based post-exploitation
- **[private-i](https://github.com/rtcrowley/linux-private-i)** + **[linprivchecker](https://github.com/reider-roque/linpostexp)** — secondary options

### Windows PrivEsc — technique categories

- **Service misconfigurations** — `AlwaysInstallElevated` policy enabled, modifiable service binaries, unquoted service paths, weak service permissions
- **Token impersonation** — `SeImpersonatePrivilege` exploitation via the Potato family (HotPotato → RottenPotato → JuicyPotato → RoguePotato → PrintSpoofer → GodPotato). Standard on web/database service accounts
- **DLL hijacking** — writable directories in DLL search path; drop a malicious DLL with a known-loaded name (see @sources/dll-hijacking-overview.md)
- **Kernel exploits** — fewer modern wins (vulnerable drivers like CVE-2020-1054, CVE-2021-1732); BYOVD (Bring Your Own Vulnerable Driver) attacks against EDR
- **Stored / cached credentials** — DPAPI, LSA secrets, SAM hive, browser stores, CredentialManager, `runas /savecred`
- **Scheduled-task abuse** — modifiable scheduled-task XML, writable task binary
- **AlwaysInstallElevated** — registry-set policy that lets standard users install MSIs with elevated rights

Standard enumeration: **WinPEAS** (counterpart to LinPEAS), **PowerUp** (PowerShell, part of PowerSploit), **Seatbelt** (C#), **PrivescCheck** (PowerShell). See @concepts/windows-pentest.md for the broader AD-attack layer that often follows privesc.

### References — corpus + community canonical

- [g0tmi1k Basic Linux Privesc](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/) — the foundational pentest blog post
- [HackTricks Linux PrivEsc](https://book.hacktricks.xyz/linux-unix/privilege-escalation)
- [PayloadsAllTheThings Linux PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
- [sushant747 OSCP guide — privesc chapter](https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_-_linux.html)
- [GTFOBins](https://gtfobins.github.io/) — SUID + sudo abuse lookup
