# Project Summaries

Short descriptions of the projects in this repository. The wording reflects the current files and scope.

## SOC Log Analysis
Created a Python script to parse sample authentication logs and flag repeated failed logins followed by a successful login from the same user and source IP within five minutes. Added sample log data, test scenarios, and an incident-triage report. The GitHub Actions unit-test job and sample-log execution passed in [CI run 39006066961](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961).

[Project repository](SOC-Log-Analysis/)

## Network Traffic Analysis
Created a Python script to review sample network-flow CSV records and flag high byte counts and repeated connections for further investigation. Added unit tests for detection thresholds, malformed numeric fields, and output details. The GitHub Actions unit-test job and sample-flow execution passed in [CI run 39006066961](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961).

[Project repository](Network-Traffic-Analysis/)

## Web Application Security — IDOR/BOLA
Documented an object-level access-control case study with test scenarios, expected behavior, potential impact, and remediation recommendations. This project is a case study rather than a live application test.

[Project repository](Web-Application-Security/)

## Nmap Network Scanning
Conducted an authorized Nmap lab scan against the local host (`127.0.0.1`). Collected host-discovery, TCP port-scan, and service-detection outputs; checked selected services against local Windows service and port information; and documented findings and assessment limitations. Actual scan evidence and reports are stored in the project folder.

**Scope:** Localhost only. The scan did not assess external network reachability or perform exploitation. Open or filtered ports are observations to investigate, not proof of vulnerabilities.

[Project repository](Nmap-Network-Scanning/)

## Tools
Verified hands-on evidence in this repository includes Python-based log and network-flow analysis, Git/GitHub, GitHub Actions, and Nmap for a localhost lab scan. Wireshark, Burp Suite/OWASP ZAP, and SIEM platforms are not claimed as hands-on experience by these project summaries.
