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
    """Store the configuration for the selected test environment.

    Attributes:
        base_url: Base URL of the application under test.
        username: Valid username for authentication tests.
        password: Valid password for authentication tests.
    """
    base_url: str
    username: str
    password: str


def load_settings(environment: str) -> Settings:
    """Load the configuration for the selected test environment.

    Environment variables take precedence over values defined
    in the corresponding .env file.

    Args:
        environment: Name of the target environment.

    Returns:
        Settings: Configuration for the selected environment.
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

    def get_required(name: str) -> str:
        # CI variables take precedence over local files.
        value = os.environ.get(name)

        if value is None:
            value = file_values.get(name)

        if not value:
            raise ValueError(
                f"Missing configuration: {name}"
            )

        return value

    return Settings(
        base_url=get_required("BASE_URL"),
        username=get_required("TEST_USERNAME"),
        password=get_required("TEST_PASSWORD"),
    )
