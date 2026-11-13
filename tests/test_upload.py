
import pytest
from playwright.sync_api import expect

from config.settings import UPLOAD_DIR
from data.upload_cases import (UPLOAD_CASES, NO_FILE_CASE, DRAG_DROP_CASE,UploadCase,)
from pages.upload_page import UploadPage


@pytest.mark.smoke
def test_upload_form_is_displayed(upload_page: UploadPage,) -> None:
    upload_page.navigate()

    expect(upload_page.heading).to_be_visible()
    expect(upload_page.file_input).to_have_count(1)
    expect(upload_page.file_input).to_be_enabled()
    expect(upload_page.upload_button).to_be_visible()
    expect(upload_page.upload_button).to_be_enabled()


@pytest.mark.parametrize("case",UPLOAD_CASES,ids=lambda case: case.id,)
def test_upload_file(upload_page: UploadPage,case: UploadCase,) -> None:
    """Verify upload results for each configured file scenario."""
    file_path = UPLOAD_DIR / case.filename

    assert file_path.is_file(), f"Test resource not found: {file_path}"

    upload_page.navigate()
    upload_page.upload(file_path)

    expect(upload_page.success_heading).to_be_visible()
    expect(upload_page.uploaded_filename).to_have_text(case.expected_filename)


def test_upload_without_file(
    upload_page: UploadPage,
) -> None:
    """Verify the application's observed response to an empty submission.

    The demo application currently returns HTTP 500 rather than
    handling the missing file through client-side validation.
    """
    upload_page.navigate()

    with upload_page.page.expect_response(
        lambda response: (
            response.request.method == "POST"
            and response.url.split("?")[0].endswith(
                upload_page.PATH
            )
        )
    ) as response_info:
        upload_page.submit()

    assert response_info.value.status == (
        NO_FILE_CASE.expected_status
    )

    expect(upload_page.error_message).to_contain_text(
        NO_FILE_CASE.expected_message
    )


def test_upload_using_drag_and_drop(upload_page: UploadPage,) -> None:
    file_path = UPLOAD_DIR / DRAG_DROP_CASE.filename

    assert file_path.is_file()

    upload_page.navigate()

    expect(upload_page.drop_zone).to_be_visible()

    upload_page.drop_file(file_path)

    expect(upload_page.uploaded_preview).to_have_text(DRAG_DROP_CASE.expected_filename)
