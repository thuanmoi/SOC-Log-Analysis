# Authentication Alert — Triage Notes

## Scenario
Sample authentication events show three failed login attempts followed by a successful login for `alice` from `192.0.2.10` within the configured five-minute window.

- 09:30:01Z — login failed
- 09:30:04Z — login failed
- 09:30:07Z — login failed
- 09:30:10Z — login succeeded

## Example script output

```text
Alerts found: 1
SUSPICIOUS_LOGIN user=alice src_ip=192.0.2.10 failed_attempts=3 success_time=2026-10-01T09:30:10+00:00 line=4
```

## Initial assessment
Repeated failures followed by success can be consistent with password guessing, but this pattern alone does not prove compromise. The source and timing should be checked against normal activity.

## Follow-up steps
1. Confirm whether the source, device, and login time are expected.
2. Review nearby authentication events and MFA results.
3. Check for unusual activity after login, including new accounts or privilege changes.
4. Preserve relevant logs and follow the organization's incident-response process.
5. Contain an account or source only with appropriate authorization and according to policy.

## Limitations
This is a training scenario using synthetic events, not a real incident report.
