# Network Flow Review

## Scope
This review uses synthetic CSV flow summaries rather than traffic captured from a live network. The script was executed in a Python runtime for this review; no live network was accessed.

## Observed output

The script flagged three rows for review:

```text
Rows flagged for review: 3
REVIEW row=5 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=8500000 connections=1
REVIEW row=6 src_ip=192.0.2.25 dst_ip=198.51.100.80 reasons=high_bytes bytes=7900000 connections=1
REVIEW row=7 src_ip=192.0.2.31 dst_ip=203.0.113.53 reasons=many_connections bytes=700 connections=15
```

## Interpretation
- Rows 5 and 6 exceeded the 5,000,000-byte review threshold.
- Row 7 reached the threshold of 10 connections.
- These patterns are leads for review, not findings of malicious activity. An analyst would need context such as the asset's role, expected traffic, destination, timing, and packet-level details before drawing conclusions.

## Further investigation
In an authorized lab, compare flow-level observations with a PCAP in Wireshark. Record the filters used and note where packet evidence supports or contradicts the initial observations.

## Limitations
The dataset is synthetic. No real packets were captured, so this report makes no claim about an actual network incident.
