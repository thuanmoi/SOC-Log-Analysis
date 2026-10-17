# Portfolio Projects

A collection of security projects and exercises focused on log analysis, network traffic, and web application security.

## Projects

### SOC Log Analysis
A Python script for reviewing authentication logs and identifying repeated failed logins followed by a successful login. Includes sample logs, test scenarios, and an incident report.

[View SOC Log Analysis](SOC-Log-Analysis/)

### Network Traffic Analysis
A Python script that reviews sample network-flow CSV records and flags patterns for further investigation. Includes unit tests and a sample analysis run.

[View Network Traffic Analysis](Network-Traffic-Analysis/)

### Web Application Security
An IDOR/BOLA case study covering access-control test scenarios and remediation recommendations.

[View Web Application Security](Web-Application-Security/)

### Nmap Network Scanning
Documentation for an authorized lab workflow, including a scope checklist and findings-report template.

[View Nmap Network Scanning](Nmap-Network-Scanning/)

## CI status

GitHub Actions run [Fix network flow test module import in CI](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961) completed successfully. Both the SOC unit-test job and the network-flow job passed, including their sample-input execution steps.

## Scope and limitations

The SOC and network projects use sample data. The web security project is a case study, and the Nmap project currently contains the lab workflow and report template. The successful CI run verifies the automated tests and sample commands in this repository; it does not represent a production security assessment or a live network scan.

## Responsible practice

Only test systems you own or have explicit permission to assess. Do not publish company logs, credentials, session tokens, personal data, or confidential network details.
