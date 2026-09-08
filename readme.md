# Agentic NetDevOps Benchmark

A benchmark designed to evaluate how AI agents perform on a deliberately atypical infrastructure. Every network is unique, and for that reason we cannot rely on a simple cookie-cutter reference architecture.

The benchmark does not produce a traditional numeric score. Instead, each run creates artifacts: a branch, commit history, ADRs, evaluation notes, templates, and state information. These materials provide most of the meaningful signal.

The benchmark is multi-stage, roughly ordered from simplest to most difficult, with later stages building on the infrastructure created in earlier stages.

The environment provides the agent with access to a Linux management host and five VyOS routers. The default pre-configuration on vyos01 looks like this:

```bash
set interfaces ethernet eth0 address 'dhcp'
set interfaces ethernet eth0 address '3fff:201:911::501/64'
set interfaces ethernet eth0 hw-id 'bc:24:11:e7:2c:1f'
set interfaces ethernet eth0 offload gro
set interfaces ethernet eth0 offload gso
set interfaces ethernet eth0 offload sg
set interfaces ethernet eth0 offload tso
set interfaces loopback lo
set service ntp allow-client address '127.0.0.0/8'
set service ntp allow-client address '169.254.0.0/16'
set service ntp allow-client address '10.0.0.0/8'
set service ntp allow-client address '172.16.0.0/12'
set service ntp allow-client address '192.168.0.0/16'
set service ntp allow-client address '::1/128'
set service ntp allow-client address 'fe80::/10'
set service ntp allow-client address 'fc00::/7'
set service ntp server time1.vyos.net
set service ntp server time2.vyos.net
set service ntp server time3.vyos.net
set service ssh
set system config-management commit-revisions '100'
set system console device ttyS0 speed '115200'
set system host-name 'vyos'
set system login user vyos authentication encrypted-password '$6$rounds=656000$g3WumrG1fKDSa5Qh$OYi6SgazeQ6orbhlBA.053FCNbA.XCT8adAWpkQzNfHvN4sz.AAi40GAKqK9BtFa/EmMClo3YmRaPm1LPwKhF.'
set system login user vyos authentication plaintext-password ''
set system login user vyos authentication public-keys AGENT key 'AAAAC3NzaC1lZDI1NTE5AAAAINTxln5uZWVinDsnRDpBuP2ponLYR0vofZrHgByILs+P'
set system login user vyos authentication public-keys AGENT type 'ssh-ed25519'
set system syslog global facility all level 'info'
set system syslog global facility local7 level 'debug'
```

## Test stages

The benchmark presents the agent with the following stages:

- Stage 1 - Information gathering
- Stage 2 - Basic setup
- Stage 3 - Update devices
- Stage 4 - Configure underlay VPN
- Stage 5 - Setup overlay
- Stage 6 - Setup L2VPN
- Stage 7 - Internet VRF
- Stage 8 - High availability
- Stage 9 - Centralized zone-based firewalling
- Stage 10 - PWHT
- Stage 11 - iPOE authentication
- Stage 12 - Evaluation

## How to run

Paste the following into your agent:

```text
Please fetch this URL and perform the task within <insert URL>
```
