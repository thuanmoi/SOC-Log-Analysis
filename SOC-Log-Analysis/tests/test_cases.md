# Test Plan and Results

## Purpose

These cases check the main detection path, negative cases, and input-handling edge cases. All log events are synthetic.

| ID | Scenario | Expected behavior | Verification status |
|---|---|---|---|
| TC-01 | Three failures followed by success within five minutes for the same user/IP | Raise one alert | Passed in GitHub Actions |
| TC-02 | Only two failures followed by success | No alert | Passed in GitHub Actions |
| TC-03 | Failures followed by success outside the five-minute window | No alert | Passed in GitHub Actions |
| TC-04 | Failures belong to different users | Do not combine counts | Passed in GitHub Actions |
| TC-05 | Failures belong to different source IPs | Do not combine counts | Passed in GitHub Actions |
| TC-06 | Malformed line or invalid timestamp | Ignore invalid input | Passed in GitHub Actions |
| TC-07 | Timestamp has no timezone | Ignore the event | Passed in GitHub Actions |
| TC-08 | Unknown event type | Ignore the event | Passed in GitHub Actions |
| TC-09 | Input lines are out of chronological order | Process chronologically and preserve source line number | Passed in GitHub Actions |
| TC-10 | Custom threshold | Apply the configured threshold | Passed in GitHub Actions |
| TC-11 | Zero/negative/non-finite or excessively large window | Raise a clear `ValueError` | Awaiting CI for latest commit |
| TC-12 | A failure occurs exactly five minutes before success | Count the boundary event because the window is inclusive | Awaiting CI for latest commit |

## Verification evidence

A previous GitHub Actions run passed for commit `29c17e8`. Subsequent changes now handle excessively large finite time windows and add tests for that case and the inclusive five-minute boundary. TC-11 and TC-12 remain awaiting a workflow run for these latest changes. See the repository's Actions tab for the current result.

## Reproduce locally

From the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Scope and limitations

These unit tests cover only the documented behavior. A matching pattern is not proof of account compromise. The script accepts timezone-aware ISO timestamps and the documented event types; it does not parse arbitrary vendor-specific logs or provide production-grade alerting.
