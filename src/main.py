import argparse
from .db import init_db
from .requests_scraper import scrape_with_requests
from .logger import get_logger

logger = get_logger("main")

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument("--query", required=True)
	p.add_argument("--location", default="")
	p.add_argument("--pages", type=int, default=1)
	p.add_argument("--config", default=None)
	return p.parse_args()

def main():
	args = parse_args()
	try:
		init_db()
	except Exception as e:
		logger.debug("init_db failed or skipped: %s", e)

	results = scrape_with_requests(args.query, location=args.location, pages=args.pages)
	try:
		count = len(results)
	except Exception:
		count = 0
	logger.info("Scraped %d results", count)
	return results

if __name__ == "__main__":
	main()