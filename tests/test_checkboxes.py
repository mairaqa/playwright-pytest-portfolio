
import pytest
from playwright.sync_api import expect

from data.checkboxes_cases import CHANGE_STATE_CASES, SET_ALL_CASES, CHECKBOX_INDEPENDENCE_CASES
from pages.checkboxes_page import CheckboxesPage


@pytest.mark.smoke
def test_checkboxes_are_displayed(
    checkboxes_page: CheckboxesPage,
) -> None:
    checkboxes_page.navigate()

    expect(checkboxes_page.heading).to_be_visible()
    expect(checkboxes_page.checkboxes).to_have_count(2)

    for checkbox in checkboxes_page.checkboxes.all():
        expect(checkbox).to_be_visible()


def test_initial_checkbox_states(
    checkboxes_page: CheckboxesPage,
) -> None:
    checkboxes_page.navigate()

    expect(checkboxes_page.checkbox(0)).not_to_be_checked()
    expect(checkboxes_page.checkbox(1)).to_be_checked()


@pytest.mark.parametrize("index, checked",CHANGE_STATE_CASES,)
def test_change_checkbox_state(
    checkboxes_page: CheckboxesPage,
    index: int,
    checked: bool,
) -> None:
    checkboxes_page.navigate()

    expect(checkboxes_page.checkbox(index)).to_be_checked(
        checked=not checked
    )

    if checked:
        checkboxes_page.check(index)
    else:
        checkboxes_page.uncheck(index)

    expect(checkboxes_page.checkbox(index)).to_be_checked(
        checked=checked
    )


@pytest.mark.regression
@pytest.mark.parametrize(
    ("target_index", "other_index"),
    CHECKBOX_INDEPENDENCE_CASES,
)
def test_checkbox_independence(
    checkboxes_page: CheckboxesPage,
    target_index: int,
    other_index: int,
) -> None:
    """Verify that changing one checkbox does not affect the other.

    Args:
        checkboxes_page: Checkbox page object fixture.
        target_index: Index of the checkbox to modify.
        other_index: Index of the checkbox that must remain unchanged.
    """
    checkboxes_page.navigate()

    target = checkboxes_page.checkboxes.nth(target_index)
    other = checkboxes_page.checkboxes.nth(other_index)

    initial_target_state = target.is_checked()
    initial_other_state = other.is_checked()

    target.set_checked(not initial_target_state)

    expect(target).to_be_checked(checked=not initial_target_state)
    expect(other).to_be_checked(checked=initial_other_state)


def test_toggle_checkbox_multiple_times(
    checkboxes_page: CheckboxesPage,
) -> None:
    checkboxes_page.navigate()

    checkbox = checkboxes_page.checkbox(0)

    expect(checkbox).not_to_be_checked()

    checkboxes_page.toggle(0)
    expect(checkbox).to_be_checked()

    checkboxes_page.toggle(0)
    expect(checkbox).not_to_be_checked()


@pytest.mark.parametrize("checked",SET_ALL_CASES,)
def test_set_all_checkboxes(
    checkboxes_page: CheckboxesPage,
    checked: bool,
) -> None:
    checkboxes_page.navigate()
    checkboxes_page.set_all(checked)

    expect(checkboxes_page.checkboxes).to_have_count(2)

    for checkbox in checkboxes_page.checkboxes.all():
        expect(checkbox).to_be_checked(checked=checked)
