# Network Traffic Analysis — Simulated Dataset

## Objective
Identify repeated denied connections and a pattern that may be consistent with port scanning.

## Finding
The sample contains multiple denied TCP connections from `192.0.2.44` to `192.0.2.80` across distinct destination ports in a short period.

## Interpretation
This is consistent with service discovery or port scanning, but may also result from an authorized test or a misconfigured application. A firewall `DENY` record indicates that a policy blocked the observed connection; it does not by itself prove malicious intent.

## Follow-up
- Confirm whether the source host and activity were authorized.
- Review surrounding firewall, endpoint, and authentication logs.
- Check destination host exposure and applicable firewall rules.
- Preserve records and escalate according to local procedures.

## Limitations
CSV flow records are not full packet captures. They do not show packet payloads or all protocol details. All addresses and events are illustrative.
