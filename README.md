# Project 2: Network Traffic Analysis (CSV-based practice)

## Summary
Analyze a small, simulated network-flow dataset using Python. The exercise groups traffic by source and destination, flags repeated denied connections, and identifies a host making many connection attempts to different destination ports.

## Skills demonstrated
- TCP/IP and port interpretation
- Basic network-event analysis
- Rule-based detection and limitations
- Writing a concise investigation note

## Run
Python 3.9+; standard library only.
```bash
python src/analyze_flows.py data/sample_flows.csv
```

This project uses a CSV export-style sample, not a real packet capture. Do not claim to have performed a live Wireshark capture unless you do so separately.
