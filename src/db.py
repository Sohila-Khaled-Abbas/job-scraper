"""Small SQLite persistence layer for parsed job listings."""
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT,
    title TEXT,
    company TEXT,
    location TEXT,
    salary TEXT,
    post_date TEXT,
    summary TEXT,
    job_url TEXT UNIQUE,
    source TEXT,
    scraped_at TEXT
);
"""


def create_table(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()


def init_db(path: str | Path = "jobs.db") -> sqlite3.Connection:
    conn = sqlite3.connect(str(path))
    create_table(conn)
    return conn


def insert_job(conn: sqlite3.Connection, job: dict) -> None:
    conn.execute(
        """INSERT OR IGNORE INTO jobs
        (job_id, title, company, location, salary, post_date, summary, job_url, source, scraped_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        tuple(job.get(key) for key in (
            "job_id", "title", "company", "location", "salary", "post_date",
            "summary", "job_url", "source", "scraped_at"
        )),
    )
    conn.commit()


def get_all_jobs(conn: sqlite3.Connection) -> list[tuple]:
    return conn.execute("SELECT * FROM jobs ORDER BY id").fetchall()
