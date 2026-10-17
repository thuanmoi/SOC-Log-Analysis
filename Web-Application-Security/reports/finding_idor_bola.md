# Case Study: Broken Object-Level Authorization (IDOR/BOLA)

## Context
This is a hypothetical training scenario, not a finding from a live penetration test.

## Issue
An application may expose another user's record if it accepts a user-supplied object identifier without checking whether the signed-in user is allowed to access that object.

## Expected behavior
The server checks authorization for each requested object and operation. A user should not be able to read or modify another user's record merely by changing an identifier.

## How to validate in a lab
1. Use two dummy accounts in an authorized training app.
2. Create harmless records owned by each account.
3. Confirm each account can access its own record.
4. Try the corresponding request for the other account's record.
5. Compare the response with the expected access-control behavior and save minimal, sanitized evidence.

## Recommendations
- Enforce object-level authorization on the server for read and write operations.
- Deny access by default.
- Add automated tests for cross-user access.
- Review logs for unexpected access patterns.

## Severity and evidence
Severity cannot be assigned without verified impact and application context. No live evidence has been collected for this case study.
