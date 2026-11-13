
import pytest
from playwright.sync_api import Page, expect

from config.settings import Settings
from data.login_cases import InvalidLoginCase, INVALID_LOGIN_CASES
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.assertions import expect_path


@pytest.mark.smoke
def test_login_with_valid_credentials(
    page: Page,
    login_page: LoginPage,
    secure_page: SecureAreaPage,
    settings: Settings,
) -> None:
    login_page.navigate()
    login_page.login(
        username=settings.username,
        password=settings.password,
    )

    expect_path(page, secure_page.PATH)
    expect(secure_page.username_hint).to_have_text(
        settings.username
    )
    expect(secure_page.logout_button).to_be_visible()


@pytest.mark.smoke
def test_logout_after_successful_login(
    page: Page,
    login_page: LoginPage,
    authenticated_user: SecureAreaPage,
) -> None:
    authenticated_user.logout()

    expect_path(page, login_page.PATH)
    expect(login_page.login_button).to_be_visible()
    expect(login_page.success_message).to_contain_text(
        "You logged out of the secure area!"
    )


@pytest.mark.parametrize(
    "case",
    INVALID_LOGIN_CASES,
    ids=lambda case: case.id,
)
def test_login_with_invalid_credentials(
    page: Page,
    login_page: LoginPage,
    settings: Settings,
    case: InvalidLoginCase,
) -> None:
    """Verify authentication failures using configured credential overrides.

    None preserves the environment credential, while an empty
    string explicitly tests a missing credential.
    """
    username = (
        settings.username
        if case.username_override is None
        else case.username_override
    )
    password = (
        settings.password
        if case.password_override is None
        else case.password_override
    )

    login_page.navigate()
    login_page.login(
        username=username,
        password=password,
    )

    expect_path(page, login_page.PATH)
    expect(login_page.error_message).to_contain_text(
        case.expected_error
    )


@pytest.mark.security
def test_access_secure_page_without_authentication(
    page: Page,
    login_page: LoginPage,
    secure_page: SecureAreaPage,
) -> None:
    secure_page.navigate()

    expect_path(page, login_page.PATH)
    expect(login_page.error_message).to_contain_text(
        "You must login to view the secure area!"
    )
    expect(login_page.login_button).to_be_visible()


@pytest.mark.security
def test_access_secure_page_after_logout(
    page: Page,
    login_page: LoginPage,
    authenticated_user: SecureAreaPage,
) -> None:
    authenticated_user.logout()
    expect_path(page, login_page.PATH)

    authenticated_user.navigate()

    expect_path(page, login_page.PATH)
    expect(login_page.error_message).to_contain_text(
        "You must login to view the secure area!"
    )
    expect(login_page.login_button).to_be_visible()
