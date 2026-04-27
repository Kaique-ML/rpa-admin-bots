"""Bot RPA: faz download e organiza documentos de portais web."""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright


class DocDownloaderBot:
    def __init__(self, output_dir: str = "downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def download_from_portal(self, url: str, login: dict, doc_selectors: list[str]):
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(accept_downloads=True)
            page = await context.new_page()

            await page.goto(url)
            if login:
                await page.fill(login["user_selector"], login["username"])
                await page.fill(login["pass_selector"], login["password"])
                await page.click(login["submit_selector"])
                await page.wait_for_load_state("networkidle")

            for selector in doc_selectors:
                async with page.expect_download() as dl:
                    await page.click(selector)
                download = await dl.value
                dest = self.output_dir / download.suggested_filename
                await download.save_as(dest)
                print(f"✅ Baixado: {dest}")

            await browser.close()
