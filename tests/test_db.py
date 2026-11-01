import sqlite3

import pytest

from src.db import create_table, get_all_jobs, insert_job


@pytest.fixture
def db_connection(tmp_path):
    conn = sqlite3.connect(tmp_path / "jobs.db")
    create_table(conn)
    yield conn
    conn.close()


def test_insert_and_retrieve(db_connection):
    job = {
        "title": "Data Scientist",
        "company": "Example Company",
        "location": "Remote",
        "summary": "Work on AI models.",
        "post_date": "2025-10-10",
    }
    insert_job(db_connection, job)
    rows = get_all_jobs(db_connection)
    assert len(rows) == 1
    assert rows[0][2] == "Data Scientist"


def test_duplicate_url_is_ignored(db_connection):
    job = {"title": "Data Analyst", "job_url": "https://example.com/jobs/1"}
    insert_job(db_connection, job)
    insert_job(db_connection, job)
    assert len(get_all_jobs(db_connection)) == 1
