import requests
import time
import random
from typing import List
from datetime import datetime
from .parser import parse_job_card
from .config import load_config
from .logger import get_logger

logger = get_logger("requests_scraper")

def rand_headers(user_agents: List[str], base_headers: dict):
h = base_headers.copy()
if user_agents:
h["User-Agent"] = random.choice(user_agents)
return h

def scrape_with_requests(query: str, location: str, pages: int, conn, config_path=None):
cfg = load_config(config_path)
base_url = cfg.get("base_url")
user_agents = cfg.get("user_agents", [])
sleep_min = cfg.get("sleep_min", 1.0)
sleep_max = cfg.get("sleep_max", 3.0)
results_per_page = cfg.get("results_per_page", 10)

for page in range(pages):
params = {"q": query, "l": location, "start": page * results_per_page}
headers = rand_headers(user_agents, {"Accept-Language": "en-US,en;q=0.9"})
try:
resp = requests.get(base_url, headers=headers, params=params, timeout=15)
resp.raise_for_status()
except Exception as e:
logger.warning("Request failed: %s", e)
continue

from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")
cards = soup.select("div.job_seen_beacon") or soup.select("div.jobsearch-SerpJobCard")
for card in cards:
raw = parse_job_card(str(card))
raw["source"] = "indeed"
raw["scraped_at"] = datetime.utcnow().isoformat()
# normalize URL
if raw.get("job_url"):
raw["job_url"] = requests.compat.urljoin(base_url, raw["job_url"])
else:
raw["job_id"] = None
# insert to DB
from .db import insert_job
insert_job(conn, raw)
time.sleep(random.uniform(sleep_min, sleep_max))