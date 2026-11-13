
from dataclasses import dataclass


@dataclass(frozen=True)
class InvalidLoginCase:
    """Represent an invalid authentication scenario.

    Attributes:
        id: Test case identifier.
        username_override: Username replacement, or None to use
            the configured username.
        password_override: Password replacement, or None to use
            the configured password.
        expected_error: Expected authentication error message.
    """

    id: str
    username_override: str | None
    password_override: str | None
    expected_error: str


INVALID_LOGIN_CASES = [
    InvalidLoginCase(
        id="AUTH-003-invalid-username",
        username_override="invalid_user",
        password_override=None,
        expected_error="Your username is invalid!",
    ),
    InvalidLoginCase(
        id="AUTH-004-invalid-password",
        username_override=None,
        password_override="invalid_password",
        expected_error="Your password is invalid!",
    ),
    InvalidLoginCase(
        id="AUTH-006-empty-username",
        username_override="",
        password_override=None,
        expected_error="Your username is invalid!",
    ),
    InvalidLoginCase(
        id="AUTH-007-empty-password",
        username_override=None,
        password_override="",
        expected_error="Your password is invalid!",
    ),
]
