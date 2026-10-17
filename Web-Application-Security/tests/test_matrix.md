# Access-Control Test Matrix

| Scenario | Identity | Requested object | Expected result |
|---|---|---|---|
| TC-01 | User A | Object owned by A | Allow if permission is valid |
| TC-02 | User A | Object owned by B | Deny |
| TC-03 | No session | Protected object | Require authentication |
| TC-04 | User A | Object A, read operation | Apply read permission |
| TC-05 | User A | Object A, update operation | Apply update permission separately |

This is a planned test matrix, not evidence that a real application was tested. Record actual results only after running the cases in an authorized lab.
