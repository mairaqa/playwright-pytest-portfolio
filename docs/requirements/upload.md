# File Upload — Functional Requirements

## 1. Purpose

Define the functional requirements for uploading files through the File Uploader page in The Internet test application.

**Application:** https://the-internet.herokuapp.com/upload  
**Module:** File Upload  
**Requirement prefix:** REQ-UPL  
**Automation framework:** Python, pytest, Playwright  
**Status:** Approved

## 2. Scope

### In Scope

- File upload form availability.
- Uploading files through the standard file input.
- Uploading different file formats.
- Handling filenames containing spaces and special characters.
- Uploading empty files.
- Submitting the form without selecting a file.
- Uploading files through drag and drop.
- Displaying upload results and filenames.

### Out of Scope

- Maximum file size and performance limits.
- Malware scanning and security validation.
- Authentication and upload permissions.
- Server-side file storage verification.
- Concurrent uploads and multi-user load testing.

These areas require additional requirements or test infrastructure.

## 3. Functional Requirements

### REQ-UPL-001 — File Upload Form Availability

The application shall provide the controls required to select and submit a file.

**Acceptance Criteria**

- The File Uploader heading is displayed.
- A file input is available and enabled.
- The Upload button is visible and enabled.

**Related Test Case:** UPL-001

### REQ-UPL-002 — Standard File Upload

The application shall support file submission through the standard file upload form.

**Acceptance Criteria**

- The user can select an existing local file.
- The user can submit the selected file.
- The application displays a successful upload confirmation.
- TXT, PDF and PNG test resources are covered by automation.

**Related Test Cases:** UPL-002, UPL-003, UPL-004

### REQ-UPL-003 — Filename Handling

The application shall correctly display the name of a successfully uploaded file, including filenames containing spaces or supported special characters.

**Acceptance Criteria**

- The uploaded filename matches the selected filename.
- Spaces and parentheses are preserved in the displayed name.

**Related Test Cases:** UPL-002, UPL-003, UPL-004, UPL-005

### REQ-UPL-004 — Empty File Handling

The application shall provide an observable result when an empty file is submitted.

**Acceptance Criteria**

- A zero-byte file can be selected for submission.
- The application accepts the empty file.
- The successful upload confirmation and filename are displayed.

**Related Test Case:** UPL-006

**Validation Status:** Verified — the empty file was accepted and its filename displayed in the successful cross-browser run.

### REQ-UPL-005 — Submission Without a Selected File

The application shall provide a response when the upload form is submitted without selecting a file.

**Acceptance Criteria**

- A submission without a selected file produces a response.
- The current observed response is HTTP 500.
- The response displays: "No file was chosen. Please choose a file to upload."

**Related Test Case:** UPL-007

**Note:** HTTP 500 is the observed behavior of the demonstration application, not a recommended validation design.

### REQ-UPL-006 — Drag and Drop File Upload

The application shall provide a drag-and-drop area for file uploads.

**Acceptance Criteria**

- The drop zone is available.
- A file can be provided through the drop interaction.
- A successful upload displays the filename and a success state.
- The upload outcome is verified rather than inferred from event dispatch alone.

**Related Test Case:** UPL-008

**Validation Status:** Verified — the simulated drop produced the expected filename and success state in the successful cross-browser run.

### REQ-UPL-007 — Upload Confirmation

The application shall display the outcome of a standard file upload.

**Acceptance Criteria**

- A successful upload displays the "File Uploaded!" heading.
- The uploaded filename is displayed.
- The filename matches the selected test resource.

**Related Test Cases:** UPL-002, UPL-003, UPL-004, UPL-005, UPL-006

## 4. Test Data

The required files are stored under:

`resources/uploads/`

| Resource | Purpose |
|---|---|
| sample.txt | Standard TXT upload |
| sample.pdf | PDF upload |
| sample.png | PNG upload |
| test file (1).txt | Filename handling |
| empty.txt | Zero-byte file handling |

All test resources must be non-sensitive and available in the test execution environment.

## 5. Dependencies and Assumptions

- The target environment is configured through `config/settings.py`.
- Local resource paths are resolved relative to the project root.
- The upload service must be accessible during execution.
- Successful upload behavior is verified using visible application results.
- The automated drag-and-drop scenario verifies the resulting upload state and filename.

## 6. Requirement Status

All seven requirements are documented, mapped, and approved based on the successful cross-browser validation recorded in the traceability matrix.