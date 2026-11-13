import re

from playwright.sync_api import sync_playwright, expect, Page


#
# def test_1():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://www.google.com")
#         page.wait_for_load_state("load")
#         title = page.title()
#
#         assert "Google" in title, f"Expected 'Google' in title, but got '{title}'"

def test_google_search(page:Page):
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept)")
    page.get_by_role("combobox", name="Search").fill("Playwright python")
    page.keyboard.press("Enter")
    expected_title = "Playwright"
    expect(page).to_have_title(re.compile(expected_title, re.IGNORECASE))


