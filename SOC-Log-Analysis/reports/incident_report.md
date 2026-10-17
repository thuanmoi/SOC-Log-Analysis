# Authentication Alert — Triage Notes

## Context
Training example based on synthetic log entries.

## Observed pattern
The sample log contains three failed login attempts followed by a successful login for `alice` from `192.0.2.10` within the configured five-minute window.

- 09:30:01Z — login failed
- 09:30:04Z — login failed
- 09:30:07Z — login failed
- 09:30:10Z — login succeeded

## Initial assessment
Repeated failures followed by success can be consistent with password guessing, but this pattern alone does not prove compromise. The source and timing need to be checked against normal activity.

## Suggested follow-up
1. Confirm whether the source, device, and login time are expected.
2. Review nearby authentication events and MFA results.
3. Check for unusual activity after login, including new accounts or privilege changes.
4. Preserve relevant logs and follow the organization's incident-response process.
5. Contain an account or source only under the appropriate authorization and policy.

## Limitations
The timestamps and events are synthetic and do not describe a real incident.
