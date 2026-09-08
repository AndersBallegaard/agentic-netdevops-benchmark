# ADR-0003: Monitoring stack

Date: 2026-09-08
Status: Accepted

## Context

Stage 2 requires Prometheus on the server monitoring reachability and
device state.

## Decision

- Install Prometheus + node_exporter + blackbox_exporter from Ubuntu
  apt (server is Ubuntu 24.04-based; systemd services).
- Reachability: blackbox `icmp` module probing each vyos0N DNS name via
  the `netdevops-devices` scrape job (probe_success per device).
- Device state: to be extended via SNMP or node_exporter on devices in
  later stages; baseline is the ICMP probe plus Prometheus's own
  server metrics.
- Config lives in /etc/prometheus/prometheus.yml (merged job block);
  a copy of the job definition is kept in templates/prometheus-netdevops-job.yaml.

## Consequences

- Any new device must be added to the static_configs target list.
