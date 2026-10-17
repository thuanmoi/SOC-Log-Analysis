# Security Engineer Portfolio

This repository contains projects I am developing while preparing for a Fresher Security Engineer role. It focuses on authentication-log review, network-flow analysis, web access control, and network scanning.

Each project documents its objective, environment, tools, workflow, findings, and recommended next steps. Results are labelled as sample or actual lab evidence so the scope is clear and the work can be reproduced.

## Projects

### 1. SOC Log Analysis
**Goal:** Identify suspicious authentication patterns for initial incident triage.

- **Implementation:** Python script for parsing authentication log entries and flagging repeated failed logins followed by a successful login from the same user and source IP within a five-minute window.
- **Current materials:** Sample log file, source code, test scenarios, and incident-triage report.
- **Current environment/tools:** Python 3, text log files, and GitHub.
- **Next practical step:** Run the script in a Linux lab (such as Ubuntu), inspect system authentication logs where available, and capture verified command output.
- **Evidence scope:** The repository's sample logs are demonstration data; they are not logs collected from a production system.

[View project](SOC-Log-Analysis/)

### 2. Network Traffic Analysis
**Goal:** Flag network-flow records that may deserve further investigation.

- **Implementation:** Python script that reviews CSV flow records and flags high byte counts or repeated connections.
- **Current materials:** Sample CSV dataset, source code, test scenarios, and analysis report.
- **Current environment/tools:** Python 3, CSV data, and GitHub.
- **Next practical step:** Capture or obtain an authorized lab PCAP, inspect it with Wireshark, and document how packet-level observations compare with the CSV analysis.
- **Evidence scope:** The current dataset is synthetic CSV data, not a real packet capture.

[View project](Network-Traffic-Analysis/)

### 3. Web Application Security
**Goal:** Understand and test object-level access control to identify potential IDOR/BOLA issues.

- **Current materials:** Case study, test matrix, finding report, and remediation recommendations.
- **Current environment/tools:** Written test scenarios and Markdown documentation.
- **Next practical step:** Reproduce the cases in an intentionally vulnerable training application, using Burp Suite or browser developer tools, and save sanitized evidence.
- **Evidence scope:** This is currently a case study, not a penetration test against a live application.

[View project](Web-Application-Security/)

### 4. Nmap Network Scanning
**Goal:** Document an authorized host and service discovery workflow.

- **Current materials:** Scope checklist and findings-report template.
- **Planned lab tools:** Nmap and a local or intentionally provided lab target.
- **Next practical step:** Run a scoped scan against a system explicitly authorized for testing, then record the exact command, tool version, output, and interpretation.
- **Evidence scope:** The folder currently contains preparation materials; no scan result is claimed yet.

[View project](Nmap-Network-Scanning/)

## Automated test status

The [GitHub Actions run for commit 0ae13fd](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961) completed successfully. Both the SOC unit-test job and the network-flow job passed, including their sample-input execution steps. This confirms those automated checks for that run; check the Actions tab for the latest status after future changes.

## Tools and environment

The current implemented code uses Python 3 and sample text/CSV files; project documentation and version control use Markdown and GitHub. Ubuntu/Linux, Wireshark, Burp Suite, and Nmap are identified as tools for planned lab exercises where noted above; they should only be described as hands-on experience after the corresponding exercise has actually been completed and verified.

## How to reproduce the Python projects

1. Install Python 3 on your computer.
2. Open the relevant project folder in VS Code or a terminal.
3. Follow that project's README for the exact command and expected example output.
4. Compare your actual output with the documented example and update the report if the results differ.

## Responsible testing

Only assess systems you own or have explicit permission to test. Use synthetic or sanitized data in public repositories. Never publish company logs, credentials, tokens, personal data, or confidential network details.
