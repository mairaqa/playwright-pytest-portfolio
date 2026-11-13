# Requirements Traceability Matrix

**Project:** Playwright Python QA Framework  
**Modules:** Authentication, Checkboxes, JavaScript Alerts  
**Version:** 1.1  
**Status:** Draft — Pending execution verification

## 1. Purpose

Provide traceability between functional requirements, test cases, and automated tests across all implemented modules.

The traceability matrix supports requirement coverage analysis, test maintenance, impact assessment, and identification of gaps between documented requirements and automation.

## 2. Traceability Matrix

### 2.1 Authentication

**Test Module:** `tests/test_login.py`

| Requirement | Test Case | Automated Test |
|---|---|---|
| REQ-AUTH-001 | AUTH-001 | `test_login_with_valid_credentials` |
| REQ-AUTH-002 | AUTH-003 | `test_login_with_invalid_credentials[AUTH-003-invalid-username]` |
| REQ-AUTH-002 | AUTH-004 | `test_login_with_invalid_credentials[AUTH-004-invalid-password]` |
| REQ-AUTH-003 | AUTH-006 | `test_login_with_invalid_credentials[AUTH-006-empty-username]` |
| REQ-AUTH-003 | AUTH-007 | `test_login_with_invalid_credentials[AUTH-007-empty-password]` |
| REQ-AUTH-004 | AUTH-005 | `test_access_secure_page_without_authentication` |
| REQ-AUTH-005 | AUTH-002 | `test_logout_after_successful_login` |
| REQ-AUTH-006 | AUTH-008 | `test_access_secure_page_after_logout` |

### 2.2 Checkboxes

**Test Module:** `tests/test_checkboxes.py`

| Requirement | Test Case | Automated Test |
|---|---|---|
| REQ-CHK-001 | CHK-001 | `test_checkboxes_are_displayed` |
| REQ-CHK-002 | CHK-002 | `test_initial_checkbox_states` |
| REQ-CHK-003 | CHK-003 | `test_change_checkbox_state[CHK-003-check-checkbox]` |
| REQ-CHK-003 | CHK-004 | `test_change_checkbox_state[CHK-004-uncheck-checkbox]` |
| REQ-CHK-004 | CHK-005 | `test_checkbox_independence[CHK-005-first-to-second]` |
| REQ-CHK-004 | CHK-005 | `test_checkbox_independence[CHK-005-second-to-first]` |
| REQ-CHK-005 | CHK-006 | `test_toggle_checkbox_multiple_times` |
| REQ-CHK-006 | CHK-007 | `test_set_all_checkboxes[CHK-007-check-all]` |
| REQ-CHK-006 | CHK-008 | `test_set_all_checkboxes[CHK-008-uncheck-all]` |

### 2.3 JavaScript Alerts

**Test Module:** `tests/test_javascript_alerts.py`

| Requirement | Test Case | Automated Test |
|---|---|---|
| REQ-JSA-001 | JSA-001 | `test_javascript_dialog_actions[JSA-001-accept-alert]` |
| REQ-JSA-002 | JSA-002 | `test_javascript_dialog_actions[JSA-002-accept-confirm]` |
| REQ-JSA-003 | JSA-003 | `test_javascript_dialog_actions[JSA-003-dismiss-confirm]` |
| REQ-JSA-004 | JSA-004 | `test_javascript_dialog_actions[JSA-004-accept-prompt]` |
| REQ-JSA-005 | JSA-005 | `test_javascript_dialog_actions[JSA-005-dismiss-prompt]` |
| REQ-JSA-006 | JSA-006 | `test_javascript_dialog_actions[JSA-006-empty-prompt]` |
| REQ-JSA-007 | JSA-007 | `test_javascript_dialog_properties[JSA-007-alert]` |
| REQ-JSA-007 | JSA-007 | `test_javascript_dialog_properties[JSA-007-confirm]` |
| REQ-JSA-007 | JSA-007 | `test_javascript_dialog_properties[JSA-007-prompt]` |

## 3. Automation Coverage

### 3.1 Coverage by Module

| Metric | Authentication | Checkboxes | JavaScript Alerts | Total |
|---|---:|---:|---:|---:|
| Defined requirements | 6 | 6 | 7 | 19 |
| Defined test cases | 8 | 8 | 7 | 23 |
| Automated test functions | 5 | 6 | 2 | 13 |
| Planned pytest executions | 8 | 9 | 9 | 26 |
| Requirements mapped to automation | 6 | 6 | 7 | 19 |
| Planned requirement mapping coverage | 100% | 100% | 100% | 100% |
| Verified execution coverage | Pending | Pending | Pending | Pending |

### 3.2 Coverage Definitions

**Requirement Mapping Coverage**

Percentage of defined requirements linked to at least one automated test case.

**Automated Test Scenarios**

Individual pytest executions, including parameterized scenarios.

**Verified Execution Coverage**

Percentage of planned automated scenarios that have been successfully executed and verified in the target environment.

The existence of an automated test does not guarantee successful execution or complete functional coverage.

## 4. Execution and Reporting

**Framework:** Python + pytest + Playwright

**Test Modules:**
- `tests/test_login.py`
- `tests/test_checkboxes.py`
- `tests/test_javascript_alerts.py`

**Reporting Tools:**
- Allure Report — Test execution results and reporting
- JUnit XML — CI/CD integration
- Playwright Trace Viewer — Failure investigation

**Execution Configuration:**
- Environment selection through `--env`
- Parallel execution through `pytest-xdist`
- Browser configuration through pytest-playwright
- Environment-specific configuration and credentials

**Execution Status:** Pending verification against actual pytest and Allure results.

## 5. Maintenance Rules

- Each functional requirement must have a unique and stable requirement ID.
- Each test case must reference at least one applicable requirement.
- Automated tests must retain traceable identifiers.
- Parameterized test cases must use stable and descriptive parameter IDs.
- Changes to requirements must trigger a review of related test cases.
- Changes to automated test names or parameter IDs must be reflected in the traceability matrix.
- Execution results must be obtained from pytest or Allure reports.
- Requirement mapping coverage must not be presented as verified functional coverage.
- New functional modules must be added to the matrix when their requirements and test cases are defined.

## 6. Current Status

Three functional modules are included in the traceability matrix:

1. Authentication
2. Checkboxes
3. JavaScript Alerts

All 19 defined requirements are mapped to at least one automated test scenario.

The framework currently includes 23 documented test cases, represented by 13 automated test functions and 26 planned pytest executions.

Actual execution results, test stability, and requirement acceptance must be verified before the modules are considered complete.

The Checkboxes execution count assumes that CHK-005 is parameterized to verify independence in both directions.

## 7. Related Documentation

**Functional Requirements:**
- `docs/requirements/authentication.md`
- `docs/requirements/checkboxes.md`
- `docs/requirements/javascript_alerts.md`

**Test Cases:**
- `docs/test-cases/authentication.md`
- `docs/test-cases/checkboxes.md`
- `docs/test-cases/javascript_alerts.md`