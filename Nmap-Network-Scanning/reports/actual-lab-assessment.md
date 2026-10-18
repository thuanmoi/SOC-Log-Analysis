Nmap Network Scanning — Hands-on Lab Assessment

> Evidence status: The actual Nmap output files from the local lab exercise are included in `../evidence/`. The scan results were collected on 2026-10-18 from the author's own workstation via `127.0.0.1`. No third-party host was scanned.

1. Objective and scope

I used Nmap to practice host discovery, TCP port scanning, and service/version identification against localhost. I then used read-only Windows PowerShell queries to cross-check listening ports, owning processes, SMB configuration, SMB shares, and Windows Firewall profiles.

- Target: `127.0.0.1` (localhost only)
- Date shown in terminal: 2026-10-18
- Nmap version: `7.992`
- Windows product: Windows 10 Home Single Language
- OS build: `26200`
- Authorization: Practice on my own workstation
- Out of scope: External hosts, public IPs, third-party systems, exploitation, and destructive testing

PowerShell also displayed `WindowsVersion 2009`. I do not interpret this internal version value as a release year; the product name and build are recorded separately.

2. Commands and methodology

Host discovery

```bash
nmap -sn 127.0.0.1 -oN scans/host-discovery.txt
```

Nmap reported localhost as up and completed a one-host scan.

TCP baseline scan

```bash
nmap -sT -p 1-1000 -oA scans/tcp-baseline 127.0.0.1
```

The displayed output reported the host as up and 995 closed TCP ports. The listed results were:

| Port | State | Service label |
|---|---|---|
| 135/tcp | open | msrpc |
| 137/tcp | filtered | netbios-ns |
| 445/tcp | open | microsoft-ds |
| 902/tcp | open | iss-realsecure |
| 912/tcp | open | apex-mesh |

Service/version detection

```bash
nmap -sT -sV --version-light -p 135,137,445,902,912 -oA scans/service-detection 127.0.0.1
```

The service-detection output reported:

| Port | State | Service/version reported |
|---|---|---|
| 135/tcp | open | Microsoft Windows RPC |
| 137/tcp | filtered | netbios-ns |
| 445/tcp | open | microsoft-ds? |
| 902/tcp | open | VMware Authentication Daemon 1.10 (uses VNC, SOAP) |
| 912/tcp | open | VMware Authentication Daemon 1.0 (uses VNC, SOAP) |

Nmap also reported OS information consistent with Windows. Service labels are identification clues, not proof of vulnerability.

3. PowerShell validation

Listening ports and processes

The filtered `Get-NetTCPConnection -State Listen` output showed:

| Local address | Port | PID | Process |
|---|---:|---:|---|
| `::` | 445 | 4 | System |
| `::` | 135 | 1652 | svchost |
| `0.0.0.0` | 912 | 6904 | vmware-authd |
| `0.0.0.0` | 902 | 6904 | vmware-authd |
| `0.0.0.0` | 135 | 1652 | svchost |

The service lookup associated PID `1652` with `RpcEptMapper` and `RpcSs`, and PID `6904` with `VMAuthdService` (VMware Authorization Service). Binding to `0.0.0.0` means all local IPv4 interfaces; it does not alone prove remote reachability.

SMB settings

`Get-SmbServerConfiguration` returned:

| Setting | Value |
|---|---|
| `EnableSMB1Protocol` | `False` |
| `EnableSMB2Protocol` | `True` |
| `EnableSecuritySignature` | `False` |
| `RequireSecuritySignature` | `False` |

SMB1 being disabled is a positive observation. The signing values mean the queried properties did not show signing enabled or required. I recorded this as **requiring policy validation**, not a confirmed exploitable vulnerability. The effective policy and expected Windows security baseline should be checked before assigning severity or changing configuration.

SMB shares

`Get-SmbShare` listed:

| Share | Path | Description |
|---|---|---|
| `ADMIN$` | `C:\WINDOWS` | Remote Admin |
| `C$` | `C:\` | Default share |
| `IPC$` | No ordinary folder path shown | Remote IPC |

These are common Windows administrative/IPC shares. Their presence alone is not a vulnerability; permissions and authorized access require separate review.

Windows Firewall

The Domain, Private, and Public firewall profiles were all enabled. The displayed `DefaultInboundAction` value was `NotConfigured` for each. My query for enabled inbound Allow rules matching local port `445` returned no rows. This is inconclusive and does not prove TCP/445 is blocked. Effective rules, address scopes, policy sources, and remote reachability would need further review.

4. Findings and follow-up

Observation 1 — Local services are listening

- Evidence: Nmap reported TCP/135, TCP/445, TCP/902, and TCP/912 open on localhost; PowerShell associated ports 902 and 912 with `vmware-authd`.
- Assessment: Informational service inventory; no severity assigned.
- Reasoning: Open ports are not automatically vulnerabilities.
- Follow-up: Confirm these services are expected. If any is unnecessary, review supported configuration guidance and restrict exposure appropriately.

Observation 2 — SMB signing settings require validation

- Evidence: `EnableSecuritySignature=False` and `RequireSecuritySignature=False`.
- Assessment: Needs validation; severity not assigned.
- Potential concern: Where policy requires SMB signing, not requiring it may reduce protection against certain tampering or adversary-in-the-middle scenarios.
- Limitations: This alone does not prove remote reachability, exploitability, or a confirmed vulnerability.
- Follow-up: Compare effective SMB signing behavior with the applicable Windows security baseline before deciding on remediation.

Observation 3 — SMB1 is disabled

- Evidence: `EnableSMB1Protocol=False`.
- Assessment: Positive configuration observation. This does not establish that every aspect of SMB is secure.

Observation 4 — Firewall review is incomplete

- Evidence: All three profiles were enabled; the initial TCP/445 inbound Allow-rule query returned no matching rows.
- Assessment: Inconclusive; I do not claim that SMB is blocked or reachable remotely based on this query alone.
- Follow-up: Review effective rule scopes and, if necessary, test reachability from a separate authorized lab host.

5. Limitations

1. All Nmap scans targeted '127.0.0.1', not the entire LAN or an external attacker's view.
2. The original Nmap output files are included in `Nmap-Network-Scanning/evidence/` in the repository. The results can be reviewed from these artifacts; reproducing the scan requires an equivalent environment and rerunning the documented commands.
3. I did not perform vulnerability scanning, exploitation, credential testing, or external reachability testing.
4. I queried SMB signing properties but did not fully validate effective policy or negotiated signing behavior.
5. The firewall query was a limited filter, not a complete firewall audit.
6. These are observations and review items, not confirmed vulnerabilities; I have not assigned severity without sufficient evidence.

6. What I learned

Through this exercise, I practiced host discovery, TCP connect scanning, saving results with '-oA', service/version detection with '-sV --version-light', validating listening services with PowerShell, reviewing SMB settings and firewall profiles, and documenting evidence and limitations without overstating conclusions.

7. Next steps

1. Upload sanitized original Nmap outputs while preserving their provenance.
2. Complete the lab scope record without exposing sensitive host details.
3. Validate SMB signing baseline and effective firewall policy.
4. If an approved lab configuration change is made, document it and compare before/after scans.
5. Reassess severity only when baseline, exposure, and impact are supported by evidence.

Evidence integrity note

This report documents observations from my local exercise. The repository's separate 'evidence/sample-nmap-output.txt' and simulated reports remain synthetic training examples and must not be confused with this hands-on assessment.
