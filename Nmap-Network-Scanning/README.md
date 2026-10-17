# Nmap Network Scanning

## Goal
Use Nmap in an authorized lab to identify visible hosts and services, then explain which results need further review.

## Before scanning
Record the target and confirm that the scan is permitted. Keep the scan within the agreed scope; do not scan company networks, public IPs, or third-party systems without explicit authorization.

Use [scope-template.md](scope-template.md) to record the target, permission, allowed techniques, and exclusions.

## Workflow
1. Run a basic scan against the approved lab target.
2. Save the exact command and output.
3. Review the reported ports and services.
4. Check which services are expected for the target.
5. Recommend changes based on observed evidence, not on open ports alone.
6. If a configuration change is made in the lab, scan again and compare the results.

## Files
- `scope-template.md` — target and authorization details.
- `evidence/sample-nmap-output.txt` — **fabricated training fixture**, not actual Nmap output.
- `reports/findings-template.md` — blank report structure for actual observations.
- `reports/sample-findings-report.md` — completed **simulated** findings report to demonstrate analysis and documentation.
- `reports/illustrative-practice-walkthrough.md` — synthetic example explaining commands and interpretation.
- `reports/nmap-case-study.md` — scenario-based service review with simulated findings, risk reasoning, and recommendations.

## Current status
The portfolio now includes a complete sample report and sample output fixture for demonstration. **No verified real Nmap scan has been performed or added yet.** All sample findings are explicitly labeled simulated and must not be represented as evidence from an actual scan. Replace them with output from an authorized lab scan when available.

Tool: [Nmap](https://nmap.org/)
