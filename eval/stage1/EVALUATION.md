# Stage 1 Evaluation

## What was done
- Read ENV.md and WoW.md; cloned repo, created branch hermes-glm53-flash.
- Discovered all devices: all five are VyOS (kernel 6.6.43, FRR 9.1.1),
  each with a single preconfigured WAN interface on 192.168.5.0/24 /
  3fff:201:911::/64 and a default route via 192.168.5.1.
- Verified SSH key connectivity to vyos01/02/03/05 (op-mode and vtysh
  both reachable).
- Backed up running configs (config.boot) to eval/stage1/backups/.

## Issues
- vyos04.netagent.srv6.dk resolves only to IPv6 (3fff:201:911::504);
  no A record, and the address does not respond to ping or SSH at
  discovery time. Treated as currently unreachable; will retry in
  later stages. Not a blocker for stage 1 discovery of the others.

## Assessment
Straightforward discovery stage. Connectivity verified for 4/5 nodes,
with the exception documented in state/network-discovery.md.
