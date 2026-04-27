"""Bot RPA: preenche formulários em sistemas web legados automaticamente."""
import asyncio
import yaml
from pathlib import Path
from playwright.async_api import async_playwright


class FormFillerBot:
    def __init__(self, config_path: str):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    async def run(self):
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()

            url = self.config["url"]
            fields = self.config["fields"]
            submit_selector = self.config.get("submit", "button[type=submit]")

            print(f"Acessando: {url}")
            await page.goto(url, timeout=30000)
            await page.wait_for_load_state("networkidle")

            for field in fields:
                selector = field["selector"]
                value = field["value"]
                action = field.get("action", "fill")

                if action == "fill":
                    await page.fill(selector, str(value))
                elif action == "select":
                    await page.select_option(selector, str(value))
                elif action == "click":
                    await page.click(selector)
                elif action == "check":
                    await page.check(selector)

                print(f"  ✅ Campo preenchido: {selector}")

            await page.click(submit_selector)
            await page.wait_for_load_state("networkidle")
            print("✅ Formulário enviado com sucesso!")
            await browser.close()


async def main(config_path: str):
    bot = FormFillerBot(config_path)
    await bot.run()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    asyncio.run(main(args.config))
