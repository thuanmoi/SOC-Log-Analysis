# SOC Log Analysis — Authentication Anomaly Detection

## Project overview

This project demonstrates a small SOC Tier 1 workflow: parse authentication events, correlate repeated failures with a later successful login, and produce a triage alert for further investigation.

The detector flags three or more failed login attempts followed by a successful login for the same username and source IP within five minutes. An alert is a lead for investigation, not proof of account compromise.

## What it demonstrates

- Python log parsing using the standard library.
- Correlation by username and source IP.
- Threshold and time-window logic.
- Handling malformed events and timezone-aware timestamps.
- Unit tests for expected, negative, and edge-case behavior.
- Basic analyst triage and documenting limitations.

## Repository structure

```text
SOC-Log-Analysis/
├── logs/sample_auth.log
├── src/detect_login.py
├── tests/
│   ├── test_cases.md
│   └── test_detector.py
├── reports/
│   ├── incident_report.md
│   └── execution_report.md
└── evidence/
    ├── README.md
    └── sample_run_output.txt
```

## Run locally

Requires Python 3.9+ and no third-party packages. Run these commands from this directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Validation

A GitHub Actions workflow runs the unit tests on pushes and pull requests. See the repository's **Actions** tab for the current result. Do not treat an old saved output file as evidence for the current code version.

- [Test plan](tests/test_cases.md)
- [Execution and triage report](reports/execution_report.md)
- [Incident report](reports/incident_report.md)
- [Sample log](logs/sample_auth.log)

## Analyst interpretation

Repeated failures followed by a success can be consistent with password guessing, but may also be caused by a user repeatedly entering an incorrect password. In a real SOC workflow, validate the source and device, check MFA results, compare the activity with the user's normal behavior, and review post-login actions before recommending containment.

## Scope and limitations

- The included events are synthetic and use documentation-range IP addresses.
- Only timezone-aware ISO timestamps and the documented event types are accepted.
- Events are processed chronologically, and original line numbers are retained for traceability.
- This is a learning detector, not a production SIEM or a complete incident-response solution.
