# Stage 9 - Centralized Zone-Based Firewalling

## Prerequisites

- Read ENV.md
- Read WoW.md

## Tasks

- Have vyos05 act as the firewall.
- Create internal and DMZ VRFs.
- Create a DMZ loopback on vyos01.
- Create a ZBFW policy using the following logic:
  - Internal can reach anything.
  - Internet can reach the DMZ.
  - The DMZ cannot initiate outbound connections.
  - Outbound connections from internal clients toward the internet should be NATed.
  - Discard the rest.
- Everything except NAT should be dual-stack, including any interfaces you previously created without it. Go back and fix those if needed.

## Verification

- Verify that connectivity works as described.

## Next step

Once you have completed all tasks and your evaluation, continue to .tasks/stage10.md.
