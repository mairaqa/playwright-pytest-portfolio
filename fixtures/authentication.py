"""Provide authenticated browser state for protected-area tests."""

import pytest
from playwright.sync_api import Page, expect

from config.settings import Settings
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.assertions import expect_path


@pytest.fixture
def authenticated_user(
    page: Page,
    login_page: LoginPage,
    secure_page: SecureAreaPage,
    settings: Settings,
) -> SecureAreaPage:
    """Provide access to the Secure Area after authentication.

    Log in using the configured environment credentials and verify
    the destination URL and authenticated username.

    The fixture uses a function-scoped browser page, keeping
    authentication state isolated between tests.

    Args:
        page: Browser page used for authentication.
        login_page: Page Object for the login form.
        secure_page: Page Object for the protected area.
        settings: Environment configuration containing credentials.

    Returns:
        Secure Area Page Object after successful authentication.
    """
    login_page.navigate()

    login_page.login(username=settings.username,password=settings.password,)

    expect_path(page, secure_page.PATH)
    expect(secure_page.username_hint).to_have_text(settings.username)

    return secure_page