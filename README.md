# Job Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)  
![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)  


A learning project that scrapes job listings (Indeed) and stores them into a SQLite database. The repo includes:

- a `requests` + BeautifulSoup scraper with pagination and header rotation
- a Selenium fallback for JS-heavy pages
- ETL utilities with pandas
- SQLite for storage
- pytest unit tests and GitHub Actions CI

> This project is for learning and local experimentation — please follow the site's robots.txt and Terms of Service.

## Quickstart

1. Clone the repo:

```bash
git clone git@github.com:YOUR_USERNAME/job-scraper.git
cd job-scraper
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
   
```bash
pip install -r requirements.txt
```

4. Run tests locally:

```bash
pytest -q
```

5. Run the scraper (example):

```bash
python -m src.job_scraper.main --query "data analyst" --location "Cairo" --pages 2
```

---

## Structure

- `src/job_scraper`: core code
- `tests`: unit tests and fixtures
- `configs/example_config.yml`: configurable settings
- `.github/workflows/python-ci.yml`: CI that runs tests on push/PR

---

## Database

A SQLite database named `jobs.db` will be created in the repo root (or configured location). The schema used is in `src/job_scraper/db.py`.

---

## Contributing & CI

- Branch: `main` for releases, `develop` for daily work
- Open PRs to `main` from `develop` or feature branches
- CI runs tests and reports status via GitHub Actions

---

## License

This project is licensed under the [MIT License](LICENSE).