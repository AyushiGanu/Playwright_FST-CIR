import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://10.10.1.102:6001/login")
    page.get_by_role("textbox", name="User Name").click()
    time.sleep(5)
    page.get_by_role("textbox", name="User Name").fill("Ayushi")
    time.sleep(5)
    page.get_by_role("textbox", name="Password").click()
    time.sleep(5)
    page.get_by_role("textbox", name="Password").fill("Cir@123")
    time.sleep(5)
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
    page.get_by_role("link", name="Dashboard icon Dashboard").click()
    time.sleep(5)
    page.get_by_role("link", name="Master icon Masters").click()
    time.sleep(5)
    page.get_by_role("link", name="Additional Masters icon").click()
    time.sleep(5)
    page.get_by_role("link", name="Costing icon Costing").click()
    time.sleep(5)
    page.get_by_role("link", name="Simulation icon Simulation").click()
    time.sleep(5)
    page.get_by_role("link", name="Reports And Analytics icon").click()
    time.sleep(5)
    page.get_by_role("link", name="Users icon Users").click()
    time.sleep(5)
    page.get_by_role("button", name="logout").click()
    time.sleep(5)
    page.get_by_role("button", name="OK").click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
