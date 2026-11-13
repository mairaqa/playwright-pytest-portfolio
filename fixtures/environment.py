"""Provide test environment and browser context configuration."""

import pytest

from config.settings import Settings, load_settings


@pytest.fixture(scope="session")
def settings(request: pytest.FixtureRequest) -> Settings:
    """Load configuration for the selected test environment.

    The environment is selected through the --env pytest option.

    Args:
        request: Pytest request used to access the environment option.

    Returns:
        Configuration for the selected environment.
    """
    environment = request.config.getoption("--env")
    return load_settings(environment)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict,settings: Settings,) -> dict:
    """Configure the browser context with the environment base URL.

    Preserve the options provided by pytest-playwright and override
    base_url with the value from the selected environment.

    Args:
        browser_context_args: Existing browser context options.
        settings: Configuration for the selected environment.

    Returns:
        Browser context options including the configured base URL.
    """
    return {
        **browser_context_args,
        "base_url": settings.base_url,
    }