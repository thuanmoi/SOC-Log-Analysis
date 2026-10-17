# Test Scenarios

The following cases describe the expected behavior of the CSV analysis script. The current implementation silently skips a row when either required numeric field is missing or cannot be converted to an integer.

| Case | Input | Expected behavior |
|---|---|---|
| TC-01 | Byte count at or above 5,000,000 | Flag with `high_bytes` |
| TC-02 | Connection count of at least 10 | Flag with `many_connections` |
| TC-03 | Both thresholds met | Include both reasons |
| TC-04 | Low byte and connection counts | Do not flag |
| TC-05 | Missing or non-integer `bytes` / `connection_count` value | Skip that row without stopping the analysis |

## Run locally

Open the `Network-Traffic-Analysis` folder in Visual Studio Code, open its integrated terminal, and run:

```bash
python src/analyze_flows.py data/sample_flows.csv
python -m unittest discover -s tests -v
```

The automated tests cover both thresholds, the case where both rules match, rows below the thresholds, invalid numeric fields, and preservation of row numbers and addresses.

## Example output

With the current sample CSV, three rows should be flagged for review:

```text
Rows flagged for review: 3
REVIEW row=5 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=8500000 connections=1
REVIEW row=6 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=7900000 connections=1
REVIEW row=7 src_ip=192.0.2.31 dst_ip=203.0.113.53 reasons=many_connections bytes=700 connections=15
```

## Limitations

- This is analysis of synthetic CSV flow summaries, not a real PCAP or Wireshark capture.
- Thresholds are simple review rules; a flagged row is not proof of malicious activity.
