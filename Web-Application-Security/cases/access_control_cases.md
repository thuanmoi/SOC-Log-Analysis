# Access-Control Scenarios

These examples describe behavior to check in an authorized training application.

## Case A — Own record
User A signs in and requests a record owned by User A.

**Expected:** the server returns the record if the account has the required permission.

## Case B — Another user's record
User A signs in and requests a record owned by User B.

**Expected:** the server denies access or returns a safe not-found response.

**Potential impact if authorization is missing:** one user may view or change another user's data.

## Case C — No valid session
A request is made without a valid session.

**Expected:** the application requires authentication before returning protected data.

## Review note
An identifier change alone is not enough to establish IDOR/BOLA. The key check is whether the server enforces object-level authorization for the signed-in user and requested operation.
