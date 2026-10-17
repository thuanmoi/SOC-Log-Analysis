# Network Flow Review

## Scope
This review uses synthetic CSV flow summaries rather than traffic captured from a live network.

## Patterns flagged by the script
- Rows with at least 5,000,000 bytes are flagged for review.
- Rows with 10 or more connections are flagged for review.
- The sample includes a large transfer from `192.0.2.25` and repeated DNS connections from `192.0.2.31`.

## Interpretation
These patterns are leads for review, not findings of malicious activity. An analyst would need context such as the asset's role, expected traffic, destination, timing, and packet-level details before drawing conclusions.

## Further investigation
In an authorized lab, compare flow-level observations with a PCAP in Wireshark. Record the filters used and note where packet evidence supports or contradicts the initial observations.

## Limitations
The dataset is synthetic. No real packets were captured, so this report makes no claim about an actual network incident.
