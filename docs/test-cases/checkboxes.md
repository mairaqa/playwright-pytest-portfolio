# Checkboxes — Test Cases

**Module:** Checkboxes  
**Application:** The Internet  
**Test level:** System / UI  
**Test type:** Functional  
**Automation framework:** Playwright + Python + pytest  
**Automation file:** `tests/test_checkboxes.py`

## 1. Objective

Verify that checkbox controls are displayed correctly, support checking and unchecking, maintain their individual states, and respond consistently to repeated interactions.

## 2. Test Cases

### CHK-001 — Verify Checkboxes Are Displayed

**Priority:** High

**Preconditions:** The application is accessible.

**Steps:**
1. Navigate to `/checkboxes`.
2. Locate the checkbox controls.

**Expected Results:**
- The Checkboxes page is displayed.
- Exactly two checkbox controls are present.
- Both controls are visible.

### CHK-002 — Verify Initial Checkbox States

**Priority:** Medium

**Preconditions:** The page is loaded in a new browser context.

**Steps:**
1. Navigate to `/checkboxes`.
2. Inspect the state of checkbox 1.
3. Inspect the state of checkbox 2.

**Expected Results:**
- Checkbox 1 is unchecked.
- Checkbox 2 is checked.

### CHK-003 — Check an Unchecked Checkbox

**Priority:** High

**Preconditions:** Checkbox 1 is initially unchecked.

**Steps:**
1. Navigate to `/checkboxes`.
2. Check checkbox 1.

**Expected Results:**
- Checkbox 1 becomes checked.

### CHK-004 — Uncheck a Checked Checkbox

**Priority:** High

**Preconditions:** Checkbox 2 is initially checked.

**Steps:**
1. Navigate to `/checkboxes`.
2. Uncheck checkbox 2.

**Expected Results:**
- Checkbox 2 becomes unchecked.

### CHK-005 — Verify Checkbox Independence

**Priority:** High

**Preconditions:** Both checkboxes are available.

**Steps:**
1. Navigate to `/checkboxes`.
2. Record the initial states of both checkboxes.
3. Change the state of the target checkbox.
4. Verify that the target checkbox changes state.
5. Verify that the other checkbox retains its original state.
6. Repeat the scenario using the other checkbox as the target.

**Expected Results:**
- CHK-005-A: Changing checkbox 1 does not affect checkbox 2.
- CHK-005-B: Changing checkbox 2 does not affect checkbox 1.
- Both scenarios are executed independently using pytest parametrization.

### CHK-006 — Toggle Checkbox Multiple Times

**Priority:** Medium

**Preconditions:** Checkbox 1 is available.

**Steps:**
1. Navigate to `/checkboxes`.
2. Record the initial state of checkbox 1.
3. Toggle checkbox 1.
4. Verify that its state changes.
5. Toggle checkbox 1 again.

**Expected Results:**
- The first toggle reverses the original state.
- The second toggle restores the original state.

### CHK-007 — Check All Checkboxes

**Priority:** Medium

**Preconditions:** Both checkbox controls are available.

**Steps:**
1. Navigate to `/checkboxes`.
2. Check both checkboxes.

**Expected Results:**
- Checkbox 1 is checked.
- Checkbox 2 is checked.

### CHK-008 — Uncheck All Checkboxes

**Priority:** Medium

**Preconditions:** Both checkbox controls are available.

**Steps:**
1. Navigate to `/checkboxes`.
2. Uncheck both checkboxes.

**Expected Results:**
- Checkbox 1 is unchecked.
- Checkbox 2 is unchecked.

## 3. Test Data

No external test data or credentials are required.

The tests use the two checkbox elements available on the demonstration page.

## 4. Automation Considerations

- Use the Page Object Model.
- Use Playwright's `check()`, `uncheck()`, and `set_checked()` methods where appropriate.
- Verify state using `expect(locator).to_be_checked()` and `expect(locator).not_to_be_checked()`.
- Avoid hardcoded absolute URLs.
- Keep test cases independent.
- Use pytest parametrization where scenarios share the same interaction and assertion structure.
