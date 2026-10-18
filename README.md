# Security Engineer Portfolio

This repository contains projects developed while preparing for a Fresher Security Engineer role. It focuses on authentication-log review, network-flow analysis, web access control, and authorized network scanning.

Each project documents its objective, environment, tools, workflow, findings, and recommended next steps. Results are labelled as sample data or actual lab evidence so the scope is clear.

## Projects

### 1. SOC Log Analysis
**Goal:** Identify suspicious authentication patterns for initial incident triage.

- **Implementation:** Python script for parsing authentication log entries and flagging repeated failed logins followed by a successful login from the same user and source IP within a five-minute window.
- **Current materials:** Sample log file, source code, test scenarios, and incident-triage report.
- **Current environment/tools:** Python 3, text log files, and GitHub.
- **Evidence scope:** Repository sample logs are demonstration data, not logs collected from a production system.

[View project](SOC-Log-Analysis/)

### 2. Network Traffic Analysis
**Goal:** Flag network-flow records that may deserve further investigation.

- **Implementation:** Python script that reviews CSV flow records and flags high byte counts or repeated connections.
- **Current materials:** Sample CSV dataset, source code, test scenarios, and analysis report.
- **Current environment/tools:** Python 3, CSV data, and GitHub.
- **Evidence scope:** The current dataset is synthetic CSV data, not a real packet capture.

[View project](Network-Traffic-Analysis/)

### 3. Web Application Security
**Goal:** Understand object-level access control and potential IDOR/BOLA issues.

- **Current materials:** Case study, test matrix, finding report, and remediation recommendations.
- **Current environment/tools:** Written test scenarios and Markdown documentation.
- **Evidence scope:** This is a case study, not a penetration test against a live application.

[View project](Web-Application-Security/)

### 4. Nmap Network Scanning
**Goal:** Practice scoped host discovery, TCP port scanning, and service identification in an authorized local lab.

- **Completed lab:** Scanned the local host (`127.0.0.1`) using Nmap 7.992 on Windows.
- **Commands and evidence:** Host discovery, TCP baseline scan, and selected-port service detection outputs are stored under `Nmap-Network-Scanning/evidence/`.
- **Reporting:** Includes an actual lab assessment and findings report. Selected ports/services were cross-checked against local Windows port and service information.
- **Scope and limitations:** Localhost only. No external network scan, exploitation, or production security assessment was performed. A port being open or filtered is not, by itself, proof of a vulnerability.

[View project](Nmap-Network-Scanning/)

## Automated test status

The [GitHub Actions run for commit 0ae13fd](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961) completed successfully. Both the SOC unit-test job and the network-flow job passed, including their sample-input execution steps. This confirms those automated checks for that recorded run; check the Actions tab for the latest status after future changes.

## Tools and environment

Verified practical evidence in this repository includes Python-based log and network-flow analysis, Git/GitHub, GitHub Actions, and Nmap used for a localhost lab scan. Wireshark, Burp Suite/OWASP ZAP, and SIEM platforms are not claimed as hands-on experience here because no completed practical evidence for them is documented in this portfolio.

## How to reproduce the Python projects

1. Install Python 3 in an appropriate personal or lab environment.
2. Open the relevant project folder in VS Code or a terminal.
3. Follow that project's README for the exact command and expected example output.
4. Compare actual output with the documented example and update the report if results differ.

## Responsible testing

Only assess systems you own or have explicit permission to test. Use synthetic or sanitized data in public repositories. Never publish company logs, credentials, tokens, personal data, or confidential network details.
