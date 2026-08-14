---
title: "YAVIN — unified TEE + processing-in-memory secure edge architecture (arXiv 2608.13496)"
type: source
tags: [source, arxiv, hardware-security, tee, pim, post-quantum, k280]
keywords: [2608.13496, YAVIN, processing-in-memory, PIM, TEE, trusted computing base, LightSaber, ASCON, DRAM PUF, memory bus, HPCA 2027]
related:
  - concepts/pim-tee-untrusted-memory-bus.md
  - concepts/chiplet-llm-hardware-security.md
  - concepts/hardware-id-masking-opsec.md
maturity: draft
read_status: read
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "REFERENCE 2026-08-14 — HPCA-2027 academic hardware architecture; no public RTL/code at retrieval (gh search empty). Threat-model + architecture steal only. K280 containment/hardware wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc (K280) — REFERENCE, hardware"
---

**Briefs:** `briefs/2026-08-14_k280-yavin-secure-edge-pim.md`

## Relations

- @concepts/pim-tee-untrusted-memory-bus.md — the synthesized concept
- @concepts/chiplet-llm-hardware-security.md — sibling hardware-security concept (chiplet/EDA LLM)
- @concepts/hardware-id-masking-opsec.md — DRAM PUF root of trust touches hardware-identity considerations

## Raw Concept

| Field | Value |
|-------|-------|
| Title | YAVIN: A Unified Architecture for Secure Edge Processing in Memory |
| Authors | Shouzhi Fang, William C. Tegge, Md Omar Faruque, Peipei Zhou, Endadul Hoque, Alex K. Jones (Syracuse + Brown) |
| arXiv | 2608.13496 (cs.AR, v1 13 Aug 2026) — appears in 2027 IEEE HPCA proceedings |
| Code | None public at retrieval (gh search empty) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.13496-yavin-a-unified-architecture-for-secure-edge-pro.pdf` |
| Retrieved | 2026-08-14 |
| Read status | read (13 pp, full text extracted) |

## Narrative

YAVIN is a **unified trusted computing base (TCB)** that extends a conventional processor-centric TEE (SGX/SEV/CCA-style protected memory regions) to also cover **processing-in-memory (PIM) execution**, while treating the **memory bus as untrusted**.

**The problem it solves.** Existing TEEs establish trust only inside the processor: data is encrypted at rest in DRAM but decrypted inside the CPU — trusted computation cannot run *inside memory*. At the other extreme, FHE is impractical for edge. PIM moves compute closer to data but assumes plaintext operands, which would expose secrets on the shared bus.

**YAVIN's design:**
- **Cooperative CPU + PIM TEE** — each tenant's TEE spans processor and a physically isolated trusted memory region; data is decrypted, processed, and re-encrypted entirely within the TCB, never crossing the bus as plaintext.
- **LightSaber post-quantum KEM** — first PIM implementation; CPU + memory generate independent key pairs to establish a shared secret over the untrusted bus. Memory-side key pair derived from a **DRAM physically unclonable function (PUF)** as hardware root of trust.
- **ASCON-128 AEAD** — first in-DRAM authenticated encryption framework; lightweight, PIM-friendly, provides authentication tags directly within charge-sharing DRAM.
- **Tensor/bit-level scheduling** — reorganizes computation to satisfy AEAD ordering constraints while limiting plaintext exposure to only the bit-slices currently in use (complete plaintext values never simultaneously materialized).
- **Results** — >20× speedup vs latest PIM AES; 34% (INT8) / 9.3% (INT32) overhead vs plaintext execution for edge-class quantized LLMs.

**Cemini relevance.** Pure hardware-academic — **REFERENCE**, no code, no clone. The **threat-model framing** transfers to any hardware evaluation: a TEE's trust boundary is exactly what it says it is — SGX/SEV do **not** cover the memory bus or PIM unless explicitly designed to. For hardware-keystore / owned-lab hardware work, YAVIN's bus-as-untrusted + in-region re-encryption model is the reference mental model.

## Snippets

> YAVIN enables data to be decrypted, processed, and re-encrypted by either processor or PIM execution while remaining within the trusted execution environment, without exposing plaintext on the shared memory bus. [Source: arXiv 2608.13496 abstract]

> The memory-side key pair is derived from a DRAM physically unclonable function (PUF), providing a hardware root of trust. [Source: arXiv 2608.13496 §I]
