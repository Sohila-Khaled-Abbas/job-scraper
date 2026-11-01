"""Optional Selenium fallback for manually authorized browsing."""
import time
from datetime import datetime, timezone

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .db import insert_job
from .parser import parse_job_card


def scrape_with_selenium(url: str, conn, headless: bool = True) -> list[dict]:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = []
        for card in soup.select("div.job_seen_beacon"):
            job = parse_job_card(str(card))
            if not job["title"]:
                continue
            job["source"] = "indeed"
            job["scraped_at"] = datetime.now(timezone.utc).isoformat()
            insert_job(conn, job)
            results.append(job)
        return results
    finally:
        driver.quit()
