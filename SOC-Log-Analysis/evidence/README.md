# Execution Evidence

This folder contains text output captured while validating the project in a temporary Python environment.

- `sample_run_output.txt` — detector output for the included synthetic authentication log.
- `unit_test_output.txt` — output from the five-test Python `unittest` suite.

To reproduce the run from the `SOC-Log-Analysis` directory:

```bash
python src/detect_login.py logs/sample_auth.log
PYTHONPATH=src python -m unittest discover -s tests -v
```

The output is evidence of a controlled run against synthetic data, not a real company incident or a terminal capture from the portfolio owner's personal computer. Do not upload company logs, credentials, or identifying information.
