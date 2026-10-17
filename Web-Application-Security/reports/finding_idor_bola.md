# Finding: Potential Broken Object-Level Authorization (IDOR/BOLA)

## Status
Fictional training case study; not a finding from a live penetration test.

## Severity
Not assigned. Severity depends on verified impact, data sensitivity, exploitability, and the application's context.

## Description
An application may be vulnerable when it relies on a user-supplied object identifier without checking whether the authenticated user is authorized to access that object.

## Expected behavior
The server checks authorization on every request for the specific object and operation.

## Safe validation plan
1. Use two test accounts in an authorized lab.
2. Create harmless test records owned by each account.
3. Verify that each account can access its own record.
4. Attempt the corresponding request for the other test account's record.
5. Record only the minimum evidence needed and avoid real user data.

## Remediation
- Enforce server-side object-level authorization for read and write operations.
- Deny by default.
- Add automated tests for cross-user access.
- Review logs for suspicious access patterns where appropriate.

## Evidence
No live evidence collected. Attach request/response excerpts only after safe, authorized lab testing.
