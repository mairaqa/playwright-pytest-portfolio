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
    """Provide an authenticated browser session for a test."""
    username, password = settings.require_credentials()

    login_page.navigate()
    login_page.login(
        username=username,
        password=password,
    )

    expect_path(page, secure_page.PATH)
    expect(secure_page.username_hint).to_have_text(username)

    return secure_page