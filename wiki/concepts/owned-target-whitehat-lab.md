---
title: Owned-Target Whitehat Lab
type: concept
tags: [lab, ethics, whitehat, authorization, offensive-security, sandbox]
keywords: [owned target, whitehat lab, self-authorization, attack box, lab VLAN, WireGuard, iron-proxy, snapshot rebuild, authorized practice]
related:
  - concepts/system-hardening.md
  - concepts/linux-security.md
  - concepts/agent-vm-sandboxing.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - concepts/network-security.md
  - entities/tools/iron-proxy.md
  - entities/tools/vpn-self-hosted.md
  - concepts/responsible-disclosure.md
  - concepts/llm-pentest-automation.md
  - concepts/bug-bounty.md
  - concepts/pre-release-product-pentest.md
  - concepts/operator-lab-playbook.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/cyberstrike.md
  - concepts/ai-pentest-harness-landscape.md
  - entities/tools/bloodbash.md
  - entities/tools/bbot.md
  - entities/tools/strix.md
  - sources/rizvi-automating-bug-bounty-recon-2026.md
  - entities/tools/strix-omlx.md
  - entities/tools/pentestgpt.md
  - entities/tools/cai-framework.md
  - entities/tools/hexstrike-ai.md
  - sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md
  - entities/tools/damn-vulnerable-drone.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - sources/epic-games-v-araujo-hwid-spoofer-judgment.md
  - concepts/commercial-spyware-stalkerware-defense.md
  - entities/tools/cyberscraper-2077.md
  - entities/tools/rustscan.md
maturity: draft
created: 2026-08-02
updated: 2026-08-15
---

## Relations

- @entities/tools/damn-vulnerable-drone.md — intentional drone/MAVLink lab (MIT)
- @concepts/hardware-bound-identity-anticheat-licensing.md — third-party AC only with written scope; own license/AC is the product-pentest lane
- @sources/epic-games-v-araujo-hwid-spoofer-judgment.md — HWID spoof pled as DMCA circumvention (not lab research)
- @concepts/commercial-spyware-stalkerware-defense.md — spyware class is studied as defense in an authorized lab, never installed
- @sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md — K220 lab notes

- @entities/tools/cai-framework.md
- @entities/tools/pentestgpt.md
- @entities/tools/strix-omlx.md
- @sources/rizvi-automating-bug-bounty-recon-2026.md — anti-noise recon article (2026)
- @entities/tools/strix.md — Strix Apache-2.0 harness (CONDITIONAL-GO Phase-0)
- @concepts/ai-pentest-harness-landscape.md — AI pentest harness landscape; harness runs only against owned lab targets
- @entities/tools/cyberstrike.md — AGPL AI offensive harness — CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02)
- @concepts/system-hardening.md
- @concepts/linux-security.md
- @concepts/agent-vm-sandboxing.md
- @concepts/docker-agent-sandbox-allowlist-proxy.md
- @concepts/network-security.md
- @entities/tools/iron-proxy.md
- @entities/tools/vpn-self-hosted.md
- @concepts/responsible-disclosure.md
- @concepts/llm-pentest-automation.md
- @concepts/bug-bounty.md
- @concepts/pre-release-product-pentest.md
- @concepts/operator-lab-playbook.md
- @concepts/local-abliterated-llm-pentest-stack.md

## Raw Concept

Authorization and isolation floor for offensive practice on **owned** hosts and VMs. Separates legal whitehat lab operations from unauthorized targeting. Feeds product-pentest and bounty practice without requiring third-party victims. Prompted by the need for a durable ethics + topology baseline before agent-assisted or manual offensive work on self-run infrastructure.

## Narrative

An **owned-target whitehat lab** is a deliberately authorized practice environment: you own (or have explicit written permission for) every host, VM, container, and network path under test. It is the legal and operational floor under offensive skill-building, agent-driven recon/exploit loops, and pre-release product security work. Unauthorized targets — random internet hosts, neighbors’ Wi-Fi, production SaaS outside program scope — are out of bounds even when tooling makes them easy to reach.

### 1. Written self-authorization (even on owned hosts)

Owning the hardware or cloud account is not a substitute for a written scope record. Before any offensive action:

- **Write the scope** — assets (IPs, hostnames, VMs, images), time window, allowed techniques, and hard exclusions (e.g. production customer data, shared cloud tenants, ISP CPE you do not control).
- **Self-authorization memo** — date, operator identity, purpose (skill practice / product pre-release / agent eval), and rollback plan. Treat it like an engagement letter to yourself; it clarifies intent if logs or traffic ever need explanation.
- **Re-authorize on change** — new VLAN, new public IP, or shared lab with another person triggers a scope update.

This habit transfers cleanly to client SOWs, bug-bounty program rules, and @concepts/responsible-disclosure.md workflows. [CONFIRMED] (industry standard: authorization before testing, including own infrastructure)

### 2. Separate attack box vs target VMs/servers

Do not run exploit tooling from the same OS instance you are trying to break:

| Role | Purpose | Notes |
|------|---------|--------|
| **Attack box** | Kali/Parrot/custom toolbox, C2, scanners, LLM agents | Disposable tools; assume it will get noisy and dirty |
| **Target VMs / servers** | Vulnerable apps, AD lab, product staging, intentional misconfigs | Snapshot-backed; rebuild often |
| **Operator host** | Daily driver (laptop) | Prefer not as the attack box; if shared, isolate with VM substrate |

Separation limits blast radius when a reverse shell, malware sample, or agent runaway misfires. Pair with @concepts/agent-vm-sandboxing.md for agent workloads and @concepts/linux-security.md / @concepts/system-hardening.md for hardening the attack box and operator host (not the deliberately weak targets).

### 3. Snapshot, rebuild, and logging for learning

Labs exist to **break and restore**, not to keep a permanent compromised estate:

- **Snapshots before risky steps** — hypervisor or cloud AMI/image snapshots so a bad pivot is one click away from clean state.
- **Rebuild cadence** — after major exercises, rebuild targets from golden images so residual persistence does not pollute the next session.
- **Logging for learning** — capture attack-box command history, target auth/app logs, and (where useful) packet or proxy logs. Review what worked, what was noisy, and what a defender would have seen.
- **No production PII** — synthetic data only unless a written data-handling rule says otherwise (same rule as @concepts/pre-release-product-pentest.md staging).

### 4. Network isolation (lab VLAN / WireGuard / iron-proxy egress)

Offensive traffic must not casually egress into production LAN, guest Wi-Fi, or the public internet:

- **Lab VLAN or dedicated virtual network** — targets and attack box share an isolated L2/L3 segment; no default route to corporate or home IoT without explicit bridges. See @concepts/network-security.md.
- **WireGuard (or equivalent self-hosted VPN)** — when lab nodes span hosts or a remote VPS, tunnel lab traffic only; do not full-tunnel everyday browsing through the attack path. Catalog: @entities/tools/vpn-self-hosted.md.
- **Egress allowlist / iron-proxy** — default-deny outbound from agent or untrusted attack containers so a runaway tool cannot hit unauthorized destinations. See @entities/tools/iron-proxy.md and @concepts/docker-agent-sandbox-allowlist-proxy.md.

Isolation is both safety (containment) and ethics (hard technical barrier against accidental out-of-scope scans).

### 5. Concrete topologies (pick one and document it)

```
[ Operator laptop ]
        │ (SSH / WireGuard)
        ▼
[ Attack VM ] ── lab VLAN ── [ Target VM A: Juice Shop / DVWA-class ]
        │                         [ Target VM B: intentional misconfig API ]
        │
        ├── optional [ Local AI host :11434 loopback or lab-only ]
        └── optional [ Bolt / remote scanner VPS ] (owned only; Ed25519; VPN)
```

- **Minimal:** one attack VM + one target VM on a host-only/virt network.
- **Product rehearsal:** attack VM + staging clone of *your* product (synthetic data) — @concepts/pre-release-product-pentest.md.
- **Agentic:** attack VM runs harness (@concepts/ai-pentest-harness-landscape.md); CyberStrike only inside VM (@entities/tools/cyberstrike.md CONDITIONAL-GO); prefer sandboxed harnesses when available (@entities/tools/strix.md CONDITIONAL-GO Phase-0).

### 5b. Golden-image checklist

- [ ] Target golden image: OS + vulnerable app class (OWASP Juice Shop, DVWA, or your sanitized staging) — no production dumps
- [ ] Attack golden image: toolbelt + scoped agent config templates (empty secrets)
- [ ] Snapshot tag before each major exercise; rebuild after messy persistence tests
- [ ] Written self-auth memo lists the image IDs / IPs in scope

Hands-on ordered form (may be local-only): `briefs/2026-08-02_owned-lab-golden-image-recon.md`.

### 5c. Practice the bounty pipeline on owned targets first

Run the same chain you will use on VRPs against **owned** lab apps: gau/wayback (optional) → @entities/tools/katana.md → staged Nuclei → Burp proof → report draft with local Tier-1 LLM. Only after the pipeline is boringly reliable do you point it at a public program (@concepts/bug-bounty.md).

### 6. Feeds product-pentest and bounty practice without unauthorized targets

The lab is the safe gym for skills used elsewhere:

- **Pre-release product pentest** — owned staging and intentional vulns map to the product loop in @concepts/pre-release-product-pentest.md.
- **Bug bounty readiness** — recon, proxy workflows, and report writing practiced on owned apps before public programs (@concepts/bug-bounty.md). Program rules replace self-authorization only when you leave the lab.
- **LLM / agent assist** — Tier-1 plan/report and Tier-2 scoped execution (@concepts/llm-pentest-automation.md) stay pointed at lab IPs and golden images; scope files and egress policy enforce that. Local stacks and operator playbooks (@concepts/local-abliterated-llm-pentest-stack.md, @concepts/operator-lab-playbook.md) sit on top of this floor.

Never use “I’m practicing for bounty” as a reason to scan hosts outside a program or engagement.

### 7. Ethics floor

Non-negotiable constraints for this wiki’s whitehat lab model:

1. **Authorization is mandatory** — owned or written permission; no exceptions for “harmless” scans.
2. **Isolation is mandatory** — network and process boundaries so mistakes fail closed.
3. **Dual-use tools stay in authorized scope** — C2, exploit frameworks, and credential tools are lab/engagement instruments, not toys on the open internet.
4. **Upstream bugs leave the lab via responsible disclosure** — not drive-by public dumps.
5. **Agents inherit the same rules** — automation does not create a new permission class; see lab red-team policy and agent containment wires elsewhere in this workspace.

If a proposed exercise fails any of the above, redesign the lab — do not weaken the floor.
