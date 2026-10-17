# Test Scenarios and Results

The analysis script was checked in a Python runtime using the source and synthetic CSV stored in this repository. Additional temporary CSV rows were used to check threshold boundaries and malformed numeric values.

| Case | Input | Expected behavior | Observed result |
|---|---|---|---|
| TC-01 | Byte count exactly 5,000,000 | Flag with `high_bytes` | Pass |
| TC-02 | Connection count exactly 10 | Flag with `many_connections` | Pass |
| TC-03 | Both thresholds met | Include both reasons | Pass |
| TC-04 | Low byte and connection counts | Do not flag | Pass |
| TC-05 | Invalid numeric field | Skip the row | Pass |

## Sample run

Command, run from the `Network-Traffic-Analysis` folder:

```bash
python src/analyze_flows.py data/sample_flows.csv
```

Observed standard output:

```text
Rows flagged for review: 3
REVIEW row=5 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=8500000 connections=1
REVIEW row=6 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=7900000 connections=1
REVIEW row=7 src_ip=192.0.2.31 dst_ip=203.0.113.53 reasons=many_connections bytes=700 connections=15
```

## Limitations

- This is analysis of synthetic CSV flow summaries, not a real PCAP or Wireshark capture.
- Thresholds are simple review rules; a flagged row is not proof of malicious activity.
- These results were checked in the Python runtime used for this review, not in the user's Colab session.
