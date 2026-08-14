---
title: "TEE trust boundary vs processing-in-memory — the untrusted memory bus problem"
type: concept
tags: [concept, hardware-security, tee, pim, memory-bus, trust-boundary, k280]
keywords: [TEE, SGX, SEV, CCA, processing-in-memory, PIM, memory bus, trust boundary, YAVIN, LightSaber, ASCON, DRAM PUF, TCB]
related:
  - sources/arxiv-2608-13496-yavin-secure-edge-pim-tee.md
  - concepts/chiplet-llm-hardware-security.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/anti-tamper-protection-classes.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc (K280) — REFERENCE, hardware"
---

## Relations

- @sources/arxiv-2608-13496-yavin-secure-edge-pim-tee.md — source paper (HPCA 2027)
- @concepts/chiplet-llm-hardware-security.md — chiplet/EDA hardware security; same trust-boundary framing
- @concepts/hardware-id-masking-opsec.md — DRAM PUF as root of trust connects to hardware-identity
- @concepts/anti-tamper-protection-classes.md — what protection actually covers, per class

## Raw Concept

Where does a TEE's trust boundary actually end? Conventional TEEs (Intel SGX, AMD SEV, ARM CCA) establish trust **inside the processor** — DRAM is encrypted at rest, but any compute that needs plaintext operands must happen in the CPU. **Processing-in-memory (PIM)** breaks that model: if computation moves into DRAM, plaintext operands would have to cross the shared memory bus. YAVIN's answer: extend the TCB so trusted regions in memory can decrypt/process/re-encrypt locally, with the bus treated as untrusted and protected by post-quantum KEM + AEAD.

## Narrative

### The core lesson for hardware evaluation

**A TEE protects exactly what its trust boundary says it protects — nothing more.** SGX protects enclave pages in the EPC from a compromised OS; it does not make the memory bus trustworthy. SEV encrypts VM memory but the CPU is still the only place plaintext exists. When you evaluate a hardware keystore, secure enclave, or TEE-based product (owned-lab / product-pentest context), ask: **where is plaintext materialized, and does the trust boundary cover that location?**

### The PIM gap

- PIM architectures (RowClone, bulk-bitwise logic, horizontal shifting in charge-sharing DRAM) move compute into memory for efficiency — but PIM operates on **plaintext**.
- CPU-side memory encryption (Intel TME / AMD SME, AES-XTS in the memory controller) creates a contradiction: the encryption engine sits in the memory controller, so PIM compute would operate on ciphertext or expose plaintext on the bus.
- FHE avoids the problem but is impractical on edge (orders-of-magnitude overhead).

### YAVIN's pattern (reference)

1. **Distributed TCB** — CPU TEE + physically isolated trusted memory region cooperate; each tenant gets its own span.
2. **Post-quantum key establishment** (LightSaber KEM) over the untrusted bus, with the **memory-side key from a DRAM PUF** (hardware root of trust, unclonable).
3. **In-region AEAD** (ASCON-128) — decrypt/process/re-encrypt entirely inside the trusted region; plaintext never on the bus.
4. **Bit-slice scheduling** — complete plaintext values never simultaneously materialized; only the bit-slices for the current compute stage exist in plaintext. Reduces transient-observation exposure.
5. Measured: >20× vs PIM AES; 34%/9.3% overhead (INT8/INT32) vs plaintext on edge LLMs.

### Cemini application

- **REFERENCE** — no public RTL/code; do not clone.
- When threat-modeling hardware products or TEE-based attestation flows (Play Integrity, App Attest, secure elements), use the **bus-as-untrusted** framing: does the product's trust boundary cover all plaintext materialization points?
- Pairs with `chiplet-llm-hardware-security` — chiplets and PIM both expand the attack surface beyond the CPU die; trust boundaries must be enumerated, not assumed.

## Dead Ends

- No public artifacts at retrieval; architecture is simulation/FPGA-eval-level. No vendor product. [TENTATIVE]

## Snippets

> Existing TEEs establish trust only within the processor, protecting data while it traverses untrusted resources such as the memory bus. [Source: arXiv 2608.13496 abstract]
