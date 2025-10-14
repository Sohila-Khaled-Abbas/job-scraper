import pytest
from src.parser import parse_job_card


@pytest.fixture
def sample_html():
with open('tests/fixtures/indeed_card.html', encoding='utf-8') as f:
return f.read()


def test_parse_job_card(sample_html):
job = parse_job_card(sample_html)
assert isinstance(job, dict)
assert 'title' in job
assert 'company' in job
assert 'location' in job
assert 'summary' in job
assert job['title'] == 'Data Analyst'
assert job['company'] == 'TechCorp'