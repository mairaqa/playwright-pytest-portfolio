import base64
from pathlib import Path

from playwright.sync_api import Page


class UploadPage:
    """Provide standard and drag-and-drop file upload interactions."""

    PATH = "/upload"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.heading = page.get_by_role(
            "heading", name="File Uploader"
        )
        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")

        self.success_heading = page.get_by_role(
            "heading", name="File Uploaded!"
        )
        self.error_message = page.get_by_role("main").locator("p")
        self.uploaded_filename = page.locator("#uploaded-files")
        self.drop_zone = page.locator("#drag-drop-upload")
        self.uploaded_preview = page.locator(
            "#drag-drop-upload .dz-preview.dz-success [data-dz-name]"
        )

    def navigate(self) -> None:
        self.page.goto(self.PATH)

    def select_file(self, file_path: Path) -> None:
        """Select a local file through the HTML file input.

        Args:
            file_path: Path to an existing local file.
        """
        self.file_input.set_input_files(file_path)

    def submit(self) -> None:
        self.upload_button.click()

    def upload(self, file_path: Path) -> None:
        """Select and submit a file through the standard upload form.

        Args:
            file_path: Path to the file to upload.
        """
        self.select_file(file_path)
        self.submit()

    def drop_file(self, file_path: Path) -> None:
        """Simulate dropping a local file onto the upload area.

        Read and encode the file as Base64, reconstruct it in the
        browser, and dispatch synthetic drag-and-drop events.

        This method does not wait for the upload to complete.

        Args:
            file_path: Path to an existing local file.
        """

        encoded_file = base64.b64encode(
            file_path.read_bytes()
        ).decode("ascii")

        self.drop_zone.evaluate(
            """(element, fileData) => {
                const bytes = Uint8Array.from(
                    atob(fileData.content),
                    char => char.charCodeAt(0)
                );

                const file = new File(
                    [bytes],
                    fileData.filename
                );

                const transfer = new DataTransfer();
                transfer.items.add(file);

                for (const type of [
                    "dragenter", "dragover", "drop"
                ]) {
                    element.dispatchEvent(
                        new DragEvent(type, {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: transfer
                        })
                    );
                }
            }""",
            {
                "filename": file_path.name,
                "content": encoded_file,
            },
        )
