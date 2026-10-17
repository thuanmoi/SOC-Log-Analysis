# Network Traffic Analysis (Synthetic Flow Data)

## Objective
Practice reviewing network-flow records and identifying traffic patterns that may need further investigation.

## Dataset
`data/sample_flows.csv` contains synthetic flow summaries. It is not a packet capture and was not collected from a real network.

## Current scope
- Read structured flow data with Python.
- Identify simple indicators such as unusually high byte counts or repeated connections.
- Document observations and limitations.

## Tools
Python and CSV are used in this version. Wireshark has not been used to capture or inspect real packets for this artifact. A future version can add a lab PCAP and Wireshark screenshots after authorized hands-on practice.

## Limitations
Synthetic data cannot establish that a real attack occurred. A high byte count or repeated connection is only a lead for further investigation.
