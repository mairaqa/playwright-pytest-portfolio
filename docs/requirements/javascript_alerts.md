# JavaScript Alerts — Functional Requirements

**Module:** JavaScript Alerts  
**Application:** The Internet — JavaScript Alerts  
**Version:** 1.0  
**Status:** Draft — Pending validation

## 1. Purpose

Define the functional requirements for displaying and handling native JavaScript browser dialogs, including alerts, confirmations, and prompts.

## 2. Scope

**In scope:**
- JavaScript Alert dialogs
- JavaScript Confirm dialogs
- JavaScript Prompt dialogs
- Dialog acceptance and cancellation
- Text input in prompt dialogs
- Empty prompt submission
- Dialog type and message verification
- Display of results after dialog interaction

**Out of scope:**
- Custom HTML modal dialogs
- Browser permission dialogs
- File selection dialogs
- Before-unload confirmation dialogs
- Multiple simultaneous dialogs
- Browser-specific dialog styling

## 3. Functional Requirements

### REQ-JSA-001 — JavaScript Alert Handling

**Priority:** High

The system shall display a native JavaScript Alert dialog and allow users to acknowledge it.

**Acceptance Criteria:**
- Clicking the JS Alert button opens an alert dialog.
- The dialog can be accepted.
- After acceptance, the page displays "You successfully clicked an alert".

**Related Test Cases:** JSA-001

### REQ-JSA-002 — JavaScript Confirm Acceptance

**Priority:** High

The system shall allow users to accept a JavaScript Confirm dialog.

**Acceptance Criteria:**
- Clicking the JS Confirm button opens a confirmation dialog.
- The dialog provides an acceptance action.
- Accepting the dialog displays "You clicked: Ok".

**Related Test Cases:** JSA-002

### REQ-JSA-003 — JavaScript Confirm Cancellation

**Priority:** High

The system shall allow users to cancel a JavaScript Confirm dialog.

**Acceptance Criteria:**
- The confirmation dialog can be dismissed.
- Dismissing the dialog displays "You clicked: Cancel".
- The application remains accessible after cancellation.

**Related Test Cases:** JSA-003

### REQ-JSA-004 — JavaScript Prompt Text Submission

**Priority:** High

The system shall allow users to enter and submit text through a JavaScript Prompt dialog.

**Acceptance Criteria:**
- Clicking the JS Prompt button opens a prompt dialog.
- The dialog accepts text input.
- Accepting the dialog displays the submitted text.
- The displayed result matches the entered text.

**Related Test Cases:** JSA-004

### REQ-JSA-005 — JavaScript Prompt Cancellation

**Priority:** High

The system shall support cancellation of a JavaScript Prompt dialog.

**Acceptance Criteria:**
- The prompt dialog can be dismissed.
- Cancellation does not submit the entered value.
- The page displays "You entered: null".

**Related Test Cases:** JSA-005

### REQ-JSA-006 — Empty Prompt Submission

**Priority:** Medium

The system shall allow users to accept a JavaScript Prompt dialog without entering text.

**Acceptance Criteria:**
- The prompt accepts an empty string.
- The application handles empty input without displaying an error.
- The page displays "You entered:" with no submitted value.

**Related Test Cases:** JSA-006

### REQ-JSA-007 — Dialog Type and Message

**Priority:** Medium

The system shall display the appropriate native dialog type and message for each JavaScript dialog action.

**Acceptance Criteria:**
- JS Alert opens a dialog of type `alert` with the message "I am a JS Alert".
- JS Confirm opens a dialog of type `confirm` with the message "I am a JS Confirm".
- JS Prompt opens a dialog of type `prompt` with the message "I am a JS prompt".

**Related Test Cases:** JSA-007

## 4. Test Environment Requirements

- The application base URL shall be configurable per environment.
- Tests shall execute in isolated browser contexts.
- Dialog event handlers shall be registered before triggering the corresponding dialog.
- Every dialog opened during testing shall be accepted or dismissed to prevent blocked execution.
- Tests shall not depend on the execution order of other scenarios.

## 5. Requirement Traceability

Each functional requirement shall be linked to at least one test case.

The relationship between requirements, test cases, and automated tests is documented in `docs/traceability.md`.

## 6. Assumptions and Constraints

These requirements are based on the expected behavior of The Internet demonstration application.

Native JavaScript dialogs are controlled by the browser and cannot be located using standard DOM selectors.

The automation uses Playwright's dialog event handling to inspect, accept, or dismiss dialogs.

The expected messages are application-specific and must be validated against the target environment.

These requirements are not externally approved product specifications.