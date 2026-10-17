# Test Scenarios

The cases below describe the expected behavior of the detector when given sample authentication logs.

| Case | Input pattern | Expected result |
|---|---|---|
| TC-01 | Three failed logins for the same user/IP followed by success within five minutes | Alert |
| TC-02 | Fewer than three failures followed by success | No alert |
| TC-03 | Failures occur outside the five-minute window | No alert for expired failures |
| TC-04 | Failures belong to different users or source IPs | Counts remain separate |
| TC-05 | A log line is malformed | Line is skipped safely |

## Example command
Run from this directory:

```bash
python src/detect_login.py logs/sample_auth.log
```

The sample data is expected to produce an alert for `alice` from `192.0.2.10`. Record the actual output after running the command; expected behavior alone is not a test result.

## Limitations
The detector expects time-ordered events in the documented format. It does not model MFA, account lockouts, distributed password spraying, or all possible authentication-log formats.
