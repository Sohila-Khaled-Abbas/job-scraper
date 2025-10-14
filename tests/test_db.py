import sqlite3
import pytest
from src.db import create_table, insert_job, get_all_jobs

@pytest.fixture
def db_connection(tmp_path):
db_path = tmp_path / 'jobs.db'
conn = sqlite3.connect(db_path)
create_table(conn)
yield conn
conn.close()


def test_insert_and_retrieve(db_connection):
job = {
'title': 'Data Scientist',
'company': 'OpenAI',
'location': 'Remote',
'summary': 'Work on AI models.',
'date_posted': '2025-10-10'
}
insert_job(db_connection, job)
results = get_all_jobs(db_connection)
assert len(results) == 1
assert results[0][1] == 'Data Scientist'