# Nmap Network Scanning

This project is for learning how to check which hosts and services are visible in a small lab, then explain what the results mean from a security point of view.

**Status:** I have prepared the workflow and report template, but I have not added results from a real Nmap scan yet.

## Before scanning

First, write down the target and confirm that you own it or have permission to test it. Keep the scan inside that agreed scope. Don't scan a company network, public IP, or someone else's device just to practise.

Use [scope-template.md](scope-template.md) to record the target, permission, allowed techniques, and any exclusions.

## What I plan to do

1. Run a basic scan against the approved lab target.
2. Save the command and output so the result can be checked later.
3. Review the ports and service names Nmap reports.
4. Decide which services are expected and which need a closer look.
5. Write recommendations based on the evidence, rather than assuming every open port is a vulnerability.
6. If I make a change in the lab, scan again and compare the result.

## Files

- scope-template.md — record the target and testing permission before starting.
- evidence/ — place for sanitized output from an actual lab scan.
- reports/findings-template.md — report template to fill in after reviewing real output.

## What is not here yet

There is no real scan output in this repository, so I have not drawn conclusions about any host or service. I will add the command, results, and notes after completing a scan in an authorized lab.

Tool: [Nmap](https://nmap.org/)
