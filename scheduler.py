"""Agendador de todos os bots RPA."""
import asyncio
import schedule
import time
from bots.form_filler import FormFillerBot
from bots.doc_downloader import DocDownloaderBot


async def run_form_filler():
    bot = FormFillerBot("config/form_filler.yaml")
    await bot.run()


def job_form_filler():
    asyncio.run(run_form_filler())


# Agendar bots
schedule.every().day.at("08:00").do(job_form_filler)
schedule.every().monday.at("09:00").do(job_form_filler)

print("🤖 Scheduler de bots iniciado. Aguardando jobs...")
while True:
    schedule.run_pending()
    time.sleep(60)
