from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "scripts/k373_agent_trace_tampering_precheck.py").read_text()

def write(dest, kid, doc, checks, canon, st):
    t = TEMPLATE
    t = t.replace("K373 advisory precheck — agent execution trace tampering / logging integrity audit.", doc)
    t = t.replace("K373 agent trace tampering — advisory checklist", kid + " — advisory checklist")
    t = t.replace("agent-execution-trace-tampering-audit", canon)
    t = t.replace("OK k373_agent_trace_tampering_precheck selftest", st)
    old = '''CHECKS = (
    ("written_scope", "Written scope for harness trace-tampering eval on owned lab?"),
    ("oob_logging", "Plan independent append-only trace capture outside agent write path?"),
    ("harness_named", "Name harness, model, and whether eval is self-request vs external attacker?"),
    ("integrity_checks", "Include hash/signature or WORM storage for audit logs?"),
    ("faithful_asr", "Do not treat trajectory self-report as verification (pairs K271/K278)?"),
    ("no_wiki_payloads", "No trace-deletion playbooks or tamper PoCs in wiki?"),
)'''
    new = "CHECKS = (\n" + ",\n".join('    ("%s", "%s")' % c for c in checks) + ",\n)"
    t = t.replace(old, new)
    (ROOT / "scripts" / dest).write_text(t)
    (ROOT / "scripts" / ("test_" + dest)).write_text(
        "#!/usr/bin/env python3\nimport subprocess, sys\nsubprocess.check_call([sys.executable, 'scripts/%s', 'selftest'])\n" % dest
    )

write("k375_agentxploit_precheck.py", "K375", "K375 advisory precheck — AgentXploit repo-to-runtime agent audit.",
      [("written_scope","Written scope for repo-to-runtime agent audit?"),("attacker_interface","Document task-defined attacker interface?"),("external_verifier","External verifier confirms outcomes?"),("runtime_sandbox","Isolated runtime (not prod)?"),("faithful_asr","Report ASR with harness and verifier tuple?"),("no_wiki_payloads","No exploit payloads in wiki?")],
      "agentxploit-repository-runtime-red-teaming", "OK k375_agentxploit_precheck selftest")
write("k376_fragtoken_precheck.py", "K376", "K376 advisory precheck — FragToken inference cost abuse lab.",
      [("written_scope","Authorized lab only?"),("cost_metrics","Measure cost tier, latency, and token stats?"),("benign_mix","Include benign traffic mix?"),("sandbox","Owned endpoint or vendor test account?"),("no_wiki_payloads","No FragToken payloads in wiki?")],
      "fragtoken-inference-cost-amplification-lab", "OK k376_fragtoken_precheck selftest")
write("k377_system_prompt_corpus_precheck.py", "K377", "K377 advisory precheck — system prompt corpus audit.",
      [("provenance","Tag leaked vs official vs reconstructed prompts?"),("block_class","Classify tool/protocol vs safety blocks?"),("not_conscience","Prompt text is not runtime proof?"),("executable_controls","Pair with deny/grants (K303/K314)?"),("no_secrets","Redact secrets in leaked prompts?")],
      "llm-system-prompt-corpus-audit", "OK k377_system_prompt_corpus_precheck selftest")
print("done")
