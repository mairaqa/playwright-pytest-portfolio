
from playwright.sync_api import Page


class LoginPage:
    """Provide interactions with the login form."""

    PATH = "/login"

    def __init__(self, page: Page):
        self.page = page

        self.username = page.get_by_role(
            "textbox", name="Username"
        )
        self.password = page.get_by_role(
            "textbox", name="Password"
        )
        self.login_button = page.get_by_role(
            "button", name="Login"
        )
        self.error_message = page.locator("#flash.error")
        self.success_message = page.locator("#flash.success")

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def login(self, username: str, password: str) -> None:
        """Submit the login form using the provided credentials.

        Args:
            username: Username to enter.
            password: Password to enter.
        """

        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
