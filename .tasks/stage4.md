# Stage 4 - Configure Underlay VPN

## Prerequisites

- Read ENV.md
- Read WoW.md

## Tasks

- Configure a WireGuard-based underlay VPN using the following requirements:
  - IPv6 only
  - vyos01 and vyos05 should act as hubs
- Configure loopback interfaces on all routers.
- Configure IS-IS, including the WireGuard tunnels and loopbacks.

## Verification

- Verify that all VPNs are up.
- Verify that IS-IS is up.
- Verify loopback-to-loopback connectivity.

## Next step

Once you have completed all tasks and your evaluation, continue to .tasks/stage5.md.
