"""Provide Page Objects for browser-based tests."""

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.checkboxes_page import CheckboxesPage
from pages.javascript_alerts_page import JavaScriptAlertsPage
from pages.upload_page import UploadPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide the Login Page Object."""
    return LoginPage(page)


@pytest.fixture
def secure_page(page: Page) -> SecureAreaPage:
    """Provide the Secure Area Page Object."""
    return SecureAreaPage(page)


@pytest.fixture
def checkboxes_page(page: Page) -> CheckboxesPage:
    """Provide the Checkboxes Page Object."""
    return CheckboxesPage(page)


@pytest.fixture
def javascript_alerts_page(page: Page,) -> JavaScriptAlertsPage:
    """Provide the JavaScript Alerts Page Object."""
    return JavaScriptAlertsPage(page)


@pytest.fixture
def upload_page(page: Page) -> UploadPage:
    """Provide the File Upload Page Object."""
    return UploadPage(page)