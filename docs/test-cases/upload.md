# File Upload — Test Cases

## 1. Test Suite Information

**Module:** File Upload  
**Application:** https://the-internet.herokuapp.com/upload  
**Test Case Prefix:** UPL  
**Framework:** pytest + Playwright (Python)  
**Status:** Draft — Pending execution

## 2. Preconditions

- The application is accessible.
- The selected execution environment is correctly configured.
- Playwright and the required browser are installed.
- Test resources exist under `resources/uploads/`.
- Each test starts with an isolated browser context.

## 3. Test Cases

### UPL-001 — Verify File Upload Form Elements

**Requirement:** REQ-UPL-001  
**Priority:** High  
**Type:** Functional / UI  
**Automation:** `test_upload_form_is_displayed`

**Steps**

1. Navigate to `/upload`.
2. Locate the File Uploader heading.
3. Locate the file input.
4. Locate the Upload button.
5. Verify the availability of the controls.

**Expected Result**

- The heading is visible.
- The file input exists and is enabled.
- The Upload button is visible and enabled.

---

### UPL-002 — Upload a TXT File

**Requirements:** REQ-UPL-002, REQ-UPL-003, REQ-UPL-007  
**Priority:** High  
**Type:** Positive / Functional  
**Test Data:** `sample.txt`  
**Automation:** `test_upload_file[UPL-002-txt]`

**Steps**

1. Navigate to `/upload`.
2. Select `sample.txt`.
3. Submit the upload form.
4. Inspect the upload confirmation.

**Expected Result**

- The application displays "File Uploaded!".
- The displayed filename is `sample.txt`.

---

### UPL-003 — Upload a PDF File

**Requirements:** REQ-UPL-002, REQ-UPL-003, REQ-UPL-007  
**Priority:** High  
**Type:** Positive / Functional  
**Test Data:** `sample.pdf`  
**Automation:** `test_upload_file[UPL-003-pdf]`

**Steps**

1. Navigate to `/upload`.
2. Select `sample.pdf`.
3. Submit the upload form.
4. Inspect the upload confirmation.

**Expected Result**

- The application displays "File Uploaded!".
- The displayed filename is `sample.pdf`.

---

### UPL-004 — Upload a PNG File

**Requirements:** REQ-UPL-002, REQ-UPL-003, REQ-UPL-007  
**Priority:** Medium  
**Type:** Positive / Functional  
**Test Data:** `sample.png`  
**Automation:** `test_upload_file[UPL-004-png]`

**Steps**

1. Navigate to `/upload`.
2. Select `sample.png`.
3. Submit the upload form.
4. Inspect the upload confirmation.

**Expected Result**

- The application displays "File Uploaded!".
- The displayed filename is `sample.png`.

---

### UPL-005 — Upload a File With Special Characters in Its Name

**Requirements:** REQ-UPL-003, REQ-UPL-007  
**Priority:** Medium  
**Type:** Positive / Boundary-related  
**Test Data:** `test file (1).txt`  
**Automation:** `test_upload_file[UPL-005-special-filename]`

**Steps**

1. Navigate to `/upload`.
2. Select `test file (1).txt`.
3. Submit the upload form.
4. Inspect the uploaded filename.

**Expected Result**

- The application displays a successful upload confirmation.
- The displayed filename preserves the spaces and parentheses.

---

### UPL-006 — Upload an Empty File

**Requirements:** REQ-UPL-004, REQ-UPL-007 (conditional)  
**Priority:** Medium  
**Type:** Boundary Value / Functional  
**Test Data:** `empty.txt` (0 bytes)  
**Automation:** `test_upload_file[UPL-006-empty-file]`

**Steps**

1. Verify that `empty.txt` contains zero bytes.
2. Navigate to `/upload`.
3. Select `empty.txt`.
4. Submit the upload form.
5. Inspect the response and displayed result.

**Expected Result**

- The application processes the submission and produces an observable result.
- Whether the file is accepted or rejected must be confirmed through execution.
- If accepted, the filename should be displayed correctly.

**Status:** Expected success/rejection behavior pending verification. The current automated test assumes successful upload.

---

### UPL-007 — Submit Without Selecting a File

**Requirement:** REQ-UPL-005  
**Priority:** High  
**Type:** Negative / Error Handling  
**Test Data:** No file selected  
**Automation:** `test_upload_without_file`

**Steps**

1. Navigate to `/upload`.
2. Leave the file input empty.
3. Click Upload.
4. Inspect the HTTP response.
5. Inspect the error message.

**Expected Result — Current Application Behavior**

- The upload request receives HTTP 500.
- The application displays: "No file was chosen. Please choose a file to upload."

**Note:** This test characterizes the application's observed behavior. It does not define HTTP 500 as the preferred response for an invalid upload submission.

---

### UPL-008 — Upload a File Using Drag and Drop

**Requirement:** REQ-UPL-006  
**Priority:** Medium  
**Type:** Functional / Alternative Interaction  
**Test Data:** Defined by `DRAG_DROP_CASE`  
**Automation:** `test_upload_using_drag_and_drop`

**Steps**

1. Navigate to `/upload`.
2. Locate the drag-and-drop area.
3. Provide the configured file using a simulated drop interaction.
4. Wait for the upload result.
5. Verify the filename and successful upload state.

**Expected Result**

- The drop zone receives the file.
- The application processes the upload.
- A successful upload state is displayed.
- The displayed filename matches the selected resource.

**Status:** Pending verification of the simulated drag-and-drop interaction and upload result.

## 4. Automation Mapping

| Test Case | pytest Function | Parameter |
|---|---|---|
| UPL-001 | `test_upload_form_is_displayed` | None |
| UPL-002 | `test_upload_file` | `UPL-002-txt` |
| UPL-003 | `test_upload_file` | `UPL-003-pdf` |
| UPL-004 | `test_upload_file` | `UPL-004-png` |
| UPL-005 | `test_upload_file` | `UPL-005-special-filename` |
| UPL-006 | `test_upload_file` | `UPL-006-empty-file` |
| UPL-007 | `test_upload_without_file` | None |
| UPL-008 | `test_upload_using_drag_and_drop` | None |

**Automation File:** `tests/test_upload.py`  
**Test Data:** `data/upload_cases.py`  
**Page Object:** `pages/upload_page.py`  
**Resources:** `resources/uploads/`

## 5. Planned Execution Summary

- Documented test cases: 8
- Automated test functions: 4
- Planned pytest executions: 8
- Execution status: Pending complete validation
- Open behavioral validations: UPL-006 and UPL-008

## 6. Execution Evidence

Execution results will be collected using:

- Allure reports.
- JUnit XML results.
- Playwright traces and screenshots when configured.

Test results must be updated after execution. Documented automation does not imply a passing result.