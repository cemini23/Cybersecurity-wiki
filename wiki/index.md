# Cybersecurity Wiki — Index

> Content-oriented catalog of every page in this wiki. Keep this curated by hand — it's the human-readable map.

---

## How to use this index

- **Concepts** are the *answers* (synthesized understanding of a topic). Start here when you ask "what is X?"
- **Entities** are the *nouns* (tools, certs, threat actors, people, vendors, programming languages, frameworks, platforms). Start here when you ask "tell me about X"
- **Sources** are the *raw inputs* (one page per PDF/article/repo). Mostly anchored from corresponding entity/concept pages — only browse them directly when you need provenance

---

## Concepts

### Doctrine + methodology

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/red-team-operations.md | validated | Red Team vs Pentest distinction; engagement model |
| @concepts/adversary-emulation.md | validated | APT-emulation plan + AutoSUT environment gap + LLM persona convergence |
| @concepts/threat-intelligence.md | validated | CTI 3-tier model + STIX SUT limits + LLM CVE→STIX gates |
| @concepts/purple-team-operations.md | draft | Red + blue collaborative engagements |
| @concepts/soc-operations.md | validated | Security Operations Center tooling + tiers + 5 pillars |
| @concepts/incident-response.md | validated | NIST / SANS IR lifecycle |
| @concepts/ransomware.md | validated | Ransomware defensive ops + investigation runbook (T1486) |
| @concepts/threat-hunting.md | validated | Hypothesis-driven proactive detection |
| @concepts/phishing-investigation.md | validated | SOC-analyst phishing triage (Yahia 5-step workflow + SPF/DKIM/DMARC) |
| @concepts/responsible-disclosure.md | draft | Coordinated Vulnerability Disclosure + CVE process |
| @concepts/bug-bounty.md | draft | Public bounty programs + career path + beefy-box ROI |
| @concepts/operator-lab-playbook.md | draft | Start-here hub: local AI → owned lab → product pentest → bounty |
| @concepts/local-abliterated-llm-pentest-stack.md | draft | Local abliterated/low-refusal text LLM stack (Linux+NVIDIA + Apple Silicon) |
| @concepts/owned-target-whitehat-lab.md | draft | Authorization + isolation for whitehat on owned servers/VMs |
| @concepts/pre-release-product-pentest.md | draft | Pre-launch product security loop (ASVS 5.0-informed → fix → retest) |
| @concepts/ai-pentest-harness-landscape.md | draft | CyberStrike vs Strix vs MIT peers — license/containment decision matrix |
| @concepts/cybersecurity-careers.md | validated | Career map + certification ladder |
| @concepts/agent-execution-provenance.md | draft | Evidence tracing + execution provenance — CFD artifact gap (2606.09084) |
| @concepts/agent-vm-sandboxing.md | validated | LLM-driven agent-VM sandboxing; pairs with Docker allowlist proxy (K102) |
| @concepts/docker-agent-sandbox-allowlist-proxy.md | draft | Docker/gVisor agent sandbox + vp-internal egress allowlist (K102) |

### Offensive technique categories

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/web-pentest-methodology.md | validated | Web-app pentest checklist (Joas) |
| @concepts/windows-pentest.md | draft | Windows + Active Directory + O365 |
| @concepts/cloud-pentest.md | draft | AWS / Azure / GCP / O365 pentest |
| @concepts/mobile-pentest.md | draft | Android + iOS app pentest |
| @concepts/network-security.md | draft | Network / firewall / wireless / IoT / OT / prEN 50742 safety-security |
| @concepts/industrial-safety-security-convergence.md | draft | prEN 50742 / IO-Link Wireless crypto capacity collapse (2607.15840) |
| @concepts/solver-grounded-agentic-ot.md | draft | Smart-grid/OT agents: solver + verify before setpoints (2607.18147) |
| @concepts/6g-cps-closed-loop-security.md | draft | 6G CPS edge-to-network AI-native security loop (2606.08173) |
| @concepts/exploit-development.md | draft | Buffer overflow → ROP → kernel exploits |
| @concepts/buffer-overflow.md | validated | Stack/heap overflow fundamentals + shellcode |
| @concepts/av-edr-bypass.md | validated | AV/EDR evasion tradecraft |
| @concepts/privilege-escalation.md | validated | Linux + Windows privesc |
| @concepts/credential-access.md | draft | Credential dumping + password cracking (TA0006) |
| @concepts/pivoting.md | draft | Lateral movement + tunneling + port forwarding |
| @concepts/social-engineering.md | draft | Phishing + vishing + pretexting |
| @concepts/phishing.md | draft | Spear phishing + MFA bypass + infrastructure |
| @concepts/osint-for-cybersecurity.md | validated | Pre-engagement + threat-intel OSINT |
| @concepts/linux-pentest.md | draft | Linux enumeration + privesc (GTFOBins, SUID, capabilities) |
| @sources/arxiv-2607-20280-drone-fl-chained-attacks.md | draft | Drone FL deauth→impersonation chain (2607.20280; K215) |
| @sources/arxiv-2607-20852-code-monitor-red-teaming.md | draft | CodeMonitorBench public-test residual bugs (2607.20852; K216) |
| @sources/arxiv-2607-21419-pats-agentic-rl.md | draft | PATS policy-aware agent RL scaffold (2607.21419; K217) |
| @sources/arxiv-2607-21468-thinkink.md | draft | Thinkink ink-native LLM canvas HCI (2607.21468; K218) |
| @sources/arxiv-2607-21564-rf-fingerprint-probe.md | draft | RFFI probe-point open-set benchmark (2607.21564; K219) |
| @concepts/drone-fl-chained-deauth-impersonation.md | draft | Wi-Fi deauth enables FL client impersonation |
| @concepts/code-monitor-red-teaming-public-tests.md | draft | Weak monitors miss hidden bugs after public tests |
| @concepts/pats-policy-aware-agent-rl-scaffold.md | draft | Fade training scaffolds for agentic RL |
| @concepts/thinkink-ink-native-llm-canvas.md | draft | Ink-native multimodal LLM canvas (HCI light) |
| @concepts/rf-fingerprint-probe-point-benchmark.md | draft | RFFI performance depends on RX probe point |
| @sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md | draft | Evidential ceiling for AI red-team evals (2607.21735; K220) |
| @sources/arxiv-2607-23496-concept2scenario-vulnerable-scenarios.md | draft | Concept2Scenario refusal-suppression priors (2607.23496; K221) |
| @sources/arxiv-2607-25379-cyber-capable-agent-containment.md | draft | Cyber-capable agent eval containment (2607.25379; K222) |
| @sources/arxiv-2607-25987-ih-benchmark-instruction-hierarchy.md | draft | IH-Benchmark S≻U vs U≻T (2607.25987; K223) |
| @sources/arxiv-2607-25995-kutie-topology-k8s-patches.md | draft | KuTIE topology-aware K8s patches (2607.25995; K224) |
| @concepts/ai-redteam-evidential-ceiling.md | draft | What fixed-budget red-team evals can prove |
| @concepts/concept2scenario-refusal-suppression.md | draft | SAE→scenario jailbreak priors |
| @concepts/cyber-capable-agent-evaluation-containment.md | draft | Contain capability eval environments |
| @concepts/instruction-hierarchy-conflict-benchmark.md | draft | S≻U ≠ U≻T hierarchy robustness |
| @concepts/topology-aware-k8s-llm-remediation.md | draft | Call-graph context for KSPM LLM patches |
| @sources/arxiv-2607-25070-rffi-device-temperature.md | draft | RFFI temperature drift (2607.25070; K225) |
| @sources/arxiv-2607-26115-gpt-red-self-play.md | draft | GPT-Red self-play red teaming (2607.26115; K226) |
| @sources/arxiv-2607-27090-inferscale-kv-injection.md | draft | InferScale KV injection serving (2607.27090; K227) |
| @sources/arxiv-2607-27136-kamr-multihop-retrieval.md | draft | KAMR multi-hop KG retrieval (2607.27136; K228) |
| @sources/arxiv-2607-27145-bydeway-v2-spatial.md | draft | ByDeWay-V2 explainable spatial MLLM (2607.27145; K229) |
| @concepts/rf-fingerprint-temperature-drift.md | draft | Temperature shifts RF fingerprints |
| @concepts/gpt-red-self-play-red-teaming.md | draft | Self-play automated prompt-injection discovery |
| @concepts/inferscale-kv-injection-personalized-serving.md | draft | Privileged KV injection for persona memory |
| @concepts/kamr-knowledge-aligned-multihop-retrieval.md | draft | Anchor-then-expand multi-hop GRAG |
| @concepts/bydeway-v2-explainable-spatial-reasoning.md | draft | Auditable spatial predicates for MLLMs |
| @sources/arxiv-2607-28498-tca-sir-scientific-inspiration.md | draft | TCA-SIR remote-analogy SIR (2607.28498; K230) |
| @sources/arxiv-2607-28529-cogate-secure-code-codecoding.md | draft | CoGate confidence-gated secure codegen (2607.28529; K231) |
| @sources/arxiv-2607-28617-aispa-system-prompt-auditing.md | draft | AISPA system-prompt auditing (2607.28617; K232) |
| @sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md | draft | CWEEP RTL CWE static analysis (2607.29604; K233) |
| @sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md | draft | STAIR hierarchical repair trajectories (2607.29658; K234) |
| @sources/arxiv-2607-29678-toktier-stateful-tokenization.md | draft | TokTier exact stateful tokenization (2607.29678; K235) |
| @concepts/cweep-rtl-cwe-early-prevention.md | draft | Early RTL CWE lint without full security specs |
| @concepts/stair-hierarchical-repair-plans.md | draft | Hierarchical repair plans from agent trajectories |
| @concepts/toktier-exact-stateful-tokenization.md | draft | Exact stateful tokenization for agent serving TTFT |
| @sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md | draft | ART→PDDL attack-chain granularity (2608.00143; K236) |
| @sources/arxiv-2608-00677-openart-agent-redteam-evolution.md | draft | OpenART environment-evolution red team (2608.00677; K237) |
| @sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md | draft | Salami collusive memory poisoning (2608.01637; K238) |
| @sources/arxiv-2608-02520-medpress-patient-pressure-sycophancy.md | draft | MedPRESS multi-turn medical sycophancy (2608.02520; K239) |
| @sources/arxiv-2608-02585-gradcuit-test-time-latent-reasoning.md | draft | GradCuit test-time latent reasoning (2608.02585; K240) |
| @concepts/symbolic-art-attack-chain-granularity.md | draft | Predicate granularity for ART symbolic chains |
| @concepts/openart-environment-evolution-agent-redteam.md | draft | Stateful environment evolution for agent RT |
| @concepts/salami-collusive-memory-poisoning.md | draft | Collusive benign-looking memory coalitions |
| @concepts/multi-turn-pressure-sycophancy.md | draft | Pressure ladders induce unsafe agreement |
| @concepts/gradcuit-test-time-latent-reasoning.md | draft | Credit-assigned test-time latents |
| @sources/arxiv-2608-02341-wifi-broadcast-rate-edge-moe.md | draft | Wi-Fi 54 Mbps broadcast cap / edge MoE (2608.02341; K241) |
| @sources/arxiv-2608-03151-airkey-wifi-acoustic-pin-inference.md | draft | AirKey CSI+acoustic PIN side channel (2608.03151; K242) |
| @sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md | draft | Adaptive fuzzy TTS sampling (2608.03961; K243) |
| @concepts/wifi-broadcast-rate-edge-moe.md | draft | 802.11 broadcast rate cap vs edge MoE |
| @concepts/airkey-wifi-acoustic-pin-sidechannel.md | draft | Unassociated ACK-CSI + audio PIN inference |
| @concepts/adaptive-fuzzy-test-time-sampling.md | draft | Inspectable per-query TTS sample budgets |
| @sources/arxiv-2608-04317-trident-agentic-drl-redteam.md | draft | Trident agentic DRL-defense red team (2608.04317; K244) |
| @sources/arxiv-2608-04881-horffi-high-openness-rffi.md | draft | HoRFFI high-openness RFFI (2608.04881; K245) |
| @sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md | draft | Gradient Immunity malicious FT gate (2608.05045; K246) |
| @sources/arxiv-2608-05063-chiplet-llm-hardware-security.md | draft | Chiplet + LLM-EDA hardware security (2608.05063; K247) |
| @sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md | draft | PIMiner prompt-injection red team (2608.05108; K248) |
| @concepts/trident-agentic-drl-defense-redteam.md | draft | Adaptive red vs DRL cyber defenses |
| @concepts/horffi-high-openness-rffi.md | draft | Few-shot open-set RF fingerprinting |
| @concepts/gradient-immunity-malicious-finetune.md | draft | Null-space resistance to malicious FT |
| @concepts/chiplet-llm-hardware-security.md | draft | Chiplet + LLM-EDA attack surfaces |
| @concepts/piminer-agentic-prompt-injection-redteam.md | draft | Transferable PI strategy-library RT |
| @sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md | draft | ARIA instruction-backdoor RT (2608.05659; K249) |
| @sources/arxiv-2608-06246-post-training-adaptation-taxonomy.md | draft | Post-training adaptation taxonomy (2608.06246; K250) |
| @sources/arxiv-2608-06287-nl-to-ltl-requirements.md | draft | NL-to-LTL via LLMs (2608.06287; K251) |
| @sources/arxiv-2608-06301-harnessopt-bench.md | draft | HarnessOpt-Bench (2608.06301; K252) |
| @concepts/aria-instruction-backdoor-redteam.md | draft | Covert instruction backdoors on customized coding LLMs |
| @concepts/post-training-adaptation-taxonomy.md | draft | Six-axis post-training change vocabulary |
| @concepts/nl-to-ltl-requirements-llm.md | draft | LLM front-end for NL→LTL (HITL) |
| @concepts/harnessopt-bench.md | draft | Budgeted harness-optimization eval protocol |
| @sources/arxiv-ood-qnlp-discocat-financial-2608.07439.md | draft | OOD QNLP DisCoCat financial rewrite (2608.07439) |
| @sources/arxiv-2608-07440-blast-radius.md | draft | Blast Radius reversible context eviction (2608.07440; K265) |
| @sources/arxiv-2608-07446-shieldai-oss-ai-risk-tools.md | draft | ShieldAI OSS AI risk tool taxonomy map (2608.07446; K266) |
| @concepts/blast-radius-reversible-context-eviction.md | draft | Reversible, gate-licensed context eviction for coding agents |
| @concepts/taxonomy-driven-oss-ai-risk-mitigation.md | draft | Map OSS eval/guardrail tools to MIT risk taxonomy |
| @sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md | draft | ILL inaudible LF audio vs LALMs (2608.09158; K267) |
| @concepts/inaudible-low-frequency-audio-attacks.md | draft | Perception-boundary mismatch audio red team + DRG requery |
| @entities/tools/ill-inaudible-low-frequency-lockout.md | draft | ILL method (REFERENCE; K267) |
| @sources/arxiv-2608-15578-arena-audio-lalm-redteam.md | draft | ARENA audio-grounded LALM RT (2608.15578; K282) |
| @concepts/audio-grounded-lalm-redteaming.md | draft | Text-safe + audio-harmful LALM red team; split judges |
| @entities/tools/arena-audio-redteam.md | draft | ARENA controller (REFERENCE; K282) |
| @sources/arxiv-2608-09885-she-safety-harness-evolution.md | draft | SHE trajectory-driven harness evolution (2608.09885; K268) |
| @concepts/safety-harness-evolution.md | draft | Four-artifact harness evolution + validity + safety-utility selection |
| @entities/tools/she-safety-harness-evolution.md | draft | SHE harness-evolution (GO clone Apache-2.0; K268) |
| @sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md | draft | Taboo decoding-time logit-space diagnostic (2608.09900; K269) |
| @concepts/decoding-level-taboo-diagnostic.md | draft | Word-boundary logit masking off-path robustness stress test |
| @sources/arxiv-2608-06866-ood-dodtrack-wifi-doppler-tracking.md | draft | OOD DoDTrack Wi-Fi Doppler tracking (2608.06866) |
| @sources/arxiv-2608-09930-ood-beyond-naturalness-tts-eval.md | draft | OOD Beyond-Naturalness TTS eval (2608.09930) |
| @sources/arxiv-2608-10171-gflownets-llm-attacks-turkcell.md | draft | GFlowNet automated LLM attack generation (2608.10171; K270) |
| @concepts/gflownet-automated-redteam-attack-generation.md | draft | GFlowNet attacker-victim-evaluator attack-gen concept |
| @sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md | draft | REDAgentBench executable RT + faithful ASR (2608.10669; K271) |
| @concepts/faithful-agent-asr-measurement.md | draft | Exposure/execution/observation/adjudication ASR decomposition |
| @entities/tools/redagentbench.md | draft | REDAgentBench benchmark (REFERENCE; K271) |
| @sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md | draft | Cross-lingual safety transfer illusion LRLs (2608.11146; K272) |
| @concepts/cross-lingual-safety-transfer-lrl.md | draft | English-only safety ≠ LRL safety; localized prompts |
| @sources/arxiv-2608-11044-ood-teammix-htc.md | draft | OOD TEAMMix hierarchical text classification (2608.11044) |
| @sources/arxiv-2608-11121-ood-genai-statistical-research.md | draft | OOD GenAI in statistical research (2608.11121) |
| @concepts/hardware-id-masking-opsec.md | draft | HWID layers + MAC rand ≠ unlinkability (OPSEC) |
| @concepts/metadata-traffic-analysis-anonymity.md | draft | Metadata/traffic confirmation: AS/global observer beats path encryption |
| @concepts/censorship-circumvention-pluggable-transports.md | draft | Bridges + PTs (obfs4/meek/Snowflake/WebTunnel); DPI vs traffic-confirmation |
| @concepts/commercial-spyware-stalkerware-defense.md | draft | Mercenary spyware + stalkerware as endpoint compromise; Lockdown Mode / MVT |
| @concepts/account-recovery-deanonymization.md | draft | Anonymity dies at recovery: SIM swap, SSO, recovery identity |
| @concepts/hardware-bound-identity-anticheat-licensing.md | draft | AC/licensing HWID map (architecture; no spoof kits) |
| @concepts/software-license-binding.md | draft | License design: bind ≥2 layers; repair paths; no keygens |
| @concepts/anti-tamper-protection-classes.md | draft | Protection classes (integrity/pack/virtualize/heartbeat); classes not kits |
| @concepts/mobile-app-attestation.md | draft | Play Integrity + App Attest; server verifies, client relays |
| @concepts/secure-boot-vs-device-ownership.md | draft | Secure Boot/attestation trust stack vs device ownership (policy; no bypass) |
| @concepts/hardened-alternative-operating-systems.md | draft | GrapheneOS / Qubes / Whonix / Kicksecure / Tails — pick by threat, not brand |
| @concepts/endpoint-encryption-deniable-storage.md | draft | FDE ≠ anonymity; deniable-storage class (existence + limits, no how-to) |
| @concepts/product-build-integrity-slsa-sigstore.md | draft | SLSA / Sigstore / reproducible-build release-integrity layer |
| @sources/microsoft-hvci-memory-integrity.md | draft | HVCI / memory integrity (VBS kernel CI) |
| @sources/microsoft-elam.md | draft | Early Launch Anti-Malware boot classification |
| @sources/microsoft-secure-boot.md | draft | UEFI Secure Boot signature chain (PK/KEK/db/dbx) |
| @sources/microsoft-bitlocker-overview.md | draft | BitLocker FDE overview (lost-disk threat model) |
| @sources/apple-filevault.md | draft | FileVault macOS FDE (login-gated at-rest) |
| @sources/veracrypt-hidden-volumes.md | draft | Hidden-volume architecture (deniable-storage class) |
| @sources/slsa-supply-chain-levels.md | draft | SLSA v1.0 build track L0–L3 provenance |
| @sources/sigstore-overview.md | draft | Keyless signing (Fulcio/Rekor/Cosign) |
| @sources/reproducible-builds.md | draft | Deterministic build + independent verification |
| @sources/microsoft-kernel-dma-protection.md | draft | IOMMU fencing of hot-plug PCIe (DMA) |
| @sources/microsoft-wdac-appcontrol-overview.md | draft | App Control for Business / WDAC allow-list |
| @sources/microsoft-volume-activation-clients.md | draft | KMS/ADBA/MAK lease activation |
| @sources/flexera-flexnet-licensing.md | draft | FlexNet commercial entitlement stack |
| @sources/irdeto-denuvo-anti-cheat-anti-tamper.md | draft | Denuvo kernel AC + anti-piracy vendor pages |
| @sources/collberg-thomborson-software-protection-tools.md | draft | 2002 protection-taxonomy anchor (skimmed) |
| @sources/google-play-integrity-api.md | draft | Play Integrity verdicts + server verification |
| @sources/apple-app-attest.md | draft | App Attest Secure Enclave keys + DeviceCheck |
| @sources/vanhoef-asiaccs2016-mac-randomization-not-enough.md | draft | AsiaCCS 2016 — random MAC not enough |
| @sources/arxiv-1703-02874-mac-randomization-when-it-fails.md | draft | PETS 2017 MAC randomization failures (1703.02874) |
| @sources/kohno-2005-remote-physical-device-fingerprinting.md | draft | Clock-skew physical device fingerprinting |
| @sources/arxiv-1905-01051-browser-fingerprinting-survey.md | draft | Laperdrix TWEB browser-fingerprint survey |
| @sources/arxiv-2201-09956-drawn-apart-gpu-fingerprinting.md | draft | DrawnApart GPU EU fingerprint (NDSS 2022) |
| @sources/arxiv-2507-02478-statefi-wifi-fsm-fingerprinting.md | draft | StateFi FSM de-randomization (2507.02478) |
| @sources/arxiv-2606-25788-ml-mac-randomization.md | draft | ML clustering vs MAC randomization (2606.25788) |
| @sources/microsoft-systemidentification-getsystemidforpublisher.md | draft | Windows TPM/UEFI system ID persists reimage |
| @sources/microsoft-oa3-hardware-hash.md | draft | OEM Activation 3.0 hardware hash / association |
| @sources/microsoft-autopilot-motherboard-replacement.md | draft | Official Autopilot 4K HH recapture after board swap |
| @sources/arxiv-2408-00500-kernel-anticheat-rootkit-taxonomy.md | draft | ARES 2024 kernel AC vs rootkit taxonomy |
| @sources/s4dbrd-kernel-anti-cheats.md | draft | Kernel AC architecture + identifier list (blog) |
| @sources/secret-club-battleye-architecture-2019.md | draft | BattlEye four-entity architecture (2019) |
| @sources/oofhours-autopilot-hardware-hash.md | draft | OA3Tool 4K HH field inventory (encoded, not a digest) |
| @sources/checkpoint-evasions-firmware-tables.md | draft | NtQuerySystemInformation class 76 / RSMB / FIRM |
| @sources/microsoft-getruntimeattestationreport.md | draft | Signed loaded-driver attestation (HVCI; AC consumer) |
| @sources/riot-vanguard-on-demand-2026.md | draft | Riot first-party On-Demand + TPM EK as HWID |
| @sources/epic-games-v-araujo-hwid-spoofer-judgment.md | draft | Epic default judgment: HWID spoof as DMCA circumvention |
| @sources/faceit-enhanced-verification.md | draft | FACEIT multi-account checks include hardware identifiers |
| @sources/tails-mac-address-anonymization.md | draft | Tails default MAC anonymization (LAN only) |
| @sources/android-aosp-wifi-mac-randomization.md | draft | Android 10+ per-SSID randomized MAC |
| @concepts/tca-sir-target-conditioned-inspiration-retrieval.md | draft | Target-conditioned transferable inspiration rank |
| @concepts/cogate-confidence-gated-secure-code.md | draft | Gate security co-decoding on expert confidence |
| @concepts/aispa-system-prompt-assurance-audit.md | draft | Eight-dimension protective vs problematic prompt audit |
| @concepts/wireless-pentest.md | draft | WiFi / WPS / Bluetooth / RFID attacks |
| @concepts/container-security.md | draft | Docker + Kubernetes attack/defense |
| @concepts/dns-server-discovery-vs-subdomain-enumeration.md | draft | DNS recon distinction (server discovery vs subdomain enum) |

### Defensive + analytical

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/malware-analysis.md | draft | Static + dynamic malware RE |
| @concepts/defense-in-depth.md | draft | Layered security architecture |
| @concepts/system-hardening.md | draft | OS + network + application hardening |
| @concepts/linux-security.md | draft | RHEL security, SELinux, auditd, SSH hardening |
| @concepts/siem.md | draft | SIEM platform layer — log collection, correlation, alerting; BAS→Sigma detection-as-code (2606.05252) |
| @concepts/endpoint-detection-response.md | draft | EDR/XDR — endpoint telemetry, detection + response |

### Emerging / cross-domain

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/ai-for-cybersecurity.md | draft | LLM use in red + blue workflows |
| @concepts/llm-cve-to-stix-generation.md | draft | Open-weight CVE→STIX (CAV-STIXGen); gate on SRO/ATT&CK |
| @concepts/rubric-capability-tree-diagnosis.md | draft | CRAFT — rubric-criterion capability trees for targeted SFT |
| @concepts/llm-research-competency-model.md | draft | Eight competencies for LLM-literate researchers (2607.16083) |
| @concepts/coding-agent-context-pruning.md | draft | SWE-Pruner Pro internal-rep tool-output prune (2607.18213) |
| @concepts/evidence-aware-long-context-grounding.md | draft | GEAR — evidence reward vs distractor copy (2607.19345) |
| @concepts/off-context-privileged-rlvr.md | draft | OC-GRPO privileged guidance for hard RLVR (2607.19313) |
| @concepts/quantum-vqe-adversarial-robustness.md | draft | Cloud VQE red-team SoK / VQE-AdvBench (2607.19318) |
| @concepts/llm-belief-expression-robustness.md | draft | EoBench — belief framing vs prior knowledge (2607.18232) |
| @concepts/llm-vulnerability-discovery.md | draft | LLM-driven vuln-discovery pipeline (Detect→Attack); defending-code ASAN verify |
| @concepts/llm-adversarial-fuzzing.md | draft | Adversarial LLM testing methodology (FuzzyAI umbrella) |
| @concepts/defender-centric-jailbreak-utility.md | draft | A-MESS/AttackSHAP — rank jailbreaks by safety-train utility (2607.17152) |
| @concepts/llm-biosecurity-red-teaming.md | draft | Dual-use bio early-warning posture (Intern-BioBreaker 2607.18056) |
| @concepts/biosecbench-surveillance-verifiable-agent-eval.md | draft | BioSecBench surveillance agent eval (2607.19262; CCC K203) |
| @concepts/pair-prompt-pattern.md | draft | PAIR — single-turn LLM jailbreak (arXiv 2310.08419) |
| @concepts/crescendo-multi-turn-jailbreak.md | draft | Multi-turn LLM escalation attack (arXiv 2404.01833) |
| @concepts/amt-x-phase-structured-multi-turn-red-teaming.md | draft | AMT-X dual overall/full ASR + phase state machine (2607.11151) |
| @concepts/vulnerability-concept-graph-production-agent-red-teaming.md | draft | AHA VCG — enabling-condition red-team knowledge (2607.11698) |
| @concepts/skillsec-lifecycle-agent-skill-security.md | draft | SkillSec lifecycle beyond execution (2607.13987) |
| @concepts/gflowrl-distribution-matching-attacker-rl.md | draft | GFlowRL attacker-diversity RL slice; repo NO-GO (2607.13394) |
| @concepts/datashield-risky-finetune-data-filtering.md | draft | DataShield — consensus subspace filter for risky FT data (2607.15081) |
| @concepts/physical-vs-content-danger-embodied-agents.md | draft | PRISM — CD vs PD for embodied/tool agents (2607.15218) |
| @concepts/agentic-hard-example-synthesis-content-safety.md | draft | Agentic multimodal hard-example synthesis (2607.14256) |
| @concepts/llm-statistical-self-consistency-macro-fallacy.md | draft | Partition–prompt–aggregate macro fallacy (2607.15277) |
| @concepts/coding-agent-supply-chain-install-gap.md | draft | Coding-agent install gap + pre-install gate (2607.15143 / K179) |
| @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md | draft | ARMOR++ agentic deepfake-detector transfer attacks (2607.15246 / K188) |
| @concepts/mcp-security-evidence-grounded-detection.md | draft | FlowGuard — evidence-grounded MCP detection (2607.14754 / K189 route) |
| @sources/arxiv-2607-19837-know-your-agent-recon.md | draft | KYA recon-driven IPI pentest (2607.19837; K210) |
| @sources/arxiv-ethics-autonomous-offensive-ai-2607.20255.md | draft | Ethics of autonomous offensive AI agents (2607.20255; K211) |
| @sources/arxiv-2607-20270-schwartz-value-recognition.md | draft | Schwartz value recognition confusions (2607.20270; K212) |
| @sources/arxiv-2607-20286-probabilistic-llm-safety-bounds.md | draft | Sound PAC safety bounds for LLMs (2607.20286; K213) |
| @sources/arxiv-2607-20372-notes-to-self-experiential.md | draft | Experiential abstractions Notes-to-self (2607.20372; K214) |
| @concepts/agent-reconnaissance-ipi-pentesting.md | draft | Agent recon loop for IPI pentesting (KYA) |
| @concepts/llm-schwartz-value-recognition.md | draft | Schwartz Acc@1/directed confusions |
| @concepts/llm-probabilistic-safety-bounds.md | draft | Clopper-Pearson PAC harm lower bounds |
| @concepts/experiential-abstraction-memory.md | draft | Score-gated experiential abstraction memory |
| @concepts/ethics-autonomous-offensive-ai-agents.md | draft | Three indeterminacies — autonomous offensive agents |
| @entities/tools/know-your-agent.md | draft | KYA framework (CONDITIONAL-GO wait for release) |
| @entities/tools/notes-to-self.md | draft | Notes-to-self clone ~16MB Apache/verl (CONDITIONAL-GO) |
| @concepts/llm-pentest-automation.md | draft | Tier 1/2 LLM pentest automation + scope-enforcement model |
| @concepts/agent-runtime-guardrails.md | draft | Agent side-effect attacks + runtime guards; GT-MCP trajectory layer (2606.10322) |
| @concepts/llm-code-review-agent-security.md | draft | SEVRA merge-gate robustness — reversed CVE PR + framing attacks (2606.13757) |
| @concepts/authority-framing-agentic-cicd.md | draft | Authority laundering in multi-agent CI/CD (2607.19267) |
| @concepts/trajectory-context-control.md | draft | GT-MCP — multi-agent memory-commit gate + drift rollback (2606.10322) |
| @concepts/internet-of-agentic-ai-ioai.md | draft | IoAI vision — federated agent ecosystems + Table 4 threat taxonomy (2606.12835) |
| @concepts/exceptional-access-risk-quantification.md | draft | EA architecture risk framework — T-EA vs OTT-EA, deep uncertainty (2606.19106) |
| @concepts/agent-least-privilege-tool-selection.md | draft | Over-privileged tool selection — OPUR/PED, TOOLPRIVBENCH (2606.20023) |
| @concepts/agent-probabilistic-datalog-verification.md | draft | DRO probabilistic Datalog runtime verification — noisy classifiers (2606.20510) |
| @concepts/system-prompt-leakage.md | draft | System prompt exfiltration — attention drift, LeakBench, AREA (2606.18673) |
| @concepts/prompt-injection-detector-calibration.md | draft | Guard-model severity S under shift — confident FN on indirect hijack (2606.22659) |
| @concepts/self-evolving-agent-security.md | draft | MLAS matrix — self-evolving agents, attack persistence (2606.23075) |
| @sources/arxiv-2608-12851-skill-misevolution.md | draft | Skill misevolution / SKILLMISEVO (2608.12851; OSINT K237) |
| @concepts/skill-misevolution.md | draft | Practice can make a skill library unsafe — author/retrieve/execute gates |
| @sources/arxiv-2608-16465-jailbreakskill.md | draft | JailbreakSkill evolving attack skills (2608.16465; K283) |
| @concepts/evolving-attack-skill-libraries.md | draft | Offense-side evolving skill library — lab eval only |
| @entities/tools/jailbreakskill.md | draft | JailbreakSkill (NO-GO clone; null SPDX) |
| @sources/arxiv-2608-16806-esti-state-semantic-injection.md | draft | ESTI planner-state injection (2608.16806; K288) |
| @concepts/planner-state-integrity-embodied-agents.md | draft | Schema-valid env-state ≠ true; P-ASR ≠ E-ASR |
| @concepts/esti-state-semantic-injection-stub.md | draft | Pointer to Cybersec ESTI primary (CCC dual-home) |
| @entities/tools/esti-bench.md | draft | ESTI-Bench (REFERENCE; K288) |
| @sources/arxiv-2608-16747-chive-counterfactual-explanations.md | draft | CHIVE counterfactual explanations (2608.16747; K290) |
| @concepts/counterfactual-simulatability-llm-explanations.md | draft | Explanations need counterfactual tests |
| @entities/tools/chive.md | draft | CHIVE (GO REFERENCE clone; wont_wire) |
| @sources/arxiv-2608-17202-fools-gold-defensive-deception.md | draft | Fool's Gold decoy hardening (2608.17202; K295) |
| @concepts/decoy-hardening-open-weight-abliteration.md | draft | Abliterated-state decoys; denial of trust — no attack recipe |
| @sources/arxiv-2608-17361-trusted-workflow-relays.md | draft | Trusted workflow relays (2608.17361; K296) |
| @concepts/trusted-workflow-relay-email-abuse.md | draft | Service-authentic send ≠ send-authorization |
| @sources/arxiv-2608-19011-ti-to-detection-rule-grounding.md | draft | AUTOSIGMA CTI→Sigma (2608.19011; K297) |
| @concepts/knowledge-driven-detection-rule-grounding.md | draft | Enrich + template-ground + judge; no raw LLM-to-rule |
| @sources/arxiv-2608-19857-inadvertent-context-leakage.md | draft | Inadvertent context leakage (2608.19857; K298) — benign-output covert channel |
| @concepts/inadvertent-context-leakage.md | draft | Refusal ≠ no leak; tool-layer grants; no secrets in third-party-visible outputs |
| @sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md | draft | tl;dr sec #342 — ADR telemetry, SPIFFE act=agent, Cloudflare task-scoped access |
| @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md | draft | SecPro #248 — AI-ready SOC foundations (asset-ID map, gather-not-decide) |
| @concepts/agent-runtime-identity-adr.md | draft | Agent identity + ADR telemetry — sub=human / act=agent, SVIDs, Trust Ratchet |
| @concepts/agent-safety-executable-evaluation.md | draft | Benign-output predicate tests in executable eval — not only jailbreaks |
| @sources/arxiv-2608-20097-trustrag-committee-rag.md | draft | TrustRAG committee RAG (2608.20097; K299) — ZK + MPC + hash commitments |
| @concepts/committee-certified-rag-provenance.md | draft | RAG ranking/provenance = integrity boundary; schema-valid ≠ authenticated |
| @sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md | draft | BreakGuard LLM dependency tests (2608.20167; K300) — 30.3% of BUMP BCs |
| @concepts/llm-generated-dependency-breaking-tests.md | draft | LLM dependency tests are candidates, not a merge gate; crash-type > behavioral |
| @sources/arxiv-2608-16088-ood-rainfall-csi-sensing.md | draft | OOD rainfall CSI sensing (2608.16088) — CSI-as-environmental-sensor steal |
| @sources/arxiv-2608-20320-ood-travel-behavior-agents.md | draft | OOD travel-behavior agentic survey (2608.20320) — workflow-governance steal |
| @sources/arxiv-2608-17067-ood-disco-t2i-defense.md | draft | OOD DiSCO T2I defense → image-gen |
| @sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md | draft | OOD literature extraction — consensus ≠ ground truth |
| @sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md | draft | Rule blindness in compliance detectors (2608.16852; Watch) |
| @concepts/compliance-detector-rule-blindness.md | draft | Crossed-rule audit; detector verdict ≠ stated rule |
| @sources/arxiv-2608-18351-excess-authority-least-privilege.md | draft | Excess-authority least-privilege learning (CCC K290 ≠ CHIVE) |
| @concepts/task-conditioned-excess-authority.md | draft | Trajectory authority envelope; complements gates |
| @sources/arxiv-2608-14392-tripwire-safety-neuron-clamp.md | draft | Tripwire safety-neuron clamp (2608.14392; K240 Watch) |
| @concepts/tripwire-safety-neuron-clamp.md | draft | Do not clamp abliterated lab models without HITL |
| @sources/arxiv-2608-14529-deterministic-gapsvp-hardness.md | draft | Deterministic GapSVP NP-hardness (2608.14529; watch) |
| @concepts/lattice-pqc-hardness-watch.md | draft | Lattice PQC hardness story — not an attack |
| @sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md | draft | OOD astronomy backtesting — LLM-judge κ steal |
| @sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md | draft | OOD RA-Bench crisis video → image-gen |
| @concepts/differential-fault-injection-llm-code-stub.md | draft | CCC K284 DFI stub — off-nominal paired validation |
| @sources/arxiv-2608-12977-self-evolving-security.md | draft | HARD self-evolving runtime defense (2608.12977; OSINT K237) |
| @concepts/self-evolving-runtime-defense.md | draft | Evolve gates vs policy from held-out failures (HARD) |
| @concepts/ai-loss-of-control-osint-monitoring.md | draft | OSINT vectors for AI loss-of-control detection (2606.20610) |
| @concepts/cross-tool-description-poisoning.md | draft | Cross-tool MCP metadata steering + Tool-Guard isolated planning (2606.20922) |
| @concepts/local-agent-runtime-audit.md | draft | CLAWAUDIT static runtime audit — OpenClaw source (2606.21071) |
| @concepts/autonomous-defense-agent-transferability.md | draft | ARENA — SOC agent transferability gap (2606.21377) |
| @concepts/lingering-authority-revocable-capabilities.md | draft | PORTICO revocable planner capabilities (2606.22504) |
| @concepts/intent-governed-tool-authorization.md | draft | IGAC — session intent narrowing (2606.22916) |
| @concepts/agentic-offensive-security-kill-chain.md | draft | Agentic pentest agent kill chain + agent-phishing (2606.24496) |
| @concepts/multi-tool-threshold-mcp-poisoning.md | draft | ShareLock Shamir multi-tool MCP poisoning (2606.27027) |
| @concepts/tool-environment-unreliability-eval.md | draft | ToolBench-X recoverable tool hazards + diagnosis gap (2606.25819) |
| @concepts/confidence-aware-tool-orchestration.md | draft | Robust-TO Blind Trust + (result, confidence) tool routing (2606.26904) |
| @concepts/cognitive-heuristics-llm-vuln-detection.md | draft | Halo/framing/anchoring bias in LLM vuln scanners (2606.30587) |
| @concepts/mcp-execution-control-invariants.md | draft | HCP eight invariants — execution control beyond MCP connection (2606.29073) |
| @concepts/substrate-constraints-coding-agent-oversight.md | draft | Steerability via constraints — substrate + docs CLI for coding-agent oversight (2607.02389) |
| @concepts/agent-data-injection-attacks.md | draft | ADI — trusted/untrusted data isolation in agent context (2607.05120) |
| @concepts/mcp-taint-style-vulnerabilities.md | draft | MCP server taint-style vulns + SpellSmith description defense (2607.07461) |
| @concepts/cage-1-enterprise-agent-governance-eval.md | draft | CAGE-1 Prebind Assurance + 12-dimension enterprise agent eval (2607.03510) |
| @concepts/multilingual-long-horizon-agent-evaluation.md | draft | PolyWorkBench hybrid multilingual long-horizon agent eval (2607.06008) |
| @concepts/security-tool-orchestration-determinants.md | draft | Client is first-order (2.1× gap); reasoning-bound residuals — HexStrike study (2607.02873) |
| @concepts/crypter-as-a-service.md | draft | CraaS underground market — exploit.in longitudinal study (2606.24226) |
| @concepts/seclaw-agent-security-evaluation.md | draft | Trajectory-aware agent security eval — SeClaw methodology (Reference until code ships) |
| @concepts/agent-skill-injection.md | draft | K95 — skill injection + MalSkillBench/POISE + SPI + P3 memory gap (K114) |
| @concepts/context-fractured-decomposition-attacks.md | draft | CFD — artifact provenance gap jailbreaks across sessions/instances (2606.09084) |
| @concepts/mcp-security-posture.md | validated | K100 — MCP admission, DCI, SPI, WebMCP MSTI, VATS, GT-MCP trajectory (2606.10322) |
| @sources/arxiv-2608-12880-labels-not-endpoints.md | draft | Labels ≠ endpoints in MCP security eval (2608.12880; CCC K277) |
| @concepts/measurement-integrity-mcp-security-eval.md | draft | Bind treatment/behavior/authorization/outcome/unit before ASR claims |
| @sources/arxiv-2608-13030-intersage.md | draft | InterSAGE trust-native IoA protocol (2608.13030; CCC K278) |
| @concepts/intersage-trust-native-ioa-protocol.md | draft | Agent Identity Card + monotonic capability attenuation |
| @concepts/agentic-containment-principles.md | draft | K114 — P1–P6 containment matrix; LangChain/AutoGPT/OpenAI SDK audit |
| @concepts/neuro-symbolic-auditable-reasoning.md | validated | K100 — NeuroLog-style Datalog+SMT auditable vuln chains |
| @concepts/blockchain-security.md | draft | Smart-contract + DeFi security |
| @concepts/metaverse-security.md | draft | VR / AR / immersive platform risk |
| @concepts/game-hacking.md | draft | Anti-cheat RE practice; HWID map on hardware-bound-identity |
| @concepts/zero-trust.md | draft | Identity-centric defense architecture |
| @concepts/cyberwarfare.md | draft | Nation-state cyber operations |
| @concepts/anonymity-networks.md | draft | Tor + I2P; hardware IDs are a separate plane |
| @sources/arxiv-2608-06581-whitenet-spectral-whitening.md | draft | WhiteNet channel-robust overlapping 802.11 protocol ID (2608.06581; K274) |
| @concepts/spectral-whitening-wireless-protocol-id.md | draft | Spectral whitening removes the channel envelope for RF protocol classification |
| @sources/arxiv-2608-11337-association-privacy-wireless-formal.md | draft | Association inference / allowlist side-channel privacy (2608.11337; K275) |
| @concepts/association-inference-attack-wireless.md | draft | Allowlist + replay/relay tracking; Tamarin-verified mitigation |
| @sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md | draft | Tutor withhold supervisor + evidence-driven Socratic tuning (2608.12292; K276) |
| @concepts/refusal-under-knowledge-withhold-contract.md | draft | Per-turn machine-checkable withhold contracts for LLM agents |
| @sources/arxiv-2608-12311-rsm-role-specialization.md | draft | RSM multi-tool role coordination in agentic SE (2608.12311; K277) |
| @concepts/role-specialization-multi-tool-coordination.md | draft | Explicit tool responsibility domains + role-drift detection |
| @sources/arxiv-2608-12996-atobench-deceptive-observations.md | draft | ATOBench deceptive-observation verification eval (2608.12996; K278) |
| @concepts/atobench-verification-chain-deception.md | draft | Verification-chain evaluation under deceptive target observations |
| @sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md | draft | MARC v1 clinical multi-agent orchestration (2608.13476; K279) |
| @concepts/deterministic-multi-agent-orchestration-failure-attribution.md | draft | Deterministic staged orchestration + failure attribution (MARC) |
| @sources/arxiv-2608-13496-yavin-secure-edge-pim-tee.md | draft | YAVIN unified TEE + PIM secure edge (2608.13496; K280) |
| @concepts/pim-tee-untrusted-memory-bus.md | draft | TEE trust boundary vs processing-in-memory (untrusted bus) |
| @entities/tools/ente.md | draft | ente E2EE cloud (photos/auth/locker) — Atto steal (K281) |
| @concepts/e2ee-consumer-cloud-threat-model.md | draft | E2EE consumer-cloud threat model: recovery/share/metadata |
| @sources/arxiv-2608-13463-ood-mllm-routed-ensembles.md | draft | OOD MLLM-routed ensembles (2608.13463) → image-gen |
| @sources/arxiv-2608-12290-ood-i2v-agentic-optimization.md | draft | OOD I2V agentic optimization (2608.12290) → image-gen |
| @sources/arxiv-2608-13069-ood-behavioral-reprogramming.md | draft | OOD behavioral reprogramming (2608.13069) → image-gen |

### Education + ethics

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/cyber-for-kids.md | draft | Parent + teacher + LE-facing kid-safety material |

---
- [chekusu/mails — AI email parsing, dual-use phishing-domain enumeration](concepts/2026-05-13_chekusu-mails-dual-use.md) — cross-wiki stub routed from ingest — `cross-wiki`

## Entities

### Frameworks

| Page | Maturity |
|------|----------|
| @entities/frameworks/mitre-attack.md | validated |
| @entities/frameworks/cyber-kill-chain.md | validated |

### Certifications

| Page | Maturity | Vendor |
|------|----------|--------|
| @entities/certifications/oscp.md | draft | Offensive Security |
| @entities/certifications/oswa.md | draft | Offensive Security |
| @entities/certifications/oswe.md | draft | Offensive Security |
| @entities/certifications/crto.md | draft | Zero-Point Security |
| @entities/certifications/ceh.md | draft | EC-Council |
| @entities/certifications/comptia-security-plus.md | draft | CompTIA |
| @entities/certifications/comptia-pentest-plus.md | draft | CompTIA |
| @entities/certifications/ecppt.md | draft | eLearnSecurity / INE |
| @entities/certifications/ecptx.md | draft | eLearnSecurity / INE |
| @entities/certifications/ewpt.md | draft | eLearnSecurity / INE |

### Tools

| Page | Maturity | Role |
|------|----------|------|
| @entities/tools/cobalt-strike.md | draft | Commercial C2 |
| @entities/tools/metasploit.md | draft | FOSS exploitation framework |
| @entities/tools/burp-suite.md | draft | Web-app testing proxy |
| @entities/tools/caldera.md | draft | Adversary emulation automation |
| @entities/tools/maltego.md | draft | OSINT graph analysis |
| @entities/tools/wazuh.md | draft | FOSS SIEM / host-IDS |
| @entities/tools/nmap.md | draft | Network scanner |
| @entities/tools/rustscan.md | draft | Fast port-scan front-end to nmap (OSINT K237; owned-lab only) |
| @entities/tools/cyberscraper-2077.md | draft | LLM-assisted scraper — OSINT clone; cyber awareness, no second tree |
| @entities/tools/bloodhound.md | draft | AD attack-path graph |
| @entities/tools/bloodbash.md | draft | Offline SharpHound/AzureHound JSON (K242 Extract; OSINT shelf) |
| @entities/tools/bbot.md | draft | Recursive recon scanner (K241 AGPL Extract; no Atto vendor) |
| @entities/tools/battleye.md | draft | Third-party kernel AC (BEDaisy/BEService/BEClient) — REFERENCE |
| @entities/tools/easy-anti-cheat.md | draft | Epic kernel AC (demand-start) — REFERENCE |
| @entities/tools/riot-vanguard.md | draft | Riot AC; boot-start or On-Demand (TPM EK + attestation) — not DFIR `vanguard` |
| @entities/tools/denuvo.md | draft | Irdeto anti-tamper / kernel AC — REFERENCE |
| @entities/tools/kali-linux.md | draft | Pentest Linux distribution (OffSec, 600+ tools) |
| @entities/tools/atobench.md | draft | ATOBench deceptive-observation eval (REFERENCE; K278) |
| @entities/tools/marc-v1.md | draft | MARC v1 clinical multi-agent framework (GO clone; K279) |
| @entities/tools/grapheneos.md | draft | Hardened AOSP on Pixels (relock verified boot; not Play Integrity STRONG) |
| @entities/tools/qubes-os.md | draft | Xen compartmentalization desktop (contain compromise; not a phone) |
| @entities/tools/multi-cloud-red-team.md | draft | Multi-cloud red team operations (AWS/Azure/GCP) |
| @entities/tools/cua.md | validated | Agent-VM sandbox (Apple Virtualization + Lume) |
| @entities/tools/fuzzyai.md | validated | LLM adversarial fuzz framework (CyberArk, Apache-2.0) |
| @entities/tools/blast-radius-necrophoresis.md | draft | Blast Radius / NECROPHORESIS (REFERENCE; no public code) |
| @entities/tools/shieldai-risk-taxonomy-mapping.md | draft | ShieldAI tool×taxonomy matrices (Apache-2.0 ~896KB) |
| @entities/tools/aha-auto-research-red-teaming.md | draft | AHA autoresearch prod-agent red-team + VCG (MIT; CONDITIONAL-GO lab) |
| @entities/tools/datashield.md | draft | DataShield risky FT filter (MIT; CONDITIONAL-GO ~3MB) |
| @entities/tools/ifixai.md | draft | Agent deception/manipulation diagnostic harness — Adopt (K142) |
| @entities/tools/pentest-ai-agents.md | validated | LLM-driven red-team automation (MIT) |
| @entities/tools/cyberstrike.md | draft | AI offensive harness — AGPL, CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02) |
| @entities/tools/strix.md | draft | Autonomous AI pentest agents — Apache-2.0, Docker sandbox (CONDITIONAL-GO Phase-0) |
| @entities/tools/strix-omlx.md | draft | Strix → OMLX/Ollama/SGLang wrapper — Apache-2.0 CONDITIONAL-GO clone |
| @entities/tools/hexstrike-ai.md | draft | HexStrike MCP 150+ tools — MIT REFERENCE (desk Phase-0) |
| @entities/tools/cai-framework.md | draft | Alias CAI multi-agent — dual-license REFERENCE (no clone) |
| @entities/tools/pentestgpt.md | draft | PentestGPT USENIX agent — MIT REFERENCE |
| @entities/tools/ollama.md | draft | Local LLM runtime — simple pull/run + API (Linux + Apple Silicon) |
| @entities/tools/vllm.md | draft | High-throughput OpenAI-compatible LLM serving (NVIDIA) |
| @entities/tools/pydns-scanner.md | validated | DNS server discovery (ethical-use addendum) |
| @entities/tools/jadx-mcp-server.md | draft | Android RE + live debugging via MCP (JADX decompiler) |
| @entities/tools/osmedeus.md | draft | Orchestration engine for security scanning (recon/scan YAML workflows) |
| @entities/tools/splunk.md | validated | Commercial SIEM / SPL — 110-query detection catalog + SPL command reference + 24 SOC-2 use cases |
| @entities/tools/qradar.md | validated | IBM commercial SIEM — architecture/components/databases/EPS+FPM licensing/coalescing/CRE/superflows (Kothekar 2023 Ch 1-4 deep-read; Ch 5-12 deferred) |
| @entities/tools/sysmon.md | draft | Microsoft Sysinternals — high-fidelity Windows event log (process/network/registry/WMI) |
| @entities/tools/gau.md | draft | Multi-provider known-URL discovery — OTX / Wayback / Common Crawl (MIT, Go; Adopt) |
| @entities/tools/katana.md | draft | Scriptable web crawler with headless-browser mode (MIT, Go; ProjectDiscovery; Adopt) |
| @entities/tools/gopacket.md | draft | Go packet-decoding library for network analysis (Apache-2.0, Mandiant; Steal-from) |
| @entities/tools/openvpn-install.md | draft | Bash OpenVPN deployment automation — NAT / IPv6-routing logic (Unlicense; Steal-from) |
| @entities/tools/vpn-self-hosted.md | draft | VPN hub page — WireGuard, OpenVPN, wg-easy, PiVPN, Tailscale catalog + decision matrix |
| @entities/tools/defenseclaw.md | draft | Enterprise AI security governance — MCP/skill scanners + Codex sidecar observe (Apache-2.0; ADOPTED laptop) |
| @entities/tools/deepzero.md | draft | Windows kernel-driver vuln research pipeline — PE→Ghidra→Semgrep→LLM (MIT) |
| @entities/tools/grex.md | draft | Regex generation from test cases — SOC/IR log parsing (Apache-2.0) |
| @entities/tools/vanguard.md | draft | Single-binary DFIR toolkit — Velociraptor+Volatility+KAPE+YARA, 28 MITRE-mapped (MIT) |
| @entities/tools/raptor.md | draft | Claude Code offensive/defensive agent — Semgrep+CodeQL (Steal-from, no license) |
| @entities/tools/src-hunter-skill.md | draft | Claude Code bug-bounty/pentest skill — 305 payloads, 19 playbooks, 263 WAF bypasses (MIT) |
| @entities/tools/bluehood.md | draft | Bluetooth telemetry monitoring — BLE MAC correlation (MIT, Steal-from) |
| @entities/tools/super-spr.md | draft | Zero-trust networking — per-device DNS, VLAN segregation in Go (BSD-3-Clause) |
| @entities/tools/reconftw.md | draft | Apex recon automation — subdomain+web+vulns+osint+Axiom fleet distribution (MIT, 7.5k stars) |
| @entities/tools/evilsocket-audit.md | draft | 8-stage vuln-discovery agent — Glasswing pattern, reachability gating (MIT) |
| @entities/tools/offensive-claude.md | draft | Offensive-security Claude Code workstation — 25 skill modules, 8 classifications |
| @entities/tools/reverse-skill.md | draft | MIT skill router pack for authorized pentest methodology routing (K129) |
| @entities/tools/cf-hero.md | draft | Cloudflare origin-IP discovery via DNS + Shodan hashing (Go, ~2.4k stars) — Defer pending LICENSE audit |
| @entities/tools/cloakquest3r.md | draft | Origin-IP behind Cloudflare-like proxies (MIT; K220; peer CF-Hero) |
| @entities/tools/damn-vulnerable-drone.md | draft | Intentional ArduPilot/MAVLink drone hacking lab (MIT; K220) |
| @entities/tools/hacktools.md | draft | Offensive browser-extension cheatsheet (license NOT FOUND; K220) |
| @entities/tools/raccoon.md | draft | Offensive recon / vuln scanner (MIT; K220) |
| @entities/tools/black-cat.md | draft | Hypothesis-ledger Claude Code red-team skill — Steal-from, no clone (null SPDX; K220) |
| @entities/tools/bypassav.md | draft | AV/EDR bypass technique mindmap → av-edr-bypass (null SPDX; K220) |
| @entities/tools/torbot.md | draft | Dark-web OSINT crawler — GPL-3 Reference-only (K220) |
| @entities/tools/pentest-ai.md | draft | MCP offensive-security server — 205 tools, 17 agents, MIT (`ptai` CLI; distinct from pentest-ai-agents) |
| @entities/tools/nidhogg.md | draft | Windows kernel rootkit reference — DKOM/ActiveProcessLinks tradecraft (GPL-3.0; Steal-from, no deploy) |
| @entities/tools/iron-proxy.md | draft | Egress firewall for untrusted workloads (Apache-2.0; Adopt-eligible Phase-0) |
| @entities/tools/cryptex-oss.md | draft | LLM red-teaming transforms/mutators toolkit — 162 transforms (MIT; Adopt-eligible Phase-0) |
| @entities/tools/cve-mcp-server.md | draft | Security-intel MCP server — CVE/EPSS/KEV/ATT&CK enrichment (Apache-2.0; CONDITIONAL-GO) |
| @entities/tools/autosut.md | draft | STIX environment-semantics gap measurement for adversary emulation (Reference) |
| @entities/tools/cav-stixgen.md | draft | CAV CVE→STIX benchmark (figshare REFERENCE; no local clone) |
| @entities/tools/swe-pruner-pro.md | draft | SWE-Pruner Pro (Apache-2.0 pyproject; CONDITIONAL-GO ~8.7MB) |
| @entities/tools/senthex-research.md | draft | Senthex RELAY/ATLAS harness (MIT; GO ~672KB) |
| @entities/tools/oc-grpo.md | draft | OC-GRPO (Apache-2.0; GO ~24MB) |
| @entities/tools/ai-redteam-evidential-limits.md | draft | Evidential-ceiling math (MIT; GO ~528KB) |
| @entities/tools/vulncare.md | draft | VulnCare K8s remediation lab (Apache-2.0; GO ~2.6MB) |
| @entities/tools/kutie-artifacts.md | draft | KuTIE artifacts (Dynatrace lab CONDITIONAL ~2.9MB) |
| @entities/tools/inferscale.md | draft | InferScale KV injection (BSD-3; GO ~1.4MB) |
| @entities/tools/system-prompt-index.md | draft | SystemPromptIndex AISPA corpus (REFERENCE; NO LICENSE) |
| @entities/tools/cweep.md | draft | CWEEP RTL CWE lint (Apache-2.0; CONDITIONAL-GO ~15MB) |
| @entities/tools/openart.md | draft | OpenART agent RT arena (AGPL-3.0; CONDITIONAL-GO ~19MB) |
| @entities/tools/piminer.md | draft | PIMiner PI red team (MIT; CONDITIONAL-GO ~28MB) |
| @entities/tools/llms-agents-smartgrids-code.md | draft | Smart-grid agents code (NO LICENSE — REFERENCE) |
| @entities/tools/malskillbench.md | draft | Runtime-verified malicious agent skills benchmark — CI/PI detector eval (Reference) |
| @entities/tools/sevra-bench.md | draft | Malicious PR benchmark for LLM review agents — inspect_ai + Gitea (Reference) |
| @entities/tools/nvidia-skillspector.md | draft | Agent/MCP skill supply-chain scanner — prompt injection + tool poisoning (Apache-2.0; Adopt) |
| @entities/tools/netviz.md | draft | Browser network-architecture graph visualizer — D3.js + Socket.IO (MIT; Adopt, K93) |
| @entities/tools/airguard.md | draft | Runtime authority control for tool/MCP agents (MIT; CONDITIONAL-GO) |
| @entities/tools/chaincaps.md | draft | MCP proxy — composition-safe tool chains via monotonic capability budgets (Reference) |
| @entities/tools/handle-capability-protocol.md | draft | HCP reference runtime — MCP execution-control invariants + 10-case benchmark (MIT; CONDITIONAL-GO) |
| @entities/tools/spellsmith.md | draft | MCP taint mitigation via security-aware tool descriptions + reflection (Reference; 2607.07461) |
| @entities/tools/agentredguard.md | draft | Integration-aware guard for SaaS LLM agents — AgentRedBench paper (Reference) |
| @entities/tools/seclaw-eval.md | draft | Trajectory-aware agent security benchmark — SeClaw Docker testbed (Reference, K98) |
| @entities/tools/ai-research-skills.md | draft | Orchestra ML skills library — cybersec cherry-pick subset (K113 CONDITIONAL-GO) |
| @sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md | deep-read | K113 cross-wiki brief ingest |
| @entities/tools/llm-defense-lattice.md | draft | OWASP LLM Top 10 defense attribution — BAS lattice + 17-probe corpus (Reference) |
| @entities/tools/defending-code-reference-harness.md | draft | Anthropic Docker/gVisor vuln-discovery reference harness — K102 CONDITIONAL-GO |

### Vendors

| Page | Maturity |
|------|----------|
| @entities/vendors/offensive-security.md | draft |
| @entities/vendors/elearnsecurity.md | draft |
| @entities/vendors/comptia.md | draft |
| @entities/vendors/ec-council.md | draft |
| @entities/vendors/zeropoint-security.md | draft |

### Platforms (labs / CTF)

| Page | Maturity |
|------|----------|
| @entities/platforms/hackthebox.md | draft |
| @entities/platforms/polyworkbench.md | draft | Multilingual long-horizon workplace agent benchmark (Reference; 2607.06008) |

### Programming languages

| Page | Maturity | Role |
|------|----------|------|
| @entities/programming-languages/python.md | draft | Scripting + automation |
| @entities/programming-languages/c.md | draft | Exploit dev + AV/EDR bypass |
| @entities/programming-languages/javascript.md | draft | Web exploitation + Node.js |
| @entities/programming-languages/powershell.md | draft | Windows post-exploitation |

### Threat actors

| Page | Maturity | Region |
|------|----------|--------|
| @entities/threat-actors/apt28.md | draft | Russia-attributed (GRU) |
| @entities/threat-actors/apt29.md | draft | Russia-attributed (SVR) |
| @entities/threat-actors/lazarus.md | draft | DPRK-attributed (RGB) |
| @entities/threat-actors/lockbit.md | draft | Criminal RaaS (Russian-language) |

### People

| Page | Maturity | Role |
|------|----------|------|
| @entities/people/joas-a-santos.md | validated | Corpus author |
| @entities/people/mostafa-yahia.md | draft | SOC analyst author (Yahia Packt 2023) |
| @entities/people/rajneesh-gupta.md | draft | SIEM / SOC 2 use-case author (@rajneeshcyber) |
| @entities/people/ashish-m-kothekar.md | draft | IBM SWAT/SME — author of *Building a Next-Gen SOC with IBM QRadar* (Packt 2023) |

---
- [xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)](entities/pydns-scanner-xullexer.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [0xSteph/pentest-ai-agents — shell-only Claude Code subagents for pentest workflows](entities/pentest-ai-agents-0xsteph.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [apktool-mcp-server — Android Reverse Engineering via MCP](entities/apktool-mcp-server.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [T-Pot — Multi-Honeypot Deception Framework](entities/tpotce.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Decepticon — Autonomous Red-Team Multi-Agent Framework](entities/decepticon.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Claude-Red — Offensive Security Skills Library for Claude Code](entities/claude-red-offensive-skills.md) — cross-wiki stub routed from ingest — `cross-wiki`

### Cross-wiki routed tool evaluations (index-only, no entity pages)

These tools surfaced from OSINT-wiki K-batch evaluations. Verdicts below reflect the eval tier at routing time. Re-verify license + maturity before adopting.

| Tool | License | Tier | Brief | Note |
|------|---------|------|-------|------|
| YellowKey | MIT | Steal-from | K42 | Exploit PoC harness — methodology reference |
| GreenPlasma | MIT | Steal-from | K42 | Exploit PoC harness — methodology reference |
| witr | — | Steal-from | K42 | Webhook + telemetry replay harness |
| autoharness | — | Steal-from | K42 | Fuzz-harness auto-generation pattern reference |
| cypht | — | Steal-from | K42 | Secure webmail — IR inbox isolation reference |
| awesome-codex-subagents | — | Reference | K42 | Curated subagent prompt list |
| claude-code-telegram | — | Steal-from | K42 | Sandbox-hardening pattern for chatops |
| frona | BSL-1.1 | Reject (until 2029) | K42 | Policy-driven syscall filtering — methodology reference only |
| Threat-Intel SaaS cluster (9) | closed-source | Reject | K42 | Shodan/FullHunt/ONYPHE/SOCRadar/Pulsedive/IntelX/Hunter.io/PublicWWW/Coalitioninc — batch-rejected |
| Claude Code Agent Farm | MIT | Steal-from | K15 | Parallel tmux orchestration — lock-based concurrency + heartbeat for network enumeration |
| MyIP DNS Leak Detection | MIT | Steal-from | K15 | WebRTC STUN leak detection, DNS exit endpoint identification — VPN/tunnel validation |
| fingerprint-suite | Apache-2.0 | Cross-ref | K15 | Browser fingerprint generation/injection — primary fit osint-wiki. Red-team browser evasion reference |
| netviz | MIT | Adopt | K53, K93 | @entities/tools/netviz.md — browser network graph visualizer (upgraded from Steal-from) |
| iOS-pentest-list | — | Reference | K53 | Curated Markdown list of iOS pentest tools |
| opendrop | TBD | Defer | K51 | Reverse-engineered Apple AirDrop (Python, 9.6k stars, SEEMOO lab) — license audit pending |
| Shells-X | TBD | Defer | K51 | Modular single-file PHP web-shell framework — license audit pending |
| AgentGym-RL | TBD | Defer | K51 | RL framework for LLM agent training — academic, license unverified |
| Grafana-Final-Scanner | TBD | Defer | K51 | Multi-source Grafana version fingerprinting + CVE checking — license unverified |
| fd | MIT+Apache-2.0 | Adopt-eligible | K51 | Rust `find` replacement, 43k stars — eval wrongly rejected; license verified clean |
| TruffleHog | AGPL-3.0 | Reject (copyleft) | K54 | Credential scanner, 26k stars — reference-only due to AGPL poison pill |
| gitGraber | GPL-3.0 | Reject (copyleft) | K54 | Real-time GitHub credential-leak monitor — reference-only |
| H4X-Tools | GPL-3.0 | Reject (copyleft) | K54/K55 | OSINT/recon/scraping toolkit — reference-only |
| VulnWeb directory | — | Reference | K54 | Directory of OWASP initiatives (GenAI Security, AI Exchange, CycloneDX) |
| Hackers-Arise MCP log | — | Reference | K54 | Educational blueprint for AI-assisted blue-team / MCP server boundary patterns |
| Windows-Use | MIT | Reference | K54 | GUI-level Windows automation agent — lateral-movement logic reference (primary fit: CCC wiki) |
| tugarecon | GPL-3.0 | Steal-from | K55 | Subdomain recon + Temporal Intelligence & Asset Memory module — impact-scoring algorithm extractable |
| hackingtool-plugin | NO LICENSE | Defer | K55 | 183 pentest+OSINT utilities integrated into Claude Code via C#/Docker — license+maturity recheck |
| osint_stuff_tool_collection | NO LICENSE | Reference | K55 | 7,875-star markdown index of OSINT tools — threat-actor-profiling subset |
| jhalon/reverse-engineering-protocols | — | Reference | K56 | Instructional curriculum on dissecting undocumented network protocols |
| LLM4Pentest catalog | — | Defer | K56, K55-2 | `simon-p-j-r/LLM4Pentest` — academic LLM-pentest survey; gh api NO LICENSE (2026-05-22) |
| Awesome-Hacking | CC0-1.0 | Reference | K55-2 | Aggregate awesome-list — gh-api cleared NO LICENSE false negative |
| open-source-web-scanners | Apache-2.0 | Reference | K55-2 | ZAP-lead-dev curated web-scanner index (also K57 reject as aggregate — license verified) |
| CF-Hero | — | Defer | K55-2 | @entities/tools/cf-hero.md — Cloudflare origin-IP unmasking |
| jadx-ai-mcp | Apache-2.0 | Cross-ref | K55-2 | Sibling to @entities/tools/jadx-mcp-server.md (`zinja-coder`, same MCP family) |
| Galaxy-Bugbounty-Checklist | — | Reject | K57 | NO LICENSE FOUND — methodology reference only |
| BugBounty-Recon-Methodology | — | Reject | K57 | Verify license before any adoption |
| sqlmap | NOASSERTION | Reject | K57 | Confirm AGPL/GPL before use — already cited in methodology pages, no entity |
| NoSQLMap | GPL-3.0 | Reject (copyleft) | K57 | Reference-only — same copyleft posture as gitGraber/H4X-Tools |
| KaliGPT | Custom NC | Reject (commercial) | K60 | Ollama terminal harness — **do not install on prod**; eval overturned Adopt |
| h4cker | MIT | Reference | K60 | Omar Santos mega-repo — OSINT tradecraft in `osint/` subtree (~26k stars) |
| pentest-ai | MIT | CONDITIONAL-GO | K60 | @entities/tools/pentest-ai.md — MCP + 17 agents; compare vs pentest-ai-agents |
| cyber-security-llm-agents | — | Defer | K60 | NVISO catalog — gh api NO LICENSE; reference until SPDX filed |
| Nidhogg | GPL-3.0 | Steal-from | K63 | @entities/tools/nidhogg.md — DKOM/process-hiding tradecraft for MITRE mapping; **no binary import** |
| facex | Apache-2.0 | Steal-from | K68 | WASM in-browser face stack + anti-spoof — extract ideas only, no full import |
| iron-proxy | Apache-2.0 | Adopt-eligible | K68 | @entities/tools/iron-proxy.md — egress firewall for untrusted workloads |
| centaur | NOASSERTION | Steal-from | K68 | Paradigm secure multi-agent host — read LICENSE text before any code use |
| cryptex-oss | MIT | Adopt-eligible | K68 | @entities/tools/cryptex-oss.md — LLM red-team transform/mutator catalog |
| ZishanAdThandar/pentest | GPL-3.0 | Reject | K68 | Pentest/bounty notes cheatsheets — keep out of IP-sale surfaces |
| bbot | AGPL-3.0 | Extract-only (copyleft) | K71, K73, K241 | `blacklanternsecurity/bbot` — AGPL isolate; OSINT shelf; **never vendor Atto/prod**; no mass internet scan |
| Hackers-Arise AI enumeration | — | Reference | K71 | AI-assisted enumeration article (no code); complements K54 Hackers-Arise MCP log row |
| cve-mcp-server | Apache-2.0 | CONDITIONAL-GO | K73 | @entities/tools/cve-mcp-server.md — workstation CVE/KEV/EPSS intel enrichment MCP |
| nvidia-skillspector | Apache-2.0 | Adopt | K88 | @entities/tools/nvidia-skillspector.md — agent/MCP skill supply-chain scanner |
| defenseclaw | Apache-2.0 | ADOPTED (observe) | K42, CCC | @entities/tools/defenseclaw.md — CLI scanners + Codex sidecar observe 2026-05-31; action/LLM judge optional |
| train-llm-from-scratch | MIT | Reference | K88 | LLM training reference only — not a security tool |
| linux-basics-for-hackers-notes | — | Reject | K88 | NO LICENSE FOUND — do not adopt |
| Graph-R1 | CC-BY-NC-SA (eval) | Reject | K88 | K88 eval reject; gh api reports MIT 2026-05-31 — verify LICENSE before override |
| seclaw-eval | — | Reference | K98 | @entities/tools/seclaw-eval.md — trajectory-aware agent security benchmark; **no LICENSE on GitHub API 2026-06-04** |
| sevra-bench | — | Reference | digest | @entities/tools/sevra-bench.md — LLM PR merge-gate eval; **no LICENSE on GitHub API 2026-06-16** |
| toolprivbench | — | Reference | digest | @entities/tools/toolprivbench.md — OPUR/PED least-privilege tool eval; **no LICENSE on GitHub API 2026-06-19** |
| leakbench-area | — | Reference | digest | @entities/tools/leakbench-area.md — LeakBench + AREA soft-prompt defense; **no LICENSE on GitHub API 2026-06-22** |
| clawaudit | — | CONDITIONAL-GO | digest | @entities/tools/clawaudit.md — OpenClaw runtime Semgrep/CodeQL audit; **no LICENSE on GitHub API 2026-06-24** |
| tool-guard | MIT | CONDITIONAL-GO | digest | @entities/tools/tool-guard.md — isolated planning vs cross-tool description poisoning (ICML 2026) |
| aohp | Apache-2.0 | CONDITIONAL-GO | digest | @entities/tools/aohp.md — AOSP agent-native OS harness (2606.23449) |
| toolbench-x | — | Reference | digest | @entities/tools/toolbench-x.md — tool-environment unreliability benchmark; **no LICENSE 2026-06-27** |
| defengraph | — | Reference | digest | @entities/tools/defengraph.md — KG+RAG blue-team assistant; no public repo 2026-06-23 |
| picalib-research | — | Reference | digest | @entities/tools/picalib-research.md — PI guard severity metric artifacts; **no LICENSE 2026-06-23** |
| ecc | MIT | Steal-from / CONDITIONAL-GO | digest | @entities/tools/ecc.md — cross-harness operator system; **ecc-agentshield** npm for config audit |
| skillgate | closed-source SaaS | Reference | digest | @entities/tools/skillgate.md — Mitiga free skill/hook/MCP config scanner |
| llm-defense-lattice | NOASSERTION | Reference | digest | @entities/tools/llm-defense-lattice.md — OWASP LLM Top 10 per-defense BAS lattice; license audit pending |
| defending-code-reference-harness | Apache-2.0 | Reference | K102 | @entities/tools/defending-code-reference-harness.md — Docker/gVisor agent vuln pipeline; laptop lab only |
| ai-infra-guard | Apache-2.0 + NOTICE §4(d) | CONDITIONAL-GO | digest | @entities/tools/ai-infra-guard.md — multi-layer agent red team (2606.31227); **external Docker only** |
| aha-auto-research-red-teaming | MIT | CONDITIONAL-GO | K176 | @entities/tools/aha-auto-research-red-teaming.md — VCG autoresearch for Claude Code/Codex (2607.11698); **lab sandbox only**; local clone ~169MB |
| datashield | MIT | CONDITIONAL-GO | K184 | @entities/tools/datashield.md — risky fine-tune filter (2607.15081); local clone ~3MB |
| cav-stixgen | — | Reference | K196 | @entities/tools/cav-stixgen.md — CAV CVE→STIX; figshare share unverified license |
| llm-research-competencies-zenodo | CC-BY-4.0 | Reference/ADOPT-ARTIFACT | digest | Zenodo 21313656 pack ~396KB at `raw-sources/repos/llm-research-competencies-zenodo` |
| swe-pruner-pro | Apache-2.0 (pyproject) | CONDITIONAL-GO | K200 | @entities/tools/swe-pruner-pro.md — ~8.7MB shallow; no LICENSE file |
| senthex-research | MIT | GO | K202 | @entities/tools/senthex-research.md — RELAY/ATLAS ~672KB |
| oc-grpo | Apache-2.0 | GO | K204 | @entities/tools/oc-grpo.md — ~24MB |
| ai-redteam-evidential-limits | MIT | GO | K220 | @entities/tools/ai-redteam-evidential-limits.md — ~528KB |
| vulncare | Apache-2.0 | GO | K224 | @entities/tools/vulncare.md — ~2.6MB |
| kutie-artifacts | Dynatrace proprietary | CONDITIONAL-GO | K224 | @entities/tools/kutie-artifacts.md — lab-view only ~2.9MB |
| InferScale | BSD-3-Clause | GO | K227 | @entities/tools/inferscale.md — ~1.4MB |
| SystemPromptIndex | — | REFERENCE | K232 | @entities/tools/system-prompt-index.md — NO LICENSE ~11MB |
| cweep | Apache-2.0 | CONDITIONAL-GO | K233 | @entities/tools/cweep.md — Verible RTL CWE lint ~15MB |
| OpenART | AGPL-3.0 | CONDITIONAL-GO | K237 | @entities/tools/openart.md — agent RT arena ~19MB lab only |
| PIMiner | MIT | CONDITIONAL-GO | K248 | @entities/tools/piminer.md — PI strategy-library RT ~28MB lab only |
| llms-agents-smartgrids-code | — | Reference | K199 | NO LICENSE — pattern only |
| handle-capability-protocol | MIT | CONDITIONAL-GO | digest | @entities/tools/handle-capability-protocol.md — HCP execution-control invariants + benchmark (2606.29073); 0★ reference runtime |

## Meta

| Page | Maturity | Role |
|------|----------|------|
| @meta/daily-research-digest-cadence.md | draft | Federated daily research digest — K93 install; outputs to `wiki/sweeps/` |

## Sources

282 source pages live in `sources/`:

- **226** from the Joas A Santos seed corpus (shared Drive folder `ebooks Joas`)
- **22** from the Redteam Kit shared Drive folder (English-language security books + field manuals)
- **26** from the BlueTeam Kit shared Drive folder (SOC / blue-team PDFs — SIEM, threat hunting, IR, EDR)
- **2** video courses (Kali Linux 2023 50-chapter set; Python Ethical Hacking MASTERCLASS 19-section set) — `.mp4` only, each catalogued as a single page

Source pages are not individually catalogued here; each entity and concept page lists the sources that synthesize into it under `related:`. Browse `sources/` directly for provenance lookups.

The corpus inventory (file ID + title for every PDF) lives at `.scratch/drive_inventory.tsv` (gitignored — see `ROADMAP.md` for the storage decision).

**Catalog status (decided 2026-05-16):** the `sources/` layer is a deliberate *reference catalog* of the two shared Drive folders. Every source page carries `read_status: unread-stub` because the PDFs live in external Drive folders not synced to this workspace — `unread-stub` is the expected steady state here, not a defect. A page graduates to `deep-read` only when the underlying PDF is obtained and read. Tooling that scores wiki health (e.g. `wiki_scan_all.py`) should treat this wiki's cited-unread-stub count as informational, not as a backlog to burn down.

---
- [tl;dr sec — [tl;dr sec] #335 - Prompt Injection as Role Confusion, PHP Ecosystem Security, New MCP Spec](sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Packt SecPro — Identity Became the New Perimeter](sources/substack-rss-secpro-2026-07-03-identity-became-the-new-perimeter.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [The Engineering Club — Security Edition — How I’d Respond in the First Hour After a Package I Use Got Hacked](sources/substack-rss-seceng-weekly-2026-07-06-how-id-respond-in-the-first-hour-after-a-package.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Firewall3D: Hardware Firewall for Defending 3D Printers Against Firmware Attacks](sources/2026-asgar-firewall3d-firmware-hardware.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Optimistic Verifiable Claims — confidential G-code bidding (arXiv:2607.25517)](sources/2026-corn-optimistic-verifiable-claims.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [GitHub — CyberStrikeus/CyberStrike (AI offensive harness)](sources/github-cyberstrike.md) — Phase-0 2026-08-02 · AGPL · CONDITIONAL-GO lab/VM
- [OWASP ASVS 5.0.0](sources/owasp-asvs-5.md) — product verification standard (2025-05-30)
- [Penligent — Bug Bounty Hunter Software in 2026](sources/penligent-bug-bounty-hunter-software-2026.md)
- [Rizvi — Automating Bug Bounty Recon in 2026](sources/rizvi-automating-bug-bounty-recon-2026.md)
- [GitHub — usestrix/strix](sources/github-strix.md) — Apache-2.0 AI pentest agents · Phase-0 CONDITIONAL-GO 2026-08-02
- [GitHub — sw30labs/strix-omlx](sources/github-strix-omlx.md) — Strix → OMLX/Ollama · Phase-0 CONDITIONAL-GO clone 2026-08-02
- [GitHub — 0x4m4/hexstrike-ai](sources/github-hexstrike-ai.md) — HexStrike MCP · desk REFERENCE 2026-08-02
- [GitHub — aliasrobotics/cai](sources/github-cai-framework.md) — CAI dual-license · REFERENCE no-clone
- [GitHub — GreyDGL/PentestGPT](sources/github-pentestgpt.md) — MIT research agent · REFERENCE
- [OSINT K220 cyber/agent-harness eval](sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md) — cross-wiki tool register (CloakQuest3r / Black-cat / Raccoon / DVD / …)
- [GitHub — tcpiplab/AblitaFuzzer](sources/github-ablitafuzzer.md) — abliterated local attacker LLM pattern
- [DEV — Red Team AI Benchmark](sources/devto-red-team-ai-benchmark.md) — refusal-free ≠ accurate quiz methodology
- [SLM ensemble malware orchestration](concepts/slm-ensemble-malware-analysis-orchestration.md) — CCC cross-wiki
- [ChainWatch MCP kill-chain detection](concepts/chainwatch-mcp-kill-chain-detection.md) — CCC cross-wiki
- [arXiv ChainWatch MCP sequential detection](sources/arxiv-chainwatch-mcp-sequential-detection-2607.19432.md) — CCC cross-wiki stub
- [GrapheneOS features](sources/grapheneos-features.md) — first-party hardening beyond AOSP 16
- [GrapheneOS FAQ](sources/grapheneos-faq.md) — Pixel-only production; relock required
- [Qubes OS intro](sources/qubes-os-intro.md) — Xen qubes; assume software will be exploited
- [Whonix About](sources/whonix-about.md) — Gateway + Workstation, all traffic via Tor
- [Whonix vs Kicksecure](sources/kicksecure-vs-whonix.md) — hardening vs forced-Tor anonymity

## Cross-wiki anchors

When this wiki references a sibling wiki's page, the citation uses `@<alias>/path/to/page.md`. Aliases:

- `osint-wiki` — financial / quant / prediction-market research
- `image-gen-wiki` — uncensored image generation, ComfyUI, LoRA
- `seo-wiki` — local SEO, GBP, GEO/AEO, web design
- `3d-printing-wiki` — FDM/FFF, Bambu, slicers, print farms

Bidirectional invariant: if this wiki cites `@osint-wiki/...`, the matching page in the OSINT wiki should cite `@cybersecurity-wiki/...` back. Run `python3 scripts/wiki_lint.py` to check.
