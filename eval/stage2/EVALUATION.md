# Stage 2 Evaluation

## What was done
- Hostnames set on all 5 devices (vyos01..vyos05), verified in running
  config on every device.
- WAN interface descriptions set (WAN-UPLINK-MGMT), verified.
- SSH password authentication disabled on all devices, verified.
- Prometheus installed on the server with node_exporter and
  blackbox_exporter. ICMP probe job `netdevops-devices` covers all five
  devices; verified probe_success=1 for all 5 and up=1 for the
  prometheus/node jobs via the HTTP API.

## Issues / lessons
- Non-interactive VyOS config push was the hard part: piped stdin and
  `vbash -c` both fail on this build. Solved with pexpect driving an
  interactive vbash session (templates/vyos_push.py, ADR-0002).
- vyos04 came up during this stage (was unreachable in stage 1) and was
  successfully configured with everything else.

## Assessment
All tasks complete and verified. The config-push tooling built here is
reusable for the remaining stages.
