#!/usr/bin/env python3
import subprocess, sys
subprocess.check_call([sys.executable, 'scripts/k377_system_prompt_corpus_precheck.py', 'selftest'])
