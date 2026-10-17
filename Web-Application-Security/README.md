# Web Application Security — IDOR/BOLA

## Overview
This project examines object-level authorization: whether an application checks that the signed-in user is allowed to access the specific record requested.

## Scenarios covered
- A user accesses their own record.
- A user requests a record owned by another account.
- A request is made without a valid session.
- Read and update permissions are considered separately.

## Files
- `cases/access_control_cases.md` — example scenarios.
- `tests/test_matrix.md` — expected access-control behavior.
- `reports/finding_idor_bola.md` — case-study write-up and remediation ideas.

## Key point
Changing an object ID does not, by itself, prove a vulnerability. The important question is whether the server checks authorization for the user, object, and requested operation on every request.

## Scope
The current material is a case study, not a report of a live application test. Any hands-on validation should use an intentionally vulnerable training app, dummy accounts, and explicit authorization.
