# Authentication — Test Cases

**Module:** Authentication  
**Application:** The Internet — Form Authentication  
**Test level:** System / End-to-End  
**Test type:** Functional  
**Automation framework:** Playwright + Python + pytest  
**Automation file:** `tests/test_login.py`

## 1. Objective

Verify that the application authenticates users with valid credentials, rejects invalid login attempts, restricts access to protected resources, and correctly handles logout.

## 2. Test Cases Overview

| ID | Test Case | Priority | Type |
|---|---|---|---|
| AUTH-001 | Login with valid credentials | High | Positive |
| AUTH-002 | Logout after successful login | High | Positive |
| AUTH-003 | Login with invalid username | High | Negative |
| AUTH-004 | Login with invalid password | High | Negative |
| AUTH-005 | Access secure page without authentication | High | Security / Negative |
| AUTH-006 | Login with empty username | Medium | Negative |
| AUTH-007 | Login with empty password | Medium | Negative |
| AUTH-008 | Access secure page after logout | High | Security / Negative |

## 3. Test Case Specifications

### AUTH-001 — Login with valid credentials

**Priority:** High  
**Preconditions:** The user is not authenticated. Valid test credentials are configured for the execution environment.

**Steps:**
1. Navigate to the login page.
2. Enter a valid username.
3. Enter a valid password.
4. Click the Login button.

**Expected Results:**
- The user is redirected to `/secure`.
- The Secure Area is displayed.
- The authenticated username is displayed.
- The Logout button is visible.

### AUTH-002 — Logout after successful login

**Priority:** High  
**Preconditions:** The user is authenticated.

**Steps:**
1. Navigate to the Secure Area.
2. Click the Logout button.

**Expected Results:**
- The user is redirected to `/login`.
- The login form is displayed.
- The message "You logged out of the secure area!" is displayed.

### AUTH-003 — Login with invalid username

**Priority:** High  
**Preconditions:** The user is not authenticated. Valid test credentials are available.

**Steps:**
1. Navigate to the login page.
2. Enter a non-existent username.
3. Enter a valid password.
4. Click the Login button.

**Expected Results:**
- Authentication is rejected.
- The user remains on `/login`.
- The message "Your username is invalid!" is displayed.

### AUTH-004 — Login with invalid password

**Priority:** High  
**Preconditions:** The user is not authenticated. A valid username is available.

**Steps:**
1. Navigate to the login page.
2. Enter a valid username.
3. Enter an incorrect password.
4. Click the Login button.

**Expected Results:**
- Authentication is rejected.
- The user remains on `/login`.
- The message "Your password is invalid!" is displayed.

### AUTH-005 — Access secure page without authentication

**Priority:** High  
**Preconditions:** The browser context has no authenticated session.

**Steps:**
1. Navigate directly to `/secure`.

**Expected Results:**
- Access to the protected page is denied.
- The user is redirected to `/login`.
- The message "You must login to view the secure area!" is displayed.

### AUTH-006 — Login with empty username

**Priority:** Medium  
**Preconditions:** The user is not authenticated.

**Steps:**
1. Navigate to the login page.
2. Leave the username field empty.
3. Enter a valid password.
4. Click the Login button.

**Expected Results:**
- Authentication is rejected.
- The user remains on `/login`.
- The message "Your username is invalid!" is displayed.

### AUTH-007 — Login with empty password

**Priority:** Medium  
**Preconditions:** The user is not authenticated.

**Steps:**
1. Navigate to the login page.
2. Enter a valid username.
3. Leave the password field empty.
4. Click the Login button.

**Expected Results:**
- Authentication is rejected.
- The user remains on `/login`.
- The message "Your password is invalid!" is displayed.

### AUTH-008 — Access secure page after logout

**Priority:** High  
**Preconditions:** The user has successfully authenticated.

**Steps:**
1. Click the Logout button.
2. Confirm that the login page is displayed.
3. Navigate directly to `/secure` without authenticating again.

**Expected Results:**
- Access to the Secure Area is denied.
- The user is redirected to `/login`.
- The message "You must login to view the secure area!" is displayed.

## 4. Test Data Management

- Valid credentials are provided through environment configuration and pytest fixtures.
- Secrets must not be stored in source control.
- Invalid usernames and passwords use synthetic test data.
- Authentication tests must run in isolated browser contexts.
- Each execution environment must provide its own valid credentials.

## 5. Automation Mapping

| Test Case ID | Automated Test | Parameter ID |
|---|---|---|
| AUTH-001 | `test_login_with_valid_credentials` | — |
| AUTH-002 | `test_logout_after_successful_login` | — |
| AUTH-003 | `test_login_with_invalid_credentials` | `AUTH-003-invalid-username` |
| AUTH-004 | `test_login_with_invalid_credentials` | `AUTH-004-invalid-password` |
| AUTH-005 | `test_access_secure_page_without_authentication` | — |
| AUTH-006 | `test_login_with_invalid_credentials` | `AUTH-006-empty-username` |
| AUTH-007 | `test_login_with_invalid_credentials` | `AUTH-007-empty-password` |
| AUTH-008 | `test_access_secure_page_after_logout` | — |

## 6. Execution Status

**Status:** Not verified

The test cases have been defined and automation code has been prepared. Execution results must be obtained from pytest before marking individual cases as passed or failed.