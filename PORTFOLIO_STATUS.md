# Portfolio Projects

A collection of security projects and exercises focused on log analysis, network traffic, web application security, and authorized network scanning.

## Projects

### SOC Log Analysis
A Python script for reviewing authentication logs and identifying repeated failed logins followed by a successful login. Includes sample logs, test scenarios, and an incident report.

[View SOC Log Analysis](SOC-Log-Analysis/)

### Network Traffic Analysis
A Python script that reviews sample network-flow CSV records and flags patterns for further investigation. Includes unit tests and a sample analysis run.

[View Network Traffic Analysis](Network-Traffic-Analysis/)

### Web Application Security
An IDOR/BOLA case study covering access-control test scenarios and remediation recommendations. This is a documented case study, not a live application penetration test.

[View Web Application Security](Web-Application-Security/)

### Nmap Network Scanning
Completed a scoped Nmap scan of the local host (`127.0.0.1`), including host discovery, TCP port scanning, and selected service detection. Actual scan outputs and assessment reports are included in the project folder.

[View Nmap Network Scanning](Nmap-Network-Scanning/)

## CI status

GitHub Actions run [Fix network flow test module import in CI](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961) completed successfully. Both the SOC unit-test job and the network-flow job passed, including their sample-input execution steps. This describes that recorded run; check Actions for the latest result after future changes.

## Scope and limitations

The SOC and network-flow projects use sample data. The web security project is a case study, not a live application test. The Nmap project contains actual scan evidence from the local host only; it does not demonstrate external network scanning, exploitation, or a production security assessment. The successful CI run verifies the automated tests and sample commands in that run, not the security of a production system.

## Responsible practice

Only test systems you own or have explicit permission to assess. Do not publish company logs, credentials, session tokens, personal data, or confidential network details.
