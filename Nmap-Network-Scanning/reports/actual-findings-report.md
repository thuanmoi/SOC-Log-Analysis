# Nmap Findings Report — Localhost Lab

> Evidence status: Based on the actual Nmap output files in `../evidence/`. This assessment covers the author's own Windows workstation at `127.0.0.1` only.

## 1. Scope

- Target: `127.0.0.1` (localhost)
- Authorization: The author's own workstation
- Date: October 18, 2026
- Purpose: Practice TCP port discovery, service identification, and evidence-based security assessment

## 2. Method

- Tool: Nmap 7.992
- TCP baseline command: `nmap -sT -p 1-1000 -oA scans/tcp-baseline 127.0.0.1`
- Service detection command: `nmap -sT -sV --version-light -p 135,137,445,902,912 -oA scans/service-detection 127.0.0.1`
- Scan scope: TCP ports 1–1000 on localhost; service detection on selected ports
- Limitations: No external reachability testing, exploitation, or vulnerability scanning was performed.

## 3. Observed Results

| Port | State | Service identified by Nmap | Assessment |

|---|---|---|---|

| 135/tcp | Open | Microsoft Windows RPC | Confirm whether required by the host and its security policy. |

| 137/tcp | Filtered | NetBIOS-NS | Nmap could not determine whether the port was open or closed due to filtering. |

| 445/tcp | Open | `microsoft-ds?` | Likely SMB-related; verify effective SMB policy and access controls. |

| 902/tcp | Open | VMware Authentication Daemon 1.10 | Confirm VMware-related service is required and appropriately restricted. |

| 912/tcp | Open | VMware Authentication Daemon 1.0 | Confirm VMware-related service is required and appropriately restricted. |

The baseline scan reported 995 closed TCP ports in the scanned range. Open ports are not automatically vulnerabilities.

## 4. Findings and Recommendations

### Finding 1 — Listening services require an expected-service review

- Evidence: TCP/135, TCP/445, TCP/902, and TCP/912 were reported open on localhost.
- Severity: Informational; no confirmed vulnerability identified.
- Analysis: Listening services may be legitimate components of Windows or installed software. The scan alone does not establish unauthorized exposure.
- Recommendation: Confirm business and system requirements for each service. Disable or restrict only services confirmed to be unnecessary, following approved change procedures.

### Finding 2 — SMB signing configuration needs policy validation

- Evidence: The lab's PowerShell query returned `EnableSecuritySignature=False` and `RequireSecuritySignature=False`.
- Severity: Unassigned pending validation.
- Analysis: These property values warrant comparison with the applicable security baseline. They do not, by themselves, prove exploitability or remote reachability.
- Recommendation: Verify effective policy and negotiated SMB signing behavior. If signing is required by policy but not enforced, plan remediation and regression testing with the system owner.

### Finding 3 — SMB1 is disabled

- Evidence: `EnableSMB1Protocol=False`.
- Assessment: Positive configuration observation.
- Recommendation: Maintain the approved configuration and continue reviewing the remaining SMB security settings.

### Finding 4 — Firewall behavior remains inconclusive

- Evidence: Windows Firewall profiles were enabled. The initial query for enabled inbound Allow rules matching local TCP/445 returned no rows.
- Severity: No finding severity assigned.
- Analysis: This limited query does not prove that TCP/445 is blocked or reachable from another machine.
- Recommendation: Review effective firewall rules, scopes, and policy sources. Perform a remote reachability test only from a separate authorized lab host if required.

## 5. Verification Plan

- Confirm which listening services are expected.
- Validate effective SMB signing policy against the applicable baseline.
- Review effective firewall rules for TCP/445.
- Document approved configuration changes, if any.
- Repeat the relevant checks and compare results after changes.

## 6. Conclusion

This exercise produced an inventory of listening TCP services and identified configuration items for follow-up. The available evidence does not establish a confirmed exploitable vulnerability. Further conclusions require validation against the host's intended configuration and applicable security policies.

