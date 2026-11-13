from time import sleep

from playwright.sync_api import Page, expect

base_url = "https://the-internet.herokuapp.com/"
def test_form_auth(page: Page) -> None:
    page.goto(f"{base_url}login")
    page.get_by_role("textbox",name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button").click()
    expected_title = "Secure Area"
    expect(page.get_by_role("heading", name='Secure Area', exact=True)).to_have_text(expected_title)

def test_checkbox(page: Page) -> None:
    page.goto(f"{base_url}checkboxes")
    checkbox= page.get_by_role("checkbox")
    for i in range(2):
        if not checkbox.nth(i).is_checked():
            checkbox.nth(i).check()
        assert checkbox.nth(i).is_checked() == True

def test_dropdown(page: Page) -> None:
    page.goto(f"{base_url}dropdown")
    page.locator("#dropdown").select_option('1')
    expect(page.locator(
        "#dropdown")).to_contain_text("Option 1")

def test_canvas(page: Page) -> None:
    page.goto(f"{base_url}canvas")
    page.locator("#canvas").click(position={"x":91,"y":52})
    page.keyboard.type("Segundo intento")
    page.keyboard.press("Enter")
    expect(page.locator("#canvas-log")).to_contain_text("Submitted: Segundo intento")

def test_add_remove_element(page: Page) -> None:
    page.goto(f"{base_url}add_remove_elements/")
    x=3
    for i in range(x):
        page.get_by_role("button", name='Add Element').click()

    for i in range(x):
        expect(page.get_by_role("button",name='Delete').nth(i)).to_be_visible()

def dynamic_control(page: Page, button_name, text, button_s_name) -> None:
    page.get_by_role("button", name=button_name).click()
    expect(page.locator("#loading").get_by_role("img")).to_be_visible()
    expect(page.locator("#message")).to_contain_text(text)
    expect(page.get_by_role("button", name=button_s_name)).to_be_visible()

def test_dynamic_control(page: Page) -> None:
    page.goto(f"{base_url}dynamic_controls")
    dynamic_control(page, button_name="remove", text="It\'s gone!", button_s_name="Add")
    dynamic_control(page, button_name="Enable", text="It\'s enabled!", button_s_name="Disable")


def dialog_hadler(page: Page, button_name, text_expected, prompt_text=None) -> None:
    page.once("dialog", lambda dialog: dialog.accept(prompt_text=prompt_text))
    page.get_by_role("button", name=button_name).click()
    expect(page.get_by_text(text_expected)).to_be_visible()

def test_javascript_alerts_1(page: Page) -> None:
    page.goto(f"{base_url}javascript_alerts")
    dialog_hadler(page, button_name="Click for JS Alert", text_expected="You successfully clicked an alert")

def test_javascript_alerts_2(page: Page) -> None:
    page.goto(f"{base_url}javascript_alerts")
    dialog_hadler(page, button_name="Click for JS Confirm", text_expected="You clicked: Ok")

def test_javascript_alerts_3(page: Page) -> None:
    page.goto(f"{base_url}javascript_alerts")
    dialog_hadler(page, button_name="Click for JS Prompt", text_expected="You entered: test", prompt_text="test")

def test_upload_file(page: Page) -> None:
    page.goto(f"{base_url}upload")
    page.get_by_role("button", name='Choose File').set_input_files(files="/home/maira/Documents/Cross Stitch Font Dublin - Alphabet Cross Stitch Free Patterns_.pdf")
    page.get_by_role("button", name="Upload").click()
    expect(page.locator("#uploaded-files")).to_contain_text("Cross Stitch Font Dublin")


def test_new_window(page: Page) -> None:
    page.goto(f"{base_url}windows")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()

    new_page = popup_info.value

    expect(new_page.get_by_role("heading")).to_have_text("New Window")

def test_dynamic_loading(page: Page) -> None:
    page.goto(f"{base_url}dynamic_loading")
    page.get_by_role("link", name="Example 1: Element on page").click()
    page.get_by_role("button", name="Start").click()
    expect(page.locator("#finish")).to_be_visible()
    expect(page.locator("#finish")).to_contain_text("Hello World!")
    page.goto(f"{base_url}dynamic_loading")
    page.get_by_role("link", name="Example 2: Element rendered").click()
    page.get_by_role("button", name="Start").click()
    expect(page.locator("#finish")).to_be_visible()
    expect(page.locator("#finish")).to_contain_text("Hello World!")


def test_challenging_dom(page: Page) -> None:
    page.goto(f"{base_url}challenging_dom")
    #table verification
    column_header = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]
    for column_header_name in column_header:
        expect(page.get_by_role("columnheader", name=column_header_name)).to_be_visible()
    assert page.locator("table tbody tr").count() == 10
    expect(page.locator("table tbody td").get_by_text("Apeirian5")).to_be_visible()
    page.locator(".button").first.click()
    page.locator(".button.alert").click()
    page.locator(".button.success").click()

def test_permissions(page:Page) -> None:
    page.context.grant_permissions(["notifications","clipboard-read","clipboard-write", "camera"])
    page.goto(f"{base_url}permissions")
    page.get_by_role("button", name='Ask to show notifications').click()
    expect(page.locator("#notifications-result")).to_have_text("Notifications: granted")
    page.get_by_role("button", name='Copy').click()
    page.get_by_role("button", name='Paste').click()
    expect(page.locator("#clipboard-result")).to_have_text("Pasted: Copied from the-internet")
    page.get_by_role("button", name='Turn on the camera').click()
    expect(page.locator("#camera-result")).to_contain_text("Camera on:")
    page.get_by_role("button", name='Turn it off').click()
