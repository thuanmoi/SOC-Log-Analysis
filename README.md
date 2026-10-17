# Security Engineer Portfolio

Hi, I'm building this repository as I prepare for a Fresher Security Engineer role. My current focus is on the basics: reading logs, understanding network traffic, and documenting web access-control issues.

The projects below are learning exercises. Some use generated sample data and one is a fictional case study, so I have labelled those clearly instead of presenting them as work on real systems.

## Projects

### 1. SOC Log Analysis
[Open project](SOC-Log-Analysis/)

A small Python script that looks through sample authentication logs for repeated failed logins followed by a successful login. The folder includes the sample log, detection code, test scenarios, and an example incident report.

### 2. Network Traffic Analysis
[Open project](Network-Traffic-Analysis/)

A Python exercise using a made-up CSV of network-flow records. It flags a couple of simple patterns for review. This is not a packet capture, and I have not described it as a Wireshark investigation.

### 3. Web Application Security
[Open project](Web-Application-Security/)

A written IDOR/BOLA case study covering what to check, what evidence would matter, and how access control should be fixed. The examples are fictional; no live website was tested.

### 4. Nmap Network Scanning
[Open project](Nmap-Network-Scanning/)

I have prepared a scope checklist and report template for an authorized lab scan. The actual scan and its findings still need to be added after I have a suitable lab environment.

## What I have used so far

For the current files, I have worked with Python, text and CSV sample data, Markdown, and GitHub. Nmap, Wireshark, Burp Suite/OWASP ZAP, and SIEM tools are next on my practice list; I won't list them as hands-on experience until I have actually used them and can show the results.

## Notes

- Sample logs and flow data are synthetic.
- The web security scenario is fictional.
- No company or third-party systems were tested for these exercises.
- I will add screenshots and command output as I complete authorized lab work, with sensitive information removed.

See [Portfolio Status](PORTFOLIO_STATUS.md) for what is documented and what remains to be done.
