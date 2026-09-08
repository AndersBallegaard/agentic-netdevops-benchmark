# Stage 10 - PWHT

## Prerequisites

- Read ENV.md
- Read WoW.md

## Tasks

- Break up the L2VPN from stage 6; it needs to be converted into two PWHT access circuits.
- The service edge for the PWHT should be vyos01.
- The two sides should be L2 separated, but we are tight on IP addresses, so we would like you to reuse the same IP range dynamically across both.
- Also set up DHCP.
- This should all be in the internal VRF.

## Verification

- Decide what verification is relevant; there are no active devices at the end of the line, so do not expect to see traffic.

## Next step

Once you have completed all tasks and your evaluation, continue to .tasks/stage11.md.
