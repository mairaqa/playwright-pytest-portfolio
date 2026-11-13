
from playwright.sync_api import Page, Locator


class CheckboxesPage:
    """Provide interactions with the checkboxes on the page."""

    PATH = "/checkboxes"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_role(
            "heading", name="Checkboxes"
        )
        self.checkboxes = page.get_by_role("checkbox")

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def checkbox(self, index: int) -> Locator:
        """Return a checkbox by its zero-based index.

        Args:
            index: Position of the checkbox, starting at zero.

        Returns:
            Locator for the selected checkbox.
        """
        return self.checkboxes.nth(index)

    def check(self, index: int) -> None:
        """Check the specified checkbox.

        Args:
            index: Zero-based index of the checkbox.
        """
        self.checkbox(index).check()

    def uncheck(self, index: int) -> None:
        """Uncheck the specified checkbox.

        Args:
            index: Zero-based index of the checkbox.
        """
        self.checkbox(index).uncheck()

    def toggle(self, index: int) -> None:
        """Toggle the current state of the specified checkbox.

        Args:
            index: Zero-based index of the checkbox.
        """
        self.checkbox(index).click()

    def set_all(self, checked: bool) -> None:
        """Set all checkboxes to the requested state.

        Args:
            checked: True to check all boxes, False to uncheck them.
        """
        for checkbox in self.checkboxes.all():
            checkbox.set_checked(checked)
