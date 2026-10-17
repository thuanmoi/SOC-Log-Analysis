# Test Plan and Results

## Purpose

These cases check the main detection path, negative cases, and input-handling edge cases. All log events are synthetic.

| ID | Scenario | Expected behavior | Verification status |
|---|---|---|---|
| TC-01 | Three failures followed by success within five minutes for the same user/IP | Raise one alert | Awaiting CI run |
| TC-02 | Only two failures followed by success | No alert | Awaiting CI run |
| TC-03 | Failures followed by success outside the five-minute window | No alert | Awaiting CI run |
| TC-04 | Failures belong to different users | Do not combine counts | Awaiting CI run |
| TC-05 | Failures belong to different source IPs | Do not combine counts | Awaiting CI run |
| TC-06 | Malformed line or invalid timestamp | Ignore invalid input | Awaiting CI run |
| TC-07 | Timestamp has no timezone | Ignore the event | Awaiting CI run |
| TC-08 | Unknown event type | Ignore the event | Awaiting CI run |
| TC-09 | Input lines are out of chronological order | Process chronologically and preserve source line number | Awaiting CI run |
| TC-10 | Custom threshold | Apply the configured threshold | Awaiting CI run |
| TC-11 | Zero/invalid threshold or window | Raise a clear `ValueError` | Awaiting CI run |

## Reproduce locally

From the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs the same test command on pushes and pull requests. Until that workflow completes, this document intentionally does not claim the expanded suite has passed.

## Scope and limitations

These unit tests cover only the documented behavior. A matching pattern is not proof of account compromise. The script accepts timezone-aware ISO timestamps and the documented event types; it does not parse arbitrary vendor-specific logs or provide production-grade alerting.
