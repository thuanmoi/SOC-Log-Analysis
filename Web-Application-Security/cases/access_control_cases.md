# Fictional Access-Control Cases

All examples below are fictional and intended for an authorized training lab.

## Case A: Own object
- User A signs in and requests object A.
- Expected: the application returns object A if the user is authorized.

## Case B: Different user's object
- User A requests object B, which belongs to User B.
- Expected: the server denies access or returns a safe not-found response.
- Risk if authorization is missing: User A may view or modify data belonging to User B.

## Case C: Unauthenticated request
- A request is made without a valid session.
- Expected: authentication is required before protected data is returned.

## Review note
Changing an identifier alone does not prove a vulnerability. The key question is whether the server enforces authorization for the authenticated principal and requested object.
