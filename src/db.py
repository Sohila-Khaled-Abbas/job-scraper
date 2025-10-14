import sqlite3
from pathlib import Path


SCHEMA = '''
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
'''




def init_db(path: str | Path = "jobs.db"):
	conn = sqlite3.connect(str(path), check_same_thread=False)
	cur = conn.cursor()
	cur.executescript(SCHEMA)
	conn.commit()
	return conn




def insert_job(conn, job: dict):
	cur = conn.cursor()
	cur.execute(
		"""
INSERT OR IGNORE INTO jobs (job_id, title, company, location, salary, post_date, summary, job_url, source, scraped_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
		(
			job.get("job_id"),
			job.get("title"),
			job.get("company"),
			job.get("location"),
			job.get("salary"),
			job.get("post_date"),
			job.get("summary"),
			job.get("job_url"),
			job.get("source"),
			job.get("scraped_at"),
		),
	)
	conn.commit()