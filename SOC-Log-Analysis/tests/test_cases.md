# Test Scenarios and Results

The detector was checked in a Python runtime using the source and synthetic sample log stored in this repository. These checks were run outside the user's Google Colab session.

| Case | Input pattern | Expected result | Observed result |
|---|---|---|---|
| TC-01 | Three failed logins for the same user/IP followed by success within five minutes | Alert | Pass |
| TC-02 | Fewer than three failures followed by success | No alert | Pass |
| TC-03 | Three failures followed by success outside the five-minute window | No alert | Pass |
| TC-04 | Failures split across users or source IPs | No combined alert | Pass |
| TC-05 | Malformed line among valid entries | Malformed line skipped | Pass |

## Sample run

Command, run from the `SOC-Log-Analysis` folder:

```bash
python src/detect_login.py logs/sample_auth.log
```

Observed standard output:

```text
Alerts found: 1
SUSPICIOUS_LOGIN user=alice src_ip=192.0.2.10 failed_attempts=3 success_time=2026-10-01T09:30:10+00:00 line=4
```

## Limitations found during review

- Input events are expected to be ordered by timestamp.
- The parser accepts the documented log format only.
- The detector is a small learning example, not a production detection system.
- These results demonstrate checks in the Python runtime used for this review; they do not mean the script was run in the user's Colab session.
