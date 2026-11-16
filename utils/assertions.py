"""Reusable assertions for Playwright tests."""

import re

from playwright.sync_api import Page, expect


def expect_path(page: Page, expected_path: str) -> None:
    """Assert that the current URL has the exact expected path.

    Query parameters and URL fragments are allowed after the path.

    Args:
        page: Playwright page to validate.
        expected_path: Expected absolute URL path, starting with '/'.

    Raises:
        ValueError: If the expected path is not absolute.
        AssertionError: If the URL does not match the expected path.
    """
    if not expected_path.startswith("/"):
        raise ValueError("expected_path must start with '/'")

    pattern = re.compile(
        rf"^https?://[^/?#]+{re.escape(expected_path)}(?:[?#].*)?$"
    )

    expect(page).to_have_url(pattern)
