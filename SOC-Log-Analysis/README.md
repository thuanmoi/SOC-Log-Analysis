# SOC Log Analysis — Authentication Anomaly Detection

## Project overview

I built this small Python project to practice a common SOC Tier 1 task: reviewing authentication logs and identifying a login pattern that deserves investigation.

The detector looks for three or more failed login attempts followed by a successful login for the same username and source IP within five minutes. A matching event is treated as a triage alert, not proof that an account has been compromised.

## Objectives

- Parse line-based authentication events.
- Correlate failed and successful login events by user and source IP.
- Apply a configurable threshold and time window.
- Test expected and edge-case behavior.
- Write a short analyst-style triage report.

## Repository structure

```text
SOC-Log-Analysis/
├── logs/
│   └── sample_auth.log
├── src/
│   └── detect_login.py
├── tests/
│   ├── test_cases.md
│   └── test_detector.py
├── reports/
│   ├── incident_report.md
│   └── execution_report.md
└── evidence/
    ├── README.md
    ├── sample_run_output.txt
    └── unit_test_output.txt
```

## How I approached the problem

1. Defined a simple log format containing timestamp, username, source IP, and event type.
2. Parsed each line and skipped entries that do not match the expected format.
3. Tracked failed attempts separately for each user/IP pair.
4. Removed failures older than the five-minute window.
5. Raised an alert when a successful login followed at least three failures in the active window.
6. Added unit tests for the main detection path and several negative/edge cases.

## Run the project

Requires Python 3.9+ and no third-party packages. Run these commands from this directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Result

With the included sample data, the detector identifies one suspicious sequence for user `alice` from `192.0.2.10`. The repeatable unit-test suite covers five scenarios; the recorded run shows all five tests passing.

- [Sample execution output](evidence/sample_run_output.txt)
- [Unit-test output](evidence/unit_test_output.txt)
- [Execution and triage notes](reports/execution_report.md)

## Analyst interpretation

Repeated failures followed by a success can be consistent with password guessing or a user repeatedly entering an incorrect password. The pattern alone is insufficient to confirm compromise. In a real SOC workflow, I would validate the source and device, check MFA results, compare the activity with the user's normal behavior, and review post-login actions before recommending containment.

## Scope and limitations

- The included log events are synthetic and use documentation-range IP addresses.
- The script expects events to be ordered by timestamp and to follow the documented format.
- This is a learning detector, not a production SIEM or a complete incident-response solution.
- The saved execution artifacts document a controlled Python run used to validate the project; they are not logs from a real company environment.

## Skills practiced

Python log parsing, basic event correlation, threshold-based detection, unit testing, alert triage, incident-report writing, and documenting limitations.
