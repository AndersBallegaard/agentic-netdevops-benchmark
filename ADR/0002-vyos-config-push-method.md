# ADR-0002: VyOS configuration push method

Date: 2026-09-08
Status: Accepted

## Context

VyOS config mode must be driven non-interactively over SSH. Attempts
that failed on this VyOS build:

- Piping commands into `ssh ... 'vbash -i'` (or `configure` piped
  separately): vbash's readline swallows buffered input, so only the
  first command runs and later ones hit "Invalid command".
- `vbash -c "cmd1; cmd2"`: only op-mode commands are accepted; config
  commands and `configure` are rejected.
- `sudo vbash`: drops into a root admin shell that refuses config mode
  ("Please do it as an administrator level VyOS user").

## Decision

Use pexpect (templates/vyos_push.py) to drive an interactive vbash
session over SSH: spawn `ssh vyos@host`, run `vbash -i`, then
`configure`, the set/delete lines (each checked for Invalid/Error),
`commit`, `save`, `exit`, `exit`. This stays inside the VyOS CLI
(no bash work on devices) and validates every command before commit.

## Consequences

- All future stages use templates/vyos_push.py for config pushes.
- Command scripts are stored as `set`-command files per stage.
