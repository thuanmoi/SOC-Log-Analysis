# Nmap Findings Report — Simulated Training Example

> **Evidence status: SIMULATED.** This is a fictional practice report prepared to demonstrate analysis and documentation. No Nmap scan was executed. The target address `192.0.2.10` is from TEST-NET-1, reserved for documentation. Replace this report with observations from an authorized lab scan before presenting it as hands-on scan evidence.

## Scope

- **Target:** `192.0.2.10` (documentation-only example address; not a real target)
- **Authorization:** Scenario only; no network activity performed
- **Date:** Example date only — not a scan timestamp
- **Purpose:** Demonstrate how to document exposed services and reason about follow-up checks

## Method

- **Nmap version:** Example text says 7.95; not verified by running Nmap
- **Exact command:** Illustrative only: `nmap -sV 192.0.2.10`
- **Scan type:** Intended example of TCP port discovery with service/version detection
- **Limitations:** No actual scan; all output is fabricated; no OS detection, vulnerability testing, or service configuration review was performed

## Observed results (simulated)

| Port | Protocol | Service/version shown in example | Expected? | Notes |
|---|---|---|---|---|
| 22 | TCP | SSH / OpenSSH 9.6 | Unknown | Confirm remote administration is required and restricted to approved source networks. |
| 80 | TCP | HTTP / nginx 1.24.0 | Unknown | Confirm whether cleartext HTTP should redirect to HTTPS; validate configuration in the authorized lab. |
| 443 | TCP | HTTPS / nginx 1.24.0 | Unknown | Check TLS configuration and certificate validity separately; this example does not establish either. |

## Assessment

### TCP/22 — SSH

The example lists SSH as open. That alone is not a vulnerability. In a real assessment, verify whether remote administration is required, whether access is restricted, and whether authentication and patching meet the environment's policy. No such checks were performed for this simulated example.

### TCP/80 — HTTP

The example lists HTTP as open. Determine whether the service is intentionally public and whether HTTP redirects to HTTPS where appropriate. An open HTTP port alone does not prove that credentials are transmitted insecurely; inspect the actual application behavior in an authorized lab.

### TCP/443 — HTTPS

The example lists HTTPS. This does not prove that TLS is securely configured. A real follow-up could check certificate validity, supported protocol versions, and cipher configuration using approved tools and scope.

## Recommendations

1. Confirm the expected service inventory with the system owner.
2. Restrict SSH to approved administrators and source networks where feasible.
3. Verify HTTP-to-HTTPS behavior if the application is intended to use HTTPS.
4. Assess TLS configuration using a separate authorized check.
5. Save the actual Nmap command, version, timestamp, and unedited output before drawing environment-specific conclusions.

## Evidence and reproducibility

The accompanying `evidence/sample-nmap-output.txt` is a fabricated fixture for learning only. It is not command output from Nmap. When a real authorized lab scan is performed, save the original output separately, remove sensitive details, and update the report with only verified observations.
