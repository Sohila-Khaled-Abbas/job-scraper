"""Command-line entry point for best-effort job scraping."""
import argparse

from .db import init_db
from .logger import get_logger
from .requests_scraper import scrape_with_requests

logger = get_logger("job-scraper")


def parse_args():
    parser = argparse.ArgumentParser(description="Scrape public job listing cards into SQLite")
    parser.add_argument("--query", required=True)
    parser.add_argument("--location", default="")
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--config", default=None)
    parser.add_argument("--database", default="jobs.db")
    return parser.parse_args()


def main():
    args = parse_args()
    conn = init_db(args.database)
    try:
        jobs = scrape_with_requests(
            args.query, location=args.location, pages=args.pages,
            conn=conn, config_path=args.config
        )
        logger.info("Collected %d job listings", len(jobs))
        return jobs
    finally:
        conn.close()


if __name__ == "__main__":
    main()
