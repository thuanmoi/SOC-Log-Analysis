# Test Cases

All tests use synthetic data and should be treated as basic validation, not comprehensive security testing.

| Case | Input pattern | Expected result |
|---|---|---|
| TC-01 | Three failed logins for same user/IP followed by success within five minutes | Alert |
| TC-02 | Fewer than three failures followed by success | No alert |
| TC-03 | Failures older than five minutes before success | No alert for expired failures |
| TC-04 | Failures for a different user or source IP | Do not combine counts |
| TC-05 | Malformed log line | Ignore line safely |

## Manual check
Run from this directory:
```bash
python src/detect_login.py logs/sample_auth.log
```
Expected: one alert for user `alice` from `192.0.2.10`.

## Limitations
- Assumes events are time-ordered.
- Only recognizes the documented log format.
- Does not model MFA, account lockouts, successful session activity, distributed spraying, or timezone normalization beyond ISO timestamps.
- A match is suspicious behavior, not proof of account compromise.
