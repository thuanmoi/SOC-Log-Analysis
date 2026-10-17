# Access-Control Test Matrix

| Case | Signed-in identity | Requested object | Expected result |
|---|---|---|---|
| TC-01 | User A | Object owned by A | Allow if permission is valid |
| TC-02 | User A | Object owned by B | Deny |
| TC-03 | No valid session | Protected object | Require authentication |
| TC-04 | User A | Object A, read operation | Check read permission |
| TC-05 | User A | Object A, update operation | Check update permission separately |

This matrix records expected behavior for a training app. Actual results should be documented only after running the cases in an authorized environment.
