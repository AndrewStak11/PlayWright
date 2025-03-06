import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.dominos.com/en/?utm_campaign=12899946141|c|GG|Google_BR_Brand_Top&utm_source=Google&utm_medium=p_search&utm_content=kwd-24470291|12899946141|122001614375&utm_term=dominos&matchtype=e&gad_source=1&gclid=CjwKCAiAiaC-BhBEEiwAjY99qE8Psr99sqcAFyKEl7JfWvnWdZ1zWX1nTseWZR5n18Q_PW1ZEGvjLBoCpvMQAvD_BwE")
    page.get_by_role("link", name="Menu", exact=True).click()
    page.get_by_role("link", name="Build Your Own Pizza").click()
    page.get_by_role("tab", name="Carryout").click()
    page.get_by_role("button", name="Find a Store").click()
    page.get_by_role("textbox", name="ZIP Code:").click()
    page.get_by_role("textbox", name="ZIP Code:").fill("99001")
    page.get_by_role("textbox", name="City:").click()
    page.get_by_role("textbox", name="City:").fill("spokane")
    page.get_by_label("State").select_option("WA")
    page.get_by_role("button", name="Find a Store").click()
    page.get_by_role("link", name="Store Pickup - w 12622 sunset").click()
    page.get_by_role("group", name="Robust Inspired Tomato Sauce").click()
    page.get_by_role("radio", name="Alfredo Sauce").check()
    page.get_by_role("checkbox", name="Ham").check()
    page.get_by_role("checkbox", name="Hot Buffalo Sauce").check()
    page.get_by_role("checkbox", name="Pineapple").check()
    page.get_by_role("button", name="Add to Order").click()
    page.get_by_role("button", name="No Thanks").click()
    page.get_by_role("link", name="Checkout").click()
    page.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
