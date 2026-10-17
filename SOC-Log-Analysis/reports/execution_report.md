# Execution Report — Authentication Log Detector

## Scope
Executed the Python detector against the repository's synthetic authentication log and ran five repeatable unit tests. This is a controlled learning exercise, not analysis of a real organization's logs.

## Environment
- Runtime: Python 3
- Dependencies: Python standard library only
- Input: `logs/sample_auth.log`
- Commands:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Result
The sample run produced one alert for user `alice` from `192.0.2.10`, with three failed logins followed by a successful login within five minutes. All five unit tests passed: detection within the time window, fewer than three failures, expired failures, events split across users, and malformed input.

See `../evidence/sample_run_output.txt` and `../evidence/unit_test_output.txt` for captured terminal output.

## Analyst interpretation
This sequence is suspicious and merits triage, but it is not proof of compromise. In a real environment, validate the source IP, device, MFA outcome, user travel/context, and activity after login before deciding on containment.

## Provenance and limitations
These commands were run in a temporary Python environment while preparing the repository update, not on the portfolio owner's personal computer. The data is synthetic; no real endpoints or accounts were accessed. The script expects time-ordered events in the documented format and is not a SIEM replacement.
