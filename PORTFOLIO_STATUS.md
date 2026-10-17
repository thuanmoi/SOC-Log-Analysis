# Portfolio Status

I am using this checklist to keep track of what is in GitHub now and what still needs hands-on evidence. A file or template being present does not mean the test has already been run.

## 1. SOC Log Analysis

- [x] Sample authentication log (synthetic data)
- [x] Python detection script
- [x] Test scenarios and example incident report
- [ ] Run the test scenarios and record the actual output
- [ ] Add a screenshot or text capture of the result

## 2. Network Traffic Analysis

- [x] Sample network-flow CSV (synthetic data)
- [x] Python analysis script
- [x] Analysis notes and test scenarios
- [ ] Capture or obtain a safe training PCAP in an authorized lab
- [ ] Inspect it with Wireshark and record useful filters
- [ ] Add sanitized evidence and actual observations

## 3. Web Application Security

- [x] Fictional IDOR/BOLA scenario
- [x] Access-control test matrix
- [x] Remediation notes
- [ ] Try the cases against an intentionally vulnerable training app
- [ ] Save sanitized request/response evidence using Burp Suite or OWASP ZAP
- [ ] Record what happened, including any cases that did not behave as expected

## 4. Nmap Network Scanning

- [x] Project README and lab-scope checklist
- [x] Findings-report template
- [ ] Run a scan against an authorized lab target
- [ ] Add the command, sanitized output, and interpretation
- [ ] Record any retest after a lab configuration change

## Before calling a project complete

- Keep sample data clearly labelled as synthetic.
- Don't write that a tool was used unless I actually used it.
- Don't call a test a pass until I have run it and checked the output.
- Never commit company logs, credentials, cookies, tokens, customer information, or private network details.
