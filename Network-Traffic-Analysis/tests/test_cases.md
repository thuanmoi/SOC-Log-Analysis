# Test Scenarios

| Case | Input | Expected behavior |
|---|---|---|
| TC-01 | Byte count above 5,000,000 | Flag the row with `high_bytes` |
| TC-02 | Connection count of at least 10 | Flag the row with `many_connections` |
| TC-03 | Both conditions match | Flag the row with both reasons |
| TC-04 | Low byte and connection counts | Do not flag the row |
| TC-05 | Invalid numeric field | Skip or handle the row safely, as implemented |

These cases describe expected behavior. Add actual output after running the script against the sample CSV.
