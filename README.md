# Job Scraper

A small Python learning project that parses public Indeed-style job cards, optionally requests public search pages, and stores structured results in SQLite. **This is not a guaranteed live job-market feed**; websites and access rules change.

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/Sohila-Khaled-Abbas/job-scraper.git
cd job-scraper
python -m venv .venv
python -m pip install -r requirements.txt
python -m pytest -q
```

On Windows, run `.venv\\Scripts\\python.exe -m pip install -r requirements.txt` and use that interpreter for the following commands.

Run a best-effort scraper only where the destination site's terms and robots rules permit:

```bash
python -m src.main --query "data analyst" --location "Cairo" --pages 1
```

The CLI writes to `jobs.db` by default; use `--database` to choose another path. Set `--config` to a YAML file to customize the base URL and request pacing.

## What is tested

The offline suite checks HTML parsing and basic SQLite persistence (including deduplication on a known job URL). CI compiles Python sources and runs unit tests without network access. Selenium remains an optional manual fallback requiring a suitable browser/driver; it is not exercised by CI.

## Layout

- `src/parser.py`: pure HTML parser
- `src/requests_scraper.py`: conservative paginated HTTP fetcher
- `src/selenium_scraper.py`: optional browser-assisted fetcher
- `src/db.py`: local SQLite storage
- `src/main.py`: command-line entry point
- `tests/`: offline regression tests

Do not try to bypass rate limits, CAPTCHAs, or access controls. Use provider APIs when available, keep request volume low, and do not collect personal details unnecessarily.

Licensed under [MIT](LICENSE).
