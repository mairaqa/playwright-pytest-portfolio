"""Provide reusable Playwright assertions."""

import re

from playwright.sync_api import Page, expect


def expect_path(page: Page, path: str) -> None:
    """Verify that the current page URL ends with the expected path.

    Allow an optional trailing slash, query string, or fragment
    without depending on the application's base URL.

    Args:
        page: Playwright page to validate.
        path: Expected URL path, such as "/login" or "/secure".
    """
    pattern = rf"{re.escape(path.rstrip('/'))}/?(?:[?#].*)?$"
    expect(page).to_have_url(re.compile(pattern))