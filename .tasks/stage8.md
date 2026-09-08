# Stage 8 - High Availability

## Prerequisites

- Read ENV.md
- Read WoW.md

## Tasks

- Set up a high-availability access interface.
  - There is a shared segment between vyos02 and vyos03; unfortunately, no one has documented which interface it is. It is your task to determine this and move the configuration if anything is in the way.
  - You decide how to achieve HA; there is no LACP, but we do expect gateway redundancy.
  - The network should be in the internet VRF.

## Verification

- Verify that redundancy is operating correctly.
- Verify that the gateway is reachable from other nodes.

## Next step

Once you have completed all tasks and your evaluation, continue to .tasks/stage9.md.
