# Test Plan and Results

## Purpose

I use these cases to check both the expected alert path and situations where the detector should remain quiet. The input data is synthetic.

| ID | Scenario | Expected behavior | Recorded result |
|---|---|---|---|
| TC-01 | Three failures followed by success within five minutes for the same user/IP | Raise an alert | PASS |
| TC-02 | Only two failures followed by success | No alert | PASS |
| TC-03 | Three failures followed by success after the five-minute window | No alert | PASS |
| TC-04 | Failures belong to different users | Do not combine the counts | PASS |
| TC-05 | Malformed log line | Ignore the malformed line | PASS |

## Reproduce the tests

From the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

The saved terminal output is in `../evidence/unit_test_output.txt`.

## Notes

These tests validate the listed cases only. They do not prove that the detector is production-ready, and a matching pattern is not proof of account compromise. Additional tests should cover out-of-order timestamps, timezone handling, repeated successful logins, and malformed timestamps.
