# Run Evidence

The text files in this folder record executions performed in a temporary Python environment for this portfolio update. They are **not screenshots or logs from the user's personal computer**.

- `sample_run_output.txt` — output from running the detector against `logs/sample_auth.log`.
- `unit_test_output.txt` — output from the repeatable Python `unittest` suite.

Reproduce locally from the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

The log events are synthetic and use documentation-range IP addresses. Passing tests demonstrate expected behavior for these cases only; they do not prove production readiness or that an account was compromised. Do not upload company logs, credentials, or identifying information.
