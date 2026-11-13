
from playwright.sync_api import Page


class JavaScriptAlertsPage:
    """Provide interactions with JavaScript dialog triggers."""

    PATH = "/javascript_alerts"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.alert_button = page.get_by_role(
            "button", name="Click for JS Alert"
        )
        self.confirm_button = page.get_by_role(
            "button", name="Click for JS Confirm"
        )
        self.prompt_button = page.get_by_role(
            "button", name="Click for JS Prompt"
        )
        self.result = page.locator("#result")

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def trigger_dialog(self, dialog_type: str) -> None:
        """Trigger the requested JavaScript dialog.

        Args:
            dialog_type: Dialog to trigger: alert, confirm, or prompt.
        """
        buttons = {
            "alert": self.alert_button,
            "confirm": self.confirm_button,
            "prompt": self.prompt_button,
        }
        buttons[dialog_type].click()
