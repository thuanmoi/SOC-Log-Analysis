# Nmap Network Scanning — Authorized Lab

## Objective
Document how to inventory hosts and services in a small lab, interpret results, and recommend defensive actions.

## Important status
This repository currently contains a **planned lab workflow**, not evidence of a completed Nmap scan. No scan output is claimed as real.

## Scope and authorization
- Scan only a system you own or a training target where you have explicit permission.
- Define the target IP/range and permitted scan types before starting.
- Do not scan company, public, or third-party systems without written authorization.
- Avoid aggressive scripts or intrusive checks unless explicitly approved.

## Planned workflow
1. Record the lab target and authorization.
2. Run a basic host/service discovery scan appropriate to the lab.
3. Save the terminal output in `evidence/`.
4. Review open ports and service/version details.
5. Map each exposed service to its business purpose and potential risk.
6. Recommend remediation and, after changes, verify the result.
7. Write down limitations, including what the scan cannot prove.

## Suggested evidence to add after an actual lab scan
- `evidence/scan-output.txt` — sanitized output from your own authorized lab.
- `reports/findings.md` — observed ports/services, risk reasoning, recommendations, and limitations.
- Screenshot(s) showing the scan command and result, with unrelated details removed.

## Report template
Use `reports/findings-template.md` after collecting real results.

## Tools
- Nmap: https://nmap.org/

## Current limitations
No scan has been executed as part of this repository update. Do not list Nmap as hands-on experience until you have run it in an authorized lab and reviewed the output.
