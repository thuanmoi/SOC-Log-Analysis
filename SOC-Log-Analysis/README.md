# SOC Log Analysis & Incident Triage

A beginner cybersecurity portfolio project demonstrating basic analysis of **simulated authentication logs** with Python.

## Objectives
- Parse authentication events from a text log.
- Identify repeated failed logins followed by a successful login from the same source within a configurable time window.
- Produce a concise alert summary for analyst review.

## Project structure
- `logs/sample_auth.log` — synthetic sample events; IP addresses use documentation ranges.
- `src/detect_login.py` — basic detection script.
- `tests/test_cases.md` — test scenarios and limitations.
- `reports/incident_report.md` — example triage report.

## Requirements
- Python 3.9+ (standard library only).

## Run
From this folder:
```bash
python src/detect_login.py logs/sample_auth.log
```

## Scope and limitations
This project uses synthetic data and is for learning only. Alerts are indicators for investigation, not proof of compromise. The detector is intentionally simple and does not replace a SIEM, correlation engine, or analyst review. No production systems were accessed.
