# JavaScript Alerts — Test Cases

**Module:** JavaScript Alerts  
**Application:** The Internet — JavaScript Alerts  
**Test Level:** System / UI  
**Test Type:** Functional  
**Automation Framework:** Playwright + Python + pytest  
**Automation File:** `tests/test_javascript_alerts.py`  
**Status:** Approved — Passed 27/27 test instances across Chromium, Firefox, and WebKit

## 1. Objective

Verify that the application correctly displays and handles native JavaScript dialogs, including alerts, confirmations, and prompts, and displays the appropriate results after user interactions.

## 2. Test Cases Overview

| ID | Test Case | Priority | Requirement |
|---|---|---|---|
| JSA-001 | Accept JavaScript Alert | High | REQ-JSA-001 |
| JSA-002 | Accept JavaScript Confirm | High | REQ-JSA-002 |
| JSA-003 | Dismiss JavaScript Confirm | High | REQ-JSA-003 |
| JSA-004 | Accept JavaScript Prompt with text | High | REQ-JSA-004 |
| JSA-005 | Dismiss JavaScript Prompt | High | REQ-JSA-005 |
| JSA-006 | Accept JavaScript Prompt with empty text | Medium | REQ-JSA-006 |
| JSA-007 | Verify dialog type and message | Medium | REQ-JSA-007 |

## 3. Test Case Specifications

### JSA-001 — Accept JavaScript Alert

**Priority:** High  
**Requirement:** REQ-JSA-001  
**Preconditions:** The JavaScript Alerts page is accessible.

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Alert" button.
3. Accept the alert dialog.

**Expected Results:**
- A native JavaScript Alert dialog is displayed.
- The dialog is accepted successfully.
- The page displays "You successfully clicked an alert".

### JSA-002 — Accept JavaScript Confirm

**Priority:** High  
**Requirement:** REQ-JSA-002  
**Preconditions:** The JavaScript Alerts page is accessible.

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Confirm" button.
3. Accept the confirmation dialog.

**Expected Results:**
- A native JavaScript Confirm dialog is displayed.
- The confirmation is accepted.
- The page displays "You clicked: Ok".

### JSA-003 — Dismiss JavaScript Confirm

**Priority:** High  
**Requirement:** REQ-JSA-003  
**Preconditions:** The JavaScript Alerts page is accessible.

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Confirm" button.
3. Dismiss the confirmation dialog.

**Expected Results:**
- The confirmation dialog is dismissed.
- The page displays "You clicked: Cancel".
- The application remains accessible.

### JSA-004 — Accept JavaScript Prompt with Text

**Priority:** High  
**Requirement:** REQ-JSA-004  
**Preconditions:** The JavaScript Alerts page is accessible.

**Test Data:** `QA testing`

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Prompt" button.
3. Enter "QA testing".
4. Accept the prompt dialog.

**Expected Results:**
- The prompt accepts the entered text.
- The dialog closes after acceptance.
- The page displays "You entered: QA testing".

### JSA-005 — Dismiss JavaScript Prompt

**Priority:** High  
**Requirement:** REQ-JSA-005  
**Preconditions:** The JavaScript Alerts page is accessible.

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Prompt" button.
3. Dismiss the prompt dialog.

**Expected Results:**
- The prompt is dismissed successfully.
- No text is submitted.
- The page displays "You entered: null".

### JSA-006 — Accept JavaScript Prompt with Empty Text

**Priority:** Medium  
**Requirement:** REQ-JSA-006  
**Preconditions:** The JavaScript Alerts page is accessible.

**Test Data:** Empty string (`""`)

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Click the "Click for JS Prompt" button.
3. Leave the input field empty.
4. Accept the prompt dialog.

**Expected Results:**
- The prompt accepts the empty input.
- No error is displayed.
- The page displays "You entered:" without a submitted value.

### JSA-007 — Verify Dialog Type and Message

**Priority:** Medium  
**Requirement:** REQ-JSA-007  
**Preconditions:** The JavaScript Alerts page is accessible.

**Test Data:**

| Dialog | Expected Type | Expected Message |
|---|---|---|
| JS Alert | `alert` | I am a JS Alert |
| JS Confirm | `confirm` | I am a JS Confirm |
| JS Prompt | `prompt` | I am a JS prompt |

**Steps:**
1. Navigate to `/javascript_alerts`.
2. Trigger the selected JavaScript dialog.
3. Capture the dialog type.
4. Capture the dialog message.
5. Dismiss the dialog.
6. Repeat independently for each dialog type.

**Expected Results:**
- Each button opens the correct native dialog type.
- Each dialog displays its expected message.
- Each dialog can be dismissed without blocking the test execution.

## 4. Test Data

The module uses predefined dialog types, actions, messages, and input values.

Test data is stored in:

`data/javascript_alert_cases.py`

The module contains two data models:

- `DialogActionCase`: defines dialog actions and expected page results.
- `DialogPropertyCase`: defines expected dialog types and messages.

No external credentials or sensitive data are required.

## 5. Automation Mapping

| Test Case ID | Automated Test | Parameter ID |
|---|---|---|
| JSA-001 | `test_javascript_dialog_actions` | `JSA-001-accept-alert` |
| JSA-002 | `test_javascript_dialog_actions` | `JSA-002-accept-confirm` |
| JSA-003 | `test_javascript_dialog_actions` | `JSA-003-dismiss-confirm` |
| JSA-004 | `test_javascript_dialog_actions` | `JSA-004-accept-prompt` |
| JSA-005 | `test_javascript_dialog_actions` | `JSA-005-dismiss-prompt` |
| JSA-006 | `test_javascript_dialog_actions` | `JSA-006-empty-prompt` |
| JSA-007 | `test_javascript_dialog_properties` | `JSA-007-alert`, `JSA-007-confirm`, `JSA-007-prompt` |

## 6. Execution Status

**Status:** Passed — 27/27 test instances across Chromium, Firefox, and WebKit.

Seven test cases are implemented through two parametrized functions, producing nine executions per browser. All dialog action, result, type, and message checks passed in the successful full cross-browser run recorded in the traceability matrix.

## 7. Notes

- Native browser dialogs are handled using Playwright's dialog events.
- Dialog handlers are registered before triggering the corresponding dialog.
- Dialog type and message assertions are performed using the captured dialog properties.
- The expected messages are specific to The Internet demonstration application.
- The scenarios must be independent and must not rely on execution order.
- JSA-007 verifies three dialog types through separate parameterized executions.