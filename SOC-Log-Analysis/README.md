# SOC Log Analysis

## Overview
This project uses Python to review sample authentication logs and flag a pattern that may need investigation: repeated failed logins followed by a successful login from the same user and source IP within five minutes.

## Files
- `logs/sample_auth.log` — sample authentication events using documentation-range IP addresses.
- `src/detect_login.py` — log parsing and detection logic.
- `tests/test_cases.md` — test scenarios and known limitations.
- `reports/incident_report.md` — example triage report based on the sample events.

## Run
Requires Python 3.9+ and uses the standard library. From this folder, run:

```bash
python src/detect_login.py logs/sample_auth.log
```

## Detection logic
The script groups events by user and source IP, counts failed attempts within the configured time window, and checks whether a successful login follows. A matching pattern is an alert for review, not proof that an account was compromised.

## Limitations
The sample data is synthetic. The script expects the documented log format and time-ordered events, and it does not replace a SIEM or a full incident investigation.
