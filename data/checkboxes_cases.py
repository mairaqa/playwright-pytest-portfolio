"""Define parameterized checkbox state and independence scenarios."""

import pytest


CHANGE_STATE_CASES = [
    pytest.param(
        0,
        True,
        id="CHK-003-check-checkbox",
    ),
    pytest.param(
        1,
        False,
        id="CHK-004-uncheck-checkbox",
    ),
]


SET_ALL_CASES = [
    pytest.param(
        True,
        id="CHK-007-check-all",
    ),
    pytest.param(
        False,
        id="CHK-008-uncheck-all",
    ),
]
