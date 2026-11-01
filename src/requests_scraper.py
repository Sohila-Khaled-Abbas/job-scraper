"""Best-effort, conservative HTML scraper; external sites can change."""
import random
import time
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .config import load_config
from .db import insert_job
from .logger import get_logger
from .parser import parse_job_card

logger = get_logger("requests_scraper")


def rand_headers(user_agents: list[str], base_headers: dict) -> dict:
    headers = base_headers.copy()
    if user_agents:
        headers["User-Agent"] = random.choice(user_agents)
    return headers


def scrape_with_requests(
    query: str, location: str = "", pages: int = 1, conn=None, config_path=None,
) -> list[dict]:
    if pages < 1:
        raise ValueError("pages must be at least 1")
    cfg = load_config(config_path)
    base_url = cfg["base_url"]
    results = []
    for page in range(pages):
        params = {"q": query, "l": location, "start": page * cfg["results_per_page"]}
        headers = rand_headers(
            cfg.get("user_agents", []), {"Accept-Language": "en-US,en;q=0.9"}
        )
        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
        except requests.RequestException as exc:
            logger.warning("Page %d failed: %s", page + 1, exc)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select("div.job_seen_beacon, div.jobsearch-SerpJobCard")
        for card in cards:
            job = parse_job_card(str(card))
            if not job["title"]:
                continue
            job["source"] = "indeed"
            job["scraped_at"] = datetime.now(timezone.utc).isoformat()
            if job.get("job_url"):
                job["job_url"] = urljoin(base_url, job["job_url"])
            if conn is not None:
                insert_job(conn, job)
            results.append(job)
        if page + 1 < pages:
            time.sleep(random.uniform(cfg["sleep_min"], cfg["sleep_max"]))
    return results
