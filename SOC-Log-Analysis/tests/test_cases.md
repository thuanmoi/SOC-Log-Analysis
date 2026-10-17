# Test Scenarios

The following cases describe the detector's expected behavior with the sample authentication logs.

| Case | Input pattern | Expected result |
|---|---|---|
| TC-01 | Three failed logins for the same user/IP followed by success within five minutes | Alert |
| TC-02 | Fewer than three failures followed by success | No alert |
| TC-03 | Three failures followed by success outside the five-minute window | No alert |
| TC-04 | Failures split across users or source IPs | No combined alert |
| TC-05 | Malformed line among valid entries | Malformed line skipped |

## Run locally

Open the `SOC-Log-Analysis` folder in Visual Studio Code, open its integrated terminal, and run:

```bash
python src/detect_login.py logs/sample_auth.log
```

## Example output

With the current sample log, the script should report one alert for `alice` from `192.0.2.10`:

```text
Alerts found: 1
SUSPICIOUS_LOGIN user=alice src_ip=192.0.2.10 failed_attempts=3 success_time=2026-10-01T09:30:10+00:00 line=4
```

## Limitations

- Input events are expected to be ordered by timestamp.
- The parser accepts the documented log format only.
- The detector is a small learning project, not a production detection system.
- The example uses synthetic data and does not represent a real incident.
