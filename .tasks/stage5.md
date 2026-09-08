# Stage 5 - Setup Overlay

## Prerequisites

- Read ENV.md
- Read WoW.md

## Tasks

- Set up SRv6 and BGP between the routers:
  - Both SRv6 and BGP traffic must traverse the WireGuard tunnels.
  - The WireGuard hubs act as route reflectors.
  - Use AS65001.
  - Source traffic on loopbacks.

## Verification

- Verify that all BGP peerings are established.
- Verify that SRv6 is functioning at the control plane level.

## Next step

Once you have completed all tasks and your evaluation, continue to .tasks/stage6.md.
