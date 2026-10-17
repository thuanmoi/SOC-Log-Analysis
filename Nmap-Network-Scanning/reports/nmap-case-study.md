# Nmap Case Study: Local Lab Service Review

> **Scenario status: simulated case study.** The target output in this folder is illustrative training data, not captured from a real Nmap execution. It demonstrates the analysis workflow and must not be represented as actual scan evidence.

## Scenario

For a portfolio exercise, assume an authorized lab host at `192.0.2.10` (TEST-NET-1 documentation range) is expected to provide SSH administration and an HTTP test page. The address is reserved for documentation and is not a real target to scan.

## Objective

Interpret a sample Nmap service scan, distinguish observations from conclusions, and recommend safe validation steps.

## Simulated command

```bash
nmap -sV -oN nmap_scan.txt 192.0.2.10
```

This command is shown for learning only. Do not run it against the documentation address expecting a real host.

## Simulated Nmap output

```text
Starting Nmap 7.95 ( https://nmap.org )
Nmap scan report for lab-web-01 (192.0.2.10)
Host is up (0.0010s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 9.6 (protocol 2.0)
80/tcp  open  http    nginx 1.24.0
443/tcp open  https   nginx 1.24.0
Service Info: OS: Unix
Nmap done: 1 IP address (1 host up) scanned in 6.42 seconds
```

**All host names, port states, versions, latency, counts and timings above are fabricated for the scenario.** They are not claims about a real machine.

## Analysis

| Observation in the scenario | Security interpretation | Recommended validation |
|---|---|---|
| TCP/22 reports SSH | Remote administration may be available. This is not automatically a vulnerability. | Confirm SSH is required, restrict source networks, review authentication and patch level. |
| TCP/80 reports HTTP | A web service may be reachable without transport encryption. | Determine whether HTTP is intentionally used for redirect or public content; verify behavior in the authorized lab. |
| TCP/443 reports HTTPS | An HTTPS service may be available. Nmap service detection alone does not validate TLS configuration. | Inspect certificate validity, protocol versions, ciphers and redirect behavior with approved tools. |
| Service versions are reported | Version detection offers clues, but banners may be hidden, customized or misleading. | Verify installed package versions on the host and compare against vendor advisories. |

## Findings (scenario-based)

### F-01: Remote administration exposure
- **Evidence:** simulated output lists `22/tcp open ssh`.
- **Risk:** depends on whether SSH is necessary, who can reach it, and the authentication configuration.
- **Recommendation:** allow SSH only from approved admin networks; prefer key-based authentication where appropriate; disable unused accounts; monitor authentication logs.
- **Confidence:** low-to-moderate for the scenario because this is synthetic output and host configuration has not been inspected.

### F-02: HTTP service available
- **Evidence:** simulated output lists `80/tcp open http`.
- **Risk:** depends on content and behavior; the port alone does not establish that sensitive data is transmitted insecurely.
- **Recommendation:** verify whether HTTP redirects to HTTPS and whether any sensitive content is served over HTTP.

### F-03: HTTPS configuration not assessed
- **Evidence:** simulated output lists `443/tcp open https`.
- **Risk:** unknown. The port being open does not establish that TLS is configured securely.
- **Recommendation:** perform an authorized TLS configuration review and document certificate, protocol and cipher results separately.

## Method and limitations

- Method represented: TCP common-port scan with service/version detection (`-sV`).
- The sample does not cover all TCP ports, UDP services, authenticated configuration, application vulnerabilities or firewall rules beyond the scan's vantage point.
- Version strings are not sufficient to prove a vulnerability.
- An open port is an observation, not a vulnerability verdict.
- No actual scan was run to produce this sample.

## How to turn this case study into verified evidence

1. Run Nmap against a lab machine that you own or are explicitly authorized to test.
2. Save the exact command output to `evidence/nmap_scan.txt`.
3. Record the real target scope, date, Nmap version and scan options.
4. Replace scenario-based observations with values copied from the actual output.
5. Keep the original output sanitized but otherwise unaltered; separate facts from interpretation.
6. Re-scan after any approved configuration change and compare the two real outputs.

## Portfolio disclosure

This is a simulated case study prepared to demonstrate Nmap result interpretation. It should be described as a lab scenario / case study until verified scan output is collected.
