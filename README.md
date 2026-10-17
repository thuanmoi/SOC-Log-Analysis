# Security Engineer Portfolio

This repository contains projects I have been building while preparing for a Fresher Security Engineer role. The main topics are authentication-log review, network-flow analysis, web access control, and network scanning.

## Projects

### SOC Log Analysis
A Python script that reads authentication logs and flags repeated failed logins followed by a successful login from the same user and source IP within a five-minute window. The project includes sample logs, test scenarios, and an incident-triage report.

[View project](SOC-Log-Analysis/)

### Network Traffic Analysis
A Python script that reviews sample network-flow records and flags high byte counts or repeated connections for further review. The input is a sample CSV, not a packet capture.

[View project](Network-Traffic-Analysis/)

### Web Application Security
An IDOR/BOLA case study covering object-level access control, test scenarios, and remediation recommendations.

[View project](Web-Application-Security/)

### Nmap Network Scanning
A lab scope checklist and report template for documenting an authorized scan.

[View project](Nmap-Network-Scanning/)

## Tools and scope

The current projects use Python, text and CSV data, Markdown, and GitHub. The network-flow dataset is synthetic, and the web security work is a case study. The Nmap folder contains preparation materials; scan results will be documented when an authorized lab scan is completed.

## Responsible testing

Only assess systems you own or have explicit permission to test. Do not publish company logs, credentials, tokens, personal data, or confidential network details.
