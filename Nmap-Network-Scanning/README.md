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
- `evidence/` — sanitized output from a completed lab scan.
- `reports/findings-template.md` — report structure for observed results.
- `reports/illustrative-practice-walkthrough.md` — a clearly labeled synthetic example explaining commands and interpretation; it is not real scan evidence.
- `reports/nmap-case-study.md` — a structured scenario-based service review with simulated findings, risk reasoning, recommendations and a path to verified evidence.

## Current status
This repository has the workflow, report template, and an illustrative training walkthrough. **There is still no verified real scan output in this repository.** The walkthrough's sample output is synthetic and must not be represented as a scan that was actually run.

Tool: [Nmap](https://nmap.org/)
