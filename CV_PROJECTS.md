# Project Summaries

Short descriptions of the projects in this repository. The wording reflects the current files and scope.

## SOC Log Analysis
Created a Python script to parse sample authentication logs and flag repeated failed logins followed by a successful login from the same user and source IP within five minutes. Added sample log data, test scenarios, and an incident-triage report. The GitHub Actions unit-test job and sample-log execution passed in [CI run 39006066961](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961).

[Project repository](SOC-Log-Analysis/)

## Network Traffic Analysis
Created a Python script to review sample network-flow CSV records and flag high byte counts and repeated connections for further investigation. Added unit tests for detection thresholds, malformed numeric fields, and output details. The GitHub Actions unit-test job and sample-flow execution passed in [CI run 39006066961](https://github.com/thuanmoi/SOC-Log-Analysis/actions/runs/39006066961).

[Project repository](Network-Traffic-Analysis/)

## Web Application Security — IDOR/BOLA
Documented an object-level access-control case study with test scenarios, expected behavior, potential impact, and remediation recommendations. The current project is a case study rather than a live application test.

[Project repository](Web-Application-Security/)

## Nmap Network Scanning
Prepared a scope checklist and findings-report template for an authorized lab scan. Scan output has not yet been added.

[Project repository](Nmap-Network-Scanning/)

## Tools
Used in the current repository: Python, CSV/text files, Markdown, GitHub, and GitHub Actions for automated tests. Nmap, Wireshark, Burp Suite/OWASP ZAP, and SIEM platforms are not listed as hands-on experience in these project summaries because there is no practical evidence for them here.
