# Nmap Practice Walkthrough (Illustrative)

> For the author's actual localhost scan observations, see [actual-lab-assessment.md](actual-lab-assessment.md). This walkthrough remains a separate synthetic learning example.

> **Evidence status: illustrative training example — not an actual scan result.**  
> This report was prepared to demonstrate how to interpret Nmap output. No Nmap command was executed as part of creating this document, so the sample output below must not be presented as evidence of a real scan.

## Objective

Practice the basic workflow for identifying TCP ports and reported services on a system you own or are explicitly authorized to test.

## Safe lab target

Use `127.0.0.1` (loopback / the same computer) only when Nmap is installed locally. This avoids selecting an unrelated external target. The exact services visible will depend on the machine and may differ from the illustrative output below.

## Commands to run in an authorized lab

Check the installed version:

```bash
nmap --version
```

Scan common TCP ports and ask Nmap to identify services:

```bash
nmap -sV -oN nmap_scan.txt 127.0.0.1
```

- `-sV`: probe open ports to identify the service/version where possible.
- `-oN nmap_scan.txt`: save normal output to a file.
- `127.0.0.1`: scan the local host, not a public or third-party system.

This default command scans Nmap's common TCP port set; it does **not** scan every TCP port. To scan all TCP ports on your own lab target, a separate command is `nmap -p- 127.0.0.1`, but it may take longer.

## Example output format (synthetic)

The following is a made-up example to explain the fields. It is **not captured evidence** and should not be used to claim that a real host was scanned.

```text
Starting Nmap (illustrative output only)
Nmap scan report for localhost (127.0.0.1)
Host is up (example latency).
PORT     STATE  SERVICE  VERSION
22/tcp   open   ssh      OpenSSH (example version)
631/tcp  open   ipp      CUPS (example version)
Nmap done: 1 IP address (1 host up) scanned
```

Actual ports, states, latency, service names, and version strings depend on the target. Do not copy this synthetic output into the evidence folder as if it came from a scan.

## How to interpret the example

| Observation | What it means | Follow-up |
|---|---|---|
| `22/tcp open ssh` | A service identifying itself as SSH responded on TCP port 22 in this hypothetical example. | Confirm whether remote administration is required; review access controls and authentication policy. |
| `631/tcp open ipp` | A service associated with Internet Printing Protocol responded on TCP port 631 in this hypothetical example. | Confirm whether printing is needed and whether the service should be reachable from the relevant network. |
| `open` state | Nmap received a response indicating that an application is accepting connections on the port. | Verify service ownership and intended exposure; an open port alone does not prove a vulnerability. |

## Example findings and recommendations

These are conditional recommendations based on the hypothetical rows above, not findings about an actual system:

1. Confirm each service is required by the system owner.
2. Disable unneeded services through the approved administration process.
3. Restrict management services to trusted hosts or networks where appropriate.
4. Keep required services patched and use strong authentication.
5. Repeat the scan after an approved configuration change and compare actual outputs.

## Limitations

- This report contains no verified scan output.
- Service/version detection can be incomplete or inaccurate.
- A port being open is not, by itself, proof of compromise or a vulnerability.
- Scan only systems within explicit authorization and scope.

## Evidence needed to complete the hands-on version

After running the commands in an authorized lab, replace this illustrative walkthrough with:
- the exact command and date;
- the unedited output saved as `nmap_scan.txt` (sanitize sensitive details before publishing);
- observed ports/services copied from the real output;
- an assessment distinguishing observation from inference;
- a short comparison if a configuration change is made.
