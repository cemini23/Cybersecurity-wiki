#!/usr/bin/env python3
"""Fill out pages for the inbound briefs of 2026-10-05..07. No attack payloads.

Sources: briefs/2026-10-05_agent-safety-eval-from-osint.md,
         briefs/2026-10-05_k421-k423-agent-security-and-benchmark-validity.md,
         briefs/2026-10-06_k283-cyber-agent-verification.md,
         briefs/2026-10-07_babelfake-from-image-gen.md
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
DATE = "2026-10-07"


def w(rel, body):
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump(t):
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", t, count=1, flags=re.M)


def add_related(rel, ref, note):
    assert ref.endswith(".md"), ref
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
    p.write_text(bump(t), encoding="utf-8")
    print("patched", rel, "→", ref)


def source(slug, title, ident, kind, location, narrative, related, read="read (routed brief)"):
    assert not slug.endswith(".md")
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title}"
type: source
tags: [source, routed, agent-security]
keywords: [{ident}]
related:
{rels}
maturity: draft
read_status: {read}
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

{inl}

## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| Identifier | {ident} |
| Type | {kind} |
| Location | {location} |
| Retrieved | {DATE} |
| Read status | {read} |

## Narrative

{narrative}

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route ({DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept(slug, title, kid, ident, narrative, related, wire):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, agent-security, {kid.lower()}]
keywords: [{ident}, {kid}]
related:
{rels}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{inl}

## Raw Concept

Question: **{title}** — operator steal from the inbound brief ({ident})?

## Narrative

{narrative}

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route ({DATE})]
"""
    w(f"concepts/{slug}.md", body)


def main() -> int:
    # ---------- 1. K421 Kubernetes agent containment ----------------------
    source("arxiv-2610-02861-kubernetes-agent-containment",
        "Containment architecture for LLM agents operating Kubernetes",
        "arXiv 2610.02861", "arXiv paper (routed by CCC as K421)",
        "not held locally — routed brief only",
        "**K421 — the model is not a security boundary.** Alignment, system prompts, and input "
        "classifiers **lower the probability** of misbehaviour but guarantee nothing, and their failure "
        "modes are adversarially discoverable. An agent with cluster credentials must therefore be "
        "secured like a multi-tenant workload: **assume it is fully compromised and constrain what it "
        "can reach, do, and exfiltrate.**\n\n"
        "**What breaks.** Agents collapse the **data/control separation** cloud-native security rests on. "
        "Content the agent merely *reads* — a log line written by an attacker-controlled workload, an "
        "annotation, a ticket field, a **third-party MCP tool description** — becomes a command it runs "
        "with its own credentials. That is the confused deputy returning when the deputy is an LLM.\n\n"
        "**The portable rule:** break the combination of **untrusted input + sensitive access + external "
        "egress**. Any one alone is survivable; the three together are the lethal trifecta.\n\n"
        "**Seven layers, all Kubernetes-native or widely adopted:** identity (ServiceAccounts, "
        "audience-bound projected tokens, workload-identity federation); authorization (RBAC plus "
        "**ValidatingAdmissionPolicy** in CEL for fine-grained object validation); sandboxing (gVisor / "
        "Kata via the SIG Apps Agent Sandbox project); **FQDN-aware** egress (Cilium or managed "
        "equivalents); a **tool/MCP gateway applying policy-as-code over tool arguments**; runtime eBPF "
        "(Tetragon, Falco); and API-server audit logging.\n\n"
        "**Honest limits, stated by the author:** the paper reports a threat–control coverage matrix and "
        "four attack walkthroughs but **no measured attack-success or overhead figures**, and names the "
        "measurements needed to validate it. Treat it as a **design reference, not evidence.** Same "
        "paper family as CCC's `@ccc-wiki/concepts/model-is-not-a-security-boundary.md`. **No cluster "
        "attack walkthroughs in wiki.**",
        ["concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "concepts/agentic-containment-principles.md",
         "concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/coding-agent-supply-chain-install-gap.md"],
        read="skimmed (via routed brief)")
    concept("model-is-not-a-security-boundary-kubernetes-agents",
        "The model is not a security boundary (Kubernetes agents)", "K421", "arXiv 2610.02861",
        "Start from one sentence: **prompts and classifiers lower the probability of misbehaviour and "
        "guarantee nothing**, and their failure modes are discoverable by an adversary. So an agent that "
        "can act on infrastructure gets secured the way any multi-tenant workload is — **assume "
        "compromise and bound reach, action, and egress.**\n\n"
        "The specific failure to design against is the collapse of **data/control separation**: anything "
        "the agent *reads* (a log line, an annotation, a ticket field, **a third-party MCP tool "
        "description**) can become an instruction it executes with its own credentials.\n\n"
        "The most portable rule is to **never combine untrusted input + sensitive access + external "
        "egress** — the lethal trifecta. In Kubernetes the controls are ordinary platform controls: "
        "audience-bound ServiceAccount tokens, CEL admission policy for object-level validation, "
        "sandboxed runtimes, **FQDN-aware egress**, a tool gateway that applies policy to tool "
        "**arguments**, eBPF runtime enforcement, and audit logs. Enforcement lives **outside** the model. "
        "Same statement as the federation invariant \"gate the tool step; model self-arbitration is not a "
        "boundary\", applied to a cluster.",
        ["sources/arxiv-2610-02861-kubernetes-agent-containment.md",
         "concepts/agentic-containment-principles.md",
         "concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/coding-agent-supply-chain-install-gap.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K421)")

    # ---------- 2. Agent-memory supply chain ------------------------------
    source("wublock-2026-10-06-memtensor-agent-memory-supply-chain",
        "MemTensor / MemoryOS agent-memory supply-chain compromise",
        "WuBlock / SlowMist report 2026-10-06", "newsletter report (routed by OSINT K283)",
        "not held locally — routed brief only",
        "**The agent's own memory layer was the payload.** `MemoryOS` **2.0.34** on **PyPI**, and the npm "
        "plugin `memtensor/memos-cloud-openclaw-plugin` (versions 0.1.21, 0.1.23, 0.1.25) used with the "
        "OpenClaw runtime, shipped a **cross-platform Go binary that executed on load/import**. The npm "
        "plugin may also **leak prompt content**.\n\n"
        "**Why this is a different class from a poisoned tool.** The wiki already tracks the "
        "**setup-instruction supply chain** — docs that become install-time code. This extends it to the "
        "**memory package**: compromising it does not leak one tool call, it leaks the agent's **entire "
        "context**, because that is what a memory layer holds. Install-time execution plus full-context "
        "access is the worst combination available in an agent stack.\n\n"
        "**Mitigation as reported (SlowMist):** uninstall or downgrade, kill running processes, review "
        "network activity, and **rotate exposed credentials**. **No payload, no binary, no PoC in wiki.**",
        ["concepts/agent-memory-supply-chain-compromise.md",
         "concepts/coding-agent-supply-chain-install-gap.md",
         "concepts/agent-skill-injection.md"],
        read="read (routed brief)")
    concept("agent-memory-supply-chain-compromise",
        "The agent memory layer is a supply-chain target", "K283-b", "WuBlock/SlowMist 2026-10-06",
        "A poisoned **tool** leaks what that tool can reach. A poisoned **memory package** leaks the "
        "agent's **entire context** — that is what a memory layer is for. Add install-time execution (the "
        "MemoryOS PyPI/npm case shipped a Go binary that ran on import) and you have the worst "
        "combination in an agent stack: **code that runs on install, holding the full context.**\n\n"
        "Operator rules: treat the memory package as **privileged**, not as a library; pin versions and "
        "review diffs; and know that on compromise the response is **uninstall/downgrade, kill processes, "
        "review egress, rotate exposed credentials** — rotating credentials is the step people skip, and "
        "it is the one that matters because the context has already left. This is the memory-layer "
        "instance of the install-gap pattern.",
        ["sources/wublock-2026-10-06-memtensor-agent-memory-supply-chain.md",
         "concepts/coding-agent-supply-chain-install-gap.md",
         "concepts/agent-skill-injection.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K283-b)")

    # ---------- 3. EvoRiskBench -------------------------------------------
    source("arxiv-2610-03153-evoriskbench-runtime",
        "EvoRiskBench: runtime risk across model x harness configurations",
        "arXiv 2610.03153", "arXiv paper (routed by OSINT K282)",
        "not held locally — routed brief only",
        "**The number the federation did not have.** Nine model x harness configurations, indirect "
        "prompt injection arriving through **MCP tools, skills, and subagents** — the exact surfaces this "
        "federation ships. Aggregate attack success rate **37.46%**; worst configuration **68.44%** "
        "(DeepSeek-V4-Pro-0813 x Codex).\n\n"
        "**The finding that matters for how we measure:** **model spread (54.37 pp) is far larger than "
        "harness spread (5.41 pp)**. So the harness is *not* where most of the variance lives — but 5 pp "
        "across harnesses is still a real, measurable difference, and it is the part an operator can "
        "change. Operator steal: when you report an agent-security number, **say which model and which "
        "harness produced it**; a model-only or harness-only claim is under-specified. Pairs K341 and the "
        "containment line. **Measurement recommendation, not an adoption.** Any run against our own "
        "harness is a scoped, authorised test. **No injection payloads in wiki.**",
        ["concepts/harness-vs-model-risk-share.md",
         "concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/agentic-containment-principles.md"],
        read="read (routed brief)")
    concept("harness-vs-model-risk-share",
        "Separate model risk from harness risk", "K282-b", "arXiv 2610.03153",
        "An agent-security number is produced by a **model running in a harness**. EvoRiskBench measured "
        "nine combinations and found **model spread 54.37 pp against harness spread 5.41 pp** — most of "
        "the variance is the model, but the harness contributes a real, repeatable 5 pp, and that is the "
        "part an operator can actually change (tool gating, sandboxing, egress rules).\n\n"
        "So: always report **model x harness** together, and when you harden the harness, expect a "
        "**single-digit** improvement, not a transformation — the rest is the model. Injection arrives "
        "through tools, skills, and subagents, so those are the surfaces to instrument. This is the "
        "measurement counterpart to the K421 containment rule.",
        ["sources/arxiv-2610-03153-evoriskbench-runtime.md",
         "concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/agentic-containment-principles.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K282-b)")

    # ---------- 4. BabelFake ----------------------------------------------
    source("arxiv-2610-06339-babelfake-multilingual-av-deepfake",
        "BabelFake: a multilingual audio-visual deepfake benchmark",
        "arXiv 2610.06339", "arXiv paper (routed from image-gen 2026-10-07)",
        "not held locally — routed brief only",
        "**A detection benchmark, not a generation resource** — which is why image-gen routed it here. "
        "First **consent-sourced, multilingual audio-visual** deepfake detection benchmark: IRB-approved, "
        "paid participants consenting to their likeness and voice being manipulated, released behind a "
        "data-use agreement.\n\n"
        "**Scale:** 399k clips / 1,323 hours / 496 individuals across English, German, Italian, French, "
        "Spanish. **20,117 real + 379,582 fake**, identity-disjoint 70/10/20 split. Built from **11 video "
        "manipulation methods** (face swap, lipsync, portrait animation) and **4 voice-cloning engines**, "
        "conditioned on pristine and synthetic audio.\n\n"
        "**Detection results:** SpeechForensics best overall at **AUC 79.79** (peak **83.83** Spanish, "
        "**80.99** English). Multimodal beats unimodal (**74.27 vs 71.44** macro AUC). The operational "
        "finding: detectors **degrade sharply when the visual fake keeps authentic audio** — the real "
        "audio track removes the signal they lean on. No language is consistently hardest; demographic "
        "gaps mostly under 4 AUC.\n\n"
        "**Access:** no repository, no code, no weights, not on GitHub or Hugging Face — controlled "
        "non-commercial licence with institutional verification and a data-use agreement.",
        ["concepts/armor-plusplus-agentic-deepfake-detector-attacks.md"],
        read="read (routed brief)")
    add_related("concepts/armor-plusplus-agentic-deepfake-detector-attacks.md",
        "sources/arxiv-2610-06339-babelfake-multilingual-av-deepfake.md",
        "K-b: BabelFake multilingual AV deepfake detection benchmark")

    # ---------- 5. Inbound wave digest ------------------------------------
    concept("inbound-security-wave-2026-10-07",
        "Inbound brief wave — agent verification, refusal bias, jailbreak benchmark", "Wave",
        "OSINT K282/K283 + CCC K421-K423",
        "Digest of the inbound briefs of 2026-10-05..07 whose items did not each warrant a page. Each "
        "entry is **second-hand from the routed brief**, not a first-hand read.\n\n"
        "**Agent verification (K283).** **CLIFT** (2610.06829) replaces an LLM judge with a "
        "**conformal-rectified bank of URL-scoped verification questions**, a Mondrian-ACI tracker per "
        "URL tier giving a trust weight, and an **additive-only** training reward: **+11.3 pp on OM2W at "
        "K=4 with zero policy training.** **Wikidata Search Traces** (2610.06650): a persistent-Python-"
        "state harness beats stateless tool-calling (gpt-6-luna 49→61; Qwen3.8-27B 60→74). **T-Search** "
        "(2610.06782, Apache-2.0): return **ranked evidence chunks with reasons, not answers**, keeping "
        "verifier and generator swappable. **BTTF** (2610.06790): multi-agent text-to-SQL over a "
        "normalised DB beats a single agent by **17.3%**. The shared pattern: **verification should be a "
        "separate, certified, judge-free layer.**\n\n"
        "**Refusal surface (K282).** **PowerBench** (2610.02303), 24 models: refusals rank "
        "**power-grabbing > disempowerment > self-empowerment**; average refusal 1.0–35.1%; refusal "
        "**triples** when the request is framed at society scale; AI-agent requesters were refused more "
        "than humans. **MLCommons Jailbreak Benchmark v1.0** (2610.02827): unsafe-response rate "
        "**11.08% → 18.65%**, average **Resilience Gap 7.57 pp** (was 19.8 in v0.5), Role-Play and "
        "Template strongest at 35.7%. The reusable idea is the **paired metric** — attack-conditioned "
        "result against a baseline, so the attack's effect is separated from the model's starting "
        "disposition. **MoE router gradient** (2610.02910): router-gradient expert selection cuts "
        "refusals more than activation frequency does, in 24 of 25 conditions; OLMoE refusals fell "
        "**34 → 9 of 100**. Dual-use and local-lab only — the same gradient that finds the experts "
        "gating a refusal is what an attacker would target.\n\n"
        "**Also noted (K283), headlines only.** Liquid Network consensus exploit — cache-key ambiguity "
        "in Elements Rangeproof verification, ~4,000 unbacked L-BTC minted, ~602 BTC unrecovered: **a "
        "validation cache is part of the consensus security boundary.** iOS **DarkSword** exploit kit "
        "reused in the wild (WebKit → PAC bypass → sandbox escape → kernel). NetScaler: **a patch does "
        "not undo a compromise** — patch and recovery are separate decisions. LLM vulnerability "
        "discovery produced >1,000 reports on Bitcoin Core, mostly false positives — prefer fuzzing and "
        "property tests. OWASP **Securing Agentic Applications**: watch for the Agentic TOP 10, ANS, "
        "and A2AS standards.\n\n"
        "**Boundary:** FILE only. No PoC, no exploit steps, no payloads, no injection strings anywhere "
        "in this wiki.",
        ["concepts/k277-security-wave.md",
         "concepts/agentic-containment-principles.md",
         "concepts/coding-agent-supply-chain-install-gap.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound wave)")

    # ---------- backlinks --------------------------------------------------
    for rel, ref, note in (
        ("concepts/agentic-containment-principles.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "K421 Kubernetes containment: the model is not a boundary"),
        ("concepts/agentic-containment-principles.md",
         "concepts/harness-vs-model-risk-share.md",
         "K282-b separate model risk from harness risk"),
        ("concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "K421 seven-layer Kubernetes containment"),
        ("concepts/cyber-capable-agent-evaluation-containment.md",
         "concepts/harness-vs-model-risk-share.md",
         "K282-b model x harness reporting"),
        ("concepts/coding-agent-supply-chain-install-gap.md",
         "concepts/agent-memory-supply-chain-compromise.md",
         "K283-b the memory layer is a supply-chain target"),
        ("concepts/coding-agent-supply-chain-install-gap.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "K421 third-party MCP tool descriptions as untrusted input"),
        ("concepts/agent-skill-injection.md",
         "concepts/agent-memory-supply-chain-compromise.md",
         "K283-b poisoned memory package leaks the whole context"),
    ):
        add_related(rel, ref, note)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
