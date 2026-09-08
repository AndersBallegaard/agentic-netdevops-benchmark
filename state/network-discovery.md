# Network Layout Discovery (Stage 1)

Discovery date: 2026-09-08 (UTC)

## Management/WAN segment

All devices sit on a shared "WAN" segment 192.168.5.0/24 with an
unsecured out-of-band network that provides reachability (per ENV.md).
IPv6 on that segment is 3fff:201:911::/64.

| Device  | DNS name                     | WAN v4        | WAN v6                 | Interface |
|---------|------------------------------|---------------|------------------------|-----------|
| vyos01  | vyos01.netagent.srv6.dk      | 192.168.5.48/24 | 3fff:201:911::501/64 | eth0      |
| vyos02  | vyos02.netagent.srv6.dk      | 192.168.5.53/24 | 3fff:201:911::502/64 | eth1      |
| vyos03  | vyos03.netagent.srv6.dk      | 192.168.5.67/24 | 3fff:201:911::503/64 | eth1      |
| vyos04  | vyos04.netagent.srv6.dk      | (no A record)   | 3fff:201:911::504/64 | unknown   |
| vyos05  | vyos05.netagent.srv6.dk      | 192.168.5.248/24| 3fff:201:911::505/64 | eth1      |
| server  | netagent (this host)         | via DHCP        | 3fff:201:911:0:be24:11ff:fe37:445f | - |

## Software

- VyOS with kernel 6.6.43-amd64-vyos (VyOS 1.5 rolling / current, FRR 9.1.1).
- Default route via 192.168.5.1 on the WAN interface, tag 210.
- No other routing protocols configured. Configs are essentially stock.

## Connectivity verification

- SSH (key auth, user vyos) works to vyos01, vyos02, vyos03, vyos05.
- vyos04: resolves only to IPv6 (3fff:201:911::504); no A record.
  ICMPv6 ping and ssh-keyscan both fail (address unreachable) at time
  of discovery. Device appears down or not yet attached to the WAN
  segment. Will be re-checked in later stages.
