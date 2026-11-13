
import pytest
from playwright.sync_api import Dialog, Page, expect

from data.javascript_alert_cases import (
    DIALOG_ACTION_CASES,
    DIALOG_PROPERTY_CASES,
    DialogActionCase,
    DialogPropertyCase,
)
from pages.javascript_alerts_page import JavaScriptAlertsPage
from utils.assertions import expect_path


@pytest.mark.parametrize(
    "case",
    DIALOG_ACTION_CASES,
    ids=lambda case: case.id,
)
def test_javascript_dialog_actions(
    page: Page,
    javascript_alerts_page: JavaScriptAlertsPage,
    case: DialogActionCase,
) -> None:
    """Verify dialog actions and their resulting page messages.

    A one-time dialog listener handles the dialog triggered
    by each parameterized scenario.
    """
    javascript_alerts_page.navigate()
    expect_path(page, javascript_alerts_page.PATH)

    def handle_dialog(dialog: Dialog) -> None:
        if case.action == "accept":
            if case.prompt_text is not None:
                dialog.accept(prompt_text=case.prompt_text)
            else:
                dialog.accept()
        else:
            dialog.dismiss()

    page.once("dialog", handle_dialog)
    javascript_alerts_page.trigger_dialog(case.dialog_type)

    expect(javascript_alerts_page.result).to_have_text(
        case.expected_result
    )


@pytest.mark.parametrize(
    "case",
    DIALOG_PROPERTY_CASES,
    ids=lambda case: case.id,
)
def test_javascript_dialog_properties(
    page: Page,
    javascript_alerts_page: JavaScriptAlertsPage,
    case: DialogPropertyCase,
) -> None:
    """Verify the type and message of each JavaScript dialog.

    The dialog is dismissed after capturing its properties
    to allow the browser interaction to complete.
    """
    javascript_alerts_page.navigate()

    captured_dialogs: list[tuple[str, str]] = []

    def handle_dialog(dialog: Dialog) -> None:
        captured_dialogs.append(
            (dialog.type, dialog.message)
        )
        dialog.dismiss()

    page.once("dialog", handle_dialog)
    javascript_alerts_page.trigger_dialog(case.dialog_type)

    assert captured_dialogs == [
        (case.dialog_type, case.expected_message)
    ]
