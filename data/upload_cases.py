
from dataclasses import dataclass


@dataclass(frozen=True)
class UploadCase:
    """Represent a file upload scenario.

    Attributes:
        id: Test case identifier.
        filename: Name of the local test resource.
        expected_filename: Filename expected in the upload result.
    """

    id: str
    filename: str
    expected_filename: str


@dataclass(frozen=True)
class UploadErrorCase:
    """Represent the expected response to an invalid file submission.

    Attributes:
        id: Test case identifier.
        expected_status: Expected HTTP response status code.
        expected_message: Expected error message displayed by the page.
    """
    id: str
    expected_status: int
    expected_message: str


UPLOAD_CASES = [
    UploadCase(
        id="UPL-002-txt",
        filename="sample.txt",
        expected_filename="sample.txt",
    ),
    UploadCase(
        id="UPL-003-pdf",
        filename="sample.pdf",
        expected_filename="sample.pdf",
    ),
    UploadCase(
        id="UPL-004-png",
        filename="sample.png",
        expected_filename="sample.png",
    ),
    UploadCase(
        id="UPL-005-special-filename",
        filename="test file (1).txt",
        expected_filename="test file (1).txt",
    ),
    UploadCase(
        id="UPL-006-empty-file",
        filename="empty.txt",
        expected_filename="empty.txt",
    ),
]


NO_FILE_CASE = UploadErrorCase(
    id="UPL-007-no-file",
    expected_status=500,
    expected_message=(
        "No file was chosen. Please choose a file to upload."
    ),
)


DRAG_DROP_CASE = UploadCase(
    id="UPL-008-drag-drop",
    filename="sample.txt",
    expected_filename="sample.txt",
)
