# Sample Alert Triage Report

## Status
Training exercise — synthetic data only.

## Summary
The detector identifies three failed login attempts followed by a successful login for user `alice` from `192.0.2.10` within the configured five-minute window.

## Evidence
- 09:30:01Z — login failed
- 09:30:04Z — login failed
- 09:30:07Z — login failed
- 09:30:10Z — login succeeded

## Assessment
This pattern may indicate repeated password guessing followed by a successful authentication. The log alone does not prove that the account was compromised.

## Recommended investigation
1. Verify whether the source, device, and login time are expected.
2. Review MFA results, surrounding authentication events, and account activity.
3. Check for new accounts, privilege changes, and unusual access after login.
4. Preserve relevant logs and escalate according to the organization's incident-response process.
5. Contain the account or source only with appropriate authorization and according to policy.

## Limitations
All timestamps and events are synthetic. No real incident or production system was investigated.
