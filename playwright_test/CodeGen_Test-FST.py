import re
import time
from pydoc import browse

#import pyautogui

# Get screen size
#screen_width, screen_height = pyautogui.size()

# Adjust size to prevent overflow
#adjusted_width = screen_width - 100
#adjusted_height = screen_height - 100

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Get screen width and height
    #screen_width, screen_height = pyautogui.size()
    #print(f"Screen size: {screen_width}x{screen_height}")
    browser = playwright.chromium.launch(headless=False)

    # Set viewport to match screen resolution
    context = browser.new_context(no_viewport=True)

    page = context.new_page()
    page.goto("http://10.10.1.102:6001/login")
    print("Waiting for Masters element to appear...")

    page.get_by_role("textbox", name="User Name").click()
    print("User Name found")
    time.sleep(3)

    page.get_by_role("textbox", name="User Name").fill("Ayushi")
    print("User name input")
    time.sleep(3)

    page.get_by_role("textbox", name="Password").click()
    print("Password found")
    time.sleep(3)

    page.get_by_role("textbox", name="Password").fill("Cir@123")
    print("Password input")
    time.sleep(3)

    page.get_by_role("button", name="Login").click()
    print("Login Successful")
    time.sleep(3)

    page.get_by_role("link", name="Dashboard icon Dashboard").click()
    print("Dashboard icon Dashboard")
    time.sleep(3)

    page.get_by_role("link", name="Master icon Masters").click()
    print("Master icon Masters")
    time.sleep(3)

    page.get_by_role("link", name="Additional Masters icon").click()
    print("Additional Masters icon")
    time.sleep(3)

    page.get_by_role("link", name="Costing icon Costing").click()
    print("Costing icon Costing")
    time.sleep(3)

    page.get_by_role("link", name="Simulation icon Simulation").click()
    print("Simulation icon Simulation")
    time.sleep(3)

    page.get_by_role("link", name="Reports And Analytics icon").click()
    print("Reports And Analytics icon")
    time.sleep(3)

    page.get_by_role("link", name="Users icon Users").click()
    print("Users icon Users")
    time.sleep(3)

    page.get_by_role("button", name="logout").click()
    print("Logout Successful")
    time.sleep(3)

    page.get_by_role("button", name="OK").click()
    print("OK button")
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
