from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from .parser import parse_job_card
from .logger import get_logger

logger = get_logger("selenium_scraper")

def scrape_with_selenium(url: str, conn, headless=True):
opts = Options()
if headless:
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=opts)
try:
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.select("div.job_seen_beacon")
for card in cards:
raw = parse_job_card(str(card))
raw["source"] = "indeed"
raw["scraped_at"] = None
from .db import insert_job

insert_job(conn, raw)
finally:
driver.quit()