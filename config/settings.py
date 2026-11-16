
"""Manage environment-specific test configuration."""

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPLOAD_DIR = PROJECT_ROOT / "resources" / "uploads"


@dataclass(frozen=True)
class Settings:
    """Store configuration for the selected test environment.

    Attributes:
        base_url: Base URL of the application under test.
        username: Optional username for authentication tests.
        password: Optional password for authentication tests.
    """

    base_url: str
    username: str | None
    password: str | None

    def require_credentials(self) -> tuple[str, str]:
        """Return credentials required by authentication tests.

        Returns:
            Validated username and password.

        Raises:
            ValueError: If authentication credentials are missing.
        """
        if not self.username:
            raise ValueError("Missing configuration: TEST_USERNAME")

        if not self.password:
            raise ValueError("Missing configuration: TEST_PASSWORD")

        return self.username, self.password


def load_settings(environment: str) -> Settings:
    """Load configuration for the selected test environment.

    Environment variables take precedence over .env file values.

    Args:
        environment: Name of the target environment.

    Returns:
        Configuration for the selected environment.

    Raises:
        ValueError: If the environment or base URL is invalid.
    """
    logger.info(
        "Loading configuration for environment: %s",
        environment,
    )

    allowed_environments = {"dev", "qa", "staging"}

    if environment not in allowed_environments:
        raise ValueError(
            f"Unsupported environment: {environment}"
        )

    env_file = PROJECT_ROOT / f".env.{environment}"
    file_values = dotenv_values(env_file)

    def get_value(name: str) -> str | None:
        """Read a configuration value, prioritizing environment variables."""
        value = os.environ.get(name)

        if value is None:
            value = file_values.get(name)

        return value

    base_url = get_value("BASE_URL")

    if not base_url:
        raise ValueError("Missing configuration: BASE_URL")

    return Settings(
        base_url=base_url,
        username=get_value("TEST_USERNAME"),
        password=get_value("TEST_PASSWORD"),
    )
