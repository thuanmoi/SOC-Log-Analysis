# Nmap Network Scanning

## Goal

I built this project to practice a structured, evidence-based network reconnaissance workflow with Nmap on my own Windows workstation. I combined scan results with Windows PowerShell checks to identify listening services, review SMB settings, and document what could—and could not—be concluded from the available evidence.

## Scope and authorization

The hands-on scan documented in this repository targeted **localhost (`127.0.0.1`) only** on my own workstation. It was not a scan of a public IP, company network, or third-party system.

Before scanning a different target, I would record the authorization, target range, permitted techniques, time window, exclusions, and stop procedure using [scope-template.md](scope-template.md).

## My workflow

1. Checked the installed Nmap version.
2. Ran host discovery against `127.0.0.1`.
3. Performed a TCP connect scan of ports 1–1000 and saved output in Nmap, XML, and grepable formats.
4. Used service/version detection on selected ports.
5. Cross-checked listening ports and owning processes with Windows PowerShell.
6. Reviewed SMB protocol settings, SMB shares, SMB signing properties, and Windows Firewall profiles.
7. Documented observations, limitations, and recommended follow-up checks without treating every open port as a vulnerability.

## Hands-on results

See [reports/actual-lab-assessment.md](reports/actual-lab-assessment.md) for observations transcribed from my terminal screenshots, including commands, ports, service identification, PowerShell validation, and limitations.

**Evidence available:** the repository includes the actual Nmap output files collected during the local exercise, alongside the assessment reports. These artifacts allow readers to inspect the recorded results. Reproducing the scan still requires an equivalent environment and rerunning the documented commands.

## Repository contents

- `scope-template.md` — authorization and scope checklist.
- `reports/actual-lab-assessment.md` — findings from my local hands-on exercise, with limitations stated.
- `evidence/host-discovery.txt`, `tcp-baseline.*`, and `service-detection.*` — actual outputs from the documented localhost scan.
- `evidence/sample-nmap-output.txt` — **synthetic training fixture**, not actual Nmap output.
- `reports/findings-template.md` — blank report structure.
- `reports/sample-findings-report.md` — **simulated** report for documentation practice.
- `reports/illustrative-practice-walkthrough.md` — synthetic command walkthrough.
- `reports/nmap-case-study.md` — scenario-based example with simulated findings.

The synthetic examples are kept separate from the hands-on report and must not be presented as real scan evidence.

## Key lessons

- An open port is an observation, not automatically a vulnerability.
- Service/version detection improves identification but does not prove exploitability.
- Host-side validation helps explain which local process owns a listening port.
- Firewall query results must be interpreted carefully; an empty filtered result does not prove that traffic is blocked.
- Security findings should include evidence, impact considerations, limitations, and a practical next step.

## Tools

- [Nmap](https://nmap.org/)
- Windows PowerShell
- Git and GitHub
