
from playwright.sync_api import Page


class SecureAreaPage:
    """Provide interactions with the protected Secure Area."""

    PATH = "/secure"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.username_hint = page.locator("span#username")

        self.logout_button = page.get_by_role(
            "link", name="Logout"
        )
        self.success_message = page.locator("#flash.success")

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def logout(self) -> None:
        """Submit the logout action from the Secure Area."""

        self.logout_button.click()
