# ADR-0001: Discovery tooling and device access method

Date: 2026-09-08
Status: Accepted

## Context

We must discover and manage 5 VyOS routers over SSH from this server,
without leaving the VyOS CLI unnecessarily (WoW.md).

## Decision

- Use plain OpenSSH with key auth (user `vyos`) for ad-hoc access.
- On-device `show` commands will be executed via the VyOS op-mode CLI
  where possible; FRR-level detail via `sudo vtysh -c "..."` (still
  VyOS-shipped tooling, no bash shell work on the devices).
- Configuration will be applied via VyOS `set`-style command batches
  piped into the configured CLI, keeping us out of interactive bash.
- We will build small Python/automation helpers (templates dir) rather
  than installing heavy frameworks unless a later stage requires it.
