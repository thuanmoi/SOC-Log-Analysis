# Network Traffic Analysis

## Overview
This project uses Python to review sample network-flow records and flag entries that may deserve a closer look.

## Input
`data/sample_flows.csv` contains synthetic flow summaries. It is not a PCAP and was not captured from a real network.

## What the script checks
- Byte counts at or above 5,000,000.
- Connection counts of 10 or more.
- Rows that meet both conditions.

These are simple review rules, not proof of malicious activity. High-volume transfers and repeated connections may be normal depending on the system and its role.

## Files
- `data/sample_flows.csv` — sample flow records.
- `src/analyze_flows.py` — analysis script.
- `reports/analysis_report.md` — notes on the sample data.
- `tests/test_cases.md` — expected behavior for test scenarios.

## Current scope
This version analyzes CSV data. It does not include a real packet capture or Wireshark analysis.
