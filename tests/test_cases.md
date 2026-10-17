# Test cases

| Test | Input | Expected |
|---|---|---|
| T1 | Multiple DENY records from one source | Source deny count printed |
| T2 | One source touches 4+ distinct denied ports on one destination | REVIEW message |
| T3 | No DENY records | No denied-connections message |
| T4 | Missing required CSV column | Clear error |
