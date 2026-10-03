#!/usr/bin/env python3
"""Run a command fully detached: new session (setsid), own process group, stdio redirected.

macOS has no setsid(1). os.setsid() in the child detaches it from the launching
terminal's session and process group, which is what survives when the launching
command exits -- plain nohup+disown only reparents to launchd and leaves the
process in the original process group.

usage: daemonize.py <stdout-file> <stderr-file> <cmd> [args...]
Exit status is the daemonize call itself, not the child.
"""
from __future__ import annotations

import os
import sys


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    out_path, err_path, cmd = sys.argv[1], sys.argv[2], sys.argv[3:]

    pid = os.fork()
    if pid > 0:
        return 0  # parent returns immediately; child carries on

    os.setsid()  # new session + process group: survives the launching shell

    pid = os.fork()
    if pid > 0:
        os._exit(0)  # first child exits so the daemon is not a session leader

    os.chdir(os.environ.get("DAEMON_CWD", os.getcwd()))
    os.umask(0o22)

    devnull = os.open(os.devnull, os.O_RDONLY)
    out_fd = os.open(out_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    err_fd = os.open(err_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    os.dup2(devnull, 0)
    os.dup2(out_fd, 1)
    os.dup2(err_fd, 2)
    for fd in (devnull, out_fd, err_fd):
        if fd > 2:
            os.close(fd)

    os.execvp(cmd[0], cmd)
    os._exit(127)


if __name__ == "__main__":
    raise SystemExit(main())
