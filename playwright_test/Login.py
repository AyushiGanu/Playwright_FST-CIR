import asyncio
import time
from playwright.async_api import async_playwright


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Hit the URL
        await page.goto("http://10.10.1.102:6001/")
        await page.set_viewport_size({"width": 1366, "height": 768})
        print("URL Hit Successfully")
        time.sleep(10)

        # Login
        await page.fill('input[name="username"]', 'Ayushi')
        print("User name entered")
        time.sleep(10)

        await page.locator('//*[@id="password"]').fill("Cir@123")
        print("Password entered")
        time.sleep(10)

        await page.click('input[type="submit"]')
        print("Login Successfully")
        time.sleep(10)

        # Wait for and click on Masters
        print("Waiting for Masters element to appear...")
        await page.get_by_role("raw-material-master")
        print("Masters element found")

        masters = page.locator('//*[@id="Master_NavBar"]/span')

        # Optional: Scroll and hover just in case
        await masters.scroll_into_view_if_needed()
        await masters.hover()
        await masters.click()
        print("Clicked on Masters")

        time.sleep(10)

asyncio.run(run())
