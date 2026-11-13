
from dataclasses import dataclass
from typing import Literal


DialogType = Literal["alert", "confirm", "prompt"]
DialogAction = Literal["accept", "dismiss"]


@dataclass(frozen=True)
class DialogActionCase:
    """Represent an action and its expected dialog result.

    Attributes:
        id: Test case identifier.
        dialog_type: JavaScript dialog type.
        action: Action performed on the dialog.
        prompt_text: Text entered into a prompt, if applicable.
        expected_result: Expected result displayed by the page.
    """
    id: str
    dialog_type: DialogType
    action: DialogAction
    prompt_text: str | None
    expected_result: str


@dataclass(frozen=True)
class DialogPropertyCase:
    """Represent the expected properties of a JavaScript dialog.

    Attributes:
        id: Test case identifier.
        dialog_type: Expected JavaScript dialog type.
        expected_message: Expected dialog message.
    """

    id: str
    dialog_type: DialogType
    expected_message: str


DIALOG_ACTION_CASES = [
    DialogActionCase(
        id="JSA-001-accept-alert",
        dialog_type="alert",
        action="accept",
        prompt_text=None,
        expected_result="You successfully clicked an alert",
    ),
    DialogActionCase(
        id="JSA-002-accept-confirm",
        dialog_type="confirm",
        action="accept",
        prompt_text=None,
        expected_result="You clicked: Ok",
    ),
    DialogActionCase(
        id="JSA-003-dismiss-confirm",
        dialog_type="confirm",
        action="dismiss",
        prompt_text=None,
        expected_result="You clicked: Cancel",
    ),
    DialogActionCase(
        id="JSA-004-accept-prompt",
        dialog_type="prompt",
        action="accept",
        prompt_text="QA testing",
        expected_result="You entered: QA testing",
    ),
    DialogActionCase(
        id="JSA-005-dismiss-prompt",
        dialog_type="prompt",
        action="dismiss",
        prompt_text=None,
        expected_result="You entered: null",
    ),
    DialogActionCase(
        id="JSA-006-empty-prompt",
        dialog_type="prompt",
        action="accept",
        prompt_text="",
        expected_result="You entered:",
    ),
]


DIALOG_PROPERTY_CASES = [
    DialogPropertyCase(
        id="JSA-007-alert",
        dialog_type="alert",
        expected_message="I am a JS Alert",
    ),
    DialogPropertyCase(
        id="JSA-007-confirm",
        dialog_type="confirm",
        expected_message="I am a JS Confirm",
    ),
    DialogPropertyCase(
        id="JSA-007-prompt",
        dialog_type="prompt",
        expected_message="I am a JS prompt",
    ),
]
