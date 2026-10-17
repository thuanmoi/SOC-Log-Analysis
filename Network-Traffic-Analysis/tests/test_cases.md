# Test Scenarios

| Case | Input | Expected behavior |
|---|---|---|
| TC-01 | Byte count above 5,000,000 | Flag row with `high_bytes` |
| TC-02 | Connection count at least 10 | Flag row with `many_connections` |
| TC-03 | Both conditions match | Flag row with both reasons |
| TC-04 | Low byte and connection counts | Do not flag row |
| TC-05 | Invalid numeric field | Skip invalid row safely |

These are documented scenarios. They should be executed and results recorded before claiming the tests have passed.
