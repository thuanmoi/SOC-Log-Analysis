# Execution and Validation Report — Authentication Anomaly Detector

## Objective

Check whether the detector identifies repeated failed logins followed by a success for the same username and source IP, and document how to reproduce the check.

## Environment and data

- Runtime target: Python 3.9+
- Dependencies: Python standard library only
- Input: `logs/sample_auth.log`
- Data classification: synthetic demonstration events; no company or production logs

## Reproduce

Run from the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Validation result

The user confirmed that the latest GitHub Actions run for the recent detector and test changes completed successfully, including the unit-test and sample-log steps. The configured job runs the detector unit tests and then the script against the sample log. See the repository's Actions tab for the run details.

This verifies that the configured automated checks passed in GitHub Actions; it does not by itself establish production readiness or prove that the detector has been used against real company logs.

## Expected sample behavior

The included sample contains three failed logins for `alice` from `192.0.2.10`, followed by a successful login within five minutes. The expected alert shape is:

```text
Alerts found: 1
SUSPICIOUS_LOGIN user=alice src_ip=192.0.2.10 failed_attempts=3 success_time=2026-10-01T09:30:10+00:00 line=4
```

## Triage interpretation

Several failed logins followed by a success may be consistent with password guessing, but can also result from a legitimate user mistyping a password. The pattern alone does not confirm compromise. For a real alert, validate the source IP, device, time, MFA outcome, and nearby authentication events, then inspect relevant post-login activity.

## Current detection behavior

- Groups events by username and source IP.
- Uses a configurable failure threshold and time window.
- Processes parsed events chronologically while retaining original line numbers.
- Ignores malformed lines, timezone-naive timestamps, and unsupported event types.
- Rejects invalid thresholds and non-positive, non-finite, or excessively large time-window values.
- Treats the five-minute boundary as inclusive: a failure exactly five minutes before success remains in the window.

## Limitations

The data is synthetic and the parser supports only the documented format. This is a learning exercise, not a production SIEM or a complete incident-response solution. Real-world use would require vendor-specific parsing, stronger data validation, monitoring, and review of false positives and false negatives.

## Evidence provenance

The GitHub Actions run is the evidence for the automated checks described above. The sample output shown here is the expected behavior derived from the sample data and detector logic, not a separately captured terminal transcript. Keep future saved outputs labelled with the code version and command that produced them.
