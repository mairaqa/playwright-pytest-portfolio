# Requirements Traceability Matrix

**Project:** Playwright Python QA Framework  
**Modules:** Authentication, Checkboxes, JavaScript Alerts, Upload
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

### 2.4 Upload

**Test Module:** `tests/test_upload.py`

| Requirement | Test Case | Automated Test |
|---|---|---|
| Pending | UPL-001 | `test_upload_form_is_displayed` |
| Pending | UPL-002 | `test_upload_file[UPL-002]` |
| Pending | UPL-003 | `test_upload_file[UPL-003]` |
| Pending | UPL-004 | `test_upload_file[UPL-004]` |
| Pending | UPL-005 | `test_upload_file[UPL-005]` |
| Pending | UPL-006 | `test_upload_file[UPL-006]` |
| Pending | UPL-007 | `test_upload_without_file` |
| Pending | UPL-008 | `test_upload_using_drag_and_drop` |

## 3. Automation Coverage

### 3.1 Coverage by Module

| Metric | Authentication | Checkboxes | JavaScript Alerts | Upload | Total |
|---|---:|---:|---:|---:|---:|
| Defined requirements | 6 | 6 | 7 | 7 | 26 |
| Defined test cases | 8 | 8 | 7 | 8 | 31 |
| Automated test functions | 5 | 6 | 2 | 4 | 17 |
| Planned pytest executions | 8 | 9 | 9 | 8 | 34 |
| Requirements mapped to automation | 6 | 6 | 7 | Pending | Pending |
| Planned requirement mapping coverage | 100% | 100% | 100% | Pending | Pending |
| Verified execution coverage | Pending | Pending | Pending | Pending | Pending |


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
- `tests/test_upload.py`

**Reporting Tools:**
- Allure Report — Consolidated HTML report containing results from Chromium, Firefox, and WebKit.
- JUnit XML — Test execution results and CI/CD integration.
- dorny/test-reporter — Automated test results published through GitHub Checks and GitHub Actions Summary.
- Playwright Trace Viewer — Browser trace analysis for failed tests.

**Execution Configuration:**
- Environment selection through `--env`.
- Cross-browser execution using Chromium, Firefox, and WebKit.
- Parallel browser execution through GitHub Actions Matrix.
- Sequential test execution within each browser job (`-n 0`).
- Optional test-level parallelism through `pytest-xdist`.
- Browser configuration through `pytest-playwright`.
- Environment-specific configuration and credentials.
- Automated CI/CD execution on pushes, pull requests targeting `main`, and manual workflow dispatch.

**Execution Status:** Automated cross-browser execution is configured in GitHub Actions. Successful execution coverage must be verified against the latest CI results and generated reports.

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
4. Upload

The framework currently includes 26 documented functional requirements and 31 documented test cases, represented by 17 automated test functions and 34 pytest executions per browser.

The CHK-005 test case uses two independent pytest parameterizations to verify checkbox independence in both directions.

Requirement mapping coverage for Upload is pending final verification against its requirements and test-case documentation.

Execution results must be verified using current pytest, GitHub Actions, and Allure reports before claiming successful cross-browser execution coverage.

## 7. Related Documentation

**Functional Requirements:**
- `docs/requirements/authentication.md`
- `docs/requirements/checkboxes.md`
- `docs/requirements/javascript_alerts.md`
- `docs/requirements/upload.md`

**Test Cases:**
- `docs/test-cases/authentication.md`
- `docs/test-cases/checkboxes.md`
- `docs/test-cases/javascript_alerts.md`
- `docs/test-cases/upload.md`