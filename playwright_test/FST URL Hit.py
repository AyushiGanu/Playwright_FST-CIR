import asyncio
import time

from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Set to True to run in background
        page = await browser.new_page()
        await page.goto("http://10.10.1.102:6001/")
        #await page.screenshot(path="example.png")
        await browser.close()
        time.sleep (10)
asyncio.run(run())