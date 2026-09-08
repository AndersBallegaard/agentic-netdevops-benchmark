#!/usr/bin/env python3
"""Push a batch of VyOS configuration commands to a device over SSH.

Uses pexpect to drive an interactive vbash session, which is the only
reliable non-interactive way to enter VyOS config mode (piped stdin is
swallowed by vbash's readline and multi-command -c strings are rejected).

Usage: python3 vyos_push.py <host-fqdn> <commands-file>
       python3 vyos_push.py --all <prefix-stem>   # e.g. /tmp/vyos{}.cmds
"""
import sys
import pexpect

PROMPTS = [r"vyos@\S+[:~#$][#$]?\s*$", r"vbash\S*\$\s*$", r"\$\s*$", r"#\s*$"]


def run(host: str, cmds: list[str]) -> str:
    child = pexpect.spawn(
        f"ssh -o StrictHostKeyChecking=accept-new vyos@{host}",
        encoding="utf-8", timeout=60,
    )
    child.expect(PROMPTS)
    child.sendline("vbash -i")
    child.expect(PROMPTS)
    child.sendline("configure")
    for c in cmds:
        child.sendline(c)
        i = child.expect(PROMPTS + [r"Invalid", r"Error"])
        if i >= len(PROMPTS):
            raise RuntimeError(f"{host}: command failed: {c}\n{child.before}")
    child.sendline("commit")
    i = child.expect(PROMPTS + [r"Invalid", r"Error", r"Commit in progress"])
    if 0 < i < len(PROMPTS) + 3 and i != len(PROMPTS):
        raise RuntimeError(f"{host}: commit failed:\n{child.before}")
    child.sendline("save")
    child.expect(PROMPTS)
    child.sendline("exit")
    child.expect(PROMPTS)
    child.sendline("exit")
    child.close()
    return child.before or ""


def main() -> None:
    host, path = sys.argv[1], sys.argv[2]
    with open(path) as f:
        cmds = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    run(host, cmds)
    print(f"{host}: applied {len(cmds)} commands OK")


if __name__ == "__main__":
    main()
