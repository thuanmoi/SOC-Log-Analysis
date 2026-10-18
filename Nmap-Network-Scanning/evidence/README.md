# Nmap Scan Evidence

## Overview

This directory contains Nmap outputs collected during an authorized scan of the author's own Windows machine.

- Target: `127.0.0.1` (localhost)
- Scan date: October 18, 2026
- Tool version: Nmap 7.992
- Environment: Windows 10 Home Single Language
- Scope: Localhost only; TCP ports 1–1000, followed by service detection on selected ports
- Authorization: Self-owned lab environment

## Evidence Files

| File | Description |
|---|---|
| `host-discovery.txt` | Host discovery result |
| `tcp-baseline.nmap` | Human-readable TCP scan results |
| `tcp-baseline.gnmap` | Grep-friendly TCP scan results |
| `tcp-baseline.xml` | Structured TCP scan output |
| `service-detection.nmap` | Human-readable service detection results |
| `service-detection.gnmap` | Grep-friendly service detection results |
| `service-detection.xml` | Structured service detection output |

## Key Observations

- Five TCP ports were listed separately: `135`, `137`, `445`, `902`, and `912`.
- Four ports were reported as open and one as filtered.
- Service detection identified Microsoft Windows RPC and VMware Authentication Daemon.
- Port `445/tcp` was identified as `microsoft-ds`, but detailed service version information was not established.
- An open port indicates a listening service; it does not, by itself, establish a vulnerability.

## Evidence Integrity

The seven files listed above are outputs from the actual local scan. `sample-nmap-output.txt` is a synthetic training example, not evidence from the actual assessment.

The scan was limited to the author's own localhost. No external systems were targeted.

## Limitations

These results represent a point-in-time assessment of localhost. They do not establish the security posture of the entire computer or network. Findings should be validated against host configuration and applicable security policies before assigning severity.