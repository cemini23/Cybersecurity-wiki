#!/usr/bin/env python3
"""Unit tests for K303 deny + K298 secret_grant (no extra deps)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import k303_k298_policy as policy  # noqa: E402


class PathPolicyTests(unittest.TestCase):
    def test_deny_dotenv(self):
        self.assertTrue(policy.is_secret_path(str(ROOT / ".env")))
        self.assertTrue(policy.is_secret_path("/tmp/.env.production"))

    def test_allow_example(self):
        self.assertFalse(policy.is_secret_path(str(ROOT / ".env.example")))

    def test_deny_ssh_key(self):
        self.assertTrue(policy.is_secret_path(str(Path.home() / ".ssh/id_ed25519")))
        self.assertFalse(policy.is_secret_path(str(Path.home() / ".ssh/id_ed25519.pub")))


class CommandPolicyTests(unittest.TestCase):
    def test_deny_cat_env(self):
        self.assertTrue(policy.is_secret_command("cat .env"))
        self.assertTrue(policy.is_secret_command("head -n 20 ./.env"))

    def test_allow_example_and_lint(self):
        self.assertFalse(policy.is_secret_command("cat .env.example"))
        self.assertFalse(policy.is_secret_command("python3 scripts/wiki_lint.py"))
        self.assertFalse(policy.is_secret_command("git status"))

    def test_allow_grant_wrapper(self):
        self.assertFalse(
            policy.is_secret_command("python3 scripts/secret_grant.py -- env")
        )

    def test_deny_printenv_key(self):
        self.assertTrue(policy.is_secret_command("printenv BRAVE_API_KEY"))
        self.assertTrue(policy.is_secret_command("printenv"))
        self.assertTrue(policy.is_secret_command("env"))

    def test_allow_git_commit_mentioning_dotenv(self):
        self.assertFalse(
            policy.is_secret_command(
                'git commit -m "hooks now block .env and key files from the planner"'
            )
        )
        self.assertTrue(policy.is_secret_command("git commit -m x; cat .env"))
        self.assertTrue(policy.is_secret_command("git add .env"))


class HookPayloadTests(unittest.TestCase):
    def test_before_read_file_deny(self):
        perm, _ = policy.decide(
            {
                "hook_event_name": "beforeReadFile",
                "file_path": str(ROOT / ".env"),
                "content": "SHOULD_NOT_MATTER=1",
            }
        )
        self.assertEqual(perm, "deny")

    def test_before_read_example_allow(self):
        perm, _ = policy.decide(
            {
                "hook_event_name": "beforeReadFile",
                "file_path": str(ROOT / ".env.example"),
                "content": "BRAVE_API_KEY=",
            }
        )
        self.assertEqual(perm, "allow")

    def test_shell_deny(self):
        perm, _ = policy.decide(
            {"hook_event_name": "beforeShellExecution", "command": "cat .env", "cwd": str(ROOT)}
        )
        self.assertEqual(perm, "deny")

    def test_hook_json_roundtrip(self):
        payload = json.dumps({"file_path": "/x/.env", "hook_event_name": "beforeReadFile"})
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/k303_k298_policy.py"), "--hook"],
            input=payload,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        out = json.loads(proc.stdout)
        self.assertEqual(out["permission"], "deny")
        self.assertNotIn("SHOULD", proc.stdout)


class SecretGrantTests(unittest.TestCase):
    def test_redacts_child_stdout(self):
        with tempfile.TemporaryDirectory() as tmp:
            envf = Path(tmp) / ".env"
            envf.write_text("UNITTEST_GRANT_SECRET=s3cretVALUE99\n", encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/secret_grant.py"),
                    "--env-file",
                    str(envf),
                    "--",
                    sys.executable,
                    "-c",
                    "import os; print(os.environ.get('UNITTEST_GRANT_SECRET',''))",
                ],
                cwd=tmp,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0)
            self.assertIn("***REDACTED***", proc.stdout)
            self.assertNotIn("s3cretVALUE99", proc.stdout)
            self.assertNotIn("s3cretVALUE99", proc.stderr)


class RestoreCheckTests(unittest.TestCase):
    def test_check_current_tree(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/restore_cybersec_dual_id.py"), "--check"],
            cwd=str(ROOT),
            text=True,
            capture_output=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
